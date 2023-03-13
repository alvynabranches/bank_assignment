import sys
import pandas as pd

N = int(sys.argv[1]) if len(sys.argv) == 2 else 26
TARGET_COL = "target"
ROUND = 2

data = [144725, 251537, 326429, 347205, 282604, 305602, 333478, 360101, 455159, 383369, 456355, 464042, 474477, 454011, 487010, 582097, 561658, 569113, 550166, 598060, 564671, 614442, 634581, 	669939, 687840, 692310, 552706, 690540, 694737, 637037, 643942, 700215, 642001, 679133]

df = pd.DataFrame(data, columns=[TARGET_COL])

MA = df[TARGET_COL].rolling(N).mean().tolist()[-1]
EMA = df[TARGET_COL].ewm(span=N, adjust=False).mean().tolist()[-1]

print(round(MA, ROUND), round(EMA, ROUND))

