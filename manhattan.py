import matplotlib.pyplot as plt

from source.manhattan_plot import man_plot
from source.preprocessing import pre_processing


def manhattan(df):
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
             y_column='-log(p)')
    
    # 
    max_neglog = df['-log(p)'].max() if df['-log(p)'].max() > 9 else 9
    plt.ylim((0, max_neglog+2))
    plt.show()


def miami(male_df, female_df):
    """
    doc
    """
    pass
