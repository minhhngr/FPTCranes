import pandas as pd

students = pd.DataFrame(
    {
        "StudentID": [1, 2, 3],
        "Name": ["Alice", "Bob", "Charlie"],
    }
)

scores = pd.DataFrame(
    {
        "StudentID": [1, 3, 2],
        "Score": [85, 90, 95],
    }
)

print("-" * 30)
print(pd.merge(students, scores, on="StudentID"))
print("-" * 30)
print(pd.merge(students, scores, on="StudentID", how="left"))
print("-" * 30)
print(pd.merge(students, scores, on="StudentID", how="right"))

students = students.set_index("StudentID")
scores = scores.set_index("StudentID")
print("-" * 30)
print(students.join(scores)) # join index
print("-" * 30)