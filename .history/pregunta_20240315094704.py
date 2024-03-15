"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    #
    # Inserte su código aquí
    #

    df.dropna(axis=0, inplace=True)
    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    
    df["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )
        for date in df["fecha_de_beneficio"]
    ]
    


    for fila in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[fila] = df[fila].str.lower()
        df[fila] = df[fila].str.replace('_', ' ')
        df[fila] = df[fila].str.replace('-', ' ')

    return df

print(clean_data().sexo.value_counts().to_list())