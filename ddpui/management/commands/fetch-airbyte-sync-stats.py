"""for each org fetch orchestration pipelines for airbyte sync"""
from django.core.management.base import BaseCommand, CommandParser

from ddpui.models.tasks import DataflowOrgTask
from ddpui.ddpairbyte.airbyte_service import get_jobs_for_connection
from ddpui.ddpairbyte.airbytehelpers import get_job_info_for_connection


class Command(BaseCommand):
    """Docstring"""

    help = "Updates the mapping with the correct value of dataflow type in orgdataflow table"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--jobs",
            action="store_true",
            help="run airbyte_service.get_jobs_for_connection",
        )
        parser.add_argument(
            "--job-info",
            action="store_true",
            help="run airbyte_helpers.get_job_info_for_connection",
        )
        parser.add_argument("--org", type=str, help="org slug")

    def handle(self, *args, **options):
        """for each org, fetch orchestration pipeline(s) for airbyte sync"""
        for dfot in DataflowOrgTask.objects.filter(
            orgtask__task__slug="airbyte-sync", dataflow__dataflow_type="orchestrate"
        ):
            if options["org"] and options["org"] != dfot.orgtask.org.slug:
                continue
            print(dfot.orgtask.org.slug, dfot.orgtask.connection_id)
            if options["jobs"]:
                jobs = get_jobs_for_connection(dfot.orgtask.connection_id)
                print(jobs)
            if options["job_info"]:
                job_info = get_job_info_for_connection(
                    dfot.orgtask.org, dfot.orgtask.connection_id
                )
                print(job_info)
