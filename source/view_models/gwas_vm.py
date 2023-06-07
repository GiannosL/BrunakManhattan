import pandas as pd

from manhattan import manhattan


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
    manhattan(df=gwas_data,
              plot_title='Manhattan plot')
    
