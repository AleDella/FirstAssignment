# This file contains the functions used for the assignment plus a test function to test
# all the functionalities of the program.
import spacy

# This function is a simple tree visit in order to get the pathfrom the root
# to a node (token).
# Input:
#       root --> root of the dependency tree (Token object)
#       path --> path leading to the target token (initially empty)
#       token --> target token (Token object)
# Return: 
#       a boolean value used for recursion. The desired dependency path
#       is stored in 'path'
def extract_path(root, path, token): 
    if (not root):
        return False
    path.append(root)
    if (root == token):     
        return True
    for child in root.children: 
      if (extract_path(child, path, token)):
          return True     
    path.pop(-1) 
    return False

# Function that extracts every dep path from root to another token.
# Input: a string
# Return: the List of paths
def dep_paths(sentence):
  nlp = spacy.load("en")
  doc = nlp(sentence)
  processed = parser(doc)
  paths = []
  for token in processed:
    path = []
    extract_path(list(processed.sents)[0].root, path, token)
    paths.append(path)
  return paths

# Function that takes in input a Token and returns
# its subtree as a List (is only a support function)
def extract_subtree(token):
  return list(token.subtree)

# Function that extracts the dep subtrees of all the tokens in a sentence
# Input: a string
# Return: a list of lists
def ex_subtrees(sentence):
  nlp = spacy.load("en")
  doc = nlp(sentence)
  processed = parser(doc)
  subtrees = []
  for token in processed:
    subtrees.append(extract_subtree(token))
  return subtrees

# Defines the equality between a list of words and a list of tokens
def equality(tk1, wd2):
  if(len(tk1)!=len(wd2)):
    return False
  else:
    for i in range(len(tk1)-1):
      if(tk1[i].text != wd2[i]):
        return False
    return True

# Checks if a given list of Words (aka strings) form a subtree of a given sentence
# Input:
#       tokens --> List of strings(words)
#       sentence --> string
# Return: boolean value
def subtree_checking(tokens, sentence):
  nlp = spacy.load("en")
  doc = nlp(sentence)
  processed = parser(doc)
  subtrees = ex_subtrees(sentence)
  for st in subtrees:
    if(equality(st, tokens)):
      return True
  return False

# Given a Span (list of words as String), return the head of the span
# Input: string
# Return: a Token that is the head of the Span
def identify_head(span):
  nlp = spacy.load("en")
  doc = nlp(span)
  processed = nlp.parser(doc)
  head = list(processed.sents)[0].root
  return head

# Function that extracts nsubj, dobj, iobj of a sentence as span(if present).
# Input: a string
# Returns a dictionary of lists of spans. 
def extract_so(sentence):
  nlp = spacy.load("en")
  doc = nlp(sentence)
  processed = nlp.parser(doc)
  d = {
      'nsubj': [],
      'dobj' : [],
      'iobj' : []
  }
  for token in processed:
    if(token.dep_ == 'nsubj'):
      d["nsubj"].append(processed[token.i:token.i+1])
    elif(token.dep_ == 'dobj'):
      d["dobj"].append(processed[token.i:token.i+1])
    elif(token.dep_ == 'iobj'):
      d["iobj"].append(processed[token.i:token.i+1])
  return d

# Function that tries all the other functionalities and prints the relevant results
def assignment_test():
  sentence = "I saw a man with a Telescope"
  print("------------------------------------------")
  print("1st")
  print("Input sentence: ", sentence)
  paths = dep_paths(sentence)
  print("Paths found:")
  for p in paths:
    print(p)
  print("------------------------------------------")
  print("2nd")
  print("Input sentence: ", sentence)
  subtree = ex_subtrees(sentence)
  print("Subtree found:")
  for st in subtree:
    for t in st:
      print(t)
    print("===========")
  print("------------------------------------------")
  print("3rd")
  inputs = ["with", "a", "Telescope"]
  print("Input tokens: ", inputs)
  print("Result:")
  print(subtree_checking(inputs, sentence))
  print("------------------------------------------")
  print("4th")
  span = "a man with a Telescope"
  print("Input span: ", span)
  head = identify_head(span)
  print("The head is: ", head)
  print("------------------------------------------")
  print("5th")
  print("Input sentence: ", sentence)
  so = extract_so(sentence)
  print("Elements found:")
  print(so)
  print("------------------------------------------")

if __name__==__main__:
    assignment_test()
