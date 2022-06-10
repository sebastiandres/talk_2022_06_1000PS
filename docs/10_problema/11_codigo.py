import streamlit as st

st.markdown("# El código")
st.markdown("""
Imaginemos que hemos desarrollado 2 funciones:
* Leer un dataframe, adivinando el encoding, y retornando un dataframe de pandas + encoding.
* Guardar un dataframe (o un diccionario de strings:dataframes) en un archivo excel.
""")

with st.expander("Leer un csv genérico"):
    st.code('''
def read_csv(csv_filename, sep=";", encoding="Infer from data"):
    """
    Reads a csv file, trying to guess the best encoding
    """
    # Guess the encoding
    if encoding == "Infer from data":
        with open(csv_filename, "rb") as file_handler:
            data = file_handler.read()
        analysis = chardet.detect(data[:10000])
        encoding = analysis["encoding"]
    df = pd.read_csv(csv_filename, dtype="str", sep=sep, encoding=encoding)
    return df, encoding
    ''')

with st.expander("Guardar dataframes en un excel"):
    st.code('''
def save_to_excel(excel_filepath, df_dict):
    """
    Save dataframe to excel file
    """
    print(f"Saving dataframes to {excel_filepath}")
    with pd.ExcelWriter(excel_filepath) as ew:
        for sheet_name, df in df_dict.items():
            df.to_excel(ew, sheet_name=sheet_name, index=False)
    print(f"open {excel_filepath}")
    return
    ''')

with st.expander("Ejemplo de uso"):
    st.code('''
df, guessed_encoding = read_csv(csv_filename, sep=user_separator)
excel_filepath = csv_filename.replace(".csv", ".xlsx")
save_to_excel(excel_filepath, {"original csv":df})
''')

st.markdown("¿Cómo compartimos este código *fácilmente*?")
