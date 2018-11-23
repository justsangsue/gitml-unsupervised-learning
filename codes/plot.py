'''
Generate plot from csv files
'''
import pandas as pd
import pylab as plt
from matplotlib.font_manager import FontProperties
import math

def plot_two(filename, title, y1=1, y2=2, 
			xlabel="Number of clusters (k)", 
			ylabel="Within cluster sum of squared errors", 
			legend1="Euclidean", legend2="Manhattan",
			color1='m', color2='c', marker1="*-", marker2="*-"):
	'''use when the csv file has two y and one x'''
	df = pd.read_csv(filename, header=None)
	x_values = df[0:1].values.tolist()[0]
	ecl_values = df[y1:y1+1].values.tolist()[0]
	mah_values = df[y2:y2+1].values.tolist()[0]
	plt.plot(x_values, ecl_values, color1+marker1,
			 x_values, mah_values, color2+marker2)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.legend([legend1, legend2], loc="best",
	            fancybox=True, shadow=True,
	            prop=FontProperties().set_size("small"))
	plt.grid(True)
	plt.grid(color='silver', linestyle='--', linewidth=.5)
	plt.show()

def plot_one(filename, title, xlabel="Number of clusters (k)", ylabel="Cost function values", yrow=1, color='b', markers="*-"):
	df = pd.read_csv(filename, header=None)
	x_values = df[0:1].values.tolist()[0]
	cost_values = df[yrow:yrow + 1].values.tolist()[0]
	plt.plot(x_values, cost_values, color+markers)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.grid(True)
	plt.grid(color='silver', linestyle='--', linewidth=.5)
	plt.show()

def main():
	head = "/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/"

	#plot_two("./figures/kmeans_manh_eucl_mice.csv", "K-Means, Mice Protein")
	#plot_two("./figures/kmeans_manh_eucl_cost.csv", "K-Means, Medical Cost")
	#plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/kmin_cost.csv", "Medical Cost")
	#plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/kmin_mice.csv", "Mice Proteins")
	#plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/EM_kmin_cost.csv", "Medical Cost", ylabel="Log Likehood")
	#plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/EM_kmin_mice.csv", "Mice Proteins", ylabel="Log Likehood")
	#plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/BIC_cost.csv", "BIC, Medical Cost", ylabel="BIC values", color='y')
	#plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/BIC_cost.csv", "Successive Difference of BIC, Medical Cost", ylabel="Difference values of BIC", yrow=2, color='y')
	##plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/BIC_mice.csv", "BIC, Mice Proteins", ylabel="BIC values", color='g')
	#plot_one("/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/processing/BIC_mice.csv", "Successive Difference of BIC, Mice Proteins", ylabel="Difference values of BIC", yrow=2, color='g')
	#plot_two(head+"silhouette_cost.csv", "Silhouette Score, Medical Cost", y1=1, y2=3, ylabel="Silhouette index", legend1="K-Means", legend2="EM")
	#plot_two(head+"silhouette_cost.csv", "Silhouette Score Difference, Medical Cost", y1=2, y2=4, ylabel="Silhouette index difference", legend1="K-Means", legend2="EM")
	#plot_two(head+"silhouette_mice.csv", "Silhouette Score, Mice Proteins", y1=1, y2=3, ylabel="Silhouette index", legend1="K-Means", legend2="EM", color1='r', color2='g')
	#plot_two(head+"silhouette_mice.csv", "Silhouette Score Difference, Mice Proteins", y1=2, y2=4, ylabel="Silhouette index difference", legend1="K-Means", legend2="EM", color1='r', color2='g')	
	#plot_one(head+"PCA_cost.csv", "PCA, Medical Cost", ylabel="Eigen value", xlabel="Principal components", color='k')
	#plot_one(head+"PCA_cost.csv", "PCA, Medical Cost", ylabel="Cumulative", yrow=2,xlabel="Principal components", color='k')
	#plot_one(head+"PCA_mice.csv", "PCA, Mice Proteins", ylabel="Eigen value", xlabel="Principal components", color='m')
	#plot_one(head+"PCA_mice.csv", "PCA, Mice Proteins", ylabel="Cumulative", yrow=2, xlabel="Principal components", color='m')
	#plot_two(head+"NN_cost_woPCA_time.csv", "Neural Network, Medical Cost", xlabel="Training set size (%)", ylabel="Running time (s)", y1=1, y2=2, legend1="Without PCA", legend2="With PCA", color1='k', color2='y', marker2='*--')
	#plot_two(head+"NN_cost_woPCA_rae.csv", "Neural Network, Medical Cost", xlabel="Training set size (%)", ylabel="Relative absolute error", y1=1, y2=2, legend1="Without PCA", legend2="With PCA", color1='g', color2='c', marker2='*--')
	#plot_two(head+"NN_mice_woPCA_time.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Running time (s)", y1=1, y2=2, legend1="Without PCA", legend2="With PCA", color1='r', color2='c', marker2='*--')
	#plot_two(head+"NN_mice_woPCA_rae.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Relative absolute error", y1=1, y2=2, legend1="Without PCA", legend2="With PCA", color1='r', color2='c', marker2='*--')
	#plot_two(head+"NN_cost_woICA_time.csv", "Neural Network, Medical Cost", xlabel="Training set size (%)", ylabel="Running time (s)", y1=1, y2=2, legend1="Without ICA", legend2="With ICA", color1='r', color2='c', marker2='*--')
	#plot_two(head+"NN_cost_woICA_rae.csv", "Neural Network, Medical Cost", xlabel="Training set size (%)", ylabel="Relative absolute error", y1=1, y2=2, legend1="Without ICA", legend2="With ICA", color1='r', color2='c', marker2='*--')
	#plot_two(head+"NN_mice_woICA_time.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Running time (s)", y1=1, y2=2, legend1="Without ICA", legend2="With ICA", color1='b', color2='g', marker2='*--')
	#plot_two(head+"NN_mice_woICA_rae.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Relative absolute error", y1=1, y2=2, legend1="Without ICA", legend2="With ICA", color1='b', color2='g', marker2='*--')
	#plot_two(head+"NN_cost_woRP_rae.csv", "Neural Network, Medical Cost", xlabel="Training set size (%)", ylabel="Relative absolute error", legend1="Without RP", legend2="With RP")
	#plot_two(head+"NN_cost_woRP_time.csv", "Neural Network, Medical Cost", xlabel="Training set size (%)", ylabel="Running time", legend1="Without RP", legend2="With RP")
	#plot_two(head+"NN_mice_woRP_rae.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Relative absolute error", legend1="Without RP", legend2="With RP", color1='c', color2='m', marker2='*--')
	#plot_two(head+"NN_mice_woRP_time.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Running time", legend1="Without RP", legend2="With RP", color1='c', color2='m', marker2='*--')
	plot_two(head+"NN_mice_woIG_rae.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Relative absolute error", legend1="Without IG", legend2="With IG", color1='r', color2='k', marker2='*--')
	plot_two(head+"NN_mice_woIG_time.csv", "Neural Network, Mice Proteins", xlabel="Training set size (%)", ylabel="Running time", legend1="Without IG", legend2="With IG", color1='r', color2='k', marker2='*--')
if __name__ == "__main__":
	main()