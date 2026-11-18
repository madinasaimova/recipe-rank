import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Recipe Ranking System",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Recipe Ranking System")

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/processed/ranked_recipes.csv"
)

df["recipe_id"] = df["recipe_id"].astype(int)

# ==========================================
# TOP 20 TABLE
# ==========================================

st.subheader("🏆 Top 20 Recipes")

top20 = (
    df.sort_values(
        by="final_score",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    top20,
    use_container_width=True
)

# ==========================================
# BAR CHART
# ==========================================

st.subheader("📊 Top 20 Final Scores")

st.bar_chart(
    top20.set_index("recipe_id")["final_score"]
)

# ==========================================
# SEARCH RECIPE
# ==========================================

st.subheader("🔍 Search Recipe")

recipe_id = st.selectbox(
    "Choose Recipe ID",
    sorted(df["recipe_id"].unique())
)

result = df[
    df["recipe_id"] == recipe_id
]

st.success(f"Recipe ID {recipe_id} found")

st.dataframe(
    result,
    use_container_width=True
)