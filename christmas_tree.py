#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# christmas_tree.py
# --
# Prints a colored christmas tree.
# Eetu "Eeko" Korhonen, Christmas 2011
#
# Usage:
# Just execute the script. Eg.
# $ python christmas_tree.py
#      _^_
#      ´ `
#       "
#      /*\
#     //"\\
#    ///*\\\
#   ///*"*\\*
#  /**//*\\\\\
# /**///**\\*\\
#      |||
#
# You can give a desired tree-height as a parameter.
# E.g.
# $ python christmas_tree.py 6
#     _^_
#     ´ `
#      "
#     /"\
#    /**\\
#   /**"\\\
#  //*/"\\*\
# //*/*"*\*\\
#     |||
# 
import sys, random, datetime, getpass

def colored (string, color):
    color_code="\x1B["
    parameter = "3" + str(color) + ";40m"
    return color_code + parameter + string + color_code + "0m"
    
def main():
    # check if we have the tree-size in parameter
    if len(sys.argv) == 1:
        size = random.randint(7,15)
    else:
        size = int(sys.argv[1])
        
    #first of, print out the star
    star = "" + " " * (size - 2) + "_^_\n" + " " * (size - 2) + "´ `"
    print colored(star, 3)
    
    for i in range(size):
        current_line = list((size-1-i)* " " + "/"* i + "\"" + "\\" * i)
        # ornaments
        for j in range((i)*2 +1):
            if random.randint(0,3) == 3:
                current_line[size-i-1 + j] = "*"
        colored_line = ''
        for char in current_line:
            #join each character of a line in appropriate color
            if char == "/" or char == "\\" or char == "\"" or char == " ":
                colored_line = colored_line + colored("".join(char),2)
            else:
                colored_line = colored_line + colored("".join(char),random.randint(1,7))
        print colored_line
        #print colored("".join(current_line), 2)
    
    print colored((size-2)*" " + "|||",1)
    print "      " + "Merry Christmas and a Happy New Year " + str(datetime.date.today().year + 1) + ", " + getpass.getuser() + "!"

main()
