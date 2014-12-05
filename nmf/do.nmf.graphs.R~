a= read.csv("./setA.a.cos.test.predictions.scaled")
b= read.csv("./setA.b.cos.test.predictions.scaled")
p1 = hist(a[1:1000,3],prob=TRUE)
p2 = hist(b[1:999,3],prob=TRUE)

width=12
height=8
pdf("cos.validate.pdf",width=width,height=height)
plot( p1, col=rgb(0,0,0,1/4),main=NULL,sub=NULL,xlab=NULL)  # second
plot( p2, col=rgb(1,0,0,1/4),  add=T,main=NULL,sub=NULL,xlab=NULL)  # second

dev.off()

