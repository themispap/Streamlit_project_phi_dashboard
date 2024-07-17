import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from sqlalchemy import text
from static.functions import sql_table, month_plot, bar_plot, duration_plot, stud_plot

# connect to database
conn = st.connection("phi_server",type='sql')

# academic year selector
acad_year=st.sidebar.selectbox("Ακαδημαϊκό έτος",
                                ("2022-2023","2023-2024", "2024-2025", "2025-2026"),
                                index=2)
# past academic year
acad_year_past={"2022-2023": "2022-2023",
                "2023-2024": "2022-2023",
                "2024-2025": "2023-2024",
                "2025-2026": "2024-2025"}

# start and end date of each academic year
acad_years={"2022-2023": ("'2022-06-20'","'2023-06-18'"),
            "2023-2024": ("'2023-06-19'","'2024-06-16'"),
            "2024-2025": ("'2024-06-17'","'2025-06-15'"),
            "2025-2026": ("'2025-06-15'","'2026-06-14'")}
# start and end date of selected academic year
start=acad_years[acad_year][0]
stop=acad_years[acad_year][1]

percent_covered=len(pd.date_range(start=start,end=datetime.today()))/len(pd.date_range(start=start,end=stop))

# personal expenses checkbox
personal_expenses=st.sidebar.checkbox('Προσωπικά έξοδα')

# definining the tabs of the dashboard
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Ισολογισμός',
                                                'Υπόλοιπα',
                                                'Διδακτικές ώρες',
                                                'Εγγραφές/Διαγραφές',
                                                'Χάρτης',
                                                'Πελάτες',
                                                'Μαθητές']
                                                )


with tab1: # Ισολογισμός
    # income dataframe of the selected academic year
    income = sql_table('static/sql/income_table.sql',conn,acad_year,start,stop)
   
    # income dataframe of the past academic year
    income_past = sql_table('static/sql/income_table.sql',conn,
                            acad_year_past[acad_year],
                            acad_years[acad_year_past[acad_year]][0],
                            acad_years[acad_year_past[acad_year]][1])
    
    # cost dataframe of the selected academic year
    cost = sql_table('static/sql/cost_table.sql',conn,acad_year,start,stop,
                     values=(str(personal_expenses).upper()))
    # cost dataframe of the selected academic year
    cost_past = sql_table('static/sql/cost_table.sql',conn,
                            acad_year_past[acad_year],
                            acad_years[acad_year_past[acad_year]][0],
                            acad_years[acad_year_past[acad_year]][1],
                            values=(str(personal_expenses).upper()))
    
    # profit dataframe of the selected academic year
    profit=pd.DataFrame(income['sum']-cost['sum'])
    profit['date']=income['pay_date']
    # profit dataframe of the selected academic year
    profit_past=pd.DataFrame(income_past['sum']-cost_past['sum'])
    profit_past['date']=income_past['pay_date']

    col1, col2, col3 = st.columns(3)
    with col1: # Έσοδα
         # total income of the selected academic year
         total_income=income['sum'].sum().round(2)
         # total income of the past academic year
         total_income_past=income_past['sum'].sum().round(2)
         # the percentage change in revenue
         income_percent=round((total_income*1/percent_covered-total_income_past)/total_income_past*100,2)
         # total income indicator
         st.metric("Έσοδα", "€"+str(total_income), f"{income_percent} %")
         # monthly income barchart

         month_plot(acad_year, acad_year_past, income, income_past, x='pay_date', y='sum', yrange=[0,2500])

    with col2: # Έξοδα
        # total cost of the selected academic year
        total_cost=cost['sum'].sum().round(2)
        # total cost of the past academic year
        total_cost_past=cost_past['sum'].sum().round(2)
        # the percentage change in expenses
        cost_percent=round((total_cost*1/percent_covered-total_cost_past)/total_cost_past*100,2)
        # total cost indicator
        st.metric("Έξοδα", "€"+str(total_cost), f"{cost_percent} %")
        # monthly cost barchart
        month_plot(acad_year,acad_year_past,cost, cost_past, x='pay_date', y='sum',yrange=[0,2500])

    with col3: # Κέρδος
        # profit of the selected academic year
        total_profit=(total_income-total_cost).round(2)
        # profit of the past academic year
        total_profit_past=(total_income_past-total_cost_past).round(2)
        # the percentage change in profit
        profit_percent=round((total_profit*1/percent_covered-total_profit_past)/total_profit_past*100,2)
        # profit indicator
        st.metric("Κέρδος", "€"+str(total_profit), f"{profit_percent} %")
        # monthly profit barchart
        
        month_plot(acad_year,acad_year_past,profit, profit_past, x='date', y='sum',yrange=[0,2500])

with tab2: # Υπόλοιπα
    # balance dataframe
    balance = sql_table('static/sql/balance.sql',conn,acad_year,start,stop)
    # total credits
    total_res=balance['res'].sum().round(2)
    # debts dataframe
    pending_bills = sql_table('static/sql/pending_bills.sql',conn,acad_year,start,stop,
                              values=(str(personal_expenses).upper()))
    # total debts
    total_pending_bills=pending_bills['amount'].sum()#.round(2)

    col1, col2 = st.columns(2)
    with col1:
        # total credits indicator
        st.metric("Υπόλοιπο", "€"+str(total_res))
        bar_plot(balance[balance.res!=0],x='surname',y='res', yrange=[0,500])
        #st.table(balance[balance['res']>0].sort_values('res', ascending=False))
    with col2:
        st.metric("Ανεξόφλητοι λογαριασμοί", "€"+str(total_pending_bills))
        bar_plot(pending_bills,x='category',y='amount',yrange=[0,500])
        #st.table(pending_bills)

