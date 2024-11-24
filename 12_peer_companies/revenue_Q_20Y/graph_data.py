from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

Y_AXIS = "Revenue"
Y_AXIS_LC = "revenue"


# Generate sample data
root = Path("12_peer_companies") / f"{Y_AXIS_LC}_Q_20Y" / "data"
df = pd.DataFrame({"Date": pd.date_range(start='2004-10-01', periods=80, freq='QS-JAN')})

for p in root.iterdir():
    df_p = pd.read_csv(p)
    df[df_p["Instrument"][0]] = df_p[Y_AXIS]

# Ensure the Date column is in datetime format
df["Date"] = pd.to_datetime(df["Date"])

# --- Line Graph ---
plt.figure(1)

# Plot the data
for col in df.columns:
    if col != "Date":
        plt.plot(df["Date"], df[col], label=col)

ax = plt.gca()
ax.tick_params(axis='x', rotation=45)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _ : f'{x / 1e9:.1f}'))

plt.xlabel("Date (quarterly)")
plt.ylabel(f"{Y_AXIS} ($bn)")
plt.title(f'Quarterly {Y_AXIS}')
plt.legend(loc='best')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


# --- Stack Plot ---

plt.figure(2)
plt.stackplot(
    df["Date"],
    df.drop(columns=["Date"]).values.T,
    labels=df.columns[1:]
)

ax = plt.gca()
ax.tick_params(axis='x', rotation=45)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _ : f'{x / 1e9:.1f}'))

# Add title, legend, and grid
plt.title(f'Quarterly {Y_AXIS} (Stack Plot)')
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))  # Adjust legend outside the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()



# Show the plot
plt.show()
