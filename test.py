from .main import save_csv_as_tsv, save_tsv_as_xlsx

if __name__ == "__main__":
    tsv_file = save_csv_as_tsv("FL_insurance_sample.csv")
    xlsx_file = save_tsv_as_xlsx(tsv_file)
