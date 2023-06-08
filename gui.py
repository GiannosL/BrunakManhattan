import streamlit as st

from source import APP_NAME, PLOTTING_OPTIONS
from source.view_models.gwas_vm import manhattan_view_model, miami_view_model


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
    gwas_file_1 = col2.file_uploader('GWAS file 1 [mandatory]', type='tsv')
    gwas_file_2 = col2.file_uploader('GWAS file 2 [optional]', type='tsv')

    # horizontal line
    st.write('\n')
    st.write('---')

    submission_btn = st.form_submit_button('Plot')

# actions if submission button is pressed
if submission_btn:
    if plot_selection == 'Manhattan plot':
        man_fig = manhattan_view_model(snp_option=snp_list_option,
                                        snp_file=snp_list_file,
                                        gwas_file=gwas_file_1)
        
        st.pyplot(man_fig)
    elif plot_selection == 'Miami plot':
        mia_fig = miami_view_model(snp_option=snp_list_option,
                                   snp_file=snp_list_file,
                                   gwas_1_file=gwas_file_1,
                                   gwas_2_file=gwas_file_2)
        
        st.pyplot(mia_fig)
