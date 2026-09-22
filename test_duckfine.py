import unittest

from DuckFine import DuckFine

class TestDuckFine(unittest.TestCase):
    def test_initializes_member_id(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.member_id, "member-123")

    def test_initializes_total_owed_to_zero(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.total_owed, 0.0)

    def test_grace_period_has_no_fee(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(2), 0.0)

    def test_charges_daily_fee_after_grace_period(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(4), 1.0)

    def test_deluxe_fee_is_doubled(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(4, deluxe=True), 2.0)

    def test_fee_is_capped_at_maximum(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(20), 5.0)

    def test_fee_is_added_to_total_owed(self):
        fine = DuckFine("member-123")

        fine.charge(4)
        fine.charge(3)

        self.assertEqual(fine.total_owed, 1.5)

    def test_negative_days_late_are_rejected(self):
        fine = DuckFine("member-123")

        with self.assertRaises(ValueError):
            fine.charge(-1)


if __name__ == "__main__":
    unittest.main()