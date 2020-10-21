y=input()
U=0
A= 0
P=0

for i in y:

    if(i=='U'):
         U+=1
    elif(i=='A'):
        A+=1
    elif(i=='P'):
        P+=1
print("U =",U)
print("A =",A)
print("P =",P)
if(U >=1 and A>=1 and P>=1):
    print("Yeap UAP is and organizing way")