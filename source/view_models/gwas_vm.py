import pandas as pd

from manhattan import manhattan, miami


# save path for plots
PLOT_DIR: str = 'user-plots'


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
    df = pd.read_csv(gwas_filename, sep='\t')

    return df


def manhattan_view_model(snp_option, snp_file, 
                         gwas_file, save_flag=False):
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
    
    if save_flag:
        plot_name = f'{PLOT_DIR}/manhattan-test.png'
        manhattan_figure.savefig(plot_name, dpi=800)
    
    return manhattan_figure
    

def miami_view_model(snp_option, snp_file,
                      gwas_1_file, gwas_2_file,
                      save_flag=False):
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
    
    if save_flag:
        plot_name = f'{PLOT_DIR}/miami-test.png'
        miami_figure.savefig(plot_name, dpi=800)
    
    return miami_figure
