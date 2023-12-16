library(ggplot2)
library(gridExtra)
library(corrplot)

getwd()
setwd(getwd())
main_data<-read.csv("bodyPerformance.csv")
View(main_data)

gender_count <- table(main_data$gender)

################################################################################
# Male and female %
################################################################################


data <- data.frame(
  Category = c("Female", "Male"),
  Value = c(gender_count)
)
data$Percentage <- (data$Value / sum(data$Value)) * 100
p <- ggplot(data, aes(x = "", y = Value, fill = Category)) +
  geom_bar(width = 1, stat = "identity") +
  coord_polar(theta = "y") +
  labs(title = "Pie Chart of Percentage of male and female") +
  geom_text(aes(label = paste(round(Percentage,2), "%")), position = position_stack(vjust = 0.5)) +
  theme_void()
print(p)

################################################################################
# no of people in a class
################################################################################

class_count=table(main_data$class)
print(class_count)
barplot(table(main_data$class),
        xlab = 'class',ylab = 'Number of people',
        ylim = c(0,5000) ,col=c('blue'))
title(main='number of people in each class',sub='')
box()
text(
  x = 1:4, 
  y = class_count + 2,  
  labels = class_count, 
  pos = 3,  
  cex = 1,  
  col = "black"  
)

################################################################################
# no of male and female in each class//bar
################################################################################


data <- data.frame(
  encoded_class = main_data$class,
  gender = main_data$gender
)
ggplot(data, aes(x = encoded_class, fill = gender)) +
  geom_bar(position = "dodge") +
  geom_text(
    aes(label = stat(count)),
    stat = "count",
    vjust = -0.5,  
    hjust=0.5,
    size = 3.5,      
    color = "black"
  ) +
  labs(title = "Count of People by Gender in each Class", x = "Class", y = "No. of people") +
  theme_minimal()

################################################################################
# frequency of age//histogram
################################################################################


data <- data.frame(Values = main_data$age)

ggplot(data, aes(x = Values)) +
  geom_histogram(binwidth = 1, fill = "blue", color = "black", alpha = 0.7) +
  labs(title = "Histogram of Sample Data", x = "Values", y = "Frequency") +
  theme_minimal()


################################################################################
# box plot between age and class
################################################################################


data <- data.frame(
  Category = main_data$class,
  Value = main_data$age
)
p <- ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_boxplot(width = 0.2) +
  scale_fill_manual(values = c("orange", "green", "skyblue", "purple")) +
  coord_flip()+
  # theme_minimal() +
  labs(title = "Horizontal Box Plots Between Class and Age",x='Class',y='Age')
print(p)


################################################################################
# mean of PA and class 
################################################################################

A_mean_grip <- mean(main_data$gripForce[main_data$class == 'A'])
B_mean_grip <- mean(main_data$gripForce[main_data$class == 'B'])
C_mean_grip <- mean(main_data$gripForce[main_data$class == 'C'])
D_mean_grip <- mean(main_data$gripForce[main_data$class == 'D'])

A_mean_SBF <- mean(main_data$sit.and.bend.forward_cm[main_data$class == 'A'])
B_mean_SBF <- mean(main_data$sit.and.bend.forward_cm[main_data$class == 'B'])
C_mean_SBF <- mean(main_data$sit.and.bend.forward_cm[main_data$class == 'C'])
D_mean_SBF <- mean(main_data$sit.and.bend.forward_cm[main_data$class == 'D'])

A_mean_SU <- mean(main_data$sit.ups.counts[main_data$class == 'A'])
B_mean_SU <- mean(main_data$sit.ups.counts[main_data$class == 'B'])
C_mean_SU <- mean(main_data$sit.ups.counts[main_data$class == 'C'])
D_mean_SU <- mean(main_data$sit.ups.counts[main_data$class == 'D'])

A_mean_BrJ <- mean(main_data$broad.jump_cm[main_data$class == 'A'])
B_mean_BrJ <- mean(main_data$broad.jump_cm[main_data$class == 'B'])
C_mean_BrJ <- mean(main_data$broad.jump_cm[main_data$class == 'C'])
D_mean_BrJ <- mean(main_data$broad.jump_cm[main_data$class == 'D'])


data1 <- data.frame(Category = c('A','B','C','D'), Value = c(A_mean_grip,B_mean_grip,C_mean_grip,D_mean_grip))
data2 <- data.frame(Category = c('A','B','C','D'), Value = c(A_mean_SBF, B_mean_SBF, C_mean_SBF,D_mean_SBF))
data3 <- data.frame(Category = c('A','B','C','D'), Value = c(A_mean_SU, B_mean_SU, C_mean_SU,D_mean_SU))
data4 <- data.frame(Category = c('A','B','C','D'), Value = c(A_mean_BrJ, B_mean_BrJ, C_mean_BrJ,D_mean_BrJ))

color_palette <- c("red", "green", "blue", "purple")


p1 <- ggplot(data1, aes(x = Category, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = "", x = "Class", y = "Mean Grip Force(kg)",cex.main=15)+
  # scale_fill_manual(values = color_palette) +
  labs(title = "Mean Grip Force ")
  # scale_y_continuous(breaks=seq(0:50:5))

p2 <- ggplot(data2, aes(x = Category, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = "", x = "Class", y = "Mean Seat and Bend forward(cm)")+
  # scale_fill_manual(values = color_palette) +
  labs(title = "Mean Seat and Bend forward")

p3 <- ggplot(data3, aes(x = Category, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = "", x = "Class", y = "Mean Situp Count")+
  # scale_fill_manual(values = color_palette) +
  labs(title = "Mean Situp Count")

p4 <- ggplot(data4, aes(x = Category, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = "", x = "Class", y = "Mean Broad Jump(cm)")+
  # scale_fill_manual(values = color_palette) +
  labs(title = "Mean Broad Jump")

grid.arrange(p1, p2, p3, p4, ncol = 2)

################################################################################
# Box plots of Body attributes and age
################################################################################


data <- data.frame(
  Category = main_data$class,
  Value = main_data$height_cm
)
bp1 <- ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_boxplot(width = 0.2) +
  scale_fill_manual(values = c("orange", "green", "skyblue", "purple")) +
  coord_flip()+
  # theme_minimal() +
  labs(title = "Horizontal Box Plots Between Class and Height",x='Class',y='Height')
print(p1)

data <- data.frame(
  Category = main_data$class,
  Value = main_data$weight_kg
)
bp2 <- ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_boxplot(width = 0.2) +
  scale_fill_manual(values = c("orange", "green", "skyblue", "purple")) +
  coord_flip()+
  # theme_minimal() +
  labs(title = "Horizontal Box Plots Between Class and weight",x='Class',y='weight')
print(p2)

data <- data.frame(
  Category = main_data$class,
  Value = main_data$body.fat_.
)
bp3 <- ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_boxplot(width = 0.2) +
  scale_fill_manual(values = c("orange", "green", "skyblue", "purple")) +
  coord_flip()+
  # theme_minimal() +
  labs(title = "Horizontal Box Plots Between Class and Body Fat%",x='Class',y='Body Fat%')
print(p3)
data <- data.frame(
  Category = main_data$class,
  Value = main_data$diastolic
)


s<-grid.arrange(bp1, bp2,bp3, ncol = 2)

################################################################################
# Correlation matrix
################################################################################

num_data<-main_data[sapply(main_data,is.numeric)]
cor_matrix <- cor(num_data)
corrplot(
  cor_matrix,
  method = "color",        # Use color to represent the correlations
  diag = FALSE,
  type = "upper",           # Display the upper triangle of the matrix
  tl.cex = 0.8,             # Adjust the size of the text labels
  tl.col = "black",         # Label color
  tl.srt = 45,              # Rotate text labels for better visibility
  tl.pos = "t",            # Label position (left-top)
  addCoef.col = "black",    # Color of coefficient values
  col = colorRampPalette(c("#3c4ec2","white", "#b50927"))(100),  # Color palette
  number.cex = 0.6,         # Adjust the size of the correlation values
  mar = c(4, 0, 0.1, 0)       # Adjust the margin of the plot
)
title("Correlation Matrix(Heat Map) Plot", line = 2, outer = FALSE)


####################################################

 