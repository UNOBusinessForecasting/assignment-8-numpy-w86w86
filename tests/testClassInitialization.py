import unittest
import json
import pandas as pd

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            python_code = "".join(i['source'])
            compiled_code = compile(python_code, "<string>", "exec")
            exec(compiled_code)
            
# todo: replace this with an actual test
class TestCaseW(unittest.TestCase):
    def testClassInit(self):
      data = pd.read_csv("tests/files/assignment8Data.csv")
      x = data[['sex','age','educ','white']]
      y = data['incwage']
      reg = RegressionModel(x, y, create_intercept=True)
      
      x = x.assign(intercept=pd.Series([1]*np.shape(x)[0]))
      self.assertTrue((reg.x.equals(x)) & (reg.y.equals(y)), "Your 'x' and 'y' attributes are not properly initialized.")
