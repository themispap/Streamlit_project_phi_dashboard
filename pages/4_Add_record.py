import streamlit as st
import pandas as pd
import static.functions as sf

conn = st.connection("phi_server",type='sql')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Νέο γεγονός',
                                        'Καταχώρηση εξόδου',
                                        'Καταχώρηση εσόδου',
                                        'Νέος πελάτης',
                                        'Νέος μαθητής'])

with tab1:
    with st.form("new_record"):
        st.write("Νέο γεγονός")
        entry={}
        entry['record_date']=st.date_input('Ημερομηνία')
        entry['duration']=st.number_input('Διάρκεια (διδακτικές ώρες)',format="%.1f")
        entry['student_id']=st.text_input('Κωδικός μαθητή')
        entry['course_id']=st.text_input('Κωδικός μαθήματος')
   
        submitted = st.form_submit_button("Καταχώρηση")
        if submitted:
            sf.insert_record('records',entry,conn)

    acad_year=st.selectbox("Ακαδημαϊκό έτος",
                                ("2022-2023","2023-2024", "2024-2025", "2025-2026"),
                                index=1)
    col1, col2 = st.columns(2)

    with col1:
        studs=conn.query(f"SELECT student_id, student_name, surname FROM students WHERE acad_year = '{acad_year}'")
        st.dataframe(studs)

    with col2:
        crses=conn.query('SELECT * FROM courses')
        st.dataframe(crses)

with tab2:
    with st.form("new_payment"):
        st.write("Καταχώρηση εξόδου")
        entry={}
        entry['amount']=st.number_input('Ποσό (€)',format="%.2f")
        entry['category']=st.text_input('Κατηγορία εξόδου')
        entry['issue_date']=st.date_input('Ημερομηνία έκδοσης')
        entry['paydate']=st.date_input('Ημερομηνία πληρωμής')
        entry['paid']=st.checkbox('Πληρωμένο')
        entry['business']=st.checkbox('Έξοδο επιχείρησης')
   
        submitted = st.form_submit_button("Καταχώρηση")
        if submitted:
            sf.insert_record('payments',entry,conn)
        
    with st.form("update_payment"):
        st.write("Ενημέρωση εξόδου")
        payment_pkey=st.text_input('Κωδικός εξόδου')
   
        submitted = st.form_submit_button("Ενημέρωση")
        if submitted:
            sf.update_payment(conn,payment_pkey)

    pending_payments=conn.query('SELECT * FROM payments WHERE NOT paid ORDER BY issue_date')
    st.table(pending_payments)

with tab3:
    with st.form("new_income"):
        st.write("Καταχώρηση εσόδου")
        entry={}
        entry['amount']=st.number_input('Ποσό (€)',format="%.2f")
        entry['customer_id']=st.text_input('Κωδικός πελάτη')
        entry['cause']=st.text_input('Αιτιολογία')
        entry['charge_date']=st.date_input('Ημερομηνία χρέωσης')
   
        submitted = st.form_submit_button("Καταχώρηση")
        if submitted:
            sf.insert_record('income',entry,conn)

    with st.form("update_income"):
        st.write("Ενημέρωση εσόδου")
        income_pkey=st.text_input('Κωδικός εσόδου')
        paydate=st.date_input('Ημερομηνία εξόφλησης')
   
        submitted = st.form_submit_button("Ενημέρωση")
        if submitted:
            sf.update_income(conn,income_pkey,paydate)

    pending_income=conn.query('SELECT * FROM income WHERE paydate ISNULL ORDER BY charge_date')
    st.table(pending_income)

with tab4:
    with st.form("new_customer"):
        st.write("Νέος πελάτης")
        entry={}
        entry['customer_id']=st.text_input('Κωδικός πελάτη')
        entry['customer_name']=st.text_input('Όνομα')
        entry['surname']=st.text_input('Επώνυμο')
        entry['mobile']=st.text_input('Κινητό')
        entry['phone']=st.text_input('Σταθερό')
        entry['email']=st.text_input('Διεύθυνση ηλεκτρονικού ταχυδρομίου (email)')
        entry['address']=st.text_input('Διεύθυνση')
        entry['zip']=st.text_input('Ταχυδρομικός κώδικας')
        entry['region']=st.text_input('Περιοχή')
        entry['city']=st.text_input('Πόλη')
        entry['lat']=st.number_input('Γεωγραφικό πλάτος',format="%.13f")
        entry['lon']=st.number_input('Γεωγραφικό μήκος',format="%.13f")
   
        submitted = st.form_submit_button("Καταχώρηση")
        if submitted:
            sf.insert_record('customers',entry,conn)

with tab5:
    with st.form("new_student"):
        st.write("Νέος μαθητής")
        entry={}
        entry['student_id']=st.text_input('Κωδικός μαθητή')
        entry['student_name']=st.text_input('Όνομα')
        entry['surname']=st.text_input('Επώνυμο')
        entry['mobile']=st.text_input('Κινητό')
        entry['email']=st.text_input('Διεύθυνση ηλεκτρονικού ταχυδρομίου (email)')
        entry['grade']=st.text_input('Τάξη')
        entry['level']=st.text_input('Βαθμίδα')
        entry['school']=st.text_input('Σχολείο')
        entry['parent_id']=st.text_input('Κωδικός γονέα')
        entry['plan_id']=st.text_input('Κωδικός πλάνου')
        entry['discount']=st.number_input('Έκπτωση(%)',format="%.2f")
        entry['cohort']=st.text_input('Τμήμα')
        entry['signup_date']=st.date_input('Ημερομηνία εγγραφής')
        entry['acad_year']=st.text_input('Ακαδημαϊκό έτος',placeholder='2024-2025')
   
        submitted = st.form_submit_button("Καταχώρηση")
        if submitted:
            sf.insert_record('students',entry,conn)
