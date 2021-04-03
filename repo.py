from dagster import pipeline, repository, schedule, solid, sensor, SkipReason


@solid
def hello(_):
    return 1


@pipeline
def my_pipeline():
    hello()


@schedule(cron_schedule="* * * * *", pipeline_name="my_pipeline", execution_timezone="US/Central")
def my_schedule(_context):
    return {}


@sensor(pipeline_name="my_pipeline")
def always_skips(_context):
    yield SkipReason("I always skip!")


@repository
def deploy_docker_repository():
    return [my_pipeline, my_schedule, always_skips]
