from env import get_db_url
import numpy as np
from pydataset import data
import pandas as pd

############################ Exercise PT 1 ###############################

# 4 Use your function to obtain a connection to the employees database.

url = get_db_url('employees')
sql = '''
SELECT * 
FROM employees
LIMIT 15
'''
our_employees = pd.read_sql(sql, url)
print(our_employees.head())

# 5a) Intentionally make a typo in the database url. What kind of error
#     message do you see?

"""
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1044, 
"Access denied for user 'jemison_1739'@'%' to database 'employes'")
"""


# 5b) Intentionally make an error in your SQL query. What does the error 
#     message look like?

"""
sqlalchemy.exc.ProgrammingError: (pymysql.err.ProgrammingError) 
(1146, "Table 'employees.employe' doesn't exist")
"""

# 6) Read the employees and titles tables into two separate DataFrames.

titles_sql = """
SELECT * 
FROM titles
"""

titles = pd.read_sql(titles_sql, url)

employees_sql = """
SELECT *
FROM employees
"""

employees_table = pd.read_sql(employees_sql, url)
print(employees_table.head())
print(titles.head())


# 7) How many rows and columns do you have in each DataFrame? 
#    Is that what you expected?


print(f"titles rows x col: {titles.shape}")
print(f"employees rows x col: {employees_table.shape}")

"""
titles rows x col: 443308 x 4
employees rows x col: 300024 x 6
It's what I expected.
"""

# 8) Display the summary statistics for each DataFrame.

print(titles.describe())
print(employees_table.describe())

# 9) How many unique titles are in the titles DataFrame?

print(f"Unique titles: {len(titles.title.unique())}")

""" Answer: 7 """

# 10) What is the oldest date in the to_date column?

print(f"oldest date in to-date col: {titles.to_date.min()}")

""" Answer: 1985-03-01 """

# 11) What is the most recent date in the to_date column?

recent_dates = ~titles.to_date.astype('str').str.contains('9999')
print(f"Most recent date in to-date col: {titles[recent_dates].to_date.max()}")

""" Answer: 2002-08-01 """

other_title = """
SELECT MAX(to_date) FROM (SELECT to_date FROM titles WHERE YEAR(to_date) <> '9999') as NewDate;
"""
print(f"most recent date: {pd.read_sql(other_title, url)}")

############################ Exercise PT 2 ###############################


# 1) Copy the users and roles DataFrames from the examples above.
# Create the roles/users DataFrames

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

# 2) What is the result of using a right join on the DataFrames?

#users.merge(roles, left_on='role_id', right_on='id', how='right')
#print(users)
"""
   id   name  role_id
0   1    bob      1.0
1   2    joe      2.0
2   3  sally      3.0
3   4   adam      3.0
4   5   jane      NaN
5   6   mike      NaN
"""

# 3) What is the result of using an outer join on the DataFrames?

#users.merge(roles, left_on='role_id', right_on='id', how='outer')
#print(users)

"""
   id   name  role_id
0   1    bob      1.0
1   2    joe      2.0
2   3  sally      3.0
3   4   adam      3.0
4   5   jane      NaN
5   6   mike      NaN
"""

# 4 What happens if you drop the foreign keys from the DataFrames and 
# try to merge them?
"""
users.drop('role_id')
roles.drop('id')

users.merge(roles, left_on='role_id', right_on='role_id')
print(users)
"""
# KeyError: "['role_id'] not found in axis"



# 5) Load the mpg dataset from PyDataset.

mpg = data('mpg', show_doc=True)
mpg = data('mpg')

# 6) Output and read the documentation for the mpg dataset.

# see above


# 7) How many rows and columns are in the dataset?


# 234 rows, 11 columns see above for code



# 8) Check out your column names and perform any cleanup you may want on 
#    them.

print(mpg.head())


# 9) Display the summary statistics for the dataset.
mpg.describe()

# 10) How many different manufacturers are there?

print(f"# of different manufacturers: {len(mpg.manufacturer.unique())}")

# 11) How many different models are there?

print(f"# of different models: {len(mpg.model.unique())}")

# 12) Create a column named mileage_difference like you did in the
#     DataFrames exercises; this column should contain the difference 
#     between highway and city mileage for each car.

mpg['mileage_difference'] = mpg.hwy - mpg.cty

# 13) Create a column named average_mileage like you did in the DataFrames 
#     exercises; this is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg.hwy + mpg.cty) / 2

# 14) Create a new column on the mpg dataset named is_automatic that holds
#     boolean values denoting whether the car has an automatic transmission.

mpg['is_automatic'] = mpg.trans.str.contains('auto')

# 15) Using the mpg dataset, find out which which manufacturer has the best 
#     miles per gallon on average?

print(f"manufacturer with best mpg on average: {mpg.groupby(by='manufacturer').average_mileage.mean().idxmax()}")

# 16) Do automatic or manual cars have better miles per gallon?

autos = mpg.trans.str.contains('auto')
manuals = ~autos

if mpg[autos].average_mileage.mean() > mpg[manuals].average_mileage.mean():
    print('autos have better mpg')
else:
    print('manuals have better mpg')

# alternatively

# do automatics have higher mpg than manuals
print(mpg.groupby(by='is_automatic').average_mileage.mean().idxmax())
# False

print(mpg.head())