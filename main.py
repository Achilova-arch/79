for i in range (1,21):
    if i == 15 :
        break
    else:
        print(i)

son=1,2,3,4,5,6,7,8,9
for i in  [1,5,-6,8,-4,3,-9]:
    if i == son  :
     continue
    else:
        print(i)

for i in  [1,5,-6,8,-4,3,-9]:
    if i == -6 :
     break
    else:
        print(i)



soz=input("Soz kiriting, men bu sozni undosh harflarini olb tashliman:")
text=soz
for harf in text:
    if harf  in "bdfghjklmnpqrstvxyzshchn":
         continue
    else:
         print(harf)
    