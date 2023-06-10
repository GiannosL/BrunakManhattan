import matplotlib.pyplot as plt


def man_plot(df,
             plot_ax,
             y_column,
             snp_list,
             horizontal_lines,
             palette,
             plot_features):
    """
    doc
    """
    # set group's position
    previous_last_position = 0

    # chromosome ticks list
    chr_ticks, chr_tick_pos = [], []

    # group data by chromosome
    chrom_groups = df.groupby(('chr'))

    for i, (chr_name, chr_data) in enumerate(chrom_groups):

        # set the color of the chromosome
        chr_color = palette['chr-even'] if i % 2 else palette['chr-odd']

        # set positions in the x-axis
        x_axis_position = chr_data['pos'] + previous_last_position

        # scatter-plot
        plot_ax.scatter(x=x_axis_position,
                        y=chr_data[y_column],
                        s=plot_features['size'],
                        c=chr_color)
        
        # snps that need to be highlighted
        if snp_list:
            mini_df = chr_data[chr_data['snp'].isin(snp_list)]
            mini_pos = mini_df['pos'] + previous_last_position
            plot_ax.scatter(x=mini_pos,
                            y=mini_df[y_column],
                            s=plot_features['size'],
                            c=palette['special'],
                            edgecolors=palette['sp-edges'])

        # save ticks for each chromosome
        chr_ticks.append(f'chr-{chr_name}')
        chr_tick_pos.append(
            (x_axis_position.iloc[-1] - (x_axis_position.iloc[-1] - x_axis_position.iloc[0])/2)
        )

        # reset the last position for this chromosome
        previous_last_position += chr_data.iloc[-1]['pos']

    # set x-axis ticks
    plot_ax.set_xticks(chr_tick_pos)
    plot_ax.set_xticklabels(chr_ticks, rotation=60)

    # horizontal lines
    plot_horizontal_lines(a=horizontal_lines['small'], 
                          b=horizontal_lines['large'],
                          a_color=horizontal_lines['small-color'], 
                          b_color=horizontal_lines['large-color'])
    
    # remove top, right spines
    plot_ax.spines[['top', 'right']].set_visible(False)


def plot_horizontal_lines(a, b, a_color, b_color):
    """
    doc
    """
    plt.axhline(y=a, color=a_color, linestyle='-')
    plt.axhline(y=b, color=b_color, linestyle='-')