with tab3: # Διδακτικές ώρες
    duration = sql_table('static/sql/duration.sql',conn,acad_year,start,stop)
    duration['month']=income['pay_date']
    duration_past = sql_table('static/sql/duration.sql',conn,
                            acad_year_past[acad_year],
                            acad_years[acad_year_past[acad_year]][0],
                            acad_years[acad_year_past[acad_year]][1])
    duration_past['month']=income_past['pay_date']
    col1, col2 = st.columns(2)
    with col1:
        total_duration=(duration['stud'].sum()+
                           duration['foit'].sum()+
                           duration['dyn'].sum())
        total_duration_past=(duration_past['stud'].sum()+
                           duration_past['foit'].sum()+
                           duration_past['dyn'].sum())
        total_duration_prcnt=round((total_duration*1/percent_covered-total_duration_past)/total_duration_past*100,2)
        st.metric("Σύνολο διδακτικών ωρών", str(total_duration)+' ώρες', f"{total_duration_prcnt} %")

    with col2:
        hourly_income=(total_income/total_duration)
        hourly_income_past=(total_income_past/total_duration_past)
        hourly_income_prcnt=round((hourly_income-hourly_income_past)/hourly_income_past*100,2)
        st.metric("Έσοδα ανά ώρα", str(round(total_income/total_duration,2))+' €/ώρα', f"{hourly_income_prcnt} %")

    st.columns(1)


    duration_plot(acad_year,acad_year_past,duration,duration_past,x='month', y=['stud','foit','dyn'],yrange=[0,180])
    # fig_duration = px.bar(duration,x='month', y=['stud','foit','dyn'])
    # fig_duration.update_layout(xaxis_title="",
    #                             yaxis_title="")
    # st.plotly_chart(fig_duration, use_container_width=True)

    #st.bar_chart(duration,y=['stud','foit','dyn'])

with tab4:
    signups = sql_table('static/sql/signups.sql',conn,acad_year,start,stop)
    signups_past = sql_table('static/sql/signups.sql',conn,
                            acad_year_past[acad_year],
                            acad_years[acad_year_past[acad_year]][0],
                            acad_years[acad_year_past[acad_year]][1])
    students_phi=sql_table('static/sql/students_phi.sql',conn,acad_year,start,stop)
    n_students_phi=students_phi.count()[0]
    students_phi_past=sql_table('static/sql/students_phi.sql',conn,
                            acad_year_past[acad_year],
                            acad_years[acad_year_past[acad_year]][0],
                            acad_years[acad_year_past[acad_year]][1])
    n_students_phi_past=students_phi_past.count()[0]
    signups_count=signups['signups'].sum()
    signups_count_past=signups_past['signups'].sum()
    signouts_count=signups['signouts'].sum()
    signouts_count_past=signups_past['signouts'].sum()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        signups_prcnt=round((signups_count-signups_count_past)/signups_count_past*100,2)
        st.metric("Εγγραφές", f'{signups_count}',f'{signups_prcnt}%')
    with col2:
        continue_prcnt=round((n_students_phi-signups_count-n_students_phi_past+signups_count_past)/(n_students_phi_past+signups_count_past)*100,2)
        st.metric("Μαθητές που συνέχισαν", f'{n_students_phi-signups_count}',f'{continue_prcnt}%')
    with col3:
        signouts_prcnt=round((signouts_count-signouts_count_past)/signouts_count_past*100,2)
        st.metric("Μαθητές που σταμάτησαν", f'{-signouts_count}',f'{signouts_prcnt}%')
    with col4:
        students_phi_prcnt=round((n_students_phi-n_students_phi_past)/n_students_phi_past*100,2)
        st.metric("Σύνολο μαθητών", f'{n_students_phi}',f'{students_phi_prcnt}%')
    st.columns(1)
    #st.bar_chart(signups,x='week_number',y=['signups','signouts'])
    stud_plot(acad_year,acad_year_past,signups,signups_past,x='date',y=['signups','signouts'])

with tab5:
    df = conn.query('SELECT lat, lon FROM customers WHERE lat IS NOT NULL;')
    map_data = pd.DataFrame(df,columns=['lat', 'lon'])
    st.map(map_data, use_container_width=False)
with tab6:
    cust_cols='customer_name AS Όνομα, surname AS Επώνυμο, mobile, email, address, region, city'
    customers = conn.query('SELECT %s FROM customers WHERE active;'%cust_cols)
    st.table(customers)

with tab7:
    stud_cols='student_name AS Όνομα, surname AS Επώνυμο, mobile, email'
    students = conn.query('SELECT %s FROM students WHERE acad_year= %s ORDER BY student_name;'%(stud_cols,"'"+acad_year+"'"))
    st.table(students)
