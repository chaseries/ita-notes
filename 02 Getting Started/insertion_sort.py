import doctest

def insertion_sort(a):
  '''
  >>> insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  '''
  for j in range(1, len(a)):
    i = j - 1
    key = a[j]
    while i >= 0 and a[i] > key:
      a[i + 1] = a[i]
      i = i - 1
    a[i + 1] = key
  return a


if __name__ == '__main__':
  doctest.testmod()
