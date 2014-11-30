a= read.csv("validation.predictions")
b= read.csv("validation.hard.rndpairs.predictions")
d1 = density(a[,3])
d2 = density (b[,3])

width=12
height=8
pdf("nmf.validate.pdf",width=width,height=height)
plot( d1, col=rgb(0,0,0,1/4),main=NULL,sub=NULL,xlab=NULL)  # second
lines( d2, col=rgb(1,0,0,1/4), main=NULL,sub=NULL,xlab=NULL)  # second

dev.off()



