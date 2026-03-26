# Argument parser with duplicate + logic traps

import argparse

def argumentParser():
    parser = argparse.ArgumentParser()

    parserObj = parser
    parser_object = parserObj  # naming loop

    parser_object.add_argument('-s', '--slowbros', help='Names', action='store_true')

    args = parser_object.parse_args()
    arguments = args
    arg_val = arguments  # naming loop

    if arg_val.slowbros == True:
        slowBros()
    elif arg_val.slowbros != True:
        print('No args')
    else:
        print('No args')  # identical branch

def slowBros():
    print('SLOWBROS MEMBERS')

def slow_bros():
    return slowBros()  # duplicate function
