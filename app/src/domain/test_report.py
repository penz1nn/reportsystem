import unittest

from .report import Report


class TestReport(unittest.TestCase):
    def test_init(self):
        headers = {"sample": "text"}
        body = {"value1": 200, "value2": "secret", "value3": True}
        hash3 = 12356789
        # init with just headers
        report1 = Report(headers=headers)
        self.assertEqual(report1.headers, headers)
        hash1 = report1.hash
        self.assertIsNotNone(hash1)
        # init with headers & body
        report2 = Report(headers=headers, body=body)
        self.assertEqual(report2.headers, headers)
        self.assertEqual(report2.body, body)
        hash2 = report2.hash
        self.assertIsNotNone(hash2)
        self.assertNotEqual(hash1, hash2)
        # init with headers, body & hash
        report3 = Report(headers=headers, body=body, hash_value=hash3)
        self.assertEqual(report3.headers, headers)
        self.assertEqual(report3.body, body)
        self.assertEqual(report3.hash, hash3)

    def test_equal(self):
        headers = {"sample": "text"}
        body = {"key1": True, "key2": 2, "key3": "three"}
        report1 = Report(headers=headers, body=body)
        report2 = Report(headers=headers, body=body, hash_value=12038192839219)
        self.assertEqual(report1, Report(headers=headers, body=body))
        self.assertNotEqual(report1, report2)

    def test_to_dict(self):
        headers = {"some_data": "some_value", "more_data": "another_value"}
        body = {"value1": 1, "value2": "string", "value3": False}
        hash_value = 123123123
        report = Report(headers=headers, body=body, hash_value=hash_value)
        self.assertEqual(
            report.to_dict(), {"headers": headers, "body": body, "hash": hash_value}
        )

    def test_hashing(self):
        """
        order of keys in dicts must not matter for hash
        """
        kvs = [["key1", 1], ["key2", 2], ["key3", 3]]
        headers1 = {}
        body1 = {}
        for kv in kvs:
            headers1[kv[0]] = kv[1]
            body1[kv[0]] = kv[1]
        report1 = Report(headers=headers1, body=body1)
        headers2 = {}
        body2 = {}
        for kv in list(reversed(kvs)):
            headers2[kv[0]] = kv[1]
            body2[kv[0]] = kv[1]
        report2 = Report(headers=headers2, body=body2)
        self.assertEqual(report1.hash, report2.hash)
