from .main import save_csv_as_tsv, save_tsv_as_xlsx
import unittest
import os,io

class TestConvert(unittest.TestCase):

    def test_convert_csv_xl(self):
        tsv_file = save_csv_as_tsv("FL_insurance_sample.csv")
        assert(os.path.exists(tsv_file))
        xlsx_file = save_tsv_as_xlsx(tsv_file)
        assert(os.path.exists(xlsx_file))


if __name__ == "__main__":
    unittest.main()
