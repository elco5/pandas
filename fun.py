# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
# https://ipython.readthedocs.io/en/stable/interactive/tutorial.html


from xml.etree.ElementTree import Element
import pandas as pd

data_file = r"C:\Users\count\dev\pandas\data\titanic.csv"

titanic = pd.read_csv(data_file)

# print(titanic.head())

ages = titanic["Age"]

over_35 = titanic[titanic["Age"] > 35]

# I’m interested in rows 10 till 25 and columns 3 to 5.
titanic.iloc[9:25, 2:5]

# /////////////////////
A = [1,2,3]
def build_series(A):
    n = 2 #repeat each element n times
    B = []
    for element in A:
        for i in range(n):
            B.append(element)
    return B

def find_step_index(A):
    print(f'len(A)=', len(A))
    for index, element in enumerate(A):
        print(index, element)
        
        # if index < len(A):
        #     avg = (element + A[index + 1] )/2
        #     print(index, element, avg)

B = build_series(A)            
find_step_index(B)