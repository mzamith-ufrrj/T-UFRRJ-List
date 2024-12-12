library(ggplot2)
#print("Gráfico fluxo x densidade")
# log <-read.table("SF.MLA-STANDARD-HR-1.5-0.csv", header = T, quote = '"', 
#                        row.names = NULL, 
#                        stringsAsFactors = FALSE, sep=";")
# p <- ggplot(log, aes(X0.00000.4, X0.00000.3)) +
#   geom_point(size=2, shape=23)
# 
# print(p)
rm(list=ls())
print("Cluster de influência")
log_SL_SLOW <-read.table("CA.SL-SLOW-HR-1.5-0.csv", header = T, quote = '"',
                         row.names = NULL,
                         stringsAsFactors = FALSE, sep=";")
log_SL_STAN <-read.table("CA.SL-STANDARD-HR-1.5-0.csv", header = T, quote = '"',
                         row.names = NULL,
                         stringsAsFactors = FALSE, sep=";")
log_SL_DARI <-read.table("CA.SL-DARING-HR-1.5-0.csv", header = T, quote = '"',
                         row.names = NULL,
                         stringsAsFactors = FALSE, sep=";")
# log_MLA <- read.table("CA.MLA-STANDARD-HR-1.5-0.csv", header = T, quote = '"',
#                       row.names = NULL,
#                       stringsAsFactors = FALSE, sep=";")
# log_MLS <- read.table("CA.MLS-STANDARD-HR-1.5-0.csv", header = T, quote = '"',
#                       row.names = NULL,
#                       stringsAsFactors = FALSE, sep=";")

 p <- ggplot(log_SL_STAN, aes(X0.00500, X0.20)) + 
     geom_line(color='blue')+ 
   geom_line(aes(log_SL_DARI$X0.00500, log_SL_DARI$X0.20), color='green') +
   geom_line(aes(log_SL_SLOW$X0.00500, log_SL_SLOW$X0.20), color='red') 
   #   geom_line(aes(X0.00500, X0.20), color='blue') 
# pallet <- c("black", "darkgreen","darkgrey", "darkkhaki", "darkorange", "darkorchid", "darkred", "darkorchid4","firebrick1", "dodgerblue3", "gold", "lawngreen", "lightblue", "lightgreen", "hotpink2", "lightskyblue4", "lightslategrey", "magenta", "mediumaquamarine", "navyblue", "orange", "red2", "plum3", "seagreen1", "plum1") 
#  p <- ggplot(log_SL, aes(X0.00500, X0.2)) +
#    geom_line(color=pallet[1]) +
#    geom_line(aes(X0.00500, X0.3), color=pallet[8])  + 
#    geom_line(aes(X0.00500, X0.4), color=pallet[2]) +
#    geom_line(aes(X0.00500, X0.5), color=pallet[3])  +
#    geom_line(aes(X0.00500, X0.6), color=pallet[4])  +
#    geom_line(aes(X0.00500, X0.7), color=pallet[5])  +
#    geom_line(aes(X0.00500, X0.8), color=pallet[6])  +
#    geom_line(aes(X0.00500, X0.9), color=pallet[7])  +
#    geom_line(aes(X0.00500, X0.10), color=pallet[9])  + 
#    geom_line(aes(X0.00500, X0.11), color=pallet[10]) +
#    geom_line(aes(X0.00500, X0.12), color=pallet[11])  +
#    geom_line(aes(X0.00500, X0.13), color=pallet[12])  +
#    geom_line(aes(X0.00500, X0.14), color=pallet[13])  +
#    geom_line(aes(X0.00500, X0.15), color=pallet[14])  +
#    geom_line(aes(X0.00500, X0.16), color=pallet[15])  
#    
# +
#   geom_point(data=log_MLA, aes(X0.00950, X0.00000), size=3, shape=21, color='red') +
#   geom_line(data=log_MLA, aes(X0.00950, X0.00000),  color='red') +
#   geom_point(data=log_MLS, aes(X0.00950, X0.00000), size=3, shape=15, color='green') +
#   geom_line(data=log_MLS, aes(X0.00950, X0.00000),  color='green')

#
#  geom_point(data=log_MLA, aes(X0.00950, X0.00000), size=3, shape=23) +
#  geom_line(log_MLA, aes(X0.00950, X0.00000)) 
  
  

print(p)