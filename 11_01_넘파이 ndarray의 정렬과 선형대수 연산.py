### 11_넘파이 ndarray의 정렬과 선형대수 연산
## 배열의 정렬 - sort()와 argsort()

## sort()
## 넘파이 sort() 유형
# - np.sort(): 원 행렬은 그대로 유지한 채 원 행렬의 정렬된 행렬을 반환한다.
# - ndarray.sort(): 원 행렬 자체를 정렬한 형태로 변환하며 반환 값은 None이다.
# np.sort()를 쓰면 괄호 안에 인자로 원 행렬이 들어간다.
# np.sort()나 ndarray.sort() 모두 기본적으로 오름차순으로 행렬 내 원소를 정렬한다.
# 내림차순으로 정렬하기 위해서는 [::-1]을 적용한다.
# np.sort()[::-1]과 같이 사용한다.

## 2차원 배열에서 axis 기반의 sort()

## argsort()
# 많이 사용된다.
# 원본 행렬 정령 시 정렬된 행렬의 원래 인덱스를 필요로 할 때 np.argsort()를
# 사용한다. np.argsort()는 정렬 행렬의 원본 행렬 인덱스를 ndarray 형으로 반환
# sorting을 하긴 하는데 sorting된 데이터를 반환하는 것이 아니라,
# sorting을 했을 때, 원본 행렬에 있던 인덱스를 반환한다.
# ndarray는 판다스 데이터 프레임이나 IDMS table 같이 column 형이나
# 메타성 데이터가 없다.
# 그래서 key하고 value를 mapping 해야 된다.
# 이름이 a인 값은 9, 이름이 bd인 값은 10 이렇게 맵핑을 하고자 하는데,
# 맵핑을 할 수가 없다. 그래서 a의 매타성 값을 가지고 있는 값을 ndarray로
# 만들어 놓고, value 값들은 또 다른 ndarray로 만들어서 암묵적으로 맵핑을 한다.
# 그럴 때 sorting을 해야 하는 경우가 있다.
# 그때 argsort()를 쓰면, 이런 메타성 데이터들, 또 key value에 있는 key 값들에 대한
# value 값이 정렬이 되면서, key 값들이 어떻게 반환이 되는지 명확하게 알 수가 있다.

## 선형대수 연산 - 행렬 내적
# np.dot(A, B)
# 행렬 곱셈 방식 숙지
## 선형대수 연산 - 전치 행렬
# np.transpose(A)
# 행과 열의 위치를 바꾸는 것이다.
# 코드를 보면서 확인해 보자.
import numpy as np

org_array = np.array([3, 1, 9, 5])  # 1차원 ndarray 이다.
print('원본 행렬: ', org_array)         # 원본 행렬:  [3 1 9 5]

# np.sort()로 정렬
sort_array1 = np.sort(org_array)
print('np.sort() 호출 후 반환된 정렬 행렬: ', sort_array1)
# np.sort() 호출 후 반환된 정렬 행렬:  [1 3 5 9] <== 변환이 돼서 반환.

print('np.sort() 호출 후 원본 행렬: ', org_array)
# np.sort() 호출 후 원본 행렬:  [3 1 9 5] <== np.sort()로 정렬을 하면,
# 원본 행렬은 변하지 않는다.
print()

## ndarray.sort()로 정렬
sort_array2 = org_array.sort()      # 원본 array에 sort()를 호출하면,
                                                # 원본 array가 변하게 된다.
org_array.sort()
print('org_array.sort() 호출 후 반환된 행렬: ', sort_array2)
# org_array.sort() 호출 후 반환된 행렬:  None
# <- 이렇게 반환 값은 None이다.
# <- 이런 식으로 호출이 됐을 때, None을 반환하는 유형들을 알아 둬야 한다.

print('org_array.sort() 호출 후  원본 행렬: ', org_array)
# org_array.sort() 호출 후  원본 행렬:  [1 3 5 9]
# <- 원본 array도 변환이 됐다.
print()

## 내림차순 정렬, [::-1]
sort_array1_desc = np.sort(org_array)[::-1]
print('내림 차순으로 정렬: ', sort_array1_desc)
# 내림차순으로 정렬:  [9 5 3 1]
print()

## axis의 방향으로도 sorting을 할 수 있다.
array2d = np.array([[8, 12],
                             [7, 1]])
sort_array2d_axis0 = np.sort(array2d, axis=0)
print('row 방향으로 정렬: \n', sort_array2d_axis0)    # 같은 열의 행 끼리 sorting
# row 방향으로 정렬:
#  [[ 7  1]
#  [ 8 12]]
# <- axis=0은 행이 바뀐다.

sort_array2d_axis1 = np.sort(array2d, axis=1)           # 같은 행의 열 끼리 sorting
print('column 방향으로 정렬: \n', sort_array2d_axis1)
# [[8 12]
#  [1  7]]
# <- axis=1은 열이 바뀐다.
print()

## argsort, argument sort
org_array = np.array([3, 1, 9, 5])
print(np.sort(org_array))
# [1 3 5 9]

