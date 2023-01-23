def count_users(group):
  print("function call")
  count = 0
  for member in get_members(group):
    print("for loop start")
    count += 1
    print(count)
    if is_group(member):
      print("if start\nfunction is_group() was called")
      count += count_users(member)
    else:
      print("function is_group() was not called\nend for loop")
  print("function exit")
  return count

print("\n",count_users("sales"), "\nend\n") # Should be 3
print("\n",count_users("engineering"), "\nend\n") # Should be 8
print("\n",count_users("everyone"), "\nend") # Should be 18_users(group):


###################SOLUTION BELOW######################################
########################################################################
def count_users(group):
  count = 0
  for member in get_members(group):
    count += count_users(member)
    if is_group(member) == False:
      count += 1
      
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
########################################################################
