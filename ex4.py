import random
import string
txt=[]
rndm = "".join(random.choice(string.ascii_letters) for _ in range(3))
rndm2 = "".join(random.choice(string.ascii_letters) for _ in range(3))
txt.append(rndm)
txt.append(rndm2)
print(txt)


# st = input("Enter word to translate : ")
# words = st.split(" ")

# coding = int(input("Enter:\n1- to code\n0-to decode\n"))

# if(coding):
#     nwords=[]
#     for word in words:
#         if(len(word)>=3):
#             r1="frs"
#             r2="hsf"
#             nword= r1+ word[1:] + word[0] + r2
#             nwords.append(nword)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
# else:
#     nwords=[]
#     for word in words:
#         if(len(word)>=3):
#             nword = word[3:-3]
#             nword = nword[-1] + nword[:-1]
#             nwords.append(nword)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords)) 
