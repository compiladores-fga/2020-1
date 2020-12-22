import pandas as pd
from pathlib import Path
import os
from collections import defaultdict

COLS = ['regex', 'cfg', 'automatos', 'arquitetura', 'algoritmos']

def comp(t):
    return t[[c for c in t.columns if c[0].islower()]]

path = Path(__file__).parent
files = [path / f for f in os.listdir(path) if f.endswith('.csv') and f != 'final.csv']
db = defaultdict(dict)

dfs = [comp(pd.read_csv(f, index_col=0)) for f in files]
for col in COLS:
    df = pd.read_excel('grades.xlsx', col, engine="openpyxl")
    df = (df
        .replace({1.0: True})
        .fillna(False)
        .astype({"id": int})
        .set_index('id')
    )
    dfs.append(df)

for df in dfs:
    for rec in df.reset_index().to_dict('records'):
        # print(rec)
        db[str(rec.pop('id'))].update({k: v for k, v in rec.items() if v is True})

data: pd.DataFrame = pd.DataFrame.from_dict(db).fillna(False).T
data = data.sort_index(0)
data = data.sort_index(1)
data['grade'] = data.sum(1)
data = data.replace({True: 1, False: 0})

print(data[["grade"]])
data.to_csv('final.csv')