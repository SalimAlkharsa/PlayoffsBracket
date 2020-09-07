#This program is made to visualize the results of the neural network
df <- read.csv("VizualisingNN.csv", header = TRUE)
#Put the libraries in
library(plotly)
library(formattable)
library(data.table)
library(tidyr)
library(stringr)
library(tidyverse)

#Quick Housekeeping
customGreen0 = "#DeF7E9"
customGreen = "#71CA97"
df[is.na(df)] <- 0
df <- df %>% 
  rename(
    ProbabilityOfLosingR1 = Number.of.Times.w.0,
    ProbabilityOfLosingR2 = Number.of.Times.w.1,
    ProbabilityOfLosingR3 = Number.of.Times.w.2,
    ProbabilityOfLosingFinals = Number.of.Times.w.3,
    ProbabilityOfWinningItAll = Number.of.Times.w.4)
#Do some data editing
df$ProbabilityOfLosingR1 <- round(((df$ProbabilityOfLosingR1/30)*100),2)
df$ProbabilityOfLosingR2 <- round(((df$ProbabilityOfLosingR2/30)*100),2)
df$ProbabilityOfLosingR3 <- round(((df$ProbabilityOfLosingR3/30)*100),2)
df$ProbabilityOfLosingFinals <- round(((df$ProbabilityOfLosingFinals/30)*100),2)
df$ProbabilityOfWinningItAll <- round(((df$ProbabilityOfWinningItAll/30)*100),2)
#Visualize
formattable(df, align = c("l"), list(
  `Indicator Name` = formatter("span", style = ~ style(color = "grey",font.weight = "bold")), 
   ~ color_tile("#DeF7E9", "#71CA97")))
