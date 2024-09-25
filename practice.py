names  = ['Danny', 'Hannah', 'Eli']
print("Original List:", names)

del names[0] # names.remove() or .pop would also work

print("Altered List:", names)
print(names)

names.append('Ben')
print(names)

for name in names:
    print(f"{name} is at my table.")
