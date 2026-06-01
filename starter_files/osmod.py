import os as s

print(s.getcwd())
s.chdir("/Users")
print(s.getcwd())


# if(not s.path.exists("data")):
#     s.mkdir("data")

# for i in range(0,50):
#     # s.mkdir(f"data/Day{i+1}")
#     # s.rename(f"data/Day{i+1}" , f"data/Renamed{i+1}")
#     folders = s.listdir("data")
# print(folders)

# for folder in folders:
#     print(folder)
#     print(s.listdir(f"data/{folder}"))


# cmd = 'time'
# print(s.system(cmd))


# with open("new.md", "w") as f:
#     f.write("Again new file !")