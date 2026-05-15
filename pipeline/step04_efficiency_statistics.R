data <- read.csv("results/tables/ngs_summary.csv")

summary(data$editing_rate)

png("results/figures/editing_rate_hist.png")

hist(data$editing_rate)

dev.off()
