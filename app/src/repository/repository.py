from typing import List
from ..domain.report import Report


class ReportRepository:

    def save_report(self, report: Report):
        """
        Save a problem report (record)
        """
        ...

    def find_reports_by_kv(self, data: dict) -> List[Report]:
        """
        Find all records which contain any of fthe key-value pairs provided
        """
        ...

    def find_reports_by_hash(self, hash_value: int) -> List[Report]:
        """
        Find all records which have matching hash value
        """
        ...
