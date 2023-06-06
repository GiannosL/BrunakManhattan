import matplotlib.pyplot as plt

from source.manhattan_plot import man_plot
from source.preprocessing import pre_processing


def manhattan(df, snp_list=[], plot_title='Manhattan plot'):
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
             snp_list=snp_list)
    
    # titles, labels
    plt.title(plot_title, fontsize=20, weight='bold')
    plt.xlabel('Chromosome', fontsize=16)
    plt.ylabel('Negative log10(p-value)', fontsize=16)

    #
    max_neglog = df['-log(p)'].max() if df['-log(p)'].max() > 9 else 9
    plt.ylim((0, max_neglog+2))
    plt.show()


def miami(male_df, female_df, 
          plot_title='Miami plot', snp_list=[]):
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
             snp_list=snp_list)
    
    man_plot(df=male_df,
             plot_ax=ax,
             y_column='log(p)',
             snp_list=snp_list,
             palette={'chr-odd': light_palette[0],
                      'chr-even': light_palette[1],
                      'special': '#230903', 
                      'sp-edges': 'red'},
            horizontal_lines={'small': -5, 'large': -8})
    
    # titles, labels
    plt.title(plot_title, fontsize=20, weight='bold')
    plt.xlabel('Chromosome', fontsize=16)
    plt.ylabel('')

    #
    max_neglog = female_df['-log(p)'].max() if female_df['-log(p)'].max() > 9 else 9
    min_neglog = male_df['log(p)'].min() if male_df['log(p)'].min() < -9 else -9
    plt.ylim((min_neglog, max_neglog+2))
    plt.show()
