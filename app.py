import streamlit as st
import random
import pandas as pd
import logging
from datetime import datetime

# ---------------- LOG CONFIG ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_event(message):
    logging.info(message)

log_event("Application démarrée")

# ---------------- APP CONFIG ----------------
st.set_page_config(
    page_title="Merch Niche Finder PRO",
    page_icon="🔥",
    layout="centered"
)

# ---------------- UI HEADER ----------------
st.image("logo.png", width=180)
st.title("🔥 Merch Niche Finder PRO")
st.caption("SEO • Niches gagnantes • IA • Business")

log_event("Interface chargée")

# ---------------- BASE DE DONNÉES SIMULÉE ----------------
BASE_NICHES = [
    "dog mom shirt",
    "cat lover shirt",
    "nurse life shirt",
    "gym motivation shirt",
    "funny dad shirt",
    "teacher quote shirt",
    "retro vintage shirt",
    "minimalist typography shirt",
]

# ---------------- FUNCTIONS ----------------
def generate_niches():
    log_event("Génération des niches")
    results = []
    for niche in random.sample(BASE_NICHES, 5):
        score = random.randint(60, 95)
        demand = random.choice(["Élevée", "Moyenne"])
        competition = random.choice(["Faible", "Moyenne"])

        results.append({
            "Niche": niche,
            "Demande": demand,
            "Concurrence": competition,
            "Score SEO": score
        })

        log_event(f"Niche générée : {niche} | Score : {score}")

    return pd.DataFrame(results)

def generate_prompt(niche):
    log_event(f"Génération prompt IA pour : {niche}")
    return f"""
Vintage minimalist t-shirt design,
theme: {niche},
retro colors,
high contrast,
centered composition,
print ready,
transparent background,
no mockup,
merch by amazon style
""".strip()

# ---------------- MAIN APP ----------------
st.markdown("## 🚀 Analyse automatique des niches")

if st.button("Trouver des niches gagnantes"):
    log_event("Bouton analyse cliqué")
    df = generate_niches()
    st.success("Analyse terminée")
    st.dataframe(df)

    selected_niche = st.selectbox(
        "🎯 Sélectionne une niche",
        df["Niche"]
    )

    if st.button("🎨 Générer prompt IA"):
        log_event(f"Bouton prompt IA cliqué | Niche : {selected_niche}")
        prompt = generate_prompt(selected_niche)
        st.subheader("🧠 Prompt IA Design")
        st.code(prompt)

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 Merch Niche Finder PRO")

log_event("Rendu final terminé")
