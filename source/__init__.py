APP_NAME = 'Brunak plotter'

PLOTTING_OPTIONS = ['Manhattan plot', 'Miami plot']

REGENIE_COLUMN_MAP = {
    'SNP': 'snp',
    'CHR': 'chr',
    'BP': 'pos',
    'P': 'p',
    'BETA': 'beta',
    'SE': 'se'
}


class PlottingOptions:
        marker_size: int = 10
        odd_chromosome_color: str = '#102542'
        even_chromosome_color: str = '#F87060'
        special_snps: str = '#7CFC00'
        special_snp_edges: str = '#7CFC00'

        # horizontal significance lines
        lower_limit_hl: int = 5
        upper_limit_hl: int = 8
        lower_limit_color: str = '#000000'
        upper_limit_color: str = '#000000'
