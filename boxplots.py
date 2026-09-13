#!/usr/bin/env python
# coding: utf-8
"""Box-and-whisker plots (Seaborn boxplot).

Draws vertical box-and-whisker plots for the bathymetric depths of the
Mariana Trench: one box per cross-section profile, summarising the median,
interquartile range, whiskers and outliers of each depth distribution.
The notches approximate the 95% confidence interval of the median.

Data:    Tab-Bathy.csv - bathymetric depths sampled at 517 observation
         points along 25 profiles across the Mariana Trench.

Author:  Polina Lemenkova
ORCID:   https://orcid.org/0000-0002-5759-1089
Archive: https://doi.org/10.13140/RG.2.2.31143.39840
License: MIT
"""
import os

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

sb.set_style('whitegrid')
sb.set_context('paper')

dfB = pd.read_csv(os.path.join(HERE, 'Tab-Bathy.csv'))

sb.boxplot(data=dfB, orient='v', palette='coolwarm', saturation=1,
           width=0.8, dodge=True, fliersize=5, linewidth=0.2,
           whis=5, notch=True)
sb.despine(offset=10, trim=True)  # offset the spines away from the data
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.title('Box-and-whisker plot for the Mariana Trench bathymetry',
          fontsize=12, fontfamily='sans-serif')

plt.tight_layout()
plt.savefig(os.path.join(HERE, 'plot_Boxplot.png'), dpi=300)
plt.show()
