import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

datapath = Path(__file__).parent / "data" / "fifa_players_22.csv"

fifa22 = pd.read_csv(datapath)

# Prendre que les 100 premiers joueurs

fifa100 = fifa22.head(100)

player_names = fifa100[["short_name"]]

st.write("# Dashboard joueurs FIFA 2022")

single_player = st.checkbox("Etudier un joueur en particulier ? ")

if single_player:
    st.sidebar.markdown("# Choisir un joueur de foot")
    selected_player = st.sidebar.selectbox("Players", player_names)
    player_row = fifa100[fifa100["short_name"] == selected_player]
    st.dataframe(player_row)

if not single_player:
    st.dataframe(fifa100)
    fig, ax = plt.subplots()
    ax.hist(fifa100["wage_eur"], bins=20, edgecolor = 'black')
    st.pyplot(fig)



