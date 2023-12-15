# Generated by Django 5.0 on 2023-12-14 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commutr', '0007_alter_newsarticle_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticleContent',
            fields=[
                ('article', models.ForeignKey(db_column='news_article_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='content', serialize=False, to='commutr.newsarticle')),
                ('content', models.BinaryField(db_column='news_article_content')),
            ],
            options={
                'db_table': 'news_article_content',
            },
        ),
        migrations.CreateModel(
            name='NewsArticleTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=128)),
                ('article', models.ForeignKey(db_column='news_article_id', on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='commutr.newsarticle')),
            ],
            options={
                'db_table': 'news_article_topic',
                'unique_together': {('article', 'topic')},
            },
        ),
    ]
