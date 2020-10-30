import json  
from collections import defaultdict


nodes = []
links = []
with open('names2') as readFile:
    
    data = readFile.readlines()
    i = 1
    for line in data:
        line = line.rstrip("\n")
        index = line.index(":")
        name = line[:index]
        shows = line[index+1:]
        showList = shows.split(",")
        nodes.append({"id": i, "name":name})
        for line2 in data:    
            line2 = line2.rstrip("\n")        
            index = line2.index(":")
            name2 = line2[:index]
            shows2 = line2[index+1:]
            show2List = shows2.split(",")
            if(name != name2):
                for show in showList:
                  if show in show2List:
                      links.append({"source": name,"target":name2})
                      break
        i = i + 1
with open('person.json', 'w') as f:  # writing JSON object
    json_dict = {"nodes":nodes,"links":links}
    json.dump(json_dict, f, indent=4, separators=(", ", " : "))

            
