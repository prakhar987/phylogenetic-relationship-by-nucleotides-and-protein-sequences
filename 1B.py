speciesMapping = []
# speciesMapping.append('Cow')
# speciesMapping.append('Sheep')
# speciesMapping.append('Marine Worm')
# speciesMapping.append('Rat')
# speciesMapping.append('Frog')
# speciesMapping.append('Wild Pig')
import sys
keys={ 0:'Cow', 1:'Sheep', 2:'Worm', 3:'Rat', 4:'Frog', 5:'Pig' }
f = open('Ndistance.txt','rU')
line = f.readline() # skip first line
data = [[0 for x in range(6)] for x in range(6)] 
i = j = 0
for line in f:
	lst = line.split(',')
	speciesMapping.append(lst[0])
	lst=lst[1:]
	j = 0
	for inputs in lst:
		data[i][j] = float(inputs)
		j += 1
	i += 1
cluster = []
sizeCluster = []
for i in range(6):
	cluster.append(speciesMapping[i])
	sizeCluster.append(1)
pre = None
prev = None
prevsize = None
num = len(cluster)
while num > 2:
	minValue = data[0][1]
	clusA = 0
	clusB = 1
	for i in range(len(cluster)):
		for j in range(len(cluster)):
			if minValue > data[i][j] and data[i][j] != 0.0:
				clusA = i
				clusB = j
				minValue = data[i][j]
	valueClusterA = cluster[clusA]
	valueClusterB = cluster[clusB]
	print 'The Minimum Value   :  ' + str(minValue)
	print 'FIRST CLUSTER       :  ' + str(valueClusterA)
	print 'SECOND CLUSTER      :  ' + str(valueClusterB)
	# print 'The Cluster A:' + str(clusA)
	# print 'The Cluster B:' + str(clusB)
	pre = [[0 for x in range(len(cluster))] for x in range(len(cluster))]
	for i in range(len(cluster)):
		for j in range(len(cluster)):
			pre[i][j] = data[i][j]

	prev = list(cluster) 
	if valueClusterA in cluster:
		cluster.remove(valueClusterA)
	else:
		print 'Not inside cluster'
	if valueClusterB in cluster:
		cluster.remove(valueClusterB)
	else:
		print 'Not inside cluster'
	tempTuple = (valueClusterA, valueClusterB)
	cluster.insert(0, tempTuple)
	num = len(cluster)

	prevsize = list(sizeCluster)
	if clusB > clusA:
		s2 = sizeCluster.pop(clusB)
		s1 = sizeCluster.pop(clusA)
	else:
		s1 = sizeCluster.pop(clusA)
		s2 = sizeCluster.pop(clusB)
	sum12 = s1 + s2
	sizeCluster.insert(0, sum12)

	data = [[0 for x in range(len(cluster))] for x in range(len(cluster))]

	for i in range(len(cluster)):
		for j in range(len(cluster)):
			if i == j:
				data[i][j] = 0
			elif i == 0 or j == 0:
				idx1 = prev.index(valueClusterA)
				idx2 = prev.index(valueClusterB)
				if i == 0:
					idx3 = prev.index(cluster[j])
				else:
					idx3 = prev.index(cluster[i])
				data[i][j] = (pre[idx1][idx3] + pre[idx2][idx3])/2.0
			else:
				idx1 = prev.index(cluster[i])
				idx2 = prev.index(cluster[j])
				data[i][j] = pre[idx1][idx2]
	#print
	print '~~~~~THE DATA MATRIX IS:~~~~~'
	for i in range(len(cluster)):
		for j in range(len(cluster)):
			print str(data[i][j]) + ' , ',
		print

	print '~~~~~THE CLUSTER IS:~~~~~~'
	for temp in cluster:
		# print keys[temp]
		print temp
	print ' '