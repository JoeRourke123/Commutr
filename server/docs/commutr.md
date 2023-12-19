

---- 
# commutr.controller.fallback\_article\_fetch\_controller

## FallbackArticleFetchController
```python
class FallbackArticleFetchController(viewsets.ReadOnlyModelViewSet)

```
This is a temporary ViewSet, created for keeping a set of common and useful endpoints.

This will be refactored into more concrete controllers upon further iterations.

#### articles
```python
@action(detail=False, methods=['get'])
def articles(request)

```

This GET endpoints /api/articles returns the most recent 10 articles

**Arguments**:
  

- `request` - the Django request data

**Returns**:

  a serialised list of the 10 most recent articles

#### articles\_by\_source
```python
@action(detail=False,
        methods=['get'],
        url_path="source/(?P<pk>[\w-]+)/articles")
def articles_by_source(request, pk: uuid.UUID)

```

This GET endpoint api/source/SOURCE_ID/articles returns the articles from a given source.

**Arguments**:
- `request` - the Django request data
  

- `pk` - the primary key/UUID of a news source

**Returns**:

  a serialised list of articles from the specified source

#### article\_with\_content
```python
@action(detail=False, methods=['get'], url_path="article/(?P<pk>[\w-]+)")
def article_with_content(request, pk: uuid.UUID)

```

This GET endpoint /api/article/ARTICLE_ID returns the PDF contents of the specified article

**Arguments**:
- `request` - the Django request data
  

- `pk` - the UUID of a news article

**Returns**:

  a HTTP response of type application/pdf with the binary article content PDF


---- 
# commutr.db.news\_source\_topic\_model

## NewsSourceTopic
```python
class NewsSourceTopic(models.Model)

```

Provides a many-to-one mapping of topics to news source

## Meta
```python
class Meta()

```

#### db\_table
```python
db_table = "news_source_topic"

```

Postgres table name

---- 
# commutr.db.news\_article\_model

## NewsArticle
```python
class NewsArticle(models.Model)

```

Represents a single news article

## Meta
```python
class Meta()

```

#### db\_table
```python
db_table = "news_article"

```

Actual table name in Postgres

#### ordering
```python
ordering = ['-published']

```

Orders the table by newest articles first

---- 
# commutr.db.news\_article\_topic\_model

## NewsArticleTopic
```python
class NewsArticleTopic(models.Model)

```

Provides a many-to-one mapping of topics to article

## Meta
```python
class Meta()

```

#### db\_table
```python
db_table = "news_article_topic"

```

Postgres table name

---- 
# commutr.db.news\_article\_content\_model

## NewsArticleContent
```python
class NewsArticleContent(models.Model)

```

A table which provides a one-to-one mapping of articles to their content.

## Meta
```python
class Meta()

```

#### db\_table
```python
db_table = "news_article_content"

```

The table name in Postgres

---- 
# commutr.db.news\_source\_model

## NewsSource
```python
class NewsSource(models.Model)

```

Represents a single news source/vendor

#### id
```python
id = models.UUIDField(default=uuid.uuid4,
                      primary_key=True,
                   ...

```

Unique identifier used for sources internally by us

#### name
```python
name = models.CharField(db_column="source_name", editable=False)

```

e.g. The Guardian

#### rss\_url
```python
rss_url = models.URLField(db_column="source_rss_feed_url", editable=False)

```

The URL of the RSS feed we scrape articles from for this source

#### political\_leaning
```python
political_leaning = models.FloatField(validators=(
    validators.MinValueValidator(-1.0),
    valid ...

```

-1 is very left-wing, 1 is very conservative. 0 is centrism.

#### latest\_article
```python
latest_article = models.DateTimeField(db_column="source_latest_article",
                            ...

```

The date/time of the most recent article scraped, used to identify which articles have already been pulled

## Meta
```python
class Meta()

```

#### db\_table
```python
db_table = "news_source"

```

Postgres table name



---- 
# commutr.domain.util.get\_raw\_rss\_feed

#### get\_raw\_rss\_feed
```python
def get_raw_rss_feed(rss_url=None)

```

Simple helper function which given an RSS URL will just print out the first entry as an example

**Arguments**:
  

- `rss_url` - a str URL for an RSS feed. If blank, the user will be prompted to enter one

**Returns**:

  A JSON representation of one RSS feed article.

---- 
# commutr.domain.rss.util

