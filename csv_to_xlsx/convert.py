from openpyxl import Workbook


class FileConvert():
    def __init__(self, filename):
        self.filename = filename

    def convert_csv_to_tsv(self):
        with open(self.filename, "r") as f:
            contents = f.read()
        return contents.replace(",", "\t")

    def save_csv_as_tsv(self, output_path=None):
        filename = self.filename
        contents = self.convert_csv_to_tsv()
        if output_path is None:
            tsv_filename = (filename + ".tsv")
        else:
            tsv_filename = output_path

        print("Saving TSV file as {}".format(tsv_filename))
        with open(tsv_filename, "w") as f:
            f.write(contents)

        return tsv_filename

    def save_tsv_as_xlsx(self, output_path=None, sheet_name="data"):
        filename = self.filename
        with open(filename, "r") as f:
            contents = f.readlines()

        new_filename = (filename + ".xlsx") if output_path is None else output_path

        items = [c.split("\t") for c in contents]
        wb = Workbook(write_only=True)
        ws = wb.create_sheet(sheet_name)
        row_count = 0
        for row in items:
            ws.append(row)
            row_count += 1
            if row_count % 10000 == 0:
                print("processing row {}".format(row_count))


        print("Saving Excel file as {}".format(new_filename))
        wb.save(new_filename)
        return new_filename
