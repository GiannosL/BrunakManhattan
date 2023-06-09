import matplotlib.pyplot as plt

from source import PlottingOptions
from source.beta_plot import beta_plot
from source.manhattan_plot import man_plot
from source.preprocessing import pre_processing


def manhattan(df, snp_list=[], 
              plot_title='Manhattan plot', 
              gui=False,
              options_obj: PlottingOptions = PlottingOptions):
    """
    doc
    """
    # pre-process the data
    df = pre_processing(df=df)

    #
    fig, ax = plt.subplots(figsize=(20, 10))

    # plot the manhattan plot
    man_plot(df=df,
             plot_ax=ax,
             y_column='-log(p)',
             snp_list=snp_list,
             palette={
                 'chr-odd': options_obj.odd_chromosome_color, 
                 'chr-even': options_obj.even_chromosome_color,
                 'special': options_obj.special_snps, 
                 'sp-edges': options_obj.special_snp_edges
             },
             plot_features={
                 'size': options_obj.marker_size
             },
             horizontal_lines={
                 'small': options_obj.lower_limit_hl,
                 'large': options_obj.upper_limit_hl,
                 'small-color': options_obj.lower_limit_color,
                 'large-color': options_obj.upper_limit_color
             })
    
    # titles, labels
    plt.title(plot_title, fontsize=20, weight='bold')
    plt.xlabel('Chromosome', fontsize=16)
    plt.ylabel('Negative log10(p-value)', fontsize=16)

    #
    max_neglog = df['-log(p)'].max() if df['-log(p)'].max() > 9 else 9
    plt.ylim((0, max_neglog+2))
    if gui:
        return fig
    plt.show()


def miami(male_df, female_df, 
          plot_title='Miami plot', 
          snp_list=[],
          gui=False,
          options_obj: PlottingOptions = PlottingOptions):
    """
    doc
    """
    # pre-processing dataframes
    male_df = pre_processing(df=male_df)
    female_df = pre_processing(df=female_df)

    # males are the lower plot, we need positive log p-value
    male_df['log(p)'] = -male_df['-log(p)']

    # plot size
    fig, ax = plt.subplots(figsize=(20,10))

    # lighter colour-palette
    light_palette = ('#BDD2EF', '#FDCAC4')

    # make manhattan plot for female patients
    man_plot(df=female_df,
             plot_ax=ax,
             y_column='-log(p)',
             snp_list=snp_list,
             palette={
                 'chr-odd': options_obj.odd_chromosome_color, 
                 'chr-even': options_obj.even_chromosome_color,
                 'special': options_obj.special_snps, 
                 'sp-edges': options_obj.special_snp_edges
             },
             plot_features={
                 'size': options_obj.marker_size
             },
             horizontal_lines={
                 'small': options_obj.lower_limit_hl,
                 'large': options_obj.upper_limit_hl,
                 'small-color': options_obj.lower_limit_color,
                 'large-color': options_obj.upper_limit_color
             })
    
    man_plot(df=male_df,
             plot_ax=ax,
             y_column='log(p)',
             snp_list=snp_list,
             palette={'chr-odd': options_obj.odd_chromosome_color2,
                      'chr-even': options_obj.even_chromosome_color2,
                      'special': options_obj.special_snps, 
                      'sp-edges': options_obj.special_snp_edges},
            horizontal_lines={'small': -options_obj.lower_limit_hl, 
                              'large': -options_obj.upper_limit_hl,
                              'small-color': options_obj.lower_limit_color,
                              'large-color': options_obj.upper_limit_color},
            plot_features={
                 'size': options_obj.marker_size}
            )
    
    # titles, labels
    plt.title(plot_title, fontsize=20, weight='bold')
    plt.xlabel('Chromosome', fontsize=16)
    plt.ylabel('')

    #
    max_neglog = female_df['-log(p)'].max() if female_df['-log(p)'].max() > 9 else 9
    min_neglog = male_df['log(p)'].min() if male_df['log(p)'].min() < -9 else -9
    plt.ylim((min_neglog, max_neglog+2))
    if gui:
        return fig
    plt.show()


def beta_beta(df_a, df_b, significance_thr=1e-8,
              palette={'normal': '#A2ABB5', 
                       'significant': '#6DD6DA'}):
    """
    doc
    """
    #
    plt.subplots(figsize=(10, 10))

    # pre-processing dataframes
    df_a = pre_processing(df=df_a, log=False)
    df_b = pre_processing(df=df_b, log=False)

    # filtering
    df_a_snps = df_a[df_a['p'] < significance_thr]['snp'].tolist()
    df_b_snps = df_b[df_b['p'] < significance_thr]['snp'].tolist()
    snps_of_interest = [*df_a_snps, *df_b_snps]

    # plot
    beta_plot(df_a=df_a, df_b=df_b, palette=palette,
              snps_of_interest=snps_of_interest)
    
    plt.title('Beta-Beta plot', fontsize=20, weight='bold')
    plt.xlabel('Effect size A', fontsize=16)
    plt.ylabel('Effect size A', fontsize=16)

    plt.show()
