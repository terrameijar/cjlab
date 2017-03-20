import os
import unittest
import california_property_taxes as ca_prop_tax


class CaliforniaTaxTest(unittest.TestCase):

    def test_dataset_contains_correct_url(self):
        self.assertEqual(ca_prop_tax.data,
                         'http://www2.census.gov/govs/statetax/stcfy16.zip')

    def test_that_dataset_is_saved_locally(self):
        self.assertTrue(os.path.exists(
                         ca_prop_tax.local_zipname))


if __name__ == '__main__':
    unittest.main()
