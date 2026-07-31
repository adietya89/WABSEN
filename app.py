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
