from collections import defaultdict
my_defaultdict =defaultdict(list)
print(my_defaultdict["missing"]) #affcihe []

def default_message():
    return "key is not there"
defaultdcit_obj= defaultdict(default_message)
defaultdcit_obj["key1"]="value1"
defaultdcit_obj["key2"]="value2"
print(defaultdcit_obj["key1"]) #affiche: value1
print(defaultdcit_obj["key2"]) #affiche: value2
print(defaultdcit_obj["key3"]) #affiche: key is not there"""

defaultdcit_obj= defaultdict(lambda: "key is missing") #déclaration d’une fonction lambda pour afficher un message
defaultdcit_obj["key1"]="value1"
defaultdcit_obj["key2"]="value2"
print(defaultdcit_obj["key1"]) #affiche: value1
print(defaultdcit_obj["key2"]) #affiche: value2
print(defaultdcit_obj["key3"]) #appel de la fonction lambda, affiche: key is missing
