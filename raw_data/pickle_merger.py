import os
import pickle
import sys
import locale

# Set the system's default encoding to 'utf-8' to handle non-ASCII characters
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

folder = 'raw_data/'
db = {}

for filename in os.listdir(folder):
    if filename.endswith('.pkl'):
        myfile = open(os.path.join(folder, filename), "rb")
        db[os.path.splitext(filename)[0]] = pickle.load(myfile)
        myfile.close()
        print(filename)

with open("ESPORTS.pkl", "wb") as myfile:
    pickle.dump(db, myfile)

# Redirect the output to a file
with open("output.txt", "w", encoding="utf-8") as output_file:
    sys.stdout = output_file
    print(db)
