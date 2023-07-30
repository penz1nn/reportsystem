from typing import List
from ..domain.report import Report


class ReportRepository:
    """Storage for the Report objects."""

    def save_report(self, report: Report):
        """Save a Report object in storage."""
        ...

    def find_reports_by_kv(self, data: dict) -> List[Report]:
        """Find all Reports which contain any of the key-value pairs
        provided."""
        ...

    def find_reports_by_hash(self, hash_value: int) -> List[Report]:
        """Find all records which have matching hash value."""
        ...
