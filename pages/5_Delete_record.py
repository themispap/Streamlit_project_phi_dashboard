import streamlit as st
from static.functions import delete_record

conn = st.connection("phi_server",type='sql')

with st.form("delete_record"):
    st.write("Διαγραφή καταχώρησης")
    entry={}
    entry['table']=st.text_input('Πίνακας')
    entry['id']=st.text_input('Κελί')
    entry['value']=st.text_input('Τιμή')
   
    submitted = st.form_submit_button("Διαγραφή")
    if submitted:
        delete_record(conn,entry['table'],entry['id'],entry['value'])