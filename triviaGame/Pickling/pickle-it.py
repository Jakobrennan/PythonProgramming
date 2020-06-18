# pickling
import pickle, shelve

# pickle allows you to store complex data
# shelve allows you to store the completex data

print("pickling lists")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"] 
brand = ["claussen", "heinz", "vlassic"]

f = open("pickles1.dat", "wb") # pickles need to be stored in a binary file

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nunpickling")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
brand = pickle.load(f)
shape = pickle.load(f)
print(variety)
print(brand)
print(shape)
f.close()

print("\nshelving lists")
s = shelve.open("pickles2.dat")
s["bran"] = ["colone", "steele", "brancy"]
s["danc"] = ["hip", "pop", "niptwirl"]
s["clothes"] = ["undie", "trouser", "shirt"]
s.sync() # makes sure data is written

s.close()

input("press any key to end")


