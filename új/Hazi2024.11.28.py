t2=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
utolso_index=-1
print(len(t2))
for i in range(len(t2)):
    if -10<=t2[i]<=10:
        utolso_index=i

if utolso_index!=-1:
    print("Az utolsó [-10, 10] intervallumba eső szám indexe: ",utolso_index)