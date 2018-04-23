from openpyxl import Workbook


class FileConvert():
    def __init__(self, filename):
        self.filename = filename

    def convert_csv_to_tsv(self):
        with open(self.filename) as f:
            contents = f.read()
        return contents.replace(",", "\t")

    def save_csv_as_tsv(self, output_path=None):
        filename = self.filename
        contents = self.convert_csv_to_tsv()
        tsv_filename = filename + ".tsv" if not output_path else output_path
        with open(tsv_filename, "w") as f:
            f.write(contents)

        return tsv_filename

    def save_tsv_as_xlsx(self, output_path=None):
        filename = self.filename
        with open(filename) as f:
            contents = f.readlines()

        items = [c.split("\t") for c in contents]
        wb = Workbook(write_only=True)
        ws = wb.create_sheet("data")
        row_count = 0
        for row in items:
            ws.append(row)
            row_count += 1
            if row_count % 10000 == 0:
                print("processing row {}".format(row_count))

        new_filename = filename + ".xlsx" if not output_path else output_path
        wb.save(new_filename)
        return new_filename
