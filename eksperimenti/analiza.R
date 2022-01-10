library('readxl')
library('ggplot2') 
library("ggpubr")

# Delež vozlišč v BCS grafu glede na verjetnost barvanja p 

p <- c(0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1)

ena_p <- read_excel('1x50_p.xlsx')
dva_p <- read_excel('2x50_p.xlsx')
tri_p <- read_excel('3x50_p.xlsx')
stiri_p <- read_excel('4x50_p.xlsx')

povprecje_ena_p <- data.frame(p, pov = colMeans(ena_p)/50)
povprecje_dva_p <- data.frame(p, pov = colMeans(dva_p)/100)
povprecje_tri_p <- data.frame(p, pov = colMeans(tri_p)/150)
povprecje_stiri_p <- data.frame(p, pov = colMeans(stiri_p)/200)

e_p <- ggplot(data = povprecje_ena_p, aes(x=p)) + 
  geom_col(aes(y=pov), fill = 'darkslategray3') + 
  geom_line(aes(y=pov), size=1.2, colour= 'dodgerblue4') +
  xlab("p") + 
  ylab("Delež vozlišč") +
  ggtitle("m=1") +
  theme(plot.title = element_text(hjust = 0.5, size = 14))

d_p <- ggplot(data = povprecje_dva_p, aes(x=p)) + 
  geom_col(aes(y=pov), fill = 'darkslategray3') + 
  geom_line(aes(y=pov), size=1.2, colour= 'dodgerblue4') +
  xlab("p") + 
  ylab("Delež vozlišč") +
  ggtitle("m=2") +
  theme(plot.title = element_text(hjust = 0.5, size = 14))

t_p <- ggplot(data = povprecje_tri_p, aes(x=p)) + 
  geom_col(aes(y=pov), fill = 'darkslategray3') + 
  geom_line(aes(y=pov), size=1.2, colour= 'dodgerblue4') +
  xlab("p") + 
  ylab("Delež vozlišč") +
  ggtitle("m=3") +
  theme(plot.title = element_text(hjust = 0.5, size = 14))

s_p <- ggplot(data = povprecje_stiri_p, aes(x=p)) + 
  geom_col(aes(y=pov), fill = 'darkslategray3') + 
  geom_line(aes(y=pov), size=1.2, colour= 'dodgerblue4') +
  xlab("p") + 
  ylab("Delež vozlišč") +
  ggtitle("m=4") +
  theme(plot.title = element_text(hjust = 0.5, size = 14))

z <- ggarrange(e_p, d_p, t_p, s_p, ncol = 2, nrow = 2)

print(annotate_figure(z, top = text_grob("Delež vozlišč v BCS grafu glede na verjetnost barvanja p", face = "bold", size = 14)))

# Delež vozlišč v BCS grafu glede na dolžino grafa

n <- c(5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
colors <- c("m = 1" = "cadetblue4", "m = 2" = "coral2", "m = 3" = "olivedrab3", "m = 4" = "violetred")

ena_n <- read_excel('1xn_0.5.xlsx')
dva_n <- read_excel('2xn_0.5.xlsx')
tri_n <- read_excel('3xn_0.5.xlsx')
stiri_n <- read_excel('4xn_0.5.xlsx')

povprecje_n <- data.frame(n, 
                              pov1 = colMeans(ena_n)/n, 
                              pov2 = colMeans(dva_n)/(n*2),
                              pov3 = colMeans(tri_n)/(n*3),
                              pov4 = colMeans(stiri_n)/(n*4))

gn <- ggplot(data = povprecje_n, aes(x=n, legenda = n)) + 
  geom_line(aes(y=pov1, color= 'm = 1'), size=1.1) +
  geom_line(aes(y=pov2, color= 'm = 2'), size=1.1) +
  geom_line(aes(y=pov3, color= 'm = 3'), size=1.1) +
  geom_line(aes(y=pov4, color= 'm = 4'), size=1.1) +
  labs( x = 'n',
        y = 'Delež vozlišč',
        color = ' ')+
  scale_color_manual(values=colors) +
  ggtitle("Delež vozlišč v BCS grafu glede na dolžino grafa") +
  theme(plot.title = element_text(hjust = 0.5, size = 16))

print(gn)


# Časovna zahtevnost

n2 <- c(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
cas <- read_excel('cas.xlsx', sheet = 2)
colnames(cas) <- c('ena', 'dva', 'tri', 'stiri')

gcas <- ggplot(data = cas, aes(x=n2, legenda = n2)) + 
  geom_line(aes(y=ena, color= 'm = 1'), size=1.1) +
  geom_line(aes(y=dva, color= 'm = 2'), size=1.1) +
  geom_line(aes(y=tri, color= 'm = 3'), size=1.1) +
  geom_line(aes(y=stiri, color= 'm = 4'), size=1.1) +
  labs( x = 'n',
        y = 'čas(s)',
        color = ' ')+
  scale_color_manual(values=colors) +
  ggtitle("Časovna zahtevnost algoritma") +
  theme(plot.title = element_text(hjust = 0.5, size = 16))

print(gcas)