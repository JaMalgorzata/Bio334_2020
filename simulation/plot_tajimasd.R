data <- read.table("result.dat", header=T, sep="\t")
png("tajimasd.png")
plot(data[c(1,5)], type="l")
dev.off()
