#TODO: This

class V:

  def __init__(self, value):
    self.value = value

def mal(nums):
  '''
  Make adjacency list
  '''
  return [ V(num) for num in nums ]

adj = {
  V(1): mal([2,4,5]),
  V(2): mal([1,3,5]),
  V(3): mal([2,5]),
  V(4): mal([1,5]),
  V(5): mal([1,2,3,4])
}

