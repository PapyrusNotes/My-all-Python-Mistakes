import pandas as pd

df = pd.DataFrame([[22,'남','덕영중'], [17,'여','수리중']], index=['학생1','학생2'], columns=['age','성별','학교'])
df2 = df.rename(columns={'age': 'age', '성별': 'gender', '학교': 'school'})


# eq compare
'''
print(df == df2)   # ValueError: Can only compare identically-labeled (both index and columns) DataFrame objects
print(df2 == df)    
'''

'''
# drop column, row, inplace option 존재
df.drop('학생1', inplace=True)  # 기본 axis = 0
print(df)
df.drop(['성별'], axis=1, inplace=True)
print(df)
'''

# selecting data
'''
# selecting row
label1 = df.loc['학생1']  # ['학생1':'학생101']
label2 = df.loc['학생2']
position1 = df.iloc[0]   # [3:7]
position2 = df.iloc[1]
print(label1)     # pandas.core.series.Series
print(label2)
print(position1)  # pandas.core.series.Series
print(position2)
print(label1 == position1)  # series끼리 eq연산을 해도 원소끼리 비교한다.
'''

# selecting column
col1 = df['학교']
print(col1)
