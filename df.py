import pandas as pd

import streamlit as st
import openpyxl

st.set_page_config(page_title="Education dashboard",page_icon="",layout="wide")

fl = st.file_uploader(":file_folder: Télécharger un fichier",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    df=pd.read_excel(
	io="Dashboard actuel.xlsx",
	engine='openpyxl',
	sheet_name='Elev_effec',
	skiprows=0,
	usecols='A:J',
	nrows=631,
)	

st.sidebar.header("Filtrer ici:")

annees=st.sidebar.multiselect("Selectionner une période",options=df["ANNEE_SCOLAIRE"].unique(),default=df["ANNEE_SCOLAIRE"].unique())

Régions=st.sidebar.multiselect("Selectionner une région",options=df["REGIONS"].unique())

Zones=st.sidebar.multiselect(
	"Selectionner une zone",
	options=df["ZONES"].unique()
	)

SS=st.sidebar.multiselect(
	"Selectionner un sous-système",
	options=df["SOUS_SYSTEME"].unique()
	)

OD=st.sidebar.multiselect(
	"Selectionner un ordre d'enseignement",
	options=df["ORDRE_ENSEIGENEMENT"].unique()
	)

SOD=st.sidebar.multiselect(
	"Selectionner un sous-ordre d'enseignement",
	options=df["SOUS_ORDRE_ENSEIGENEMENT"].unique()
	)

classe=st.sidebar.multiselect(
	"Selectionner une classe",
	options=df["CLASSE"].unique()
	)

filtre1=st.sidebar.multiselect(
	"Selectionner un filtre",
	options=df["FILTRE_1"].unique()
	)

genre=st.sidebar.multiselect(
	"Selectionner un genre",
	options=df["CRITERES_1"].unique()
	)

#Filtrer les données
if not annees and not Régions and not Zones and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df
#Filtre Unique
elif not annees and not Zones and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(REGIONS==@Régions)")
elif not annees and not Régions and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ZONES==@Zones)")
elif not annees and not Régions and not Zones and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(SOUS_SYSTEME==@SS)")
elif not annees and not Régions and not Zones and not SS and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ORDRE_ENSEIGENEMENT==@OD)")
elif not annees and not Régions and not Zones and not SS and not OD and not classe and not filtre1 and not genre:
	df_selection = df.query("(SOUS_ORDRE_ENSEIGENEMENT==@SOD)")
elif not annees and not Régions and not Zones and not SS and not OD and not SOD and not filtre1 and not genre:
	df_selection = df.query("(CLASSE==@classe)")
#Filtre total
elif not Régions and not Zones and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees)")
elif not Zones and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions)")
elif not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions) and (ZONES==@Zones)")
elif not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions) and (ZONES==@Zones and (SOUS_SYSTEME==@SS))")
elif not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions) and (ZONES==@Zones and (SOUS_SYSTEME==@SS) and (ORDRE_ENSEIGENEMENT==@OD))")	
elif not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions) and (ZONES==@Zones and (SOUS_SYSTEME==@SS) and (ORDRE_ENSEIGENEMENT==@OD) and (SOUS_ORDRE_ENSEIGENEMENT==@SOD))")	
elif not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions) and (ZONES==@Zones and (SOUS_SYSTEME==@SS) and (ORDRE_ENSEIGENEMENT==@OD) and (SOUS_ORDRE_ENSEIGENEMENT==@SOD) and (CLASSE==@classe))")
elif not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions) and (ZONES==@Zones and (SOUS_SYSTEME==@SS) and (ORDRE_ENSEIGENEMENT==@OD) and (SOUS_ORDRE_ENSEIGENEMENT==@SOD) and (CLASSE==@classe) and (FILTRE_1==@filtre1))")
elif annees and  Régions and  Zones and  SS and  OD and  SOD and  classe and  filtre1 and  genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions) and (ZONES==@Zones and (SOUS_SYSTEME==@SS) and (ORDRE_ENSEIGENEMENT==@OD) and (SOUS_ORDRE_ENSEIGENEMENT==@SOD) and (CLASSE==@classe) and (FILTRE_1==@filtre1) and (CRITERES_1==@genre))")




st.dataframe(df_selection)










