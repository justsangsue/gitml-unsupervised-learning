import csv 

head = "/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/"

def get_pca_data(input_file, output_file):
	with open(input_file, 'r') as fh:
		line = fh.readline()
		cnt = 1
		eigenvalue = []
		proportion = []
		cumulative = []
		while line:
			if cnt == 1:
				cnt += 1
				continue
			line = fh.readline()	
			print(len(line))
			if len(line.split()) > 3:
				eigenvalue.append(line.split()[0])
				proportion.append(line.split()[1])
				cumulative.append(line.split()[2])
			cnt += 1

	with open(output_file, 'w') as fh:
		writer = csv.writer(fh)
		writer.writerow([i for i in range(1, len(cumulative)+1)])
		writer.writerow(eigenvalue)
		writer.writerow(cumulative)

def get_gi_data(input_file, output_file):
	with open(input_file, 'r') as fh:
		line = fh.readline()
		cnt = 1
		ig = []
		component = []
		while line:
			line = fh.readline()	
			print(len(line))
			if len(line.split()) > 2:
				ig.append(line.split()[0])
				component.append(line.split()[1])
			cnt += 1

	with open(output_file, 'w') as fh:
		writer = csv.writer(fh)
		writer.writerow(ig)
		writer.writerow(component)

#get_pca_data(head+"PCA_mice.txt", head+"PCA_mice.csv")
#get_pca_data(head+"PCA_cost.txt", head+"PCA_cost.csv")
get_gi_data(head+"info_gain.txt", head+"IG_mice.csv")
