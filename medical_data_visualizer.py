import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#  Load Data 
df = pd.read_csv('medical_examination.csv')

# ── Add Overweight Column 
# BMI = weight(kg) / height(m)^2  →  overweight if BMI > 25
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# ── Normalize cholesterol and gluc 
# 0 = good (value == 1), 1 = bad (value > 1)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc']        = (df['gluc'] > 1).astype(int)


# FIGURE 1 — Categorical Plot
# ══════════════════════════════════════════════════════════════════════════════
def draw_cat_plot():

    # Melt the dataframe: each row becomes one variable-value pair
    df_cat = pd.melt(
        df,
        id_vars    = ['cardio'],
        value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # Count occurrences of each value (0 or 1) for each variable, split by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
                   .size() \
                   .reset_index(name='total')

    # Draw the categorical plot
    fig = sns.catplot(
        data    = df_cat,
        x       = 'variable',
        y       = 'total',
        hue     = 'value',
        col     = 'cardio',
        kind    = 'bar',
        height  = 5,
        aspect  = 1
    ).fig

    fig.savefig('catplot.png')
    return fig


# FIGURE 2 — Heatmap
# ══════════════════════════════════════════════════════════════════════════════
def draw_heat_map():

    # ── Clean the data ─────────────────────────────────────────────────────────
    df_heat = df[
        (df['ap_lo']  <= df['ap_hi'])                        &  # diastolic ≤ systolic
        (df['height'] >= df['height'].quantile(0.025))       &  # remove height outliers
        (df['height'] <= df['height'].quantile(0.975))       &
        (df['weight'] >= df['weight'].quantile(0.025))       &  # remove weight outliers
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # ── Correlation matrix
    corr = df_heat.corr()

    # ── Mask upper triangle (avoid duplicate info) 
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # ── Plot 
    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr,
        mask       = mask,
        annot      = True,
        fmt        = '.1f',
        center     = 0,
        vmin       = -0.16,
        vmax       = 0.32,
        square     = True,
        linewidths = 0.5,
        ax         = ax,
        cbar_kws   = {'shrink': 0.5}
    )

    fig.savefig('heatmap.png')
    return fig