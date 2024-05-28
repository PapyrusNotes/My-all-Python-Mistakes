import pandas as pd

data = pd.read_csv("./datasets/housing_data.csv", header=None, sep=',')  # if no columns , header = None
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                'MEDV', 'isHighValue']
data.columns = column_names

# print(data.head())  # data.head()  dataset 앞부분 확인
# print(data.shape)   # data.shape   dataset 헹x열 확인
# print(data.info())  # data.info()  data 타입, null 값 여부 확인
# print(data.describe()) 컬럼별 기본 통계량 확인
print(data.isnull().sum())  # 컬럼별 결측치 개수

# 결측치 처리

# 이상치 처리


