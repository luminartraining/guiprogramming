from re import *
#abababababbbbbab

matcher=finditer("ab","abababababbbbbab")
                        # 0123456789
cnt=0
for match in matcher:
    print(match.start()) #postion
    print(match.group())
    cnt+=1
print("pattern occured in",cnt,"number of time")

#