# c = cyphered message
# pax = public address
# pub address decrypts message
# public key is (e, n)
# cyphered bits (m^d mod n)
#(c, pax) = ((m^d mod n), (e, n))
# message = "I want to transfer this much Bitcoin to this public key"
# m = (amountBTC, pay)
# users = 10
# validator = 1
# p = 2 dig
# q = 2 dig
# d = 3 dig


# WRITING OUT MESSAGE
# look at two numbers at a time

### functions
#addTransaction
#validateTransaction

### variables
# c = cyphered message
# pax = public address
# 
#


import json
# opens JSON file
with open('/users.json', 'r') as userFile:
    users = json.load(userFile)


#updates JSON file with data when called
def updateJSON(ind):

    with open('/users.json', 'w') as updateFile:
        json.dump(userFile, updateFile, indent = ind)