# HistoBoxPlot/core.py

import seaborn as sns
import matplotlib.pyplot as plt

def histogram_boxplot(data, feature, figsize=(12, 7), kde=False, bins=None):
    """
    Creates a combined boxplot and histogram from a given dataset and feature.

    Parameters:
    data: pandas.DataFrame - The dataframe containing the data.
    feature: str - The column name of the feature for which the plot is to be created.
    figsize: tuple - The size of the figure (default (12,7)).
    kde: bool - Whether to show the kernel density estimate (default False).
    bins: int or sequence or str - Specification of bins for the histogram (default None).

    Returns:
    matplotlib.figure.Figure - The created figure.
    (matplotlib.axes._subplots.AxesSubplot, matplotlib.axes._subplots.AxesSubplot) - The boxplot and histogram axes.
    """

    # Creating subplots
    f2, (ax_box2, ax_hist2) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid = 2
        sharex=True,  # x-axis will be shared among all subplots
        gridspec_kw={"height_ratios": (0.25, 0.75)},
        figsize=figsize
    )  

    # Creating boxplot
    sns.boxplot(
        data=data, x=feature, ax=ax_box2, showmeans=True, color="violet"
    )

    # Creating histogram
    if bins:
        sns.histplot(
            data=data, x=feature, kde=kde, ax=ax_hist2, bins=bins, palette="winter"
        )
    else:
        sns.histplot(
            data=data, x=feature, kde=kde, ax=ax_hist2
        )

    # Adding mean and median lines to histogram
    ax_hist2.axvline(
        data[feature].mean(), color="green", linestyle="--"
    )
    ax_hist2.axvline(
        data[feature].median(), color="black", linestyle="-"
    )

    return f2, (ax_box2, ax_hist2)
