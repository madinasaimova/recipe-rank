import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading data...")

# Load data
interactions = pd.read_csv("data/raw/RAW_interactions.csv")

# Statistics for each recipe
recipe_stats = interactions.groupby("recipe_id").agg(
    avg_rating=("rating", "mean"),
    num_ratings=("rating", "count")
).reset_index()

# Global average rating
C = recipe_stats["avg_rating"].mean()

# Popularity threshold (90th percentile)
m = recipe_stats["num_ratings"].quantile(0.90)

print(f"Global average C = {C:.3f}")
print(f"Threshold m = {m:.3f}")

# Bayesian Rating
recipe_stats["bayesian_score"] = (
    (recipe_stats["num_ratings"] /
     (recipe_stats["num_ratings"] + m))
    * recipe_stats["avg_rating"]
    +
    (m /
     (recipe_stats["num_ratings"] + m))
    * C
)

# Popularity factor
recipe_stats["popularity_factor"] = np.log1p(
    recipe_stats["num_ratings"]
)

# Final score
recipe_stats["final_score"] = (
    recipe_stats["bayesian_score"]
    * recipe_stats["popularity_factor"]
)

# Top 10 recipes
top10 = recipe_stats.sort_values(
    by="final_score",
    ascending=False
).head(10)

print("\nTOP 10 RECIPES\n")

print(
    top10[
        [
            "recipe_id",
            "avg_rating",
            "num_ratings",
            "bayesian_score",
            "final_score"
        ]
    ]
)

# Save results
recipe_stats.to_csv(
    "data/processed/ranked_recipes.csv",
    index=False
)

print("\nResults saved!")


# ==========================================
# GRAPH 1
# Top 20 Recipes by Final Score
# ==========================================

top20 = recipe_stats.sort_values(
    by="final_score",
    ascending=False
).head(20)

plt.figure(figsize=(12, 6))

plt.bar(
    range(len(top20)),
    top20["final_score"],
    color="steelblue"
)

plt.title(
    "Top 20 Recipes by Final Score",
    fontsize=16
)

plt.xlabel("Recipe Rank")
plt.ylabel("Final Score")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    "plots/top20_recipes.png"
)

plt.close()

print("Top 20 chart saved!")


# ==========================================
# GRAPH 2
# Average Rating vs Number of Ratings
# ==========================================

plt.figure(figsize=(10, 6))

plt.scatter(
    recipe_stats["num_ratings"],
    recipe_stats["avg_rating"],
    alpha=0.2,
    s=10
)

plt.xscale("log")

plt.title(
    "Average Rating vs Number of Ratings",
    fontsize=16
)

plt.xlabel(
    "Number of Ratings (log scale)"
)

plt.ylabel(
    "Average Rating"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "plots/ratings_vs_popularity.png"
)

plt.close()

print("Scatter plot saved!")


# ==========================================
# GRAPH 3
# Comparison of Ranking Methods
# ==========================================

top10_avg = recipe_stats.sort_values(
    by="avg_rating",
    ascending=False
).head(10)

top10_final = recipe_stats.sort_values(
    by="final_score",
    ascending=False
).head(10)

fig, axes = plt.subplots(
    1,
    2,
    figsize=(14, 6)
)

axes[0].bar(
    range(len(top10_avg)),
    top10_avg["avg_rating"],
    color="tomato"
)

axes[0].set_title(
    "Top 10 by Average Rating"
)

axes[0].set_ylabel(
    "Average Rating"
)

axes[0].grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

axes[1].bar(
    range(len(top10_final)),
    top10_final["final_score"],
    color="seagreen"
)

axes[1].set_title(
    "Top 10 by Final Score"
)

axes[1].set_ylabel(
    "Final Score"
)

axes[1].grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    "plots/comparison_ranking_methods.png"
)

plt.close()

print("Comparison chart saved!")