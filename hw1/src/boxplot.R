
titles = c("Phenotype 2 at SNP 258 \n(p=1.13E-92)", "Phenotype 3 at SNP 119 \n(p=4.7E-7)", "Phenotype 4 at SNP 43 \n(p=1.08E-8)")
pdf("../figs/boxplot.pdf", width=6, height=3.5)
par(mfrow=c(1, 3))
for (idx in 0:2) {
    fname = paste("../data/hw.1-1.", idx, ".dat", sep="")
    t = read.table(fname)
    boxplot(t[,1] ~ t[,2])
    regline = lm(t[,1] ~ t[,2])
    abline(regline, col="blue")
    ttl = titles[idx + 1]
    title(main=ttl)
}
dev.off()
