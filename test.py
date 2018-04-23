import os
import unittest

from convert import FileConvert


class TestConvert(unittest.TestCase):
    def test_convert_csv_xl(self):
        csv = "samples/FL_insurance_sample.csv"
        converter = FileConvert(csv)
        tsv_file = converter.save_csv_as_tsv(csv)
        assert (os.path.exists(tsv_file))
        xlsx_file = converter.save_tsv_as_xlsx(tsv_file)
        assert (os.path.exists(xlsx_file))


if __name__ == "__main__":
    unittest.main()
