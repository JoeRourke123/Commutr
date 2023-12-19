from commutr.celery import app
from commutr.db.news_article_content_model import NewsArticleContent
from commutr.db.news_article_model import NewsArticle
from commutr.domain.pdf.util import PdfGenerator


@app.task
def download_article_content_pdf(news_article: NewsArticle):
    """
    A Celery task to fetch a specific article's webpage content as a single PDF page and push it to the database.

    Args:
        news_article: a NewsArticle record from the database with all the article metadata

    Returns:
        N/A.
    """
    try:
        pdf_file = PdfGenerator([news_article.url]).main()

        merged_pdf_page_bytes: bytes = PdfGenerator.merge_pdf_pages(pdf_file)

        print("Article content successfully fetched")

        article_content = NewsArticleContent.objects.create(
            article=news_article,
            content=merged_pdf_page_bytes
        )

        article_content.save()

        print("Article content saved to db")
    except Exception:
        print("Something went wrong when fetching this article's content. Skipping...")
        news_article.delete()
