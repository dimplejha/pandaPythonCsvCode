myfile = open('c.txt', "w")

# get some info to terminal
print('name:', myfile.name)
print('is openning', myfile.mode)
print('closed', myfile.close)

# write to file
myfile.write("hiiiizxcvbn")
myfile.close()


