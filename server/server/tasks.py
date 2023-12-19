from django_celery_beat.models import PeriodicTask, IntervalSchedule


def setup_rss_job():
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=20,
        period=IntervalSchedule.MINUTES,
    )

    PeriodicTask.objects.get_or_create(
        interval=schedule,
        name='Periodic fetch of RSS Feeds and Article Content',
        task='commutr.domain.rss.run_rss_workers',
    )
