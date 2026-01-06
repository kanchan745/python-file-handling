#File input output : python can be used to perforn operations on a file(read and write data)
#Types of all files
#Text files : .txt,.doc,.log etc : stores data in character form 
#Binary Files : .mp4,.mov,.png ,.jpeg etc...: not text files
#all this data stores in system in the form of bits : 0/1
#files stored data in ssd or HDD

#Open 
'''we have to open a file before reading or writing'''
#syntax
'''f = open("File_name , "mode")
data = f.read()
f.close'''

#mode : read mode-r, write mode- w or file_name = sample.txt, demo.docx
#bydefault mode : read

'''file = open("File_i/demo.txt","r")
data = file.read()
print(data)
print(type(data))
file.close()'''

#if we want to just read some characters

'''f = open("File_i/demo.txt", "r")
data = f.read(19)
print(data)
f.close()'''

#Reading a file
#data = f.read() # reads entire file
#data = f.readline() # reads one line at a time

'''f = open("File_i/demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()'''

'''f = open('File_i/demo.txt', "r")
data = f.read()
print(data)
#if we read data 1 time then ill give blank or empty space bcoz : pointer or we can say cursor  will point at last ..

line1 = f.readline() 
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()'''

#writing a file ...

#syntax : f = open("file_name ","w")
#f.write ("This is a new line") #overwrite the entire file

#f = open ("File_name","a")
#f.write("This is a new line") #adds to the file

  
'''f = open("File_i/demoo.txt","w")
f.write("i want to learn Numpy and Pandas")
f.write("\n After that i ll move forward to machine learning ")  
f.close()'''

# f = open("File_i/demoo.txt","a")
# f.write("\n I'm enjoying learning python")
# f.close()

#if txt.don't exist and we want to make a txt so we open it in 'a' or 'w' mode it'll automatically created..

# f = open("created_new.textfile",'a')
# f.close()

#if we want to write something from starting r+ (read+overwrite)(no truncate)
'''f = open ("created_new.textfile",'r+')
f.write("hello")#point in  starting
print(f.read())
f.close'''

#w+ file will open in truncate mode  means empty(truncate)
# f = open("created_new.textfile",'w+')
# print(f.read())
#f.write("Hello")
# f.close()

#a+ mode point at the end of the txt file: not over write it ll append(no truncate)
'''f = open("created_new.textfile", 'a+')
print(f.read())
f.write("it ll point in the last...")
f.close()'''

 
