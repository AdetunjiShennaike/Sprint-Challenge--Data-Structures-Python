import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# def contains(names, target, low, mid, high):
#       print(names[int(mid)], target, int(low), int(mid), int(high), len(names))
#       if len(names) > 1 and (int(mid) != int(high) or int(mid) != int(low)):
#         if names[int(mid)] == target:
#           return target
#         elif target < names[int(mid)]:
#           return contains(names[:int(mid-1)],target, 0, (mid-1)/2, mid-1)
#         elif target > names[int(mid)]:
#           return contains(names[int(mid+1):],target, 0, (mid-1)/2, mid-1)
        

# duplicates = []
# for name_1 in names_1:
#   duplicates.append(contains(sorted(names_2),name_1, 0, len(names_2)/2, (len(names_2)-1)))

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
