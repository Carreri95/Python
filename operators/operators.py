# -*- coding: utf-8 -*-


def add(a, b):
  """It add two numbers
     parameter a: First value
     type a: int, float
     parameter b: Second value
     type b: int, float

     return: int, float
  """
  if type(a) == str or type(b) == str:
    raise TypeError()
  return a + b