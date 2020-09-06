#I will try applying a Neural Network
#Library
library(neuralnet)
#Data Manipulation
df1 <- read.csv("PlayoffsTrainData.csv", header = TRUE)
#Remove Team Names To Avoid Bias
df1$Team <- NULL
#Remove Data
df1$X <- NULL
df1$X.1 <- NULL
df1$X.2 <- NULL
df1$X.3 <- NULL
df1$DefRtg <- NULL
df1$SecondaryAsts <- NULL
df1$PaceInLosses <- NULL
df1$PaceInWins <- NULL
df1$MOG <- NULL
df1$RebPercent <- NULL
df1$KeyPlayers <- NULL
#DF1 Fix up
str(df1)
df1$Seed <- as.numeric(df1$Seed)
df1$Score <- as.numeric(df1$Score)
df1$ShootingRating <- ((1.5*3+df1$X3PFGA)+(3+df1$X3PPercent)-7.5)
df1 <- as.data.frame(scale(df1, center = TRUE, scale = TRUE))
#DF2 Fix up
df2 <- read.csv("Current.csv", header = TRUE)
df2$Seed <- as.numeric(df2$Seed)
df2$ShootingRating <- ((1.5*3+df2$X3PFGA)+(3+df2$X3PPercent)-7.5)
df2$Score <- 0
df2$Team <- NULL
df2 <- as.data.frame(scale(df2, center = TRUE, scale = TRUE))
#Creating the model
#No seed bc I wanted a random simulation of n=1 (Ill work on adding later)
trial.model <- neuralnet(df1$Score~Seed+ShootingRating+OffRtg, data = df1, 
                         hidden = 2,linear.output = FALSE, 
                         threshold = 0.1)
Pred.df2 <- predict(trial.model, df2, interval="confidence")
df2$Score <- Pred.df2
df.final <- read.csv("Current.csv", header = TRUE)
df.final$Score <- df2$Score*8.294+7.906
view(df.final)
#write.csv("FinalPred.csv")

#This is not complete, as I want to run a sample of 50 simulations to create the final rankings
