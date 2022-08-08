__version__ = '0.0.1'

# Code to move column to position 1
def MoveTo1(df, col):
    col1 = df.pop(col)
    df.insert(loc= 0 , column= col, value= col1)
    return df

# Code to move column to position 2
def MoveTo2(df, col):
    col1 = df.pop(col)
    df.insert(loc= 1 , column= col, value= col1)
    return df

# Code to move column to position 3
def MoveTo3(df, col):
    col1 = df.pop(col)
    df.insert(loc= 2 , column= col, value= col1)
    return df

# Code to move column to position 4
def MoveTo4(df, col):
    col1 = df.pop(col)
    df.insert(loc= 3 , column= col, value= col1)
    return df

# Code to move column to position 5
def MoveTo5(df, col):
    col1 = df.pop(col)
    df.insert(loc= 4 , column= col, value= col1)
    return df

# Code to move column to last position
def MoveToLast(df, col):
    col1 = df.pop(col)
    df.insert(loc= len(df.columns) , column= col, value= col1)
    return df

# Code to move column to position n
def MoveToN(df, col, n):
    col1 = df.pop(col)
    df.insert(loc= n-1 , column= col, value= col1)
    return df

