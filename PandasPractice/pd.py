import pandas as pd
'''
# python dictionary obj to pd.Series obj
dict_data = {'song_name': 'STAY', 'artist': 'Bustin Jieber', 'release_date': 20220808}

sr = pd.Series(dict_data)
print(type(sr))
print('\n')
print(sr)  ## dtype: object

dict_data2 = {'a': 1, 'b': 2, '3': 20220808}
sr = pd.Series(dict_data2)
print(type(sr))
print('\n')
print(sr)  ## dtype: int64


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
'''

# python tuple obj to pd.Series obj
tuple_data = ('음성군', '진천읍', True, 4412)
sr = pd.Series(tuple_data, ['first_loc', 'second_loc', 'including', '_id'])
print(sr)

# slicing , choosing elements.



