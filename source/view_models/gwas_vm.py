import pandas as pd

from manhattan import manhattan, miami


def parse_snp_file(snp_filename):
    """
    pass
    """
    #
    with open(snp_filename, 'r') as stream:
        contents = stream.read().splitlines()
    
    return contents


def parse_gwas_file(gwas_filename):
    """
    doc
    """
    # read file into dataframe
    print(gwas_filename)
    df = pd.read_csv(gwas_filename, sep='\t')
    print(df)

    return df


def manhattan_view_model(snp_option, snp_file, gwas_file):
    """
    doc
    """
    # get list of snps
    snp_list = []
    if snp_option:
        snp_list = parse_snp_file(snp_filename=snp_file)
    
    # get gwas data
    gwas_data = parse_gwas_file(gwas_filename=gwas_file)

    # create manhattan plot
    manhattan_figure = manhattan(df=gwas_data,
                                 plot_title='Manhattan plot',
                                 snp_list=snp_list,
                                 gui=True)
    
    return manhattan_figure
    

def miami_view_model(snp_option, snp_file,
                      gwas_1_file, gwas_2_file):
    """
    doc
    """
    # get list of snps
    snp_list = []
    if snp_option:
        snp_list = parse_snp_file(snp_filename=snp_file)

    # get gwas data
    gwas_1_data = parse_gwas_file(gwas_filename=gwas_1_file)
    gwas_2_data = parse_gwas_file(gwas_filename=gwas_2_file)

    # create miami plot
    miami_figure = miami(male_df=gwas_1_data,
                         female_df=gwas_2_data,
                         plot_title='Miami plot',
                         snp_list=snp_list,
                         gui=True)
    
    return miami_figure
