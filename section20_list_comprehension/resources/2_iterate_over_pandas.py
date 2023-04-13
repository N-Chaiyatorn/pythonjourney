import pandas

student_dict = {
    "student": ["Pan", "Jean"],
    "score": [81, 85]
}

student_dataframe = pandas.DataFrame(student_dict)

for (index, row) in student_dataframe.iterrows():
    print(row.score)