prefix = "20M.cluster1.rndpairs.notrated/test"
# no hard pairs, 200 clusters, 3 rounds

prefix = "20M.cluster2.rndpairs.notrated/test"
## 200 clusters, 100 hard clusters. 3 rounds

prefix = "20M.cluster3.rndpairs.notrated/test"
## 200 clusters, 100 hard clusters, 10 rounds.

prefix = "20M.cluster4.rndpairs.notrated/test"
## 200 clusters, 100 hard clusters, 5 rounds.

prefix = "40M.cluster4.rndpairs.notrated/test"
## 200 clusters, 100 hard clusters, 5 rounds.

b= read.csv(paste(prefix,"hard.rndpairs.predictions",sep="."))
a= read.csv(paste(prefix,"predictions",sep="."))
c= read.csv(paste(prefix,"rndpairs.predictions",sep="."))
d1 = density(a[,3])
d2 = density(b[,3])
d3 = density(c[,3])

width=12
height=8
pdf("density.pdf",width=width,height=height)
plot(d1, col=rgb(0,0,0,1),main=NULL,sub=NULL,xlab=NULL)  # second
lines(d2, col=rgb(1,0,0,1),main=NULL,sub=NULL,xlab=NULL)  # second
lines(d3, col=rgb(1,1,0,1),main=NULL,sub=NULL,xlab=NULL)  # second

dev.off()

limit <- function(x){
    return (min(x,900))
}

breaks = 50
k = dim(b)[1]

p3 = hist(sapply(a[1:k,3],limit),breaks=breaks)
p4 = hist(sapply(b[,3],limit),breaks=breaks)
p5 = hist(sapply(c[,3],limit),breaks=breaks)

pdf("histogram.pdf",width=width,height=height)
#plot( p5, col=rgb(1,1,0,1/4),  main=NULL,sub=NULL,xlab=NULL)  # second
plot( p3, col=rgb(0,0,0,1/4),main=NULL,sub=NULL,xlab=NULL)  # second
plot( p4, col=rgb(1,0,0,1/4), add=T,main=NULL,sub=NULL,xlab=NULL)  # second

limit <- function(x){
    return (min(x,50))
}

dev.off()

p3 = hist(sapply(a[1:k,3]/a[1:k,4],limit),breaks=30)
p4 = hist(sapply(b[,3]/b[,4],limit),breaks=30)
p5 = hist(sapply(c[,3]/c[,4],limit),breaks=30)

pdf("histogram-scaled.pdf",width=width,height=height)
#plot( p5, col=rgb(1,1,0,1/4),  main=NULL,sub=NULL,xlab=NULL)  # second
plot( p4, col=rgb(1,0,0,1/4),main=NULL,sub=NULL,xlab=NULL)  # second
plot( p3, col=rgb(0,0,0,1/4), add = T, main=NULL,sub=NULL,xlab=NULL)  # second

dev.off() 
