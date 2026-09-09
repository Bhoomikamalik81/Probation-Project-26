import pandas as pd
data = {
    "Name": ["RAM", "BALRAM", "AAYUSHI", "GARGI", "VAIBHAV"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 75, 95, 88]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("First 3 rows:")
print(df.head(3))
print("Name column:")
print(df["Name"])
print("Students with marks greater than 85:")
print(df[df["Marks"] > 85])
df["Grade"] = ["B", "A", "C", "A", "A"]
print("DataFrame after adding Grade:")
print(df)
df = df.drop("Age", axis=1)
print("DataFrame after dropping Age:")
print(df)