# Python Learning

## Python Installation and Setup for VSCode

1. Open [Python official website](https://www.python.org/).
2. Go to Download section and select installer depended on your OS
   ![image](images/download-python.jpg)

3. During Installation, you can check Add path checkbox and click install now.
4. check whether python has installed or not

```
python --version
```

5. Install Python extension in VSCode
6. Start coding Python!

## Basics

- has no command for declaring variable data type
- use indent instead of curly bracket
- single comment (#) and multiple comment (""" """)
- string can be declared either by using single or double quotes
- case-sensitive
- no semicolon

## Multiple items Data Type

```py
# List - ordered, changeable, allow duplicate members, allow multiple data types
mylist = ["mouse", "keyboard", "screen", 24, False]

# Tuple - ordered, unchangeable, allow duplicate members, allow multiple data types
myTuple = ("mouse", "keyboard", "screen", 24, False)

# Set - unordered, unchangeable, mo duplicate members, allow multiple data types
mySet = {"mouse", "keyboard", "screen", 24, False}

# Dictionary - ordered, changeable, mo duplicate members
myDict = {
   "name": "Billy",
   "year": 2000
}
```

# Condition

```py
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# short hand if else
print("a") if a > b else print("b")
```
