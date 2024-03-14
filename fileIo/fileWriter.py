
# Python code to
# demonstrate readlines()
 
L = ["dad\n", "is\n", "cool\n"]
 
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()