
library("caret")
library("rpart")
library("tree")
library("randomForest")
library("e1071")
library("ggplot2")

df <- read.csv("seaflow_21min.csv")

#------ Step 1

# answer 1
nrow(df[df$pop=="synecho",])

# answer 2
summary(df)

#------ Step 2

set.seed(3456)
trainIndex <- createDataPartition(df$time, list = F,p = .5, times = 1)

train <- df[trainIndex,]
test <- df[-trainIndex,]

# answer 3
mean(train$time)

#------ Step 3

# answer 4
p <- ggplot(df,aes(x=pe, y=chl_small, color = pop))
p + geom_point()

#------ Step 4

# answer 5,6,7

fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=train)

print(model)

#------ Step 5

# answer 8
model <- rpart(fol, method="class", data=train)
DT_fit <- predict(model, test, type = "class")
ans8 <- DT_fit == test$pop
correct <- sum(ans8)
acc <- correct/length(ans8)
acc

#------ Step 6

# answer 9
model <- randomForest(fol, method="class", data=train)
RF_fit <- predict(model, test, type = "class")
ans9 <- RF_fit == test$pop
correct <- sum(ans9)
acc <- correct/length(ans9)
acc

# answer 10
importance(model)

#------ Step 7

# answer 11
model <- svm(fol, method="class", data=train)
SVM_fit <- predict(model, test, type = "class")
ans10 <- SVM_fit == test$pop
correct <- sum(ans10)
acc <- correct/length(ans10)
acc

#------ Step 8

# answer 12
table(pred = DT_fit, true = test$pop)
table(pred = RF_fit, true = test$pop)
table(pred = SVM_fit, true = test$pop)

# answer 13
p <- ggplot(df,aes(x=pop, y=fsc_big))
p + geom_point()

# answer 14
train_treated <- train[train$file_id != 208,]
test_treated <- test[test$file_id != 208,]

model <- svm(fol, method="class", data=train_treated)
SVM_fit <- predict(model, test_treated, type = "class")
ans14 <- SVM_fit == test_treated$pop
correct <- sum(ans14)
acc <- correct/length(ans14)
acc
0.9716409 - 0.9191065
