# 6.	 Rename key city to location in the following dictionary
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
temp = sampleDict["city"]
sampleDict.pop("city")
sampleDict["location" ] = temp

print(sampleDict)

