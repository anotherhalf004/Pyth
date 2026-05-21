# f = open("new.txt","r")
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break

# f = open("new.txt", "w")
# # lines = [ "\nline 1\n", "line 2\n", "line 3\n"] or we can 
# lines = ['line1','line2','line3']
# for line in lines:
#     f.write(line + "\n")
# # f.writelines(lines) # does not append
# f.close

# with open('myfile.txt','r') as f:
#     print(type(f))
#     f.seek(4)
#     print(f.tell())
#     t= f.read(5)
#     print(t)

with open('sample.txt','w') as f:
    f.write("Hello fellas")
    f.truncate(5)
with open('sample.txt','r') as f:
    print(f.read())





