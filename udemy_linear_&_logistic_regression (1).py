

import pandas as pd

data1=pd.read_csv('/content/sample_data/Customer.csv',header=0)

data1.head()

data2=pd.read_csv('/content/sample_data/Customer.csv',header=0,index_col=0)
data2.head()

data2.describe()

data2.iloc[0]

data2.loc['CG-12520']

data2.iloc[1:3]

"""#Seaborn"""

import seaborn as sns

sns.distplot(data2.Age)

iris=sns.load_dataset('iris')

iris.tail()

iris.describe()

sns.jointplot(x="sepal_length",y="sepal_width",data=iris)

sns.pairplot(iris)

pwd

""" # House Price Prediction """

import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv('/content/sample_data/House_Price.csv',header=0)
df.head()

df.shape

df.describe()

sns.jointplot(x='n_hot_rooms',y='price',data=df)

sns.jointplot(x='rainfall',y='price',data=df)

#Working on categorical variables
sns.countplot(x='airport',data=df)

sns.countplot(x='waterbody',data=df)

sns.countplot(x='bus_ter',data=df)

"""#Observations from the above graphs are:
###1.Missing values in n_hos_beds (Observed from describe)
###2.skewness or outliers in crime rate
###3.Outliers in n_hot_rooms and rainfall
###3.Bus_ter has only YES value

"""

df.info()

#Out-liers Treatment
uv=np.percentile(df.n_hot_rooms,[99])[0]

df[df.n_hot_rooms>uv]

df.n_hot_rooms[df.n_hot_rooms>3*uv]=3*uv

lv=np.percentile(df.rainfall,[1])[0]

df[df.rainfall<lv]

df.rainfall[df.rainfall<0.3*lv]=0.3*lv

sns.jointplot(x='crime_rate',y='price',data=df)

##Missing Values Treatment
df.info()

df.n_hos_beds=df.n_hos_beds.fillna(df.n_hos_beds.mean())

df.info()

##Variable Transformation and Deletion  
sns.jointplot(x='crime_rate',y='price',data=df)

df.crime_rate=np.log(1+df.crime_rate)

sns.jointplot(x='crime_rate',y='price',data=df)

df['avg_dist']=(df.dist1+df.dist2+df.dist3+df.dist4)/4

df.describe()

del df['dist1']
del df['dist2']
del df['dist3']
del df['dist4']

df.describe()

sns.jointplot(x='avg_dist',y='price',data=df)

del df['bus_ter']

df=pd.get_dummies(df)

df.head()

del df['airport_NO']

del df['waterbody_None']

df.head()

df.corr()

del df['parks']

df.head()

"""#Building the Linear Regression Model

"""

import statsmodels.api as sn

X=sn.add_constant(df['room_num'])

lm=sn.OLS(df['price'],X).fit()

lm.summary()

"""##Another Method for linear Regression"""

from sklearn.linear_model import LinearRegression

y=df['price']

X=df[['room_num']]

lm2=LinearRegression()

lm2.fit(X,y)

print(lm2.intercept_,lm2.coef_)

lm2.predict(X)

sns.jointplot(x=df['room_num'],y='price',kind='reg',data=df)

"""#Multiple Linear Regression"""

X_multi=df.drop('price',axis=1)

X_multi.head()

y_multi=df['price']

y_multi.head()

X_multi_const=sn.add_constant(X_multi)

X_multi_const.head()

lm_multi=sn.OLS(y_multi,X_multi_const).fit()

lm_multi.summary()

##Using SKLEARN
lm3=LinearRegression()

lm3.fit(X_multi,y_multi)

print(lm3.intercept_,lm3.coef_)

"""#Test Train Split """

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X_multi,y_multi,test_size=0.2,random_state=0)

print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

lm_a=LinearRegression()

lm_a.fit(X_train,y_train)

y_test_a=lm_a.predict(X_test)

y_train_a=lm_a.predict(X_train)

y_train_a

from sklearn.metrics import r2_score

r2_score(y_test,y_test_a)

r2_score(y_train,y_train_a)







































