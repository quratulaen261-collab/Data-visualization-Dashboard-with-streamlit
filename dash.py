import streamlit as st 
import pandas as pd 
import plotly.express as px 

movies = pd.read_csv("D:\\data visualization dashboard\\movies.csv")
reviews = pd.read_csv("D:\\data visualization dashboard\\reviews.csv")
covid = pd.read_csv("D:\\data visualization dashboard\\covid.csv")
sales = pd.read_csv("D:\\data visualization dashboard\\sales.csv")

st.set_page_config(layout="wide")  
st.title("Data Visualization Dashboard")
st.sidebar.title("Dashboard")
st.sidebar.subheader("Choose a Dataset")

dataset = st.sidebar.selectbox("Dataset", ["Movies", "Covid", "Sales", "Reviews"])
if dataset == "Sales":
    st.subheader("Sales Dataset")
    st.write(sales.head())
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sales", f"${sales['sales'].sum():,.0f}")
    with col2:
        st.metric("Average Profit", f"${sales['profit'].mean():,.0f}")
    with col3:
        st.metric("Total Orders", f"{sales.shape[0]}")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(sales, x="date", y="sales", title="Sales Over Time")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.bar(sales, x="region", y="sales", title="Region-wise Sales", color="region")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Product-wise Distribution")
    fig3 = px.pie(sales, names="product", values="sales", title="Sales by Product", hole=0.4)
    st.plotly_chart(fig3, use_container_width=True)
elif dataset == "Reviews":
    st.subheader("Reviews Dataset")
    st.write(reviews.head())

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Reviews", f"{reviews.shape[0]}")
    with col2:
        st.metric("Avg Rating", f"{reviews['rating'].mean():.2f}")
    with col3:
        st.metric("Products Reviewed", f"{reviews['product'].nunique()}")
    col1, col2 = st.columns(2)
    with col1:
        avg_rating = reviews.groupby("product")["rating"].mean().reset_index()
        fig1 = px.bar(avg_rating, x="product", y="rating", title="Average Rating per Product", color="product")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.pie(reviews, names="rating", title="Rating Distribution")
        st.plotly_chart(fig2, use_container_width=True)
elif dataset == "Covid":
    st.subheader("🦠 Covid Dataset")
    st.write(covid.head())

    # KPIs
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Cases", f"{covid['cases'].sum():,}")
    with col2:
        st.metric("Total Recovered", f"{covid['recovered'].sum():,}")
    with col3:
        st.metric("Total Deaths", f"{covid['deaths'].sum():,}")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(covid, x="country", y="cases", title="Cases by Country", color="country")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.line(covid, x="country", y=["cases", "recovered"], title="Cases vs Recovered")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Deaths Distribution")
    fig3 = px.pie(covid, names="country", values="deaths", title="Deaths by Country", hole=0.4)
    st.plotly_chart(fig3, use_container_width=True)
elif dataset == "Movies":
    st.subheader("🎬 Movies Dataset")
    st.write(movies.head())

    # KPIs
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Movies", f"{movies.shape[0]}")
    with col2:
        st.metric("Avg Rating", f"{movies['rating'].mean():.2f}")
    with col3:
        st.metric("Total Revenue", f"${movies['revenue'].sum():,}")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(movies, x="genre", y="rating", title="Genre vs Avg Rating", color="genre")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.scatter(movies, x="rating", y="revenue", size="revenue", color="genre",
                          title="Rating vs Revenue")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Genre Distribution")
    fig3 = px.pie(movies, names="genre", title="Genre Distribution", hole=0.4)
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.write("Plz select a dataset")
