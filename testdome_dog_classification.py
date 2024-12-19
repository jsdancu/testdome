import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("predictions.csv")
    df.columns = ["truth", "prediction"]
    print(df)
    total = df.shape[0]
    print('total:', total)
    accuracy_max = 0
    boundary_max = 0
    for i in range(100):
        tp = df[(df["truth"] == True) & (df["prediction"] >= i)].shape[0]
        tn = df[(df["truth"] == False) & (df["prediction"] < i)].shape[0]
        accuracy = (tp+tn)/total
        if accuracy > accuracy_max:
            accuracy_max = accuracy
            boundary_max = i

    print(boundary_max)