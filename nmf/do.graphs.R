a= read.csv("test.predictions")
b= read.csv("test.rndpairs.predictions")
p1 = hist(a[1:1000,3])
p2 = hist(b[1:1000,3])

width=12
height=8
pdf("nmf.pdf",width=width,height=height)
plot( p1, col=rgb(0,0,0,1/4),ylim=c(0,400),main=NULL,sub=NULL,xlab=NULL)  # second
plot( p2, col=rgb(1,0,0,1/4),  add=T,main=NULL,sub=NULL,xlab=NULL)  # second

dev.off()

a1 = read.csv("baseline.ratings.predictions")
b1 = read.csv("baseline.hard.rndpairs.predictions")
p3 = hist(a1[1:1000,3])
p4 = hist(b1[1:999,3])

pdf("baseline.pdf",width=width,height=height)
plot( p3, col=rgb(0,0,0,1/4),ylim=c(0,700),main=NULL,sub=NULL,xlab=NULL)  # second
plot( p4, col=rgb(1,0,0,1/4),  add=T,main=NULL,sub=NULL,xlab=NULL)  # second

dev.off() 
