import streamlit as st
import pandas as pd

st.title("Recipe Ranking System")

df = pd.read_csv(
    "data/processed/ranked_recipes.csv"
)

# TOP 20
st.subheader("Top 20 Recipes")

top20 = df.sort_values(
    by="final_score",
    ascending=False
).head(20)

st.dataframe(top20)

# График
st.subheader("Top 20 Final Scores")

st.bar_chart(
    top20.set_index("recipe_id")["final_score"]
)

# Поиск рецепта
st.subheader("Search Recipe")

recipe_id = st.number_input(
    "Recipe ID",
    min_value=1,
    step=1
)

result = df[
    df["recipe_id"] == recipe_id
]

if not result.empty:
    st.success("Recipe found")
    st.dataframe(result)
else:
    st.warning("Recipe not found")