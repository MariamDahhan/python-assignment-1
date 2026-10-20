import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pipeline.validator import validate_record
import unittest





class TestValidator(unittest.TestCase):

    def test_valid_record(self):

        record = {
            "branch_id": "B001",
            "date": "2026-10-01",
            "customer_tier": "Gold",
            "items": 5,
            "revenue": 100
        }

        self.assertIsNotNone(validate_record(record))

    def test_negative_revenue(self):

        record = {
            "branch_id": "B001",
            "date": "2026-10-01",
            "customer_tier": "Gold",
            "items": 5,
            "revenue": -100
        }

        self.assertIsNone(validate_record(record))

    def test_missing_branch_id(self):

        record = {
            "branch_id": "",
            "date": "2026-10-01",
            "customer_tier": "Gold",
            "items": 5,
            "revenue": 100
        }

        self.assertIsNone(validate_record(record))


if __name__ == "__main__":
    unittest.main()
