import pandas as pd

df = pd.DataFrame([[15,'남','덕영중'], [17,'여','수리중'], [22,'남','대한대'], [21,'여','민국대'],[25,'남','대한대']],
                  index=['학생1', '학생2', '학생3', '학생4', '학생5'], columns=['age','성별','학교'])
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

'''
# selecting column
col1 = df['학교']  # df.학교 표현은 column이 string일 때만 가능
print(col1)
df3 = df[['학교']]  # 열 하나만 뽑더라도 이중 리스트로 뽑으면 Dataframe이 반환됨
print(df3)
print(type(df3))  # pandas.core.frame.DataFrame
'''

'''
# slicing
print(df.iloc[ : 4:2])  # 0행부터 3행까지(4-1), 2행 간격으로 선택
print('\n')
print(df.iloc[ : 6:2])  # 0행부터 5행까지(6-1), 2행 간격으로 선택
print('\n')
print(df.iloc[ : : 2])  # 0행부터 끝 행까지, 모든 행에 대해 2행 간격으로 선택
print('\n')
print(df.iloc[ : : -1])  # 0행부터 끝 행까지,모든 행에 대해 역순으로 정렬
'''

'''
# choosing 1 element
print(df.loc['학생3','학교'])  # loc 행 이름, 열 이름
print(df.iloc[2, 2])  # iloc, 행 번호. 열 번호
print('\n')

# choosing 2 element
print(df.loc['학생3',['학교','성별']])  # loc 행 이름, 열 이름
print(df.iloc[2, [2, 1]])  # iloc, 행 번호. 열 번호
print('\n')

print(df.loc[['학생3','학생5'], ['학교','성별']])
print('\n')
print(df.loc['학생3':'학생5', '성별':'학교'])  # column의 순서를 지켜야지 정상적으로 출력됨, 지키지 않으면 Empty column
'''


# setting index
'''
exam_data = {'이름': ['aa','bb','cc','dd'],
             '수학': [90, 80, 70, 90],
             '영어': [90,80,70,70] }
df = pd.DataFrame(exam_data)

print(df)
df.set_index('이름',inplace=True)
print(df)

# Adding columns
df["국어"] = 80
print(df)

df["국어"] = [100,100,50,100]
print(df)

# Adding rows
df.loc['ee'] = 0
print(df)

df.loc['ff'] = [100, 100, 50]
print(df)

df.loc[6] = 80
print(df)
'''
'''
# Transpose
df = df.transpose()
print(df)
print('\n')

df = df.T
print(df)
'''

'''
# 특정 열을 행 인덱스로 지정 (inplace 옵션 존재)
ndf = df.set_index(['이름'])
print(ndf)

endf = df.set_index(['수학','영어'])  # multi-index
print(endf)
'''

'''
# 행 인데스 재배열
new_index=[0, 1, 2, 3, 4, 5]  # 기존에 존재하지 않았던 행의 열 값에는 NaN이 삽입됨
ndf = df.reindex(new_index)
print(ndf)

ndf = df.reindex(new_index, fill_value=0)  # NaN 대신 채울 값
print(ndf)
'''

# 행 인덱스 초기화
dict_data = [{'song_name': 'STAY', 'artist': 'Bustin Jieber', 'release_date': 20220808},
{'song_name': 'BEACHES', 'artist': 'Bustin Jieber', 'release_date': 20230421},
{'song_name': 'Rise', 'artist': 'The Glitch mob', 'release_date': 20170101}
             ]
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)

ndf = df.reset_index()  # 초기화시 기존 index는 열로 이동한다.
print(ndf)

# 행 인덱스 기준 정렬
ndf = df.sort_index(ascending=False) # ascending 옵션을 사용하여 오름차순, 내림차순 설정
print(ndf)

# 특정 열 값 기준 정렬
ndf = df.sort_values(by='release_date', ascending=False)
print(ndf)  # 정렬 속도? quick sort
