import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from sklearn.linear_model import LinearRegression

data = pd.read_csv("./datasets/housing_data.csv", header=None, sep=',')  # if no columns , header = None
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                'MEDV', 'isHighValue']

data.columns = column_names

# print(data.head())  # data.head()  dataset 앞부분 확인
# print(data.shape)   # data.shape   dataset 헹x열 확인
# print(data.info())  # data.info()  data 타입, null 값 여부 확인
# print(data.describe()) # 컬럼별 기본 통계량 확인
# print(data.isnull().sum())  # 컬럼별 결측치 개수
# print(data.isnull().sum()/data.shape[0])  # 컬럼별 결측치 비율 확인

# 결측치 처리 - 중앙값 대치
data1 = data.copy()  # Pandas의 Dataframe.copy는 기본 deepcopy이다.
med_val = data['CRIM'].median()
data1['CRIM'] = data1['CRIM'].fillna(med_val)


# print(data1.describe())

# 결측치 처리 - CRIM column의 행들 중 결측치가 존재하는 행들 제거
# data = data.loc[data['CRIM'].notnull(), ]
# print(data.describe())

# 결측치 처리 - 결측치가 존재하는 모든 행 제거
data.dropna(inplace=True)  # inplace option 사용할시 변경된 데이터프레임 만들지 않고 대체.

# 이상치 처리 - 판단 기준 IQR ( Interquartile range ) = q3 - q1
'''
def get_iqr_outlier_prop(x):
    Q1, Q3 = data['MEDV'].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    print(f"IQR : {IQR}")
    print(f"Upper bound : {upper_bound}")
    print(f"Lower bound : {lower_bound}")

    print("Outlier 범위 : %.2f 초과 , %.2f 미만" % (upper_bound, lower_bound))
    print("Outlier 개수 : %.0f" % len(data[(data['MEDV'] > upper_bound) | (data['MEDV'] < lower_bound)]))
    print("Outlier 비율 : %.2f" % (len(data[(data['MEDV'] > upper_bound) | (data['MEDV'] < lower_bound)]) / len(data)))

    return
'''
# print(data['CRIM'].skew())

data['CRIM'] = np.log1p(data['CRIM'])
# print(data['CRIM'].skew())

# df_r에 종속변수를 제외한 독립변수들만 남겨놓는다.
df_r = data.drop(['isHighValue'], axis=1)

# 변수간 상관관계 분석
cols = ['MEDV', 'LSTAT', 'RM', 'CHAS', 'RAD', 'TAX']
# print(df_r[cols].corr())

# 데이터 분할
X_cols = ['LSTAT', 'PTRATIO', 'TAX', 'AGE', 'NOX', 'INDUS', 'CRIM']

X = df_r[X_cols].values
y = df_r['MEDV'].values

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y, test_size=0.3, random_state=123)

# 데이터 스케일링
scaler = MinMaxScaler()

X_train_r_scaled = scaler.fit_transform(X_train_r)
X_test_r_scaled = scaler.fit_transform(X_test_r)

# 선형회귀 모델
model_lr = LinearRegression()
model_lr.fit(X_train_r_scaled, y_train_r)
print(model_lr.coef_)
print(model_lr.intercept_)
