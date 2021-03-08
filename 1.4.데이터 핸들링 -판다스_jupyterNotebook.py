#!/usr/bin/env python
# coding: utf-8

# In[1]:


#### 판다스(Pandas) 개요와 기본 API - 01, 02
### 판다스(Pandas) 개요와 기본 API - 01


# In[2]:


import pandas as pd


# In[3]:


# read_csv()
# read_csv()를 이용하여 csv 파일을 편리하게 DataFrame으로 로딩한다.
# read_csv()의 sep 인자를 콤마(,)가 아닌 다른 분리자로 변경하여
# 다른 유형의 파일도 로드가 가능하다.


# In[4]:


titanic_df = pd.read_csv('titanic_train.csv')
print('titanic 변수 type: ', type(titanic_df))


# In[5]:


# titanic 변수 type:  <class 'pandas.core.frame.DataFrame'>
# titanic_df는 이제 데이터 프레임이 됐다.

# read_csv 함수가 csv라고 돼 있어서 csv 파일만 로딩할 거 같지만,
# 다른 어떤 분리자도 가능하다.

# 쥬피터 노트북에서 titanic_df = pd.read_csv('titanic_train.csv')에 shift+tab
# 을 하면 함수 원형에 대한 설명이 뜬다.
# sep가 기본이 콤마다.
# csv는 자동으로 default로 로딩을 하게 된다.
# tab이라면 pd.read_csv('titanic_train.tsv', sep='\t') 이렇게 해 주면 된다.

# 또 함수 원형 설며에 header = 'infer'라고 돼 있다.
# csv 파일을 열어 보자.
# 맨 위에 PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 이렇게 컬럼 명이 들어가 있다.
# 이 컬럼 명을 보고 유추를 해서 판다스의 컬럼 명을 만들겠다는 의미다.
# 이것이 header = 'infer'의 의미다.


# In[6]:


### # 판다스(Pandas) 개요와 기본 API - 02
# head()
# DataFrame의 맨 앞 일부 데이터만 추출한다.
# 지난 시간에 read_csv() 써서 titanic_df라는 DataFrame을 만들었다.


# In[7]:


# titanic_df의 앞의 다섯 개만 보고 싶다.


# In[8]:


# default가 5이므로 titanic_df.head()로 해도 된다.


# In[9]:


titanic_df.head(5)


# In[10]:


# 데이터 프레임은 컬럼을 가지고 있다.
# 0, 1, 2, 3, 4는 컬럼명이 없다. index다.
# rdms에 익숙한 사람이 보면 아, 이것도 컬럼명이 있겠군, 하지만 없다.
# index는 순순하게 유일한 값만을 나타낸다.
# rdms 했던 사람이 이해를 쉽게 하려면, pk보다는 row num이나 row id 정도로
# 생각하면 된다. pk라고 논리적으로 생각하는 게 더 정확하긴 하다.
# 단지 index는 컬럼명이 할당돼 있지 않고 물리적으로 값을 가지고 있다.
# 판다스는 데이터 프레임이 기본적으로 numpy의 ndarray로 만들어져 있다.
# 전부다 ndarray다. 위 배열이 다 ndarray다. 
# 위 컬럼 값도 ndarray로 되어 있다(PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked)
# index도 ndarray로 돼 있고, 위에 있는 값이 모두 배열로 돼 있다.  


# In[11]:


# 아래와 같이 수동으로 데이터를 입력했을 때, 가장 쉽게 할 수 있는 것이 딕셔너리를 Dataframe으로 바꾸는 것이다. 
# 아래 딕셔너리의 key 값이 뭐가 될까? 바로 컬럼 명이 된다. dic1의 Name, Year, Gender
# Name, 이 키 값이 여러 개의 리스트를 가지고 있으면, 이게 바로 그 컬럼의 value가 되는 것이다. 
# 단, 리스트 안에 들어가 있는 원소는 동일한 형태라야 한다. 


# In[12]:


dic1 = {'Name': ['Chulmin', 'Eunkyung','Jinwoong','Soobeom'],
        'Year': [2011, 2016, 2015, 2015],
        'Gender': ['Male', 'Female', 'Male', 'Male']
       }
# 딕셔너리를 DataFrame으로 변환
data_df = pd.DataFrame(dic1)    # DataFrame 이 객체의 생성자로 dic1을 입력만 해 주면 된다. 그러면 키가 컬럼명으로 바뀐다. 
                                # 그리고 나머지 값들이 그 컬럼명에 value로 들어가게 된다
print(data_df)
print("#"*30)
 
# 새로운 컬럼명을 추가
data_df = pd.DataFrame(dic1, columns=["Name", "Year", "Gender", "Age"])    # columns라는 인자에 리스트를 넣어주면 된다. <-추가
print(data_df)
print("#"*30)

# 인덱스를 새로운 값으로 할당. 
data_df = pd.DataFrame(dic1, index=['one','two','three','four'])    # index는 default로 0, 1, 2와 같이 숫자로 생기지만, 
print(data_df)
print("#"*30)


# In[13]:


