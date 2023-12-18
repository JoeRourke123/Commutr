import base64
import io
import json
import time
import PyPDF2
from datetime import datetime, timedelta
from io import BytesIO
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class PdfGenerator:
    """
    Given a webpage URL, this class uses Selenium (automated web browser simulation) to "print" the webpage
    as a PDF and save it as a single paged file.
    """

    driver = None           # The driver is the browser backend engine being used. For us, this is the ChromeDriver
    # https://chromedevtools.github.io/devtools-protocol/tot/Page#method-printToPDF

    # What do we want our PDF to look like?
    print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'paperWidth': 6.97,     # inches
        'paperHeight': 16.5,    # inches
        'marginTop': 0,
        'marginBottom': 0,
        'marginLeft': 0,
        'marginRight': 0,
    }

    def __init__(self, urls: List[str]):
        self.urls = urls

    def _get_pdf_from_url(self, url, *args, **kwargs):
        # Loads the article page
        self.driver.get(url)

        # Zoom so text is readable on mobile
        self.driver.execute_script("document.body.style.zoom = '1.5'");

        time.sleep(1)  # allow the page to load, increase if needed

        print_options = self.print_options.copy()

        # Use Chrome APIs to download the page as a PDF
        result = self._send_devtools(self.driver, "Page.printToPDF", print_options)
        return base64.b64decode(result['data'])     # Decode the returned data from PDF operation

    @staticmethod
    def _send_devtools(driver, cmd, params):
        """
        Works only with chromedriver.
        Method uses cromedriver's api to pass various commands to it.
        """
        resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
        url = driver.command_executor._url + resource
        body = json.dumps({'cmd': cmd, 'params': params})
        response = driver.command_executor._request('POST', url, body)
        return response.get('value')


    def _generate_pdfs(self):
        pdf_files = []

        for url in self.urls:
            result = self._get_pdf_from_url(url)
            file = BytesIO()
            file.write(result)
            pdf_files.append(file)

        return pdf_files


    def main(self) -> List[BytesIO]:
        webdriver_options = ChromeOptions()
        webdriver_options.add_argument('--headless=new')


        try:
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=webdriver_options
            )

            self.driver.execute_cdp_cmd('Network.enable', {})

            result = self._generate_pdfs()
        finally:
            self.driver.close()

        return result

    @staticmethod
    def merge_pdf_pages(pdf_data):
        """
        Helper function to combine any number of pages from the pdf data

        Args:
            pdf_data: the raw bytes for the PDF

        Returns:
            PDF file raw bytes but with only one continuous page
        """

        # Encapsulate the raw PDF data into a PyPDF object
        pdf = PyPDF2.PdfReader(io.BytesIO(pdf_data[0].getbuffer().tobytes()))

        pages = []
        for pageNum in range(len(pdf.pages)):
            pageObj = pdf.pages[pageNum]
            pages.append(pageObj)

        width = pages[0].mediabox.width
        height = pages[0].mediabox.height * len(pdf.pages)

        # Create a blank page long enough for our webpage
        merged_page = PyPDF2.PageObject.create_blank_page(None, width, height)

        y = 0
        for page in pages:
            # Splice the old PDF page onto the new page, shifted on the y-axis accordingly
            merged_page.add_transformation(PyPDF2.Transformation().scale(1, 1).translate(0, page.mediabox.height))
            merged_page.merge_page(page)
            y = float(y) + float(page.mediabox.height)

        writer = PyPDF2.PdfWriter()
        writer.add_page(merged_page)

        pdf_data = io.BytesIO()
        writer.write(pdf_data)

        # Return the bytes of the new merged PDF page
        return pdf_data.getbuffer().tobytes()
