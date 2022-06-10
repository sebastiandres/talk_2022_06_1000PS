import streamlit as st
import pandas as pd
import chardet
import contextlib

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

@contextlib.contextmanager
def skip_echo():
    yield None

show_code = st.checkbox("Mostrar código")
with st.echo("above") if show_code else skip_echo():
    c1, c2, c3 = st.columns([10,3,3])
    uploaded_file = c1.file_uploader("Cargar csv", type=['csv'])
    user_separator = c2.selectbox("Separator", [",", ";", 'tab', '-']).replace("tab", "\t")
    user_encoding = c3.selectbox("Encoding", ["latin1", "cp1250", "utf8", "Infer from data"])
    if uploaded_file is not None:
        uploaded_file.seek(0) # Auxiliar trick required to find the file
        csv_filename = f"tmp/{uploaded_file.name}" 
        with open(csv_filename, 'wb') as fh:
            fh.write(uploaded_file.getvalue())
        # Read file
        df, guessed_encoding = read_csv(csv_filename, sep=user_separator, encoding=user_encoding)
        if guessed_encoding != user_encoding:
            c3.success(f"File has encoding {guessed_encoding}")
        # Process file
        with st.expander("Info - First 10 lines:"):
            st.write(df.head(10))
        df_describe = df.describe(include="all").fillna("").T
        with st.expander("OK - File description:"):
            st.write(df_describe)
        # Write excel file
        excel_filepath = csv_filename.replace(".csv", ".xlsx")
        save_to_excel(excel_filepath, {"original csv":df, "description":df_describe})
        # Download
        with open(excel_filepath, "rb") as file_content:
            st.download_button(label="Descargar excel", data=file_content, file_name=excel_filepath)