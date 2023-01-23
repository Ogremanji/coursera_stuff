def sum_divisors(n):
  print('\nfunction call')
  rem = 1
  num = n
  sum = 0
  # Return the sum of all divisors of n, not including n
  if n == 0:
    return sum
  print('after return')

  while n > 0:
    print('1st line of while loop')
  # all of the print statements in this script helped a lot;
  # great debugging strategy
    if n == 1:
      sum = sum + n
      print('end if 1')
      return sum
    elif rem == 0:
      sum = sum + n
      rem = num % (n - 1)
      print('end if 2')
    elif rem > 0:
      rem = num % (n - 1)
      print('end elif')
    n = n - 1

    print('num', num)
    print('n update', n)
    print('remainder', rem)
    print('sum', sum, '\n')

  print('exit while loop')
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
