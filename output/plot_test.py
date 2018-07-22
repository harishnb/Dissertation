import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

df = pd.DataFrame({"Time":["2015-11-01 00:00:00", "2015-11-02 00:00:00"], "value":[ 1, -1]})
df['Time'] = pd.to_datetime(df['Time'])
fig, ax = plt.subplots()
ax.scatter(np.arange(len(df['Time'])), df['value'], marker='o')
ax.xaxis.set_ticks(np.arange(len(df['Time'])))
ax.xaxis.set_ticklabels(df['Time'], rotation=90)
plt.xlabel("Time")
plt.ylabel("value")

plt.show()