

# Write a program to generate tables
# from 1 to 20 and store it in a folder
# for a 13-year old child.

# Solution:-

# def generate_table(n):
#     table=""
#     for i in range(1,11):
#         table +=f"{n} X {i} = {n*i}\n"
#     with open(f"Chapter7-ps/table/table_{n}", "w") as f:
#         f.write(table)

# for i in range(2,21):
#     generate_table(i)



# Q-2:- 
# Write a program to censor some words 
# in a given text file. 

# Solution:- 

# words=["shailove", "good"]
# with open("Chapter7-ps/h.txt","r") as f:
#     content=f.read()

# for word in words:
#     content=content.replace(word, "#" *len(word))

# with open("Chapter7-ps/h.txt","w") as f:
#     f.write(content)


# Q-3:
# Write a program to mine a log file and 
# find out where it contains "python" .

# Solution:- 

# with open("Chapter7-ps/log.txt", "r") as f:
#     content=f.read()

# if("PytHon".lower() in content):
#     print("Yes python is available ")
# else:
#     print("python is not available")



# Q-4: 
# Check the line no where 
# python is present in last program.

# Solution:- 

# with open("Chapter7-ps/log.txt", "r") as f:
#     lines=f.readlines()
# lineno = 1
# for line in lines:
#     if("Python".lower() in line):
#         print(f"Yes python is available at line no : {lineno}")
#         break
#     lineno+=1
# else:
#     print("python is not available")




# Q-5:-  Write a program to copy the file.

# Solution:-

# with open("Chapter7-ps/log.txt") as f:
#     content = f.read()
# with open("Chapter7-ps/log_copy.txt" , "w") as f:
#     f.write(content)








