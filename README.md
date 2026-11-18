Recipe Ranking System

Overview

This project proposes a ranking system for online recipes using the Food.com dataset.

The goal is to create a ranking that considers not only average ratings but also recipe popularity.

Dataset

Food.com Recipes and Interactions Dataset

231,637 recipes
1,132,367 user interactions
Methodology

Average Rating

AR = sum(ratings) / n

Bayesian Rating

BR = (v/(v+m))*R + (m/(v+m))*C

where:

R = average recipe rating
v = number of ratings
C = global average rating
m = popularity threshold
Proposed Score

FinalScore = BR × log(1 + v)

This score rewards both quality and popularity.

Technologies

Python
Pandas
NumPy
Matplotlib
Streamlit
Visualizations

Distribution of Final Scores
Ratings vs Popularity
How to Run

Install dependencies:

pip install -r requirements.txt

Run ranking:

python src/ranking.py

Run dashboard:

streamlit run streamlit_app.py

Results

The proposed ranking system produces more reliable rankings than a simple average rating because it balances score quality and popularity.

Visualizations

Top 20 Recipes by Final Score
Average Rating vs Number of Ratings
Comparison of Average Rating Ranking and Final Score Ranking