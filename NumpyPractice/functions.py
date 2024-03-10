import numpy as np

if __name__ == '__main__':
    array1 = np.array([1, 2, 3])
    array2 = np.array([[1, 2, 3], [4, 5, 6]])
    array3 = np.array([[1, 2, 3]])

    # array1 array info
    print(f'array1 : {array1} ')
    print(f'array1 type : {type(array1)}')
    print(f'array1 shape : {array1.shape}')  # (행, 열) 1차원 배열
    print(f'array1 dimension : {array1.ndim}')
    print("\n")

    # array2 array info
    print(f'array2 : {array2} ')
    print(f'array2 type : {type(array2)}')
    print(f'array2 shape : {array2.shape}')
    print(f'array2 dimension : {array2.ndim}')
    print("\n")

    # array3 array info
    print(f'array3 : {array3} ')
    print(f'array3 type : {type(array3)}')
    print(f'array3 shape : {array3.shape}')  # 2차원 배열
    print(f'array3 dimension : {array3.ndim}')
    print("\n")

    # generate data in a row
    new_data = np.arange(20)
    print(f'new data : {new_data}')

    # generate data with step
    new_data = np.arange(1, 20, 3)
    print(f'new data : {new_data}')

    # initialize array
    zero_a = np.zeros((2, 5))
    one_a = np.ones((3, 4))
    print(f'zero array : {zero_a}')
    print(f'one array : {one_a}')


