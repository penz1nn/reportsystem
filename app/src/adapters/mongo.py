from typing import List
from pymongo import MongoClient

from ..domain.report import Report
from ..repository.repository import ReportRepository


class MongoReportRepository(ReportRepository):

    def __init__(
            self,
            mongo_host: str = "mongo",
            mongo_port: int = 27017,
            db_name: str = "my_db"
            ):
        self.client = MongoClient(mongo_host, mongo_port)
        self.db = self.client[db_name]

    def save_report(self, report: Report):
        report_dict = report.to_dict()
        report_dict["hash"] = str(report_dict["hash"])
        self.db["problem_records"].insert_one(report.to_dict())

    def find_reports_by_kv(self, data: dict) -> List[Report]:
        query = {
                "$or": [
                    ]
                }
        for key in data:
            query["$or"].append({"headers." + key: data[key]})
            query["$or"].append({"body." + key: data[key]})
        records = self.db["problem_records"].find(query)
        reports = _records_to_reports(records)
        return reports

    def find_reports_by_hash(self, hash_value: int) -> List[Report]:
        query = {"hash": hash_value}
        records = self.db["problem_records"].find(query)
        reports = _records_to_reports(records)
        return reports


def _records_to_reports(records) -> List[Report]:
    records = [record for record in records]
    reports = []
    for record in records:
        for item in ["headers", "body", "hash"]:
            if item not in record:
                pass
        reports.append(
                Report(
                    headers=record["headers"],
                    body=record["body"],
                    hash_value=int(record["hash"])
                    )
                )
    return reports
