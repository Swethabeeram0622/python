# Sorting List of tuples
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

# Sort by age in descending order using lambda
sorted_people = sorted(people, key=lambda x: x[1], reverse=True)

print(sorted_people)
