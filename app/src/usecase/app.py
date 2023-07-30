from typing import List

from ..domain.report import Report
from ..repository.repository import ReportRepository


class App:

    storage: ReportRepository

    def __init__(self, storage: ReportRepository):
        self.storage = storage

    def run(self):
        ...

    def save_report(
            self,
            headers: dict,
            body: dict = {},
            ) -> int:
        report = Report(
                headers=headers,
                body=body
                )
        self.storage.save_report(report)
        return report.hash

    def find_reports_by_kv(self, data: dict) -> List[dict]:
        reports = self.storage.find_reports_by_kv(data)
        return _reports_to_dicts(reports)
    
    def find_reports_by_hash(self, hash_value: int) -> List[dict]:
        reports = self.storage.find_reports_by_hash(hash_value)
        return _reports_to_dicts(reports)


def _reports_to_dicts(reports: List[Report]) -> List[dict]:
    """
    transform list of Report objects to list of dicts and delete the "hash" key from them
    """
    dicts = [{key:report.to_dict()[key] for key in report.to_dict() if key != "hash"} for report in reports]
    return dicts
