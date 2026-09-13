# Box-and-Whisker Plots with Python and Seaborn

A reusable Python script that draws notched **box-and-whisker plots** with the
Seaborn `boxplot` function. Each box summarises the median, interquartile
range, whiskers and outliers of a distribution; the notch approximates the 95%
confidence interval of the median, so non-overlapping notches suggest a
difference in medians.

The worked example plots the bathymetric depth distributions of 25
cross-section profiles across the Mariana Trench (Pacific Ocean).

## Script

- `boxplots.py` — loads the table with pandas, draws one box per profile and
  saves the figure to `plot_Boxplot.png`.

## Data

- `Tab-Bathy.csv` — bathymetric depths (metres) sampled at 517 observation
  points along 25 profiles across the Mariana Trench.

## Method

Box-and-whisker plot: robust five-number summary (minimum, lower quartile,
median, upper quartile, maximum) with notches and outlier markers.

## Requirements

Python 3 with `pandas`, `seaborn` and `matplotlib`.

```
pip install pandas seaborn matplotlib
python boxplots.py
```

## Author

Polina Lemenkova — ORCID: https://orcid.org/0000-0002-5759-1089

Archived code: https://doi.org/10.13140/RG.2.2.31143.39840

## License

MIT — see the LICENSE file (Copyright Polina Lemenkova).
