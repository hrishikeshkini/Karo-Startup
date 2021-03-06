# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VmSH3uX1uowRSmOaFi16Zr0lgLCjuAyA
"""

import pandas as pd
import numpy as np

df  = pd.read_excel('/content/skill_data.xlsx')

df

web_devloper_skills = [
    'django',
    'html',
    'css',
    'nodejs',
    'reactjs',
    'nodejs',
    'flask',
    'laravel'
]

machine_learning_skills = [
    'nosql',
    'pandas',
    'numpy',
    'matpotlib',
    'seabron',
    'scipy'
]

df.isnull().sum()

df['Skills'].values

len(df['Skills'].values)

skills=df["Skills"].values
skills

skills[0]

cleaned = [i[1:-1] for i in skills[0][1:-1].split(", ")]
cleaned

np.intersect1d(cleaned,web_devloper_skills)

np.intersect1d(cleaned,machine_learning_skills)

Designation = []
No_of_skills = []


for num in range(len(skills)):
    cleaned = [i[1:-1] for i in skills[num][1:-1].split(", ")]

    web_developer = np.intersect1d(cleaned,web_devloper_skills)
    Machine_learning = np.intersect1d(cleaned,machine_learning_skills)

    No_of_skills.append(len(cleaned))

    if len(web_developer) >= 3:
        Designation.append("Web Developer")

    elif len(Machine_learning) >= 3:
        Designation.append("Machine Learning")

    else:
        Designation.append("No Skills")

Designation

No_of_skills

df["Designation"]=Designation
df

df["No_of_skills"]=No_of_skills
df

df.head()

df.to_excel("result.xlsx", sheet_name="result", index=False)