'''
Checks whether a sentence/word is a palindrome
'''

def p_check.py(sentence):
  '''
  >>> p_check('Hello')
  False
  >>> p_check('Wow')
  True
  >>> p_check('This is fun')
  False
  >>> p_check('This is si siht')
  True
  '''
  if word.lower().split() == word[::-1].lower.split():
    return True
  return False

if name == '__main__':
  from doctest import testmod
  testmod()
