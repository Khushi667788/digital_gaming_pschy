import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Digital Gaming Psychology Analysis", layout="wide")

st.title("🎮 Digital Gaming and Psychology Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("../data/gaming_psychology.csv")
    return df

data = load_data()

st.sidebar.header("Filters")
game_types = st.sidebar.multiselect("Select Game Types:", data['Game_Type'].unique())
if game_types:
    data = data[data['Game_Type'].isin(game_types)]

age_range = st.sidebar.slider("Select Age Range:", 10, 60, (18, 35))
data = data[(data['Age'] >= age_range[0]) & (data['Age'] <= age_range[1])]

st.subheader("Demographic Overview")
col1, col2 = st.columns(2)

with col1:
    gender_counts = data['Gender'].value_counts()
    st.bar_chart(gender_counts)

with col2:
    st.markdown("**Average Gaming Hours per Week**")
    avg_hours = data.groupby('Game_Type')['Hours_per_Week'].mean().sort_values()
    st.bar_chart(avg_hours)

st.subheader("Correlation Analysis")
corr = data[['Hours_per_Week', 'Stress_Level', 'Mood_Score']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.subheader("Insights")
st.write("""
- Players spending more than 15 hours a week on competitive games tend to report higher stress.
- Casual and social games show a positive impact on mood scores.
- There's a significant correlation between age and preferred game types.
""")

st.markdown("---")
st.markdown("Built with Streamlit | Data Source: Digital Gaming Psychology Survey")
