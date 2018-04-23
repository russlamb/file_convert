import os
import unittest

from convert import FileConvert

def delete_files_if_exists(path_list):
    for path in path_list:
        if os.path.exists(path):
            os.remove(path)

class TestConvert(unittest.TestCase):
    def setUp(self):

        delete_files_if_exists(["samples/FL_insurance_sample.tsv", "samples/FL_insurance_sample.csv.tsv.xlsx",
                                "samples/FL_insurance_sample.csv.xlsx",
                                "samples/my_tsv.tsv","samples/my_output.xlsx"])


    def test_convert_csv_xl(self):

        csv = "samples/FL_insurance_sample.csv"
        converter = FileConvert(csv)
        tsv_file = converter.save_csv_as_tsv(csv)
        assert (os.path.exists(tsv_file))
        xlsx_file = converter.save_tsv_as_xlsx(tsv_file)
        assert (os.path.exists(xlsx_file))

    def convert_with_output_path(self):
        csv = "samples/FL_insurance_sample.csv"
        converter = FileConvert(csv)
        tsv_file = converter.save_csv_as_tsv(csv, "my_tsv.tsv")
        assert (os.path.exists(tsv_file))
        xlsx_file = converter.save_tsv_as_xlsx(tsv_file, "my_output.xlsx")
        assert (os.path.exists(xlsx_file))

if __name__ == "__main__":
    unittest.main()
