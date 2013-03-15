#!/usr/bin/env python
import sys
from sys import argv
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    l_text = corpus.split()
    chains = {}
    value =[]
    index = 0
    for index in range(0, len(l_text)-2):
        tuple1  = (l_text[index], l_text[index + 1])
        if tuple1 not in chains:
            value = [l_text[index + 2]]
            chains[tuple1] = value
            index += 1
        else:
            chains[tuple1].append(l_text[index + 2]) 
            index += 1
    return chains 

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    text = ""
    l_pairs = chains.keys()
    r_int = random.randint(0, len(l_pairs))
    next_tuple = l_pairs[r_int]
    print next_tuple
    value = chains[next_tuple]
    for items in value:
        v_int = random.randint(0, len(value))
        word = value[v_int]
    print word


    return "Here's some random text."

def main():
    #args = sys.argv

    # Change this to read input_text from a file
    script, filename = argv

    in_file = open(filename)
    input_text = in_file.read()
    a = make_chains(input_text)
    print a

    b = make_text(a)
    print b

    in_file.close()

if __name__ == "__main__":
    main()

'''
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text
'''

