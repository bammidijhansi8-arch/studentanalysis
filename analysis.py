import pandas as pd

# Read data
df = pd.read_csv("data.csv")

# Calculate Grade
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

# Add Grade Column
df["Grade"] = df["Marks"].apply(grade)

# Average Marks
average = df["Marks"].mean()

print("Student Marks Analysis")
print("----------------------")
print(df)

print("\nAverage Marks:", average)

# Save Result
df.to_csv("result.csv", index=False)

print("\nResult saved to result.csv")