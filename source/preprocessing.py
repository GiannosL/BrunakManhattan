import numpy as np


def pre_processing(df):
    """
    doc
    """
    # keep necessary columns
    columns_to_keep = ['snp', 'chr', 'pos', 'p']
    df = df[columns_to_keep]

    # sort data
    df = df.sort_values(by=['chr', 'pos'])
    df = df.reset_index(drop=True)

    # calculate negative log p-value
    df['-log(p)'] = -np.log10(df['p'])

    return df