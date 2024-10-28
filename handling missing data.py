import numpy as np
import pandas as pd

# Creating a dataset of students' information
student_data = {
    'Age': [15, 16, np.nan, 17, 16, np.nan, 15, 18],
    'Math_Score': [78, np.nan, 85, 88, np.nan, 91, 84, 89],
    'Science_Score': [np.nan, 76, 83, np.nan, 90, 92, 88, 85],
    'Grade_Level': ['10th', '10th', '11th', np.nan, '11th', '12th', '10th', '12th']
}

df = pd.DataFrame(student_data)
print(df)

# Calculate mean values for Age and Math_Score
mean_age = df["Age"].mean()
mean_math_score = df["Math_Score"].mean()

# Fill missing values with the mean
df["Mean_Age_Imputed"] = df["Age"].fillna(mean_age)
df["Mean_Math_Score_Imputed"] = df["Math_Score"].fillna(mean_math_score)
print(df[["Age", "Math_Score", "Mean_Age_Imputed", "Mean_Math_Score_Imputed"]])

# Calculate median values for Age and Science_Score
median_age = df["Age"].median()
median_science_score = df["Science_Score"].median()

# Fill missing values with the median
df["Median_Age_Imputed"] = df["Age"].fillna(median_age)
df["Median_Science_Score_Imputed"] = df["Science_Score"].fillna(median_science_score)
print(df[["Age", "Science_Score", "Median_Age_Imputed", "Median_Science_Score_Imputed"]])

# Fill missing values in Grade_Level with the mode
mode_grade_level = df["Grade_Level"].mode()[0]
df["Mode_Grade_Level_Imputed"] = df["Grade_Level"].fillna(mode_grade_level)
print(df[["Grade_Level", "Mode_Grade_Level_Imputed"]])

# Drop rows with missing values
df_drop_rows = df.dropna()
print(df_drop_rows)

# Interpolating missing values in Age and Science_Score columns
df["Age_Interpolated"] = df["Age"].interpolate(method="linear")
df["Science_Score_Interpolated"] = df["Science_Score"].interpolate(method="linear")
print(df[["Age", "Science_Score", "Age_Interpolated", "Science_Score_Interpolated"]])

# Forward fill for Age and Math_Score
df["FFill_Age"] = df["Age"].fillna(method="ffill")
df["FFill_Math_Score"] = df["Math_Score"].fillna(method="ffill")
print(df[["Age", "Math_Score", "FFill_Age", "FFill_Math_Score"]])

# Backward fill for Age and Math_Score
df["BFill_Age"] = df["Age"].fillna(method="bfill")
df["BFill_Math_Score"] = df["Math_Score"].fillna(method="bfill")
print(df[["Age", "Math_Score", "BFill_Age", "BFill_Math_Score"]])