#### get\_rss\_entry\_data
```python
def get_rss_entry_data(entry_key: str, entry: dict) -> any

```

For a given dict and RSS field key, we want to find the specific data.
Keys can be:
* `title`: Just gets the title field at the root of entry
* `data.tags[].title` would get a list of the article's tag names, i.e. ['sport', 'football', 'Ronaldo']

* `data.author[1].name` would return 'John Doe' as it is just returning the name of the 2nd author in the author list

**Arguments**:
- `entry_key` - the RSS field key, in the format of: data.author[2].name which is equivalent to article['data']['author'][2]['name']
  

- `entry` - the dict to fetch this information from

**Returns**:

  the found or mapped value from the article RSS data

---- 
# commutr.domain.rss

#### run\_rss\_workers
```python
@app.task
def run_rss_workers()

```
A Celery beat task which will run every 20 minutes (setup in server.tasks) which will deploy

jobs to fetch RSS feeds for each news source in the database

#### get\_rss\_articles
```python
@app.task
def get_rss_articles(news_source: NewsSource)

```
A Celery task for, given a news source. scraping the latest articles from the source's RSS feeds.

These new articles are then added into the database.

**Arguments**:

- `news_source` - a NewsSource instance to scrape articles from

---- 
# commutr.domain.pdf.util

## PdfGenerator
```python
class PdfGenerator()

```
Given a webpage URL, this class uses Selenium (automated web browser simulation) to "print" the webpage

as a PDF and save it as a single paged file.

#### driver
```python
driver = None

```

The driver is the browser backend engine being used. For us, this is the ChromeDriver

#### merge\_pdf\_pages
```python
@staticmethod
def merge_pdf_pages(pdf_data)

```

Helper function to combine any number of pages from the pdf data

**Arguments**:
  

- `pdf_data` - the raw bytes for the PDF

**Returns**:

  PDF file raw bytes but with only one continuous page

---- 
# commutr.domain.pdf

#### download\_article\_content\_pdf
```python
@app.task
def download_article_content_pdf(news_article: NewsArticle)

```

A Celery task to fetch a specific article's webpage content as a single PDF page and push it to the database.

**Arguments**:
  

- `news_article` - a NewsArticle record from the database with all the article metadata

**Returns**:

  N/A.

---- 
# commutr.domain.serialiser.news\_article\_serialiser

## NewsArticleSerialiser
```python
class NewsArticleSerialiser(serializers.ModelSerializer)

```

Serialises Django NewsArticles models to JSON


---- 
# commutr.domain.serialiser.news\_source\_serialiser

## NewsSourceSerialiser
```python
class NewsSourceSerialiser(serializers.ModelSerializer)

```

Serialises Django NewsSource models to JSON


---- 
# commutr.domain.article.article\_service

## ArticleService
```python
class ArticleService(object)

```

An encapsulated abstraction layer for fetching article records from the database

#### get\_articles
```python
def get_articles(sources: [NewsSource] = None,
                 after_date: datetime = None,
                 limit: int = None)

```

Fetches articles that meet the provided criteria

**Arguments**:
- `sources` - A list of NewsSource objects to fetch from. If the field is None, return from any source
- `after_date` - Only return articles from after this datetime, unless it is None then return records from any date
  

- `limit` - An integer limit on the number of fetched articles. Unless None, then no limits are placed

**Returns**:

  A list of NewsArticle objects filtered according to the method parameters

#### get\_articles\_by\_source
```python
def get_articles_by_source(source: NewsSource, after_date: datetime = None)

```

Given a specific source, find all their articles

**Arguments**:
- `source` - the NewsSource to fetch
  

- `after_date` - an optional datetime filter, if present only articles after the specified datetime are included

**Returns**:

  A filtered list of NewsArticle instances from the specified news source

#### get\_articles\_after\_date
```python
def get_articles_after_date(after_date: datetime)

```

Returns NewsArticles only from after the specified datetime

**Arguments**:
  

- `after_date` - A non-nullable datetime set as the lower bound for the article filter

**Returns**:

  A list of NewsArticle instances which came after after_date

#### get\_article\_content
```python
def get_article_content(article: NewsArticle)

```

For a given article, fetch its PDF content from the database

**Arguments**:
  

- `article` - the NewsArticle metadata to fetch the content for

**Returns**:

  The bytes for a PDF containing article content