# 원래 인덱스는 default로 순차적으로 0, 1, 2 이런 식으로 생기지만, 'one', 'two', 'three'와 같이 문자형으로 넣어 줄 수도 있다. 
# 위 결과를 보면, 첫 번째는 컬럼이 Name, Year, Gender
# 두 번째는 Age라는 컬럼이 추가됐지만, 거기에 맵핑되는 데이터가 아무 것도 없기 때문에, 값은 NaN으로 초기화가 되었다. 
# 지금까지 index는 range 형 인덱스 즉, 숫자 0으로 시작해서 순차적으로 증가하는 형태였으나 'one', 'two', 'three'와 같이
# 지정된 문자 index 값이 지정이 된다. 


# In[14]:


### DataFrame의 컬럼명과 인덱스


# In[15]:


print('columns: ', titanic_df.columns)            # columns 출력


# In[16]:


# 위에서와 같이 컬럼명이 index 형태로 출력이 된다. 


# In[17]:


print('index: ', titanic_df.index)                # index 속성에 접속을 하면, index 값이 나오는 게 아니고, 그 index 객체가 반환됨.


# In[18]:


# index는 rangeIndex로, 0부터 시작해서 순차적으로 증가한다. 


# In[19]:


print('index value: ', titanic_df.index.values)   # index 값을 반환하려면, .values를 붙여 줘야 한다. 


# In[20]:


# 위를 보면 0부터 시작하는 ndarray다. 


# In[21]:


### DataFrame에서 series 추출 및 DataFrame 필터링 추출


# In[22]:


# dataframe에서 seires가 뭐라고 했지? 
# 컬럼이 한 개 있는 1차원 데이터 셋이다. 
# 위에서 보면 데이터 컬럼이 많다. 이 중에서 원하는 컬럼만 추출해 보자. 


# In[23]:


# DataFrame객체에서 []연산자내에 한개의 컬럼만 입력하면 Series 객체를 반환, 즉 series가 추출된다.  
series = titanic_df['Name']      # Name 컬럼을 가진 데이터를 추출해 주세요. 
print(series.head(3))             
print("## type:",type(series))   # type은 seires이다. 

# DataFrame객체에서 []연산자내에 여러 개의 컬럼을 리스트로 입력하면 그 컬럼들로 구성된 DataFrame 반환  
# 두 개 이상의 컬럼을 리스트로 입력하면, 그 컬럼으로 구성된 데이터 프레임을 반환한다. 
filtered_df = titanic_df[['Name', 'Age']]    # 두 개 이상일 경우에는 [] 리스트 안에 [] bracket이 또 들어가야 한다. 
                                             # 리스트로 이것들을 만들어 줘야 한다. 그러면 Name과 Age를 가진 데이터 프레임이 반환된다.
print(filtered_df.head(3))
print("## type:", type(filtered_df))

# DataFrame 객체에서 []연산자 내에 한 개의 컬럼을 리스트로 입력하면 한 개의 컬럼으로 구성된 DataFrame 반환
# 하나의 컬럼이지만, 아래와 같이 리스트로 감싸게 되면, series가 아니가 2차원을 가지는 데이터 프레임이 반환된다. 
one_col_df = titanic_df[['Name']]
print(one_col_df.head(3))
print("## type:", type(one_col_df))


# In[24]:


# 위 세 행이 출력 값이다. 
# 그다음 type을 보면 series이다. 첫 번째는 series인 것이다.
# 두 번째는 data type이다. 두 개의 컬럼을 가지는 이 데이터는 데이터 프레임이다. 
# 세 번째는, 브레킷 안에 리스트가 들어갔다. 컬럼이 하나지만 차원이 2차원이다. 즉 컬럼이 하나가 있다고 명시된 2차원 데이터 프레임이다. 


# ** shape ** DataFrame의 행(Row)와 열(Column) 크기를 가지고 있는 속성입니다.

# In[25]:


# 데이터 크기를 확인할 수 있는 가장 간단한 방법은 .shape()을 수행하는 것이다. 
# 어떤 사람들은 이 데이터 프레임에 들어가 있는 row 건수가 몇 건인지 알기 위해 count를 쓰는데 shape()이 더 쉽게 알 수 있다. 


# In[26]:


print('DataFrame 크기: ', titanic_df.shape)


# In[27]:


# (891, 12)는 rows 크기가 891, colunns의 크기가 12인 2차원 데이터 프레임이다. 
# 인덱스는 실제 컬럼에 포함이 되지 않는다. 확인을 해 봐라. 실제 확인을 해 보면 인덱스는 컬럼에 포함되어 있지 않음을 알 수 있다. 


# In[28]:


# infp()와 describe()에 대해서 살펴 보자. 


# info() DataFrame내의 컬럼명, 데이터 타입, Null건수, 데이터 건수 정보를 제공합니다.

# In[29]:


titanic_df.info()


# In[30]:


