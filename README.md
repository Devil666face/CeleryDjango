Запустить redis
`redis-server`

Запустить воркеры celery
`celery -A config worker`

Запустить бэкграунд celery который смотрит в базу django_celery_beat
`celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
`