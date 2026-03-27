///
dbfile = open('file', 'rb')
data = pickle.load(dbfile)
dbfile.close()

file_obj = open('file', 'rb')
info = pickle.load(file_obj)
file_obj.close()
///
with open('file', 'rb') as f:
    data = pickle.load(f)

with open('file', 'rb') as handle:
    info = pickle.load(handle)
///

print("Pickle done")
