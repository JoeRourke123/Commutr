## What the frick is going on here?

The `db` directory homes files each containing a Django model. These are Python representations of Postgres tables. One table -> One model. These can represent rich contentful tables like NewsArticle, or just be a linking table like with NewsSourceTopic (just a many-to-one mapping of topics to news source).

Tables can be linked with ForeignKeys or different Mappings, consult the documentation below.

From these models, we can automatically generate our database and this must be done whenever the models are changed: 
```shell
python manage.py makemigrations     // This will produce the database changes needed

python manage.py migrate            // This will apply these database changes
```

## What's up Doc?
Here are the official Django documentation on models:
https://docs.djangoproject.com/en/5.0/topics/db/models/