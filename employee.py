import pandas as pd

df = pd.read_csv('emp.csv')

str_input = input("what you want write for empty columns")
strs = df.select_dtypes("object").columns
df[strs] = df[strs].fillna(str_input)

nums = df.select_dtypes("number").columns
df[nums] = df[nums].fillna(0)
# ^^^^^^ Fill NaN values^^^^^^^


df = df[df["Age"] > 18]
df = df[df["Age"] < 60]
# ^^^^^for delete unrealistic age^^^^^

df = df.drop_duplicates()

print("-----------min age-----------")
min_age = df["Age"].min()
print(min_age)

print("-----------max age-----------")
max_age = df["Age"].max()
print(max_age)

print("-----------min salary-----------")
df = df[df["Salary"] > 1]
min_salary = df["Salary"].min()
print(min_salary)

print("-----------max salary-----------")
max_salary = df["Salary"].max()
print(max_salary)

print("-----------all workers-----------")
workers = df["Name"].count()
print(workers)


# ^^^^^grouping Data^^^^^^

print("-----------dept info-----------")
employees = df.groupby("Dept").size()
min_work_salary = df.groupby("Dept")["Salary"].min()
max_work_salary = df.groupby("Dept")["Salary"].max()
mean_work_salary = df.groupby("Dept")["Salary"].mean()



dept_info = pd.DataFrame({
    "workers": employees,
    "min salary": min_work_salary,
    "max salary": max_work_salary,
    "mean salary": mean_work_salary

})
dept_info = dept_info[dept_info.index != str_input]
print(dept_info)
# ^^^^^^make a Data Frame for Dept info^^^^^^^^^

print("-----------Highest-paid employee!-----------")
Highest_paid_employee= df["Salary"].idxmax()
highest_salary_index = df.loc[Highest_paid_employee]
print(highest_salary_index)

print("-----------total salary!-----------")
total = df["Salary"].sum()
print(total)

print("-----------Highest-paying average job!-----------")
best_salary = mean_work_salary.idxmax()
best_salary_index = mean_work_salary.loc[best_salary]
print(best_salary_index)

print("-----------The city with the highest number of employees!-----------")
max_workers = df.groupby("City").size()
max_city = max_workers.idxmax()
print(max_city)

print("-----------Average work experience!-----------")
average_experience = df["Exp"].mean()
print(average_experience)
