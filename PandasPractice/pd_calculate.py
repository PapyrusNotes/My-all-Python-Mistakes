"""
Pandas 객체의 산술연산은 내부적으로 3단계를 거쳐 수행된다.
1. 행/인덱스 기준으로 모든 원소를 정렬
2. 동일한 위치에 있는 원소끼리 일대일로 대응시킴
3. 일대일 대응되는 원손끼리 연산처리. 대응되는 원소가 없으면 NaN으로 처리
NaN = np.nan(NaN)
"""

import pandas as pd
import seaborn as sns
import numpy as np

'''
####################################################################### release quotation above
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1, '\n')

"""
Series 객체 + 연산자 + 숫자
과목별 점수를 200으로 나누기
"""

percentage_student1 = student1/200
print(percentage_student1, '\n')
print(type(percentage_student1), '\n')


"""
Series + 연산자 + Series
시리즈의 모든 인덱스에 대하여 인덱스를 가진 원소끼리 계산한다.
1. 두 시리즈간의 사칙 연산을 먼저 계산
2. DataFrame() 메서드를 사용하여 결과를 하나의 데이터프레임으로 합친다.

student1과 student2에 인덱스로 주어진 과목명의 순서가 다르지만
pandas는 같은 과목명을 찾아 정렬한 후 같은 과목명의 점수끼리 연산하고
새로운 시리즈 객체를 반환한다.

유효하지 않은 연산: 인덱스 대응 불가, 한 쪽이라도 대응값이 NaN인 경우
에 대해서는 NaN 반환. NaN = np.nan(NaN)
"""
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'영어':100, '수학':80, '국어':90})

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print(type(division))
print('\n')

result = pd.DataFrame([addition,subtraction,multiplication,division], index=['덧셈 결과', '뺄셈 결과', '곱셈 결과', '나눗셈 결과'])
print(result)

"""
Series + 연산 메서드(시리즈)
연산 메서드를 사용하면 fill_value 옵션으로 NaN값을 대체할 값을 지정할 수 있다.
"""
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)  # 영어 점수 80을 영어 점수 0으로 나누어서 inf(무한대) 값이 나옴.

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index=['덧셈 결과', '뺄셈 결과', '곱셈 결과', '나눗셈 결과'])
print(result)
####################################################################### release quotation below
'''

"""
DataFrame 연산.
시리즈 연산의 확장이다.
DataFrame 객체 + 연산자 + 숫자
1. 행/열 인덱스 기준으로 정렬하고 일대일 대응되는 원소끼리 연산을 처리.
어느 한 쪽에 원소가 존재하지 않거나 값이 NaN이면 연산 결과는 NaN으로 처리.
2. 새로운 DataFrame 객체로 반환된다.
seaborn 내장 데이터셋 참고
"""
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]  # age, fare column의  모든 열 표시
print(df.head(),'\n') # 첫 5행 표시
print(type(df),'\n')

addition = df + 10
print(addition.head(),'\n') # 첫 5행 표시
print(type(addition),'\n')

"""
DataFrame 연산
DataFrame + DataFrame

1. 각 DataFrame의 같은 행, 열 위치에 있는 원소끼리 게산.
2. 어느 한 쪽에 원소가 존재하지 않거나 값이 NaN이면 연산 결과는 NaN으로 처리.
"""
subtraction = addition - df
print(subtraction.tail(), '\n') # 마지막 5행 표시
print(type(subtraction),'\n')
