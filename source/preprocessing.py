import numpy as np

from source import REGENIE_COLUMN_MAP


def pre_processing(df, log=True):
    """
    doc
    """
    # rename columns
    df = df.rename(columns=REGENIE_COLUMN_MAP)

    # keep necessary columns
    columns_to_keep = ['snp', 'chr', 'pos', 'p', 'beta', 'se']
    df = df[columns_to_keep]

    # sort data
    df = df.sort_values(by=['chr', 'pos'])
    df = df.reset_index(drop=True)

    # calculate negative log p-value
    if log:
        df['-log(p)'] = -np.log10(df['p'])

    return df
