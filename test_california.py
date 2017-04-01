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

    def test_that_dataset_unpack_dir_exists(self):
        self.assertTrue(os.path.exists(ca_prop_tax.local_data_dir))

    def test_that_dataset_unpacks_successfully(self):
        self.assertNotEqual(os.listdir(ca_prop_tax.local_data_dir), [])

    def test_that_unpacked_excel_workbook_can_be_read(self):
        self.assertTrue(os.path.exists(
                         ca_prop_tax.stats_db_doc))

if __name__ == '__main__':
    unittest.main()
