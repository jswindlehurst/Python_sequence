add = 0
last = 0

for count in range(102):
    if count == 1:
        print(add, "count:", count)
        add = 1
    elif count == 2:
        print(add, "count:", count)
    elif count > 2:
        add = add + last
        print(add, "count:", count)
        last = add - last
print("The 100th number in the sequence is: ",add)
print("The count is: ", count)