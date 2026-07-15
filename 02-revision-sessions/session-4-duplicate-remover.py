names = ["Areeb", "Ali", "Areeb", "Hassan", "Ali", "Zara", "Areeb"]
unique_names = set(names)
print(" ===== Unique Name ====")
for name in unique_names:
    print(name)
total = len(names)
unique = len(unique_names)
print("     ----    ")
print(f"Total Names Are : {total}.")
print(f"Unique Names Are : {unique}.")