# 위와 같이 info()는 data의 메타 데이터를 보여준다. 
# RangeIndex가 891개 건수가 891건이다. 
# columms은 total 12개 columns가 있다. 
# 컬럼 개수가 모두 동일하지가 않다. 
# Age를 보면, 714개이다. 891 - 714 = 177개는 age 값이 non-null이다. 널 값이다. 
# 그리고 오른쪽을 보면 datatype이 int64는 64bits int type이라는 말이다. object는 그냥 string 문자열로 이해하라. 
# 봐야 할 것은, 맨아래 memory usage이다. 판다스 데이터 프레임도 메모리에 올라간다. 
# 대용량 데이터를 로딩할 때는 pysical memory를 얼마나 사용하고 있는 늘 주시해야 한다. 
# 다음은 describe()를 살펴 보자. 


# describe()
# 데이터값들의 평균,표준편차,4분위 분포도를 제공합니다. 숫자형 컬럼들에 대해서 해당 정보를 제공합니다.

# In[31]:


titanic_df.describe()


# In[34]:


# 위 Passengerld의 값은 무의미하다. Survived 카테고리도 생존이냐 사망이냐 0, 1로 보는 것이므로 카테고리성 컬럼이므로 무의미하다. 
# Pclass도 마찬가지다. 선실의 등급이므로, 1등급, 2등급, 3등급 이러므로 카테고리형일 뿐이다. 
# age 숫자형을 보면, 젊은 나이대 사람들이 많이 탔다는 걸 알 수 있다. 널 값은 빠져 있다. 
##
# 다음의 value count도 굉장히 많이 쓴다. 
# 특정 컬럼의 테이터 값의 분포도를 확인하기 위해서 많이 쓴다. 
# 예를 들면 Pclass의 값이 0, 1, 2, 3이 있다면, 0 값으로 몇 개의 데이터가 있고, 1 값으로 몇 개의 데이터가 있고, 
# 이런 히스토그램을 볼 때, value count를 쓰면 쉽게 볼 수가 있다. 
# 그런데 유의할 것은, value_count()는 series 객체에서만 호출될 수 있다. 
# 그래서 반드시 DataFrame을 단일 컬럼으로 입력하여 Series로 변환한 뒤 호출해야 한다. 
# 데이터 프레임의 함수만 쓰면, 전체 컬럼에 대해서 집합 연산을 해 주는 게 보통이다. 
# 하지만 이 value_count()는 그렇게 되지 않는다. 


# <!-- value_counts() \
# 동일한 개별 데이터 값이 몇 건이 있는지에 대한 정보를 제공합니다. \
# 즉 개별 데이터 값의 분포도를 제공합니다. 
# 주의할 점은 value_counts()는 Series객체에서만 호출 될 수 있으므로 
# 반드시 DataFrame을 단일 컬럼으로 입력하여 Series로 변환한 뒤 호출합니다. -->

# value_counts()
# 동일한 개별 데이터 값이 몇 건이 있는지에 대한 정보를 제공합니다. 
# 즉 개별 데이터 값의 분포도를 제공합니다. 
# 주의할 점은 value_counts()는 Series 객체에서만 호출 될 수 있으므로 
# 반드시 DataFrame을 단일 컬럼으로 입력하여 Series로 변환한 뒤 호출합니다.

# In[35]:


value_counts = titanic_df['Pclass'].value_counts()    # Pclass에 대해서 보고 싶다면, series로 만들어서 호출한다.
print(value_counts)


# In[36]:


# Pclass 3이 491개의 counts를 가지고 있고, 1이 216개, 2개 184개를 가지고 있다. 
# 한 가지 유의할 점은, 이것이 series인데, 맨 앞에 나와 있는 게 index다. 
# Pclass 값이기도 한데, value_counts()를 하면, 각각의 Pclass 값은 유일한 값이기 때문에, 
# 이것을 index로 사용한다. 


# In[37]:


titanic_pclass = titanic_df['Pclass']
print(type(titanic_pclass))


# In[38]:


titanic_pclass.head()


# In[39]:


value_counts = titanic_df['Pclass'].value_counts()    # value_counts()를 하면 반환이 되는데, 
print(type(value_counts))
print(value_counts)


# In[ ]:


# value_counts()를 통해서 반환되는 값은 series이다. 


# sort_values() by=정렬컬럼, ascending=True 또는 False로 오름차순/내림차순으로 정렬

# In[42]:


titanic_df.sort_values(by='Pclass', ascending=True)    # 인자로 by에 정렬하고자 하는 컬럼명을 입력한다. 오름차순은 True. 
                                                       # default는 오름차순이다. 
                                                       # 이렇게만 해 주면, Pclass를 기준으로 전체 데이터 프레임의 컬럼을 정렬한다. 
titanic_df[['Name','Age']].sort_values(by='Age')
titanic_df[['Name','Age','Pclass']].sort_values(by=['Pclass','Age'])   # 첫 번째는 Pclass로 두 번째는 Age로 정렬. 


# In[ ]:


# 그러면, Pclass로 정렬이 됐고 같은 Pclass 안에 Age가 오름차순으로 정렬됐다. 


# In[ ]:


# 판다스의 데이터 프레임에 사용되는 기본적인 API에 대해서 학습을 했다. 

