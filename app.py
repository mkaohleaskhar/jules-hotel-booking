import streamlit as st
import pandas as pd
import zipfile
import plotly.express as px

# Load the data
@st.cache_data
def load_data():
    with zipfile.ZipFile('archive (3).zip', 'r') as z:
        with z.open('hotel_booking.csv') as f:
            df = pd.read_csv(f)
    return df

df = load_data()

# Clean the data
df['company'].fillna(0, inplace=True)
df['agent'].fillna(0, inplace=True)
df['country'].fillna(df['country'].mode()[0], inplace=True)
df.drop(['credit_card', 'phone-number'], axis=1, inplace=True)

# App title
st.title('Hotel Booking Data Analysis')

# Sidebar for user input
st.sidebar.header('Filter Data')
hotel_type = st.sidebar.selectbox('Select Hotel Type', df['hotel'].unique())

# Filter data based on user input
filtered_df = df[df['hotel'] == hotel_type]

# Display some basic info
st.header(f'Data for {hotel_type} Hotel')
st.write(filtered_df.head())

# Visualizations
st.header('Visualizations')

# Booking Status
st.subheader('Booking Status')
fig = px.pie(filtered_df, names='is_canceled', title='Booking Status')
st.plotly_chart(fig)

# Bookings by month
st.subheader('Bookings by Month')
fig = px.bar(filtered_df, x='arrival_date_month', title='Bookings by Month', category_orders={'arrival_date_month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']})
st.plotly_chart(fig)

# Cancellations by month
st.subheader('Cancellations by Month')
cancellations = filtered_df[filtered_df['is_canceled'] == 1]
fig = px.bar(cancellations, x='arrival_date_month', title='Cancellations by Month', category_orders={'arrival_date_month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']})
st.plotly_chart(fig)
