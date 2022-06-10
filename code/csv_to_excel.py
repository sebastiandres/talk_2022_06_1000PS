import pandas as pd
import chardet
import sys

def read_csv(csv_filename, sep=";", encoding="Infer from data"):
    """
    Reads a csv file, trying to guess the best encoding
    """
    # Guess the encoding
    import pandas as pd
    import chardet
    if encoding == "Infer from data":
        with open(csv_filename, "rb") as file_handler:
            data = file_handler.read()
        analysis = chardet.detect(data[:10000])
        encoding = analysis["encoding"]
    df = pd.read_csv(csv_filename, dtype="str", sep=sep, encoding=encoding)
    return df, encoding

def save_to_excel(excel_filepath, df_dict):
    """
    Save dataframe to excel file
    """
    import pandas as pd
    print(f"Saving dataframes to {excel_filepath}")
    with pd.ExcelWriter(excel_filepath) as ew:
        for sheet_name, df in df_dict.items():
            df.to_excel(ew, sheet_name=sheet_name, index=False)
    print(f"open {excel_filepath}")
    return

if __name__=="__main__":
    if len(sys.argv)!=4:
        print("\nUse as:\n\tpython csv_to_excel.py <csv_file> <separator> <encoding>")
        print("\nExample:\n\tpython csv_to_excel.py ../ejemplos/hard_file.csv ',' latin1\n")
    else:
        csv_filename = sys.argv[1]
        user_separator = sys.argv[2]
        user_encoding = sys.argv[3]
        df, guessed_encoding = read_csv(csv_filename, sep=user_separator, encoding=user_encoding)
        print(df)
        excel_filepath = csv_filename.replace(".csv", ".xlsx")
        save_to_excel(excel_filepath, {"original csv":df})
        print("Excel file:", excel_filepath)