from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

from fetch_all_data import FIELDS


def configure_graphics(field: str):
    ax = plt.gca()
    ax.tick_params(axis='x', rotation=45)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _ : f'{x / 1e9:.1f}'))

    plt.xlabel("Date (quarterly)")
    plt.ylabel(f"{field} ($bn)")
    plt.title(f"Quarterly {field}")
    plt.legend(loc='best')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()


def plot_field(whole_df: pd.DataFrame, field: str, root: Path, colours: list):
    # Plots a data field, in both line and stack charts, and saves them
    # args
    # - whole_df: the df containing the data to be plotted
    # - field: the field to plot
    # - root: the root of the directory to save to
    df = pd.DataFrame({ "Date": pd.date_range(start='2004-10-01', periods=80, freq='QS-JAN') })
    instruments = whole_df["Instrument"].unique()

    for inst in instruments:
        df[inst] = whole_df[whole_df["Instrument"] == inst][field].tolist()


    cmap = plt.get_cmap("tab20", len(df.columns))
    colours = [cmap(i) for i in range(len(df.columns))]

    # Line plot
    plt.figure()
    for i, inst in enumerate(instruments):
        plt.plot(df["Date"], df[inst], label=inst, color=colours[i])

    configure_graphics(field)
    plt.savefig(root / 'plots' / f"{field}_line_plot.png", dpi=300)

    # Stack plot
    plt.figure()
    plt.stackplot(
        df["Date"],
        df.drop(columns=["Date"]).values.T,
        labels=instruments,
        colors=colours
    )
    configure_graphics(field)
#    plt.savefig(root / 'plots' / f"{field}_stack_plot.png", dpi=300)

#    plt.show()


if __name__ == "__main__":
    root = Path("COMP0105-CW1") / '12_peer_companies'
    df = pd.read_csv(root / 'data_Q_20Y' / 'data.csv')
    field_dfs = {}
    instruments = df["Instrument"].unique()

    for field in FIELDS:
        field_dfs[field] = pd.DataFrame({ "Date": pd.date_range(start='2004-10-01', periods=80, freq='QS-JAN') })
        for inst in instruments:
            field_dfs[field][inst] = df[df["Instrument"] == inst][field].tolist()

    for field in FIELDS:
        plot_field(df, field, root, None)

    plt.show()
