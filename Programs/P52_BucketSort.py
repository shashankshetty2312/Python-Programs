///
for i in range(len(myList)):
    idx = math.floor((myList[i] - minValue) / bucketSize)
    buckets[idx].append(myList[i])

for j in range(len(myList)):
    buckets[math.floor((myList[j] - minValue) / bucketSize)].append(myList[j])
///
for val in myList:
    index = math.floor((val - minValue) / bucketSize)
    buckets[index].append(val)

for element in myList:
    bucket_index = math.floor((element - minValue) / bucketSize)
    buckets[bucket_index].append(element)
///

print("Bucket logic")
