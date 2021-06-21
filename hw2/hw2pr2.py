# CS5 Gold/Black: Homework 2 Problem 2
# Filename: hw2pr2.py
# Name: Paul Burke
# Problem description: Recursion-free functions with PythonBat


# WARM-UP 1

print("I did all but 47 of the 51 functions in one line :)")
print("...sorry if it's hard to parse for some of them but I had fun")
print("My favorites are round_10() (part of round_sum()) and lucky_sum()!")


def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

def sum_double(a, b):
    return a + b if a != b else 2*(a+b)

def diff21(n):
    return 21 - n if n <= 21 else 2*abs(21-n)

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
    if not negative and bool(a < 0) != bool(b < 0):
        return True
    elif negative and a < 0 and b < 0:
        return True
    else:
        return False

def not_string(str):
    return "not " + str if not str.startswith("not") else str

def missing_char(str, n):
    return str[0:n] + str[n+1:]

def front_back(str):
    return str[-1] + str[1:-1] + str[0] if len(str) > 1 else str

def front3(str):
    return 3*str[0:3] if len(str) >= 3 else 3*str


# STRING 1


def hello_name(name):
    return "Hello " + name + "!"

def make_abba(a, b):
    return a + b + b + a

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
    return out[:2] + word + out[2:]

def extra_end(str):
    return 3*str[-2:]

def first_two(str):
    return str[0:2] if len(str) >= 2 else str

def first_half(str):
    return str[0:len(str)/2]

def without_end(str):
    return str[1:-1]

def combo_string(a, b):
    return a+b+a if len(a) < len(b) else b+a+b

def non_start(a, b):
    return a[1:] + b[1:]

def left2(str):
    return str[2:] + str[0:2]


# LIST 1


def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
    # what is the point of this one?
    return [3,1,4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    return sum(nums)

def rotate_left3(nums):
    return nums[1:] + [nums[0]]

def reverse3(nums):
    return nums[::-1]

def max_end3(nums):
    return [max(nums[0], nums[-1]) for x in nums]

def sum2(nums):
    return nums[0] + nums[1] if len(nums) >= 2 else sum(nums)

def middle_way(a, b):
    return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return 2 in nums or 3 in nums


# LOGIC 1


def cigar_party(cigars, is_weekend):
    return (40 <= cigars <= 60 and not is_weekend) or (40 <= cigars and is_weekend)

def date_fashion(you, date):
    return 0 if you <= 2 or date <= 2 else 2 if you >= 8 or date >= 8 else 1

def squirrel_play(temp, is_summer):
    return (not is_summer and 60 <= temp <= 90) or (is_summer and 60 <= temp <= 100)

def caught_speeding(speed, is_birthday):
    if is_birthday:
        return 0 if speed <= 65 else 1 if speed <= 85 else 2
    else:
        return 0 if speed <= 60 else 1 if speed <= 80 else 2

def sorta_sum(a, b):
    return a+b if not 10 <= a+b <= 19 else 20

def alarm_clock(day, vacation):
    if vacation:
        return "10:00" if day in list(range(6))[1:] else "off"
    else:
        return "7:00" if day in  list(range(6))[1:] else "10:00"

def love6(a, b):
    return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

def in1to10(n, outside_mode):
    return (not outside_mode and 1 <= n <= 10) or (outside_mode and not 1 < n < 10)

def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8


# LOGIC 2


def make_bricks(small, big, goal):
    return (goal - small) - 5*big <= 0 and goal % 5 <= small

def lone_sum(a, b, c):
    if a == b and b == c: return 0
    if b == c: return a
    if a == c: return b
    if a == b: return c
    return a + b + c

def lucky_sum(a, b, c):
    return sum([a,b,c][:[a,b,c].index(13)]) if 13 in [a,b,c] else a+b+c

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    return n if 15 <= n <= 16 or n < 13 or n > 19 else 0

def round_sum(a, b, c):
    return int(round10(a) + round10(b) + round10(c))

def round10(num):
    return round(float(str(num)[:-1] + "." + str(num)[-1]))*10

def close_far(a, b, c):
    return (b-a <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2) or (c-a <= 1 and abs(b-a) >= 2 and abs(b-c) >= 2)

def make_chocolate(small, big, goal):
    return max(goal % 5, goal - 5*big) if (goal - small) - 5*big <= 0 and goal % 5 <= small else -1
