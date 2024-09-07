import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title = "My Sales Dashboard", page_icon = ":bar_chart",layout='wide')
df = pd.read_csv('all_df.csv')
st.sidebar.header('Please Filter Here')
product_name = st.sidebar.multiselect(
    "Select Product:",
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5]

)
city_name = st.sidebar.multiselect(
    "Select City:",
    options = df['City'].unique(),
     default = df['City'].unique()[:5]
)
                 
month_name = st.sidebar.multiselect(
    "Select Month:",
    options = df['Month'].unique(),
     default = df['Month'].unique()[:5]
)
                 


st.title(':bar_chart: Sales Dashboard for 2019')
total_sales = df['Total'].sum()
product_num = df['Product'].nunique()
left_col, right_col = st.columns(2)
#a, b, c, d, e = st.columns(5)
with left_col:
        st.subheader('Total Sales')
        st.subheader(f"US$ {total_sales}")
with right_col:
        st.subheader('Number of Product')
        st.subheader(f"US$ {product_num}")
df_select = df.query("City == @city_name and Month == @month_name and Product == @product_name")

sales_by_product = df_select.groupby('Product')['Total'].sum().sort_values()
fig_product = px.bar(
    sales_by_product,
    x = sales_by_product.values,
    y = sales_by_product.index,
    orientation = 'h',
    title = "Sales by Product"
)

a_col, b_col, c_col = st.columns(3)
a_col.plotly_chart(fig_product, use_container_width = True)

sales_by_month = df_select.groupby('Month')['Total'].sum().sort_values()
fig_month = px.bar(
    sales_by_month,
    x = sales_by_month.values,
    y = sales_by_month.index,
    orientation = 'h',
    title = "Sales by Month"
)

c_col.plotly_chart(fig_month, use_container_width = True)

fig_month_pie = px.pie(
    df_select,
    values = 'Total',
    names = 'City',
    title = "Sales by City"
)

b_col.plotly_chart(fig_month_pie, use_container_width = True)

t1_col, t2_col = st.columns(2)


sales_city = px.line(
     x = sales_by_month.values,
    y = sales_by_month.index,
   title = "Sales by Month"
)

t1_col.plotly_chart(sales_city, use_container_width = True)

sales_city_scatter = px.scatter(
    df,
    x = 'Total',
    y = 'QuantityOrdered',
    title = "Sales of Item Amount"
)

t2_col.plotly_chart(sales_city_scatter, use_container_width = True)
