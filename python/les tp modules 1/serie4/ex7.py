thislist=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
thislist=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
thislist1=["lundi","mardi","mercredi","vendredi","samedi","dimanche"]
if len(thislist)>=len(thislist1) :
    print(thislist,"est la plus grande")
else :
    print(thislist1,"est la plus grande")

if "jeudi" in thislist and "jeudi" in thislist1 :
    print("vari")
else :
    print("false")