import streamlit as st

st.set_page_config(
    page_title="Dashboard Absensi",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Dashboard Absensi Puskesmas")

st.sidebar.title("MENU")

menu = st.sidebar.radio(
    "",
    [
        "Dashboard",
        "Data Pegawai",
        "Data Absensi",
        "Statistik",
        "Peta",
        "Galeri Foto"
    ]
)

if menu == "Dashboard":
    st.header("Dashboard")

elif menu == "Data Pegawai":
    st.header("Data Pegawai")

elif menu == "Data Absensi":
    st.header("Data Absensi")

elif menu == "Statistik":
    st.header("Statistik")

elif menu == "Peta":
    st.header("Peta Lokasi")

elif menu == "Galeri Foto":
    st.header("Galeri Foto")

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(creds)

# Ganti dengan nama spreadsheet Anda
spreadsheet = client.open("AKUN")

# Sheet Pegawai
sheet_pegawai = spreadsheet.worksheet("Sheet1")
pegawai = pd.DataFrame(sheet_pegawai.get_all_records())

# Sheet Absen
sheet_absen = spreadsheet.worksheet("ABSEN")
absen = pd.DataFrame(sheet_absen.get_all_records())

print(pegawai.head())
print(absen.head())
