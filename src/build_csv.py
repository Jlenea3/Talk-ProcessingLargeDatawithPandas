'''
Author: Evelyn J. Boettcher
Date: June 2019
Info: This script creates csv files from defined fields

'''
import pandas as pd
import random
import math

def strings_colums(n):
    '''
    INPUTS:
    =======
       n = Int
        n is the number of rows created

    RETURNS:
    ========
        df = dataframe
         panda dataframe with n rows
    '''
    # Define create a string of repeatable strings
    ## USING categories to spead up creation
    val_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    val_hello = [ 'Hello', 'World']
    val_locations = ['Dayton', 'Beavercreek', 'Oakwood', 'Fairfield', 'Huber', 'Riverdale']
    val_days = val_days*math.ceil(n/len(val_days))
    df = pd.DataFrame({'Days':val_days[:n]}, dtype='category')
    val_hello =val_str *math.ceil(n/len(val_hello))
    df['HELLO'] = pd.Seriese(val_hello[:n], dtype='category')
    val_locations = val_locations *math.ceil(n/len(val_locations))
    df['Locations'] = pd.Series({'Days'}:val_locations[:n], dtype='category')
    return df



def strings_colums_NoCat(n):
    '''
    INPUTS:
    =======
       n = Int
        n is the number of rows created

    RETURNS:
    ========
        df = dataframe
         panda dataframe with n rows
    '''
    # Define create a string of repeatable strings
    ## USING categories to spead up creation
    val_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    val_hello = [ 'Hello', 'World']
    val_locations = ['Dayton', 'Beavercreek', 'Oakwood', 'Fairfield', 'Huber', 'Riverdale']
    val_days = val_days*math.ceil(n/len(val_days))
    df = pd.DataFrame({'Days':val_days[:n]})
    val_hello =val_str *math.ceil(n/len(val_hello))
    df['HELLO'] = pd.Seriese(val_hello[:n] )
    val_locations = val_locations *math.ceil(n/len(val_locations))
    df['Locations'] = pd.Series({'Days'}:val_locations[:n])
    return df


def int_columns(n, r):
    '''
    INPUTS:
    =======
        n = int  (number of rows)
        r = int  (range of random numbers)
    RETURNS:
    ========
       df = dataframe (pandas dataframe with n rows)
    '''
    int_list = [random.randint(1,r) for ii in range(n)]
    df = pd.DataFrame(int_list, columns=['INT'])
    return df



def float_columns(n,r):
    '''
    INPUTS:
    =======
        n = int  (number of rows)
        r = int  (range of random numbers)
    RETURNS:
    ========
       df = dataframe (pandas dataframe with n rows)
    '''
    float_list = [random.uniform(1,101) for ii in range(n)]
    df = pd.DataFrame(int_list, columns=['FLOAT'])
    return df


def randrom_str(n,r):
    '''
    INPUTS:
    =======
        n = int  (number of rows)
        r = int  (range of random numbers)
    RETURNS:
    ========
       df = dataframe (pandas dataframe with n rows)
    '''
    list_str =[''.join(random.choice(chars) for _ in range(r)) for _ in range(n)]
    df = pd.DataFrame({"Random_String":list_str})
    return df

def main(n, r):


if __name__== "__main__":
