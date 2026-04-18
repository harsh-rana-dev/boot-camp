import pandas as pd 

exp = {
    'pizza': [12, 34, 41, 75],
    'age': [41, 52, 63, 74]
}

df = pd.DataFrame(exp, index=[1, 2, 3, 4])

df["job"] = [1234, 3456, 567, 789]

new_row = pd.DataFrame(
    [
        {'pizza': 23, 'age': 43, 'job': 543},
        {'pizza': 296, 'age': 4325, 'job': 554343},
        {'pizza': 273, 'age': 4343, 'job': 546543}
    ],
    index=[5, 6, 7]
)

df = pd.concat([df, new_row])

print(df)