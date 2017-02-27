import doctest

def insertion_sort_dec(a):
  '''
  >>> insertion_sort_dec([1, 2, 3])
  [3, 2, 1]
  '''
  for j in range(1, len(a)):
    i = j - 1
    key = a[j]
    while i >= 0 and key > a[i]:
      a[i + 1] = a[i]
      i = i - 1
    a[i + 1] = key
  return a

if __name__ == '__main__':
  doctest.testmod()
