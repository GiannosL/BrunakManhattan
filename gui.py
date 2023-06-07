import streamlit as st

from source import APP_NAME, PLOTTING_OPTIONS
from source.view_models.gwas_vm import *


# set-up page layout
st.set_page_config(page_title=f'{APP_NAME}', layout='wide')


# title 
st.write(f'# {APP_NAME}')


# create submission form
with st.form('plot_form'):
    # splti view into columns
    col1, col2, col3 = st.columns([1, 1, 1])

    # collect user input
    plot_selection = col3.selectbox(
        label='Plotting options', 
        options=PLOTTING_OPTIONS, 
        index=0
        )


    submission_btn = st.form_submit_button('Plot')
    if submission_btn:
        st.write('Hello')
