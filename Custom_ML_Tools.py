"""
Created on Fri Dec  4 19:31:23 2020
@author: ISH KAPOOR
"""

import pandas as pd
import streamlit as st

st.title("Preview Dataset")

df = None
if st.checkbox("Upload Dataset"):
    csv_file = st.file_uploader("Upload '.CSV File'", type = ["csv"])
    if csv_file is not None:
        st.write(type(csv_file))
        df = pd.read_csv(csv_file)

        if st.checkbox("Preview Dataset"):
            data = df
            if st.button("HEAD"):
                st.write(data.head(50))
            elif st.button("TAIL"):
                st.write(data.tail(50))
            else:
                st.write(data)

        if st.checkbox("View Columns"):
            st.write(df.columns)

        data_dmns = st.radio("", ("Rows", "Columns", "All"))
        if data_dmns == "Rows":
            st.text("Showing Rows")
            st.write(df.shape[0])
        elif data_dmns == "Columns":
            st.text("Showing Columns")
            st.write(df.shape[1])
        else:
            st.text("Showing Shape")
            st.write(df.shape)

        describe = st.write(df.describe())
        describe

        columns = [c for c in df.columns]
        colm = st.selectbox("Select Column", tuple(columns))
        for i in range(len(columns)):
            if colm == columns[i]:
                st.write(df[columns[i]])
                chart_data = pd.DataFrame(df[:40], columns = [columns[i]])
                st.area_chart(chart_data)

        barchart = st.bar_chart(df[columns])
        linechart = st.line_chart(df)
