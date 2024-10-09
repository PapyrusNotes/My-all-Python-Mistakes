import pandas as pd
'''
# python dict to pd.Series
dict_data = {'song_name': 'STAY', 'artist': 'Bustin Jieber', 'release_date': 20220808}

sr = pd.Series(dict_data)
print(type(sr))
print(sr)  ## dtype: object

idx = sr.index
val = sr.values
print(idx)
print(val)
print(type(val))  ## numpy.ndarray
print(type(idx))  ## pandas.core.indexes.base.Index
'''

'''
python dict to pd.Series
dict_data2 = {'a': 1, 'b': 2, '3': 20220808}
sr = pd.Series(dict_data2)
print(type(sr))
print('\n')
print(sr)  ## dtype: int64
'''


'''
# python dict to pd.Series 
dict_data3 = {'a': 'apple', 'b': 'bile', 'c': 'cyclone'}
sr = pd.Series(dict_data3)
print(type(sr))
print('\n')
print(sr)  ## dtype: object
idx = sr.index
val = sr.values
print(idx)
print(val)
print(type(val))  ## numpy.ndarray
print(type(idx))  ## pandas.core.indexes.base.Index
'''


'''
# python tuple to pd.Series
tuple_data = ('음성군', '진천읍', True, 4412)
sr = pd.Series(tuple_data, ['first_loc', 'second_loc', 'including', '_id'])
#print(sr)

# slicing , choosing elements.
sr[0]
sr['first_loc']
'''

'''
# {key:list as value} to Dataframe
dict_data = {'b1_34': ['24가1023'], 'b1_35': ['12가0734'], 'b2_22': ['09이2831', '28푸2122']}
# all arrays must be of the same length
dict_data = {'b1_34': ['24가1023'], 'b1_35': ['12가0734'], 'b2_22': ['09이2831']}
df = pd.DataFrame(dict_data)  # 행 인덱스에는 정수형 위치 인덱스가 자동 지정된다.
idx = df.index
print(df)
print(type(df))
print(idx)          # RangeIndex(start=0, stop=1, step=1)
print(type(idx))    # pandas.core.indexes.range.RangeIndex
'''


# two-dimensional python list to Dataframe
df = pd.DataFrame([[22,'남','덕영중'], [17,'여','수리중']], index=['학생1','학생2'], columns=['age','성별','학교'])
print(df)
print(df.index)
print(type(df.index))    # pandas.core.indexes.base.Index
print(df.columns)
print(type(df.columns))  # pandas.core.indexes.base.Index

df.index = ['참가자1', '참가자2']  # '참가자3' 추가시 ValueError: Length mismatch
df.columns = ['나이', 'gender', '소속']
print(df)
print(df.index)
print(type(df.index))    # pandas.core.indexes.base.Index
print(df.columns)
print(type(df.columns))  # pandas.core.indexes.base.Index

df.rename(columns={'나이': 'age', 'gender': 'gender', '소속': 'school'}, inplace=True)
df2 = df.rename(columns={'나이': 'age', 'gender': 'gender', '소속': 'school'})
# 기본적으로 rename 메서드는 새로운 df 객체를 반환한다. inplace=True 옵션으로 원본 객체 내에서 값을 대체할 수 있다.
print(df)
print(df2)
print(type(df))
print('id of df :', id(df))
print('id of df2 :', id(df2))



