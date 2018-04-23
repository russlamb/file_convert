import argparse
import convert

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="name of the file to convert")
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--tsv_to_xl", help="indicates the input file is a tab delimited file and " +
                                                  "output should be Excel", action="store_true")
    group.add_argument("-c", "--csv_to_xl", help="indicates the input file is a comma delimited file and " +
                                                  "output should be Excel", action="store_true")
    parser.add_argument("-o", "--output", help="file path at which to save output")
    parser.add_argument("-s", "--sheetname", help="name of sheet where the data is saved")
    args = parser.parse_args()

    filename = args.filename

    converter = convert.FileConvert(filename)
    if args.tsv_to_xl:
        converter.save_tsv_as_xlsx(args.output)
    elif args.csv_to_xl:
        converter.save_csv_as_tsv(args.output)