sort_indices = np.argsort(org_array)
print('행렬 정렬 시 원본 행렬의 인덱스: ', sort_indices)
# 행렬 정렬 시 원본 행렬의 인덱스:  [1 0 3 2]
# <- [1 3 5 9], 1은 원본 행렬의 위치 인덱스 1에 있었다. 3은 위치 인덱스 0에 있었다.
# 5는 원본 행렬의 위치 인덱스 3에 있어고, 9는 위치 인덱스 2에 있었다.
# 고로 [1 0 3 2]가 출력되었다.

print(type(sort_indices))
# <class 'numpy.ndarray'>
print()

# argsort() 내림차순을 알아 보자.
org_array = np.array([3, 1, 9, 5])
print(np.sort(org_array)[::-1])
# [9 5 3 1]

sort_indices_desc = np.argsort(org_array)[::-1]     # 마찬가지로 [::-1]를 붙인다.
print(sort_indices_desc)
# [2 3 0 1]
# <- [9 5 3 1]로 정렬된 행렬의 원본 행렬에서는, 9가 위치 인덱스 2다.
# 5는 원본 행렬의 위치 인덱스가 3, 3은 0, 1은 원본 행렬의 위치 인덱스가 1이다.
# 고로 [2 3 0 1]이 출려되었다.
print()

## argsort()가 자주 쓰이는 경우는, key value mapping을 해야 될 때이다.
# ndarray로는 특성상 할 수가 없다. 다음의 예를 통해 살펴 보자.
# 점수를 오름차순으로 정렬해서 사람의 이름을 출력하고 싶다.
# key-value 형태의 데이터,
# John=78, Mike=95, Sarah=84, Kate=98, Samuel=88을
# ndarray로 만들고 argsort()를 이용하여 key 값을 정렬해 보자.
name_array = np.array(['John', 'Mike', 'Sarah', 'Kate', 'Samuel'])
score_array = np.array([78, 95, 84, 98, 88])

# score_array의 정렬된 값에 해당하는 원본 행렬 위치 인덱스를 반환하고
# 이를 이용하여 name_array에서 name 값 추출.
sort_indices = np.argsort(score_array)
print('sort indices: ', sort_indices)
# sort indices:  [0 2 4 1 3]

name_array_sort = name_array[sort_indices]
score_array_sort = score_array[sort_indices]

print(name_array_sort)
# ['John' 'Sarah' 'Samuel' 'Mike' 'Kate']
print(score_array_sort)
# [78 84 88 95 98]
print()

## 선형대수 연산 - 행렬 내적과 전치 행렬 구하기
## 행렬 내적
# 행렬 내적은 간단하게 np.dot() 함수에 행렬을 넣어주면 된다.
A = np.array([[1, 2, 3],
                    [4, 5, 6]])
B = np.array([[7, 8],
                    [9, 10],
                    [11, 12]])

dot_product = np.dot(A, B)
print('행렬 내적 결과: \n', dot_product)
# 행렬 내적 결과:
#  [[ 58  64]
#  [139 154]]
print()

## 전치 행렬
# 간단하게 transpose() 함수를 호출하면 된다.
A = np.array([[1, 2],
                    [3, 4]])

transpose_mat = np.transpose(A)
print('A의 전치 행렬: \n', transpose_mat)
# A의 전치 행렬:
#  [[1 3]
#  [2 4]]

# 지금까지,
# ndarray의 sorting에 대해서 살펴 봤고
# 간단한 선형대수 연산에 대해서 살펴 봤다.

## 넘파이 Summary
# 넘파이는 파이썬 머신러닝을 구성하는 핵심 기반으로 반드시 이해가 필요하다.
# 넘파이 API는 매우 넓은 범위를 다루고 있으므로 머신러닝 애플리케이션을 작성할 때
# 중요하게 활용될 수 있는 핵심 개념 위주로 숙지하는 것이 좋다.
# 넘파이는 판다스에 비해서 친절한 API를 제공하지는 않는다.
# 2차원의 데이터라면 데이터 가공을 위해서 넘파이보다는
# 판다스를 이용하는 것이 보다 효율적이다.

# 넘파이를 처음부터 깊이 파고들면 너무 많은 양 때문에 힘들다.
# 다큐먼테이션도 그렇게 친절하지가 않다.
# 앞에서 다룬 넘파이의 중요한 개념들, shape(), 차원, axis 등 이런 것들에 대한 개념을
# 확실하게 잡는 게 1차적으로 중요하다.
# 3차원 데이터, 예를 들어 픽셀인데 RGB 값이 들어 있는 색깔로 된 이미지를 다룰 때는
# 2차원 데이터로 나타낼 수가 없으므로 3차원 데이터를 사용해야 한다.
# 이럴 때는 판다스를 못 쓰고 넘파이를 활용해야 한다.
# 그러므로 넘파이는 중요하다.
# 다음 시간부터는 판다스에 대해 살펴 본다.






