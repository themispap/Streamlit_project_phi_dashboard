import pandas as pd
import streamlit as st
from sqlalchemy import text
import plotly.express as px

def insert_record(table,entry,conn):
    with conn.session as s:
        cols=', '.join(str(key) for key in entry.keys())
        values=', '.join("'"+str(key)+"'" for key in entry.values())
        query=text("INSERT INTO %s (%s) VALUES (%s);"%(table,cols,values))
        s.execute(query)
        s.commit()
        st.success('Record added successfully')

def sql_table(sql,conn,acad_year,start,stop,values=()):
    with open(sql,'r') as f:
        table=f.read()
        table=table.format(acad_year="'"+acad_year+"'",start=start,stop=stop)
    return conn.query(table%values)

def delete_record(conn,table,id,value):
    with conn.session as s:
        with open('static/sql/delete.sql','r') as f:
            statement=f.read()
            statement=text(statement%(table,id,value))
            s.execute(statement)
            s.commit()
            st.success('Record deleted successfully')

def update_payment(conn,payment_pkey):
    with conn.session as s:
        with open('static/sql/update_payment.sql','r') as f:
            statement=f.read()
            statement=text(statement%(payment_pkey))
            s.execute(statement)
            s.commit()
            st.success('Record updated successfully')

def update_income(conn,id,paydate):
    with conn.session as s:
        with open('static/sql/update_income.sql','r') as f:
            statement=f.read()
            statement=text(statement.format(id=id,paydate="'"+str(paydate)+"'"))
            s.execute(statement)
            s.commit()
            st.success('Record updated successfully')

def month_plot(acad_year,acad_year_past,data,data_past,x,y,xtitle='',ytitle='',color='acad_year',yrange=None):
    data['acad_year']=acad_year
    data_past[x]=data[x]
    data_past['acad_year']=acad_year_past[acad_year]
    data_full=pd.concat([data_past, data], ignore_index=True, sort=False)
    fig = px.bar(data_full, x=x, y=y, color=color, barmode='group',
                 labels={"acad_year": "Academic Year",
                         "sum":"€",
                         x:'Month'})
    fig.update_layout(xaxis_title=xtitle,
                      yaxis_title=ytitle,
                      yaxis_range=yrange,
                      legend=dict(
                            yanchor="top",
                            y=0.99,
                            xanchor="right",
                            x=0.25)
                    )
    st.plotly_chart(fig, use_container_width=True)

def duration_plot(acad_year,acad_year_past,data,data_past,x,y,xtitle='',ytitle='',color='acad_year',yrange=None):
    data['acad_year']=acad_year
    data_past[x]=data[x]
    data_past['acad_year']=acad_year_past[acad_year]
    data_full=pd.concat([data_past, data], ignore_index=True, sort=False)
    fig = px.bar(data_full, x=x, y=y, barmode='group',color=color,
                 labels={"acad_year": "Academic Year",
                         'variable':'Κατηγορία',
                         'value':'Ώρες',
                         x:'Month'})
    fig.update_layout(xaxis_title=xtitle,
                      yaxis_title=ytitle,
                      yaxis_range=yrange,
                      legend=dict(
                            yanchor="top",
                            y=0.99,
                            xanchor="right",
                            x=0.1)
                    )
    st.plotly_chart(fig, use_container_width=True)

def stud_plot(acad_year,acad_year_past,data,data_past,x,y,xtitle='',ytitle='',color='acad_year',yrange=None):
    data['acad_year']=acad_year
    data_past[x]=data[x]
    data_past['acad_year']=acad_year_past[acad_year]
    data_full=pd.concat([data_past, data], ignore_index=True, sort=False)
    fig = px.bar(data_full, x=x, y=y, barmode='group',color=color,
                 labels={"acad_year": "Academic Year",
                         x:'Μήνας',
                         'value':'Μαθητές'})
    fig.update_layout(xaxis_title=xtitle,
                      yaxis_title=ytitle,
                      yaxis_range=yrange,
                      legend=dict(
                            yanchor="top",
                            y=0.99,
                            xanchor="right",
                            x=0.98))
    fig.update_xaxes(ticks= "outside",
                 dtick="M1",
                 ticklabelmode= "period", 
                 tickcolor= "white", 
                 ticklen=12,
                 tickformat="%b %y",
                 minor=dict(
                     ticklen=4,
                     dtick=7*24*60*60*1000,
                     tick0=x[0])
                )
    fig.add_hline(y=0, opacity=1, line_width=2, line_dash='dash', line_color='White')
    st.plotly_chart(fig, use_container_width=True)

def bar_plot(data,x,y,xtitle='',ytitle='',yrange=None):
    fig = px.bar(data,x=x, y=y,barmode='group',text_auto=True)
    fig.update_layout(xaxis_title=xtitle,
                      yaxis_title=ytitle,
                      yaxis_range=yrange,
                      legend=dict(
                            yanchor="top",
                            y=0.99,
                            xanchor="right",
                            x=0.25)
                    )
    st.plotly_chart(fig, use_container_width=True)