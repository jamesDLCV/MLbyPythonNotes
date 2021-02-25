### 넘파이 ndarray의 인덱싱(indexing)을 통한 데이터 세트 선택하기 - 02
# ndarray의 데이터 세트 선택하기 - indexing
# 특정 위치의 단일값 추출
# 1. 인덱스 개념, 1차원 2차원 배열
# 2. 슬라이싱
# 3. 팬시 인덱싱
# 4. 블리언 인덱싱

import numpy as np

# 1에서부터 9까지의 1차원 ndarray 생성
array1 = np.arange(start=1, stop=10)    # 10은 포함되지 않는다.
print('array1: ', array1)       # array1:  [1 2 3 4 5 6 7 8 9]

## index는 0부터 시작하므로 array1[2]는 3번째 index 위치의 데이터 값을 의미
value = array1[2]
print('value: ', value)         # value:  3
print(type(value))              # <class 'numpy.int32'>

print('맨 뒤의 값: ', array1[-1], ', 맨 뒤에서 두 번째 값: ', array1[-2])
                                      # 맨 뒤의 값:  9 , 맨 뒤에서 두 번째 값:  8

array1[0] = 9
array1[8] = 0
print('array1', array1)         # array1 [9 2 3 4 5 6 7 8 0]

##1차원, 2차원 배열
array1d = np.arange(start=1, stop=10)       # 10은 불포함, 1~9까지 9개.
array2d = array1d.reshape(3, 3)
print(array2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print('(row=0, col=0) index가 가리키는 값: ', array2d[0, 0])      # 1
print('(row=0, col=1) index가 가리키는 값: ', array2d[0, 1])      # 2
print('(row=1, col=0) index가 가리키는 값: ', array2d[1, 0])      # 4
print('(row=2, col=2) index가 가리키는 값: ', array2d[2, 2])      # 9
print()

## Slicing 슬라이싱
array1 = np.arange(start=1, stop=10)
print(array1)                   # [1 2 3 4 5 6 7 8 9]
array3 = array1[0:3]
print(array3)                   # [1 2 3]
print(type(array3))           # <class 'numpy.ndarray'>
print()

array1 = np.arange(start=1, stop=10)
array4 = array1[:3]
print(array4)                   # [1 2 3]

array5 = array1[3:]
print(array5)                   # [4 5 6 7 8 9]

array6 = array1[:]
print(array6)                   # [1 2 3 4 5 6 7 8 9]

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print('array2d: \n', array2d)
# array2d:
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print('array2d[0:2, 0:2] \n', array2d[0:2, 0:2])
# array2d[0:2, 0:2]
#  [[1 2]
#  [4 5]]

print('array2d[1:3, 0:3] \n', array2d[1:3, 0:3])
# array2d[1:3, 0:3]
#  [[4 5 6]
#  [7 8 9]]

print('array2d[1:3, :] \n', array2d[1:3, :])
# array2d[1:3, :]
#  [[4 5 6]
#  [7 8 9]]

print('array2d[:, :] \n', array2d[:, :])
# array2d[:, :]
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print('array2d[:2, 1:] \n', array2d[:2, 1:])
# array2d[:2, 1:]
#  [[2 3]
#  [5 6]]

print('array2d[:2, 0] \n', array2d[:2, 0])
# array2d[:2, 0]
#  [1 4]               <-- [1] [4] 가 아니고 [1 4]가 출력되었다. 왜?
print()

## 팬시 인덱싱( fancy indexing)
# 연속적이지 않고 불연속적인 값도 가지고 올 수 있다.
array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print(array2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

array3 = array2d[[0, 1], 2]
print('array2d[[0, 1], 2] => ', array3.tolist())
# array2d[[0, 1], 2] =>  [3, 6]

array4 = array2d[[0, 2], 0:2]
print('array2d[[0, 2], 0:2] => ', array4.tolist())
# array2d[[0, 2], 0:2] =>  [[1, 2], [7, 8]]

array5 = array2d[[0, 1]]
print('array2d[[0, 1]] => ', array5.tolist())
# array2d[[0, 1]] =>  [[1, 2, 3], [4, 5, 6]]

## 블리언 인덱싱(Boolean indexing)
print('Boolean indexing >>>>>>')
array1d = np.arange(start=1, stop=10)
print(array1d)
# [1 2 3 4 5 6 7 8 9]

print(array1d > 5)
# [False False False False False  True  True  True  True]

var1 = array1d > 5
print('var1: ', var1)
# var1:  [False False False False False  True  True  True  True]
print(type(var1))
# <class 'numpy.ndarray'>
print()

## [] 안에 array1d > 5 Boolean indexing을 적용
print(array1d)
# [1 2 3 4 5 6 7 8 9]

array3 = array1d[array1d > 5]
print('array1d > 5 boolean indexing 결괏값: ', array3)
# array1d > 5 boolean indexing 결괏값:  [6 7 8 9]

boolean_indexes = np.array([False, False, False, False, False, True, True, True, True,])
array3 = array1d[boolean_indexes]
print('boolean index로 필터링 결과: ', array3)
# boolean index로 필터링 결과:  [6 7 8 9]

indexes = np.array([5, 6, 7, 8])
print(indexes)                                              # [5 6 7 8]
array4 = array1d[ indexes ]                          # index 5, 6, 7, 8 출력
print('일반 인덱스로 필터링 결과: ', array4)
# 일반 인덱스로 필터링 결과:  [6 7 8 9]
print()
array1d = np.arange(start=1, stop=10)
target = []

for i in range(0, 9):
    if array1d[i] > 5:
        target.append(array1d[i])

array_selected = np.array(target)
print(array_selected)                                   # [6 7 8 9]
print(array1d[array1 > 5])                           # [6 7 8 9], loop로 append한 위 값과 동일
# 불리언 인덱싱를 쓰면 간단하게 값을 구할 수 있다.

# numpy ndarray에서 인덱싱을 할 수 있는 네 가지 방법을 살펴 봤다.
# 1. 인덱스 개념, 1차원 2차원 배열
# 2. 슬라이싱
# 3. 팬시 인덱싱
# 4. 블리언 인덱싱
# 그중 불리언 인덱싱을 강조했다.





