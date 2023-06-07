import streamlit as st

from source import APP_NAME, PLOTTING_OPTIONS
from source.view_models.gwas_vm import manhattan_view_model


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
    
    # SNP list
    snp_list_file = col1.file_uploader('SNP list [optional]')
    snp_list_option = col1.checkbox('Highlight SNPs')

    # GWAS files
    gwas_file_1 = col2.file_uploader('GWAS file 1')
    gwas_file_2 = col2.file_uploader('GWAS file 2 [optional]')

    # horizontal line
    st.write('\n')
    st.write('---')

    submission_btn = st.form_submit_button('Plot')
    if submission_btn:
        if plot_selection == 'Manhattan plot':
            manhattan_view_model(snp_option=snp_list_option,
                                 snp_file=snp_list_file,
                                 gwas_file=gwas_file_1)
        elif plot_selection == 'Miami plot':
            pass
