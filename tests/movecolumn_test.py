import pandas as pd
import numpy as np

import movecolumn as mc

# Create a dataframe
df = pd.DataFrame(np.array([[1, 2, 3, 5, 6,3], [4, 5, 6, 2 ,6,6], [7, 8, 9, 7, 8, 4]]),
                   columns=['a', 'b', 'c', 'd' , 'e', 'f'])
print(df.head())

# move column b to first position
df1 = mc.MoveTo1(df,'b')
print(df1.head())

# move column d to second position
df2 = mc.MoveTo2(df,'d')
print(df2.head())

# move column d to second position
df3 = mc.MoveTo3(df,'d')
print(df3.head())

# move column e to second position
df4 = mc.MoveTo4(df,'e')
print(df4.head())

# move column e to second position
df5 = mc.MoveTo5(df,'e')
print(df5.head())

# move column c to last position
df6 = mc.MoveToLast(df,'c')
print(df6.head())

# move column d to nth position, n = 1 for left most column, 2 for second column
df7 = mc.MoveToN(df,'f',3)
print(df7.head())
