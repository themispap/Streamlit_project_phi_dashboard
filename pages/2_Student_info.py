import streamlit as st
import pandas as pd
import static.functions as sf

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

student_type = st.sidebar.selectbox('Ιδιότητα:',('Μαθητής', 'Φοιτητής'))
student_type_dict={'Μαθητής':'!', 'Φοιτητής':''}
student_names=conn.query(f"SELECT student_id, student_name, surname FROM students WHERE cohort !~ '^δ' AND cohort %s~ '^Φ' AND acad_year='{acad_year}';"%(student_type_dict[student_type]))
student_names=student_names.set_index(student_names['student_name']+' '+student_names['surname']).sort_values('student_name')
#st.write(student_names)
student_dict =student_names['student_id'].to_dict()
student_selector=st.sidebar.selectbox("Όνομα:",student_names.index)
#st.write(student_dict)
student_info=sf.sql_table('static/sql/student_info/student_info.sql',conn,acad_year,start,stop,("'"+student_dict[student_selector]+"'"))

courses=sf.sql_table('static/sql/student_info/courses.sql',conn,acad_year,start,stop,("'"+student_dict[student_selector]+"'"))

col1, col2, col3 = st.columns(3)
with col1:
    st.header(student_info['student_name'].iloc[0])
    st.subheader(student_info['s_surname'].iloc[0])
    st.write('('+student_info['student_id'].iloc[0]+')')

with col2:
    for i in range(len(courses)):
        st.write(courses['course_name'].iloc[i]+': '+
                 str(courses['total_duration'].iloc[i].round(1))+' ώρες')

with col3:
    st.write('Πλάνο: '+student_info['description'].iloc[0])
    st.write('Χρέωση (μετά την έκπτωση): €'+
             str((student_info['price'].iloc[0]*(1-student_info['discount'].iloc[0])).round(2))+' '+
             student_info['charge_type'].iloc[0])
    #st.write('Ώρες ανά εβδομάδα: '+str(student_info['duration'].iloc[0]))
    st.write('Έκπτωση: '+str((student_info['discount'].iloc[0]*100).round(2))+'%')

st.columns(1)
st.divider()
st.markdown('#### Στοιχεία μαθητή')
col1, col2 = st.columns(2)
with col1:
    st.write(student_info['grade'].iloc[0]+' '+
             student_info['level'].iloc[0])
    st.write('Τμήμα: '+student_info['cohort'].iloc[0])

with col2:
    st.markdown('Σχολείο:')
    st.write(student_info['school'].iloc[0])

st.columns(1)
#st.divider()
st.markdown('#### Στοιχεία επικοινωνίας')
col1, col2 = st.columns(2)
with col1:
    st.write('Τηλέφωνο: '+student_info['s_mobile'].iloc[0])
    st.write('email: '+student_info['s_email'].iloc[0])

with col2:
    st.write('Διεύθυνση:')
    st.write(student_info['address'].iloc[0])
    st.write(student_info['zip'].iloc[0]+', '+
             student_info['region'].iloc[0]+', '+
             student_info['city'].iloc[0])

st.columns(1)
#st.divider()
st.markdown('#### Στοιχεία κηδεμόνα')

st.write(student_info['customer_name'].iloc[0]+' '+
         student_info['cust_surname'].iloc[0]+' ('+student_info['parent_id'].iloc[0]+')')
st.write('email: '+student_info['cust_email'].iloc[0])
st.write('Τηλέφωνο: '+student_info['cust_mobile'].iloc[0])
st.write('Σταθερό: '+student_info['phone'].iloc[0])