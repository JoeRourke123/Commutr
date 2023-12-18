## What the frick is going on here?
In the `domain` package is all the domain/business logic for the API. This contains the Celery tasks for scraping article data and content, the services which abstract away database access from our endpoints, serialisers for using Django library features to convert our Django models to JSON, and other helpful logic.

## Serialisers? Wtf is that?

Read this tutorial from the Django REST library: https://www.django-rest-framework.org/tutorial/1-serialization/