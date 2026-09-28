print("=== ASSIGNMENT 1: Operations on List, Tuple, Dictionary ===\n")

# ----- LIST OPERATIONS -----
print("--- LIST OPERATIONS ---")
nums = [1, 2, 3, 4, 5]
print("1. Original:", nums)

nums.append(6)
nums.insert(0, 0)
print("2. Added items:", nums)

nums.remove(3)
nums.pop()
print("3. Removed items:", nums)
print("4. Slicing [1:4]:", nums[1:4])

# ----- TUPLE OPERATIONS -----
print("\n--- TUPLE OPERATIONS ---")
tpl = (10, 20, 30, 20, 40)
print("1. Original:", tpl)
print("2. Count of 20:", tpl.count(20))
print("3. Index of 30:", tpl.index(30))
print("4. Slice & Length:", tpl[1:4], "Len:", len(tpl))

# Modifying immutable tuple using list conversion
temp = list(tpl)
temp.append(100)
tpl = tuple(temp)
print("5. Modified Tuple:", tpl)

# ----- DICTIONARY OPERATIONS -----
print("\n--- DICTIONARY OPERATIONS ---")
user = {'name': 'Aryan', 'roll': 101, 'branch': 'CSE'}
print("1. Original:", user)

user['age'] = 19
user.update({'city': 'Pune'})
print("2. Added items:", user)
print("3. Keys:", list(user.keys()), "Values:", list(user.values()))

user.pop('roll')
del user['branch']
print("4. Removed items:", user)
