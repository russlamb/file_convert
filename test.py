import os
import unittest

from convert import FileConvert

def delete_files_if_exists(path_list):
    for path in path_list:
        if os.path.exists(path):
            os.remove(path)

class TestConvert(unittest.TestCase):
    def setUp(self):

        delete_files_if_exists(["samples/FL_insurance_sample.csv.tsv", "samples/FL_insurance_sample.csv.tsv.xlsx",
                                "samples/FL_insurance_sample.csv.xlsx",
                                "samples/my_tsv.tsv","samples/my_output.xlsx"])

    def tearDown(self):

        delete_files_if_exists(["samples/FL_insurance_sample.csv.tsv", "samples/FL_insurance_sample.csv.tsv.xlsx",
                                "samples/FL_insurance_sample.csv.xlsx",
                                "samples/my_tsv.tsv","samples/my_output.xlsx"])

    def test_convert_csv_xl(self):

        csv = "samples/FL_insurance_sample.csv"
        converter = FileConvert(csv)
        tsv_file = converter.save_csv_as_tsv()
        self.assertTrue (os.path.exists(tsv_file))
        self.assertTrue (tsv_file==(csv+".tsv"))

        converter = FileConvert(tsv_file)
        xlsx_file = converter.save_tsv_as_xlsx()
        self.assertTrue (os.path.exists(xlsx_file))
        self.assertTrue (xlsx_file==(tsv_file+".xlsx"))

    def test_with_output_path(self):

        csv = "samples/FL_insurance_sample.csv"
        converter = FileConvert(csv)
        tsv_file = converter.save_csv_as_tsv(output_path="samples/my_tsv.tsv")
        self.assertTrue (os.path.exists(tsv_file))
        self.assertFalse ((tsv_file==(csv+".tsv")))

        converter = FileConvert(tsv_file)
        xlsx_file = converter.save_tsv_as_xlsx(output_path="samples/my_output.xlsx")
        self.assertTrue (os.path.exists(xlsx_file))
        self.assertFalse ((xlsx_file==(tsv_file+".xlsx")))

if __name__ == "__main__":
    unittest.main()
