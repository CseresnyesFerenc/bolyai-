print("idk")
print(23*"1"+8*"P"+9*"1"+"\n1"+
      20*"1"+2*"P"+8*"'"+3*"P"+6*"1"+"\n1"+
      7*"1"+7*"P"+4*"1"+2*"P"+12*"'"+3*"P"+4*"1"+"\n1"+
      4*"1"+3*"P"+7*"'"+2*"P"+2*"1"+"P"+14*"'"+2*"P"+4*"1"+"\n1"+
      3*"1"+12*"'"+3*"P"+15*"'"+2*"P"+4*"1"+"\n1"+
      "1"+2*"P"+14*"'"+2*"P"+2*"'"+4*"P"+9*"'"+2*"P"+3*"1"+"\n1"+
      "1"+"P"+10*"'"+3*"P"+2*"P"+2*"P"+2*"'"+5*"P"+8*"'"+2*"P"+3*"1"+"\n1"+
      "1"+"P"+9*"'"+5*"P"+2*"'"+2*"P"+2*"'"+3*"P"+9*"'"+2*"P"+3*"1"+"\n1"+
      "1"+"P"+10*"'"+3*"P"+3*"'"+3*"P"+11*"'"+4*"P"+3*"1"+"\n1"+
      "1"+2*"P"+14*"'"+2*"P"+"1"+3*"P"+8*"'"+3*"P"+2*"1"+2*"P"+"1"+"\n1"+
      2*"1"+2*"P"+12*"'"+4*"P"+4*"1"+8*"P"+4*"1"+2*"P"+"1"+"\n1"+
      3*"1"+2*"P"+10*"'"+3*"P"+"'"+20*"1"+"\n1"+
      3*"1"+13*"P"+23*"1"+"\n1"+
      39*"1")
print("idk")
a=2.7
b=7.9
c=29.7
d=50
e=90
f=130
g=60
perc=round((a/d+b/e+c/f)*60)
ora=round((a/d+b/e+c/f))
h=8
j=60
print("a.) feladat:\n"+
      20*"-"+"\nA","szükséges idő az egyetemig:",round((a/d)+(b/e)+(c/f),2),"óra","\nb.) feladat:"+
      "\n-"+19*"-"+"\nA szükséges idő az egyetemig:",round((a/d+b/e+c/f)*60),"perc","\nc.) feladat:"
      "\n-"+19*"-"+"\nAz indulási idő:",h-1,":",j-perc)




m=float(input("Kérem adja meg a magasságát m-ben:"))
tt=float(input("Kérem adja meg a súlyát kg-ben:"))
print(20*"*"+5*"-"+20*"*")
print("Az ön testtömeg indexe:",round(tt/(m)**2,2),"%")
print("Az ön sullyához ideális testömeg:",round(18.5*(m)**2,2),"KG és",round(24.9*(m)**2,2),"KG között van")