from openpyxl import Workbook


class FileConvert():
    @staticmethod
    def convert_csv_to_tsv(filename):
        with open(filename) as f:
            contents=f.read()
        return contents.replace(",","\t")

    @staticmethod
    def save_csv_as_tsv(filename):
        contents = FileConvert.convert_csv_to_tsv(filename)
        tsv_filename = filename + ".tsv"
        with open(tsv_filename, "w") as f:
            f.write(contents)

        return tsv_filename


    @staticmethod
    def save_tsv_as_xlsx(filename):
        with open(filename) as f:
            contents = f.readlines()


        items=[c.split("\t") for c in contents]
        wb = Workbook(write_only=True)
        ws=wb.create_sheet("data")
        row_count=0
        for row in items:
            ws.append(row)
            row_count+=1
            if row_count % 10000==0:
                print("processing row {}".format(row_count))

        new_filename=filename+".xlsx"
        wb.save(new_filename)
        return new_filename