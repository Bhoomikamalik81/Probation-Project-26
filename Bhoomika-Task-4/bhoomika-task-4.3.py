import pandas as pd
data = {
    "Name": ["RAM", "BALRAM", "AAYUSHI", "GARGI", "VAIBHAV",
             "ANSH", "RIYA", "KUNAL", "PRIYA", "ROHAN"],
    "Maths": [85, 72, 91, 68, 95, 78, 88, 63, 97, 81],
    "Science": [90, 65, 87, 74, 92, 80, 85, 70, 94, 89],
    "English": [88, 76, 93, 69, 86, 82, 90, 75, 91, 84]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("Average Marks of Each Subject:")
print(df[["Maths", "Science", "English"]].mean())

df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)

df["Result"] = "Fail"
df.loc[df["Total"] >= 150, "Result"] = "Pass"
print("DataFrame with Total and Result:")
print(df)

print("Student with Highest Total Marks:")
print(df.loc[df["Total"].idxmax()])

df = df.sort_values("Total", ascending=False)
print("DataFrame after sorting by Total:")
print(df)