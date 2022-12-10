import pandas as pd

l1 = [1, 3, 5, 7, 9, 11]

l2 = [0, 2, 4, 8, 10, 12]

df = pd.DataFrame({'Par' : l2, 'Impar' : l1})

df.to_csv('Lista.csv')