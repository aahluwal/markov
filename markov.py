#!/usr/bin/env pyhon
import sys
from sys import argv
import random

def make_chains(corpus, ngram_size):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    word_list = corpus.split()
    index = 0
    chains = {}
    for word in word_list[0:-(ngram_size)]:
      n_gram = tuple(word_list[index:index+ngram_size])
      word_after_ngram = word_list[index+ngram_size]  
      if n_gram not in chains:
        chains[n_gram] = [word_after_ngram]
      else:
        chains[n_gram].append(word_after_ngram)
      index +=1
    return chains  


def make_text(chains, output_length):
    """Takes a dictionary of markov chains and returns random text
     based off an original text."""
    seed = random.choice(chains.keys()) 
    final_list = list(seed)
    seed_length = len(seed)


    while len(final_list) < output_length:
      new_seed = final_list[-(seed_length):]
      new_tuple_key = tuple(new_seed)
      final_list.append(random.choice(chains[new_tuple_key]))

    final = " ".join(final_list)
    print final     










def main():
    #script, filename = sysrgv

    # Change this to read input_text from a file
    script, filename = argv

    in_file = open(filename)
    input_text = in_file.read()
    chains = make_chains(input_text, 2) 
    make_text(chains, len(input_text))
    in_file.close()

if __name__ == "__main__":
    main()



