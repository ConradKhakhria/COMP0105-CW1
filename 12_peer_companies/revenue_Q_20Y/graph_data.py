from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


NAME = {
    "full": "Revenue",
    "snake": "revenue"
}


def load_data(names: dict) -> pd.DataFrame:
    # args:
    # - anmes: contains the full and snake_case names of the data
    root = Path("12_peer_companies") / f"{names['snake']}_Q_20Y" / "data"
    df = pd.DataFrame({"Date": pd.date_range(start='2004-10-01', periods=80, freq='QS-JAN')})

    for p in root.iterdir():
        df_p = pd.read_csv(p)
        df[df_p["Instrument"][0]] = df_p[names["full"]]

    return df


def plot_graph(names: dict, df: pd.DataFrame, colours: list, tp: str):
    # args:
    # - names: the full and snake_case names of the data
    # - df: the data
    # - colours: a colours list
    # - tp: line or stack
    plt.figure()

    if tp == "line":
        for i, col in enumerate(df.drop(columns=["Date"]).columns):
            plt.plot(df["Date"], df[col], label=col, color=colours[i - 1])
    else:
        plt.stackplot(
            df["Date"],
            df.drop(columns=["Date"]).values.T,
            labels=df.columns[1:],
            colors=colours
        )

    ax = plt.gca()
    ax.tick_params(axis='x', rotation=45)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _ : f'{x / 1e9:.1f}'))

    plt.xlabel("Date (quarterly)")
    plt.ylabel(f"{names['full']} ($bn)")
    plt.title(f"Quarterly {names['full']}")
    plt.legend(loc='best')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save plot
    path = Path("12_peer_companies") / f"{names['snake']}_Q_20Y" / f"graph_{tp}.png"
    plt.savefig(path, dpi=300)


if __name__ == "__main__":
    df = load_data(NAME)

    cmap = plt.get_cmap("tab20", len(df.columns) - 1)
    colours = [cmap(i) for i in range(len(df.columns) - 1)]

    plot_graph(NAME, df, colours, "line")
    plot_graph(NAME, df, colours, "stack")

    plt.show()
