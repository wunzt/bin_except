# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/06/2022
# Description: Binary search for a_list that returns exception TargetNotFound if target is not in a_list.

class TargetNotFound(Exception):
  """Raised when target is not in list."""
  pass

def binary_search(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """
  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if a_list[middle] == target:
      return middle
    if a_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
  else:
    raise TargetNotFound