import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("🏅 Olympics Analysis")
st.sidebar.image('https://logos-world.net/wp-content/uploads/2021/09/Olympics-Symbol.png')
user_menu = st.sidebar.radio(
    '📌 Select an Option',
    ('🥇 Medal Tally', '📊 Overall Analysis', '🌍 Country-Wise Analysis')
)

st.markdown("""
    <style>
    .reportview-container {
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #262730;
        color: white;
    }
    h1, h2, h3 {
        color: #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

st.dataframe(df)

if user_menu == '🥇 Medal Tally':
    st.sidebar.header('🏆 Medal Tally')
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("📅 Select Year", years)
    selected_country = st.sidebar.selectbox("🌍 Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    st.title(f"🥇 Medal Tally: {selected_country} performance in {selected_year} Olympics")
    st.table(medal_tally)

if user_menu == '📊 Overall Analysis':
    st.title("📊 Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("📅 Editions")
        st.title(df['Year'].nunique())
    with col2:
        st.header("🏟 Hosts")
        st.title(df['City'].nunique())
    with col3:
        st.header("🏅 Sports")
        st.title(df['Sport'].nunique())

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("🎯 Events")
        st.title(df['Event'].nunique())
    with col2:
        st.header("🌍 Nations")
        st.title(df['region'].nunique())
    with col3:
        st.header("🏃 Athletes")
        st.title(df['Name'].nunique())

    countries_over_time = helper.countries_over_time(df)
    fig = px.line(countries_over_time, x="Year", y="count")
    st.title("🌍 Countries Over The Years")
    st.plotly_chart(fig)

    events_over_time = helper.events_over_time(df)
    fig = px.line(events_over_time, x="Year", y="count")
    st.title("📅 Events Over The Years")
    st.plotly_chart(fig)

    athletes_over_time = helper.athletes_over_time(df)
    fig = px.line(athletes_over_time, x="Year", y="count")
    st.title("🏅 Athletes Over The Years")
    st.plotly_chart(fig)

    st.title("🏆 Most Champion Athletes")
    list_of_sports = df['Sport'].unique().tolist()
    list_of_sports.sort()
    list_of_sports.insert(0, 'Overall')

    selected_sport = st.selectbox("Select a sport to view information 🏃", list_of_sports)
    a = helper.most_champion(df, selected_sport)
    st.table(a)

    st.markdown("### ✨ Keep exploring to discover more trends and insights! 🚀")

if user_menu == '🌍 Country-Wise Analysis':
    st.sidebar.title('🌍 Country-wise Analysis')
    country_list = sorted(df['region'].dropna().unique())
    selected_country = st.sidebar.selectbox("🌍 Select a Country", country_list)

    st.title(f"📈 Medal Tally of {selected_country} Over The Years")
    country_df = helper.year_wise_tally(df, selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.plotly_chart(fig)

    st.title(f"🏅 Top 10 Athletes from {selected_country}")
    topten_df = helper.most_champion_country_wise(df,selected_country)
    st.table(topten_df)