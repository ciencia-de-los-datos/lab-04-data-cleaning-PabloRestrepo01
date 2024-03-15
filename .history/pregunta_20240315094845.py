"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import re
from datetime import datetime

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.copy()

    df.dropna(inplace=True)  # eliminar filas vacias

    df["sexo"] = df["sexo"].str.lower()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["idea_negocio"] = [
        str.lower(idea.replace("_", " ").replace("-", " "))
        for idea in df["idea_negocio"]
    ]

    df.barrio = [
        str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in df.barrio
    ]

    df["barrio"] = [
        str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in df["barrio"]
    ]


    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df["estrato"] = df["estrato"].astype(int)

    df["línea_credito"] = [
        fila.replace("-", " ").replace("_", " ").replace(". ", ".")
        for fila in df["línea_credito"]
    ]
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip()  ##

    df["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )
        for date in df["fecha_de_beneficio"]
    ]

    df["monto_del_credito"] = [
        int(monto.replace("$ ", "").replace(".00", "").replace(",", ""))
        for monto in df["monto_del_credito"]
    ]
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)  ##
    df.drop_duplicates(inplace=True)

    return df

print(clean_data().tipo_de_emprendimiento.value_counts().to_list())