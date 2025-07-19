# Loading libraries
library(ggplot2)
library(readr)
library(dplyr)
library(scales)
library(tidyverse)

# Loading files
bayes_1990 <- read_csv("bayes_probabilities_1990.csv")
bayes_2018 <- read_csv("bayes_probabilities_2018.csv")
lh_data <- read_csv("cleaned_lh_data.csv")
dd_data <- read_delim("cleaned_death_distribution.csv")

# Left-Handed Rate by Age and Gender
ggplot(lh_data, aes(x = Age)) +
  geom_line(aes(y = Female, color = "Female"), size = 1) +
  geom_line(aes(y = Male, color = "Male"), size = 1) +
  labs(title = "Left-Handed Rate by Age and Gender", y = "Left-Handed Rate", x = "Age") +
  scale_color_manual(values = c("Female" = "#E91E63", "Male" = "#2196F3")) +
  theme_minimal()

# Birth Year and Mean Left-Handedness
lh_data <- lh_data %>%
  mutate(Birth_year = 1986 - Age,
         Mean_lh = rowMeans(select(., Male, Female), na.rm = TRUE))

# Mean Left-Handedness by Birth Year 
ggplot(lh_data, aes(x = Birth_year, y = Mean_lh)) +
   geom_line(color = "#4CAF50", size = 1.2) +
  geom_point(color = "#4CAF50", size = 2) +
  scale_x_reverse() +
  labs(title = "Mean Left-Handedness by Birth Year", y = "Left-Handed Rate (%)", x = "Birth Year") +
  theme_minimal()

# Number of Deaths by Age 
ggplot(dd_data, aes(x = Age, y = `Both Sexes`)) +
  geom_col(fill = "#FF9800") +
  labs(title = "Number of Deaths by Age", x = "Age", y = "Deaths") +
  theme_minimal()

# Combined 1990 and 2018 Probabilities 
bayes_1990$Year <- "1990"
bayes_2018$Year <- "2018"

combined_df <- bind_rows(
  bayes_1990 %>% mutate(Group = "Left-Handed", Value = P_A_given_LH_1990),
  bayes_1990 %>% mutate(Group = "Right-Handed", Value = P_A_given_RH_1990),
  bayes_2018 %>% mutate(Group = "Left-Handed", Value = P_A_given_LH_2018),
  bayes_2018 %>% mutate(Group = "Right-Handed", Value = P_A_given_RH_2018)
  )

# Death Probability by Handedness
ggplot(combined_df, aes(x = Age, y = Value, color = Group, linetype = Year)) +
  geom_line(size = 1) +
  labs(title = "Age-at-Death Probability by Handedness (1990 vs 2018)",
       x = "Age at Death", y = "Probability",
       color = "Handedness", linetype = "Study Year") +
  scale_color_manual(values = c("Left-Handed" = "#2196F3", "Right-Handed" = "#FF5722")) +
  theme_minimal()

# Peak Age for Each Group and Year
peaks <- combined_df %>%
  group_by(Year, Group) %>%
  slice_max(Value, n = 1)

# Area Overlap
ggplot(combined_df, aes(x = Age, y = Value, fill = Group)) +
  geom_area(position = 'identity', alpha = 0.4) +
  facet_wrap(~Year) +
  labs(title = "Age Distribution Overlap: Left vs Right-Handed",
       x = "Age at Death", y = "Probability") +
  scale_fill_manual(values = c("Left-Handed" = "#2196F3", "Right-Handed" = "#FF5722")) +
  theme_minimal()