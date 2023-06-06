import numpy as np


def pre_processing(df, log=True):
    """
    doc
    """
    # keep necessary columns
    columns_to_keep = ['snp', 'chr', 'pos', 'p', 'beta']
    df = df[columns_to_keep]

    # sort data
    df = df.sort_values(by=['chr', 'pos'])
    df = df.reset_index(drop=True)

    # calculate negative log p-value
    if log:
        df['-log(p)'] = -np.log10(df['p'])

    return df