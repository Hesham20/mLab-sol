#!/usr/bin/python3

import sys
import json # to load the json file

def helper( input, ans, path ):

    for key, val in input.items():
        # if there exits a parent of the current dict, 
        # make sure to add it to the path
        tempKey = path 
        if path != '' :
            tempKey += '.'
        tempKey += key

        # test if the current element is not a dictionary
        if not isinstance( val, dict):
            ans[tempKey] = val       # add that element  
        else:
            helper(val, ans, tempKey)   # call it again with the new dict


def solve( input):
    ans = {}
    helper( input, ans, '' )
    return ans

if __name__ == '__main__': 
    file = open( sys.argv[1], "r" )
    lines = json.load(file)
    print( solve( lines) )
