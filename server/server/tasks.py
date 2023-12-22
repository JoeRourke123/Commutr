from django_celery_beat.models import PeriodicTask, IntervalSchedule


def setup_rss_job():
    """
    Setup periodic RSS job as a scheduled task if it doesn't already exist
    """

    # schedule, created = IntervalSchedule.objects.get_or_create(
    #     every=20,
    #     period=IntervalSchedule.MINUTES,
    # )
    #
    # if created:
    #     schedule.save()
    #
    # task, created = PeriodicTask.objects.get_or_create(
    #     interval_id=schedule.id,
    #     name='Periodic fetch of RSS Feeds and Article Content',
    #     task='commutr.domain.rss.run_rss_workers',
    # )
    #
    # if created:
    #     task.save()


def setup_notion_job():
    """
    Set up the periodic refreshing of news source data from the Notion database
    """

    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.MINUTES
    )

    task, created = PeriodicTask.objects.get_or_create(
        schedule=schedule,
        name="Periodically refresh data from the Notion base for News Sources",
        task="commutr.domain.util.reload_sources_from_notion.reload_news_sources_from_notion"
    )

    if created:
        task.save()

