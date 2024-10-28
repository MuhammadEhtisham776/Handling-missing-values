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
