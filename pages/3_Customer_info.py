import streamlit as st
import pandas as pd
from sqlalchemy import text
from static.functions import sql_table

conn = st.connection("phi_server",type='sql')

# academic year selector
acad_year=st.sidebar.selectbox("Ακαδημαϊκό έτος",
                                ("2022-2023","2023-2024", "2024-2025", "2025-2026"),
                                index=2)

# start and end date of each academic year
acad_years={"2022-2023": ("'2022-06-20'","'2023-06-18'"),
            "2023-2024": ("'2023-06-19'","'2024-06-16'"),
            "2024-2025": ("'2024-06-17'","'2025-06-15'"),
            "2025-2026": ("'2025-06-15'","'2026-06-14'")}

# start and end date of selected academic year
start=acad_years[acad_year][0]
stop=acad_years[acad_year][1]

customer_names=conn.query(f"SELECT customer_id, customer_name, surname FROM customers WHERE active;")
customer_names=customer_names.set_index(customer_names['customer_name']+' '+customer_names['surname']).sort_values('customer_name')
customer_dict =customer_names['customer_id'].to_dict()
selected_customer=st.sidebar.selectbox("Όνομα:",customer_names.index)

customer_info=conn.query(f"SELECT * FROM customers WHERE customer_id = '{customer_dict[selected_customer]}';")

s_duration = sql_table('static/sql/customer_info/s_duration.sql',conn,acad_year,start,stop,(customer_dict[selected_customer]))

st.header(customer_info['customer_name'].iloc[0])
st.subheader(customer_info['surname'].iloc[0])

st.divider()
st.markdown('#### Στοιχεία επικοινωνίας')
# col1, col2 = st.columns(2)

# with col1:
#     st.write('Τηλέφωνο: '+customer_info['mobile'].iloc[0])
#     st.write('email: '+customer_info['email'].iloc[0])

# with col2:
#     st.write('Διεύθυνση:')
#     st.write(customer_info['address'].iloc[0])
#     st.write(customer_info['zip'].iloc[0]+', '+
#              customer_info['region'].iloc[0]+', '+
#              customer_info['city'].iloc[0])

col1, col2 = st.columns(2)

with col1:
    st.table(s_duration)