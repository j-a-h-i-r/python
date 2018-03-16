# Pattern 1
"""
*****
*****
*****
*****
*****
"""

character = "*"
num_line = 5
num_characters = 5
for i in range(num_line):
    print(character * num_characters)

# Pattern 2
"""
*
**
***
****
*****
"""

character = "*"
num_line = 5
num_characters = 1
for i in range(num_line):
    print(character * num_characters)
    num_characters += 1
    
# Pattern 3
"""
*****
****
***
**
*
"""

character = "*"
num_line = 5
num_characters = 5
for i in range(num_line):
    print(character * num_characters)
    num_characters -= 1
    
    
# Pattern 4
"""
*********
*******
*****
***
*
"""

character = "*"
num_line = 5
num_characters = 9
for i in range(num_line):
    print(character * num_characters)
    num_characters -= 2


# Pattern 4
"""
*********
*******
*****
***
*
"""

character = "*"
num_line = 5
num_characters = 9
for i in range(num_line):
    print(character * num_characters)
    num_characters -= 2
    
    
# Pattern 5
"""
*
**
***
**
*
"""

character = "*"
num_line = 5
num_characters = 1
mid = (num_line + 1) // 2
for i in range(1, line+1):
	print("*" * (mid - abs(i-mid)))
  

# Pattern 6
"""
   *
  ***
 *****
*******
"""

character = "*"
num_line = 5
num_characters = 1
num_space = num_line - 1
for i in range(num_line):
    print(" " * num_space, end = "")
    print(character * num_characters)
    num_characters += 2
    num_space -= 1
    

# Pattern 7
"""
*******
 *****
  ***
   *
"""

character = "*"
num_line = 4
num_characters = (num_line*2) - 1
num_space = 0
for i in range(num_line):
    print(" " * num_space, end = "")
    print(character * num_characters)
    num_characters -= 2
    num_space += 1
    
    
# Pattern 8
"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""

# TODO



# Pattern 7
"""
1
1   1
1   2   1
1   3   3   1
1   4   6   4   1
1   5   10   10   5   1
"""

# TODO



# Pattern 10
"""
1
2 3
4 5 6
7 8 9 10
"""

start_num = 1
num_line = 4
for i in range(1, num_line+1):
  line = [start_num + x for x in range(i)]
  line = map(str, line)
  print(" ".join(line))
  start_num += i
