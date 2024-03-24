import unittest
import json
import pandas as pd
import numpy as np
import sys as system
import io
import re


with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            ## v save original
            compile("".join(i['source']), '<string>', 'exec')
            ##this is from previous TestCase => exec("".join(i['source']))

            code_ = "".join(i['source'])
            print(f'\n*************\nThis is the entire code:\n{code_}\n*******************\n')
            ## v Souley test
            #x = compile(code_, 'file', 'exec')
            #exec(x)
            
# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def testClassInit(self):
      data = pd.read_csv("tests/files/assignment8Data.csv")
      x = data[['sex','age','educ','white']]
      y = data['incwage']
      reg = RegressionModel(x, y, create_intercept=True)
      
      x = x.assign(intercept=pd.Series([1]*np.shape(x)[0]))
      self.assertTrue((reg.x.equals(x)) & (reg.y.equals(y)), "Your 'x' and 'y' attributes are not properly initialized.")
