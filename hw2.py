Books = ["harry_potter", "lord_of_rings", "Harry Potter and the Chamber of Secrets"]
occ = Books.index("harry_potter")
print("occurance of harry_potter is in", occ)
Books.remove("harry_potter")
print(Books)
user = input(str("Enter a book name:"))
if user in Books:
    print("Book is present")
Books.append("the_hobbit")
print(Books)
Books.insert(1, "games_of_thrones")
print(Books)
count = 0
for i in range(len(Books)):
    if Books[i] == "lord_of_rings":
        count += 1
print("The total num of lords_of_rings is", count)
Books.pop(1)
print(Books)
total = len(Books)
print("total num of books in the list", total)
print(Books[0:3])
Books_2 = ["math", "science", "history"]
add = Books + Books_2
print("All books=", add)
add.sort(key=len, reverse=True)
print(add)
