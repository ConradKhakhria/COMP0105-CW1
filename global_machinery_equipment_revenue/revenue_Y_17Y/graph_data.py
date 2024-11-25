import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


path = Path("global_machinery_equipment_revenue",
            "revenue_Y_17Y",
            "data",
            "global_machinery_equipment_revenue.csv")
df = pd.read_csv(path).set_index("Company").T.rename_axis("Year", axis=1).iloc[::-1]
df.index = df.index.map(int)

data = df.loc[2022][df.loc[2022].notna()]

plt.figure(figsize=(15,8), dpi=200)
ax = data.plot(
    kind="pie",
#    autopct="%1.1f%%",
    legend=True,
    title="Global Machinery Equipment Revenue (2022)",
    ylabel="",
    labeldistance=None
)
ax.legend(bbox_to_anchor=(1, 1.02), loc="upper left")
plt.savefig(path.parents[1] / "graph_pie.png", dpi=200)

# plt.figure(figsize=(10,5), dpi=300)
# 
# for c in df.columns:
#     plt.plot(df.index, df[c])
# 
# 
# plt.savefig(path.parents[1] / "graph_line.png", dpi=300)
# plt.show()
