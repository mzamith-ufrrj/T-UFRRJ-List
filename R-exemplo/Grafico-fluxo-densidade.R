library(ggplot2)
log <- read.csv("SP.SL-STANDARD-HR-1.5-0.csv", header=FALSE, sep = ";", stringsAsFactors=FALSE)

X <- log$V4 * 133
Y <- log$V3 / 5 * 3600
#ggplot(data = log) + geom_point(aes(x = V3, y = V5))

ggplot(data = log) + 
  geom_point(aes(x = X, y = Y)) + 
  xlab("Veículos/km") + 
  ylab("Veículos/h")  + 
  scale_x_continuous(breaks = seq(0, 133, by = 10)) +
  scale_y_continuous(breaks = seq(0, 3600, by = 500)) + #+ coord_fixed()
  geom_hline(yintercept=2160, linetype="dashed", color = "green", size=1) +
  geom_hline(yintercept=2400, linetype="dashed", color = "red", size=1)


#Não incluir a questão da função beta na desaceleração ou em quqluer outra parter
#usar a versão de foto, porque será melhor para combinar com o cluster de influcencia

