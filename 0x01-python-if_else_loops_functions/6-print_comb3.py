#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i < j:
            print(f"{i}{j}", end=", ")
print()
