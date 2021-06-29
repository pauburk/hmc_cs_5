# CS5 Gold/Black: Homework 9 Problem 3
# Filename: hw9pr3.py
# Name: Paul Burke
# Problem description: PythonBat Loops!

print("This time, I managed to get all but one of the 21 problems in one line :)")
print("Again...sorry if it's hard to parse for some of them but I had fun")
print("My favorites are xyz_there(), last2(), and count_code()!")

# WARM-UP 2

def string_times(str, n):
  return str*n

def front_times(str, n):
  return str[:3]*n if len(str) > 3 else str*n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  return "".join([str[:i] for i in range(len(str)+1)])

def last2(str):
  return sum(1 for i in range(len(str)) if str.startswith(str[-2:], i)) - 1 if len(str) > 0 else 0

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  return 9 in nums[:4]

def array123(nums):
  return "123" in "".join([str(i) for i in nums])

def string_match(a, b):
  return sum([1 for i in range(len(a)-1) if a[i:i+2] == b[i:i+2]])


# STRING 2

def double_char(str):
  return "".join([2*i for i in str])

def count_hi(str):
  return str.count("hi")

def cat_dog(str):
  return str.count("cat") == str.count("dog")

def count_code(str):
  return sum([1 for i in range(len(str)-3) if str[i:i+2] == "co" and str[i+3] == "e"])

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def xyz_there(str):
  return bool([1 for i in list(range(len(str)-2))[1:] if str[i-1] != "." and str[i:i+3] == "xyz"]) if not str.startswith("xyz") else True


# LIST 2

def count_evens(nums):
  return sum([1 for i in nums if i % 2 == 0])

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  return (sum(nums)-max(nums)-min(nums))/(len(nums)-2)

def sum13(nums):
  return sum([nums[i] for i in range(len(nums)) if nums[i] != 13 and nums[max(i-1,0)] != 13])

def sum67(nums):
  res = 0
  ignore = False
  for i in nums:
    if i == 6 and ignore == True:
      continue
    elif i == 6 and ignore == False:
      ignore = True
      continue
    elif i == 7 and ignore == True:
      ignore = False
      continue
    elif ignore == False:
      res += i
  return res

def has22(nums):
  return "22" in "".join([str(i) for i in nums])
