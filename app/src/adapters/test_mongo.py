import unittest
from ..domain.report import Report
from .mongo import MongoReportRepository, _records_to_reports

DBNAME = "test_db"

report1 = Report(
    headers={"sample": "text"}, body={"key1": 1, "key2": "two", "key3": False}
)


class TestMongoReportRepository(unittest.TestCase):
    def setUp(self):
        repository = MongoReportRepository(db_name=DBNAME)
        repository.client.drop_database(DBNAME)

    def test_save_record(self):
        repository = MongoReportRepository(db_name=DBNAME)
        repository.save_report(report1)
        self.assertEqual(
            _records_to_reports(repository.db["problem_records"].find())[0], report1
        )
        repository.client.drop_database(DBNAME)

    def test_find_reports_by_kv(self):
        report2 = Report(headers={"some": "string"}, body={"sample": "string"})
        report3 = Report(headers={"additional": "string"}, body={"sample": "text"})
        repository = MongoReportRepository(db_name=DBNAME)
        repository.save_report(report1)
        repository.save_report(report2)
        repository.save_report(report3)
        # valid data
        data1 = {"sample": "text"}
        data2 = {"key1": 1}
        data3 = {"some": "string", "sample": "text"}
        self.assertEqual(len(repository.find_reports_by_kv(data1)), 2)
        self.assertEqual(repository.find_reports_by_kv(data2), [report1])
        self.assertEqual(len(repository.find_reports_by_kv(data3)), 3)
        # non existent
        data4 = {"anything": "else"}
        self.assertEqual(repository.find_reports_by_kv(data4), [])
        # weird data
        data5 = {"something_weird": {"yes": True, "No": False}, "key1": 1}
        self.assertEqual(repository.find_reports_by_kv(data5), [report1])
        repository.client.drop_database(DBNAME)

    def test_find_reports_by_hash(self):
        repository = MongoReportRepository(db_name=DBNAME)
        # find existent
        repository.save_report(report1)
        repository.save_report(report1)
        self.assertEqual(
            repository.find_reports_by_hash(report1.hash), [report1, report1]
        )
        # find non existent
        self.assertEqual(repository.find_reports_by_hash(123123123), [])
        repository.client.drop_database(DBNAME)
