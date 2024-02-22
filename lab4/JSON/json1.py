import json
file = open('sample-data.json' , 'r')
data = json.loads(file.read())
print("Interface Status\n================================================================================\nDN                                                 Description           Speed    MTU\n-------------------------------------------------- --------------------  ------  ------")
for i in data["imdata"]:
    string = ""
    string+= (str(i["l1PhysIf"]["attributes"]["dn"]) + " "*(51-len(str(i["l1PhysIf"]["attributes"]["dn"]))) + str(i["l1PhysIf"]["attributes"]["descr"]) + " "*(21-len(str(i["l1PhysIf"]["attributes"]["descr"]))) + str(i["l1PhysIf"]["attributes"]["speed"]) + " "*(10-len(str(i["l1PhysIf"]["attributes"]["speed"]))) + str(i["l1PhysIf"]["attributes"]["mtu"]))
    print(string)
