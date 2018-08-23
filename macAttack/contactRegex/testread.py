data = open("/Users/dangoodman/Library/Application Support/AddressBook/Metadata/7C62CF3B-B9EA-43DC-AD56-25E337D19171:ABPerson.abcdp", "r")

data = data.read()

if "BestBuy" in data:
    print "Found it"
else:
    print "No find"

print data
