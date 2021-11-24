#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 22:27:18 2021

@author: jruecke
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("eda_data.csv")

# choose relevant columns
df.columns

df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry','Sector', 'Revenue', 'num_comp', 'hourly', 'employer_provided','job_state', 'same_state', 'age', 'python_yn', 
'spark', 'aws', 'excel', 'job_simp', 'seniority', 'desc_len']]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train test set
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis=1)
y= df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression
# lasso regression
# random forest
# tune models using GridsearchCV
# test ensembles