with open("my_file.txt", "r") as my_file:
  for line in my_file:
      str = line.split()
      print(str)

str = "This \nis \na \ntest"
print(str)
print("\nAfter Split\n")
print(str.split())
