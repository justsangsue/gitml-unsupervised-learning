mydata=read.csv("medical_cost_classified.csv",header=TRUE)
library("foreign")
write.arff(x=mydata ,file= "medical_cost_classified.arff")