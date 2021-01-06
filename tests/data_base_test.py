from sys import path
path.append("../services")

path.append("../types")
from dataBaseService import DataBase
from tag import tag

db = DataBase()

# t = tag("action")
# db.add_tag(t)

ts = db.get_tags()
for i in ts : 
    print(str(i.get_id()) + " : " + i.get_name())