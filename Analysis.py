# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the Dataset for Left Handed
lefthanded_data = pd.read_csv("LH_Data.csv")

# Plotting Left-Handedness Rates against Age
fig, ax = plt.subplots()
ax.plot(lefthanded_data['Age'], lefthanded_data['Female'], label='Female', marker = 'o')
ax.plot(lefthanded_data['Age'], lefthanded_data['Male'], label='Male', marker = 'x')
ax.legend()
ax.set_xlabel("Age")
ax.set_ylabel("Left-Handed Rate")
ax.set_title("Left-Handed Rate against Age by Sex")
plt.grid(True)
'''plt.show()'''

# Adding new columns 
lefthanded_data['Birth_year'] = 1986 - lefthanded_data['Age']
lefthanded_data['Mean_lh'] = lefthanded_data[['Male','Female']].mean(axis=1)

# Plotting Mean Left-Handedness against Birth year
lefthanded_data.plot(x = 'Birth_year', y = 'Mean_lh', kind = 'line', legend = False, marker = 'o')
plt.xlabel("Birth Year")
plt.ylabel("Mean Left-Handedness")
plt.title("Average Left-Handedness Rate by Birth Year")
plt.grid(True)
plt.tight_layout()
plt.gca().invert_xaxis()
'''plt.show()'''

# Creating a function for P(LH | A)
def P_lh_given_A(ages_of_death, study_year=1986):
    ages_of_death = np.array(ages_of_death)

    # Calculating Mean of first 10 and last 10 points for left-handedness
    early_1900s_rate = lefthanded_data['Mean_lh'].iloc[-10:].mean() 
    late_1900s_rate = lefthanded_data['Mean_lh'].iloc[:10].mean()
    middle_rates = lefthanded_data.loc[lefthanded_data['Birth_year'].isin(study_year - ages_of_death)]['Mean_lh']
    youngest_age = study_year - 1986 + 10 # the youngest age is 10
    oldest_age = study_year - 1986 + 86 # the oldest age is 86

    # Creating an empty array to store the results
    P_return = np.zeros(ages_of_death.shape) 

    # Extracting rate of left-handedness for people of ages 'ages_of_death'
    P_return[ages_of_death > oldest_age] = early_1900s_rate / 100
    P_return[ages_of_death < youngest_age] = late_1900s_rate / 100
    P_return[np.logical_and((ages_of_death <= oldest_age), (ages_of_death >= youngest_age))] = middle_rates / 100

    return P_return

# Loading Death Distribution Dataset
death_distribution_data = pd.read_csv("DD_Data.csv", sep = '\t', skiprows = [1])

# Dropping NaN Values from the 'Both Sexes' column
death_distribution_data = death_distribution_data.dropna(subset=['Both Sexes'])

# Plotting the number of people who died as a function of Age 
death_distribution_data.plot(x = 'Age', y = 'Both Sexes', kind = 'line', legend = False, marker = 'o')
plt.xlabel("Age")
plt.ylabel("Number of Deaths")
plt.title("Age at which people died")
plt.grid(True)
plt.tight_layout()
'''plt.show()'''

# Creating a function to determine the overall probability of left-handedness in a study year
def P_lh(death_distribution_data, study_year = 1990): 

    # Extract Ages and Number of deaths 
    ages = death_distribution_data['Age'].values
    num_deaths = death_distribution_data['Both Sexes'].values

    # Calculating the probability of the people dead being left-handed
    p_lh_given_a = P_lh_given_A(ages, study_year)

    # Multiplying the number of deaths with probability calculated 
    p_list = num_deaths * p_lh_given_a
    p = p_list.sum()

    # Normalizing by total number of deaths
    return p/num_deaths.sum()

# Creating a function to find the probability that you are left-handed at the age of death
def P_A_given_lh(ages_of_death, death_distribution_data, study_year = 1990):
    
    # Probability of dying at an Age 'A'
    death_counts = death_distribution_data.set_index('Age').loc[ages_of_death, 'Both Sexes'].values
    P_A = death_counts/death_distribution_data['Both Sexes'].sum()

    # Probability of being left-handed
    P_left = P_lh(death_distribution_data, study_year)

    # Probability of being left-handed at given Age 
    P_lh_A = P_lh_given_A(ages_of_death, study_year)

    # Returning Bayes' Rule
    return (P_lh_A * P_A) / P_left

# Creating a function to find the probability that you are right-handed at the age of death
def P_A_given_rh(ages_of_death, death_distribution_data, study_year = 1990):
    
    # Probability of dying at an Age 'A'
    death_counts = death_distribution_data.set_index('Age').loc[ages_of_death, 'Both Sexes'].values
    P_A = death_counts/death_distribution_data['Both Sexes'].sum()

    # Probability of being right-handed
    P_left = P_lh(death_distribution_data, study_year)
    P_right = 1 - P_left

    # Probability that you are right-handed at given age
    P_lh_A = P_lh_given_A(ages_of_death, study_year)
    P_rh_A = 1 - P_lh_A

    # Returning Bayes' Rule
    return (P_rh_A * P_A) / P_right

# Creating a list of ages of death to plot
ages = np.arange(6, 115, 1) # ages 6 to 114

# Calculating the Probability of being left handed or right handed for each
left_handed_probability = P_A_given_lh(ages, death_distribution_data, study_year=1990)
right_handed_probability = P_A_given_rh(ages, death_distribution_data, study_year=1990)

# plotting the calculated probability of being right-handed or left-handed
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(ages, left_handed_probability, label = 'Left-Handed', color = 'blue')
ax.plot(ages, right_handed_probability, label = 'Right-Handed', color = 'green')

# Labeling the plot
ax.legend()
ax.set_xlabel("Age at Death")
ax.set_ylabel("Probability of being age A at death")
ax.set_title("P(A | LH) and P(A | RH) plotted against Age at Death")
ax.grid(True)
plt.tight_layout()
'''plt.show()'''

# Calculating Average Ages for left-handed and right-handed groups 
# Using np.array so that the two arrays can be multiplied
ages = np.arange(6, 115, 1)

# Average age at death for left-handers
average_lh_age = np.nansum(ages * np.array(left_handed_probability))

# Average age at death for right-handers
average_rh_age = np.nansum(ages * np.array(right_handed_probability))

# Printing the average ages for each group
print("Average age at death for left-handers:", round(average_lh_age, 2), "years")
print("Average age at death for right-handers:", round(average_rh_age, 2), "years")

# Printing the Difference between the average ages
print("The difference in average ages is " + str(round(average_rh_age - average_lh_age, 2)) + " years.")

# Re-Imagining the Insights by considering the study year as 2018
# Calculating the Probability of being left handed or right handed for each (2018)
left_handed_probability_2018 = P_A_given_lh(ages, death_distribution_data, study_year=2018)
right_handed_probability_2018 = P_A_given_rh(ages, death_distribution_data, study_year=2018)

# plotting the calculated probability of being right-handed or left-handed (2018)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(ages, left_handed_probability_2018, label = 'Left-Handed', color = 'blue')
ax.plot(ages, right_handed_probability_2018, label = 'Right-Handed', color = 'green')

# Labeling the plot (2018)
ax.legend()
ax.set_xlabel("Age at Death")
ax.set_ylabel("Probability of being age A at death")
ax.set_title("P(A | LH) and P(A | RH) plotted against Age at Death (based on 2018 data)")
ax.grid(True)
plt.tight_layout()
'''plt.show()'''

# Calculating the average ages for left and right-handed groups using the updated probabilities
average_lh_age_2018 = np.nansum(ages * np.array(left_handed_probability_2018))
average_rh_age_2018 = np.nansum(ages * np.array(right_handed_probability_2018))

# Printing the average ages for each group (2018)
print("Average age at death for left-handers (2018):", round(average_lh_age_2018, 2), "years")
print("Average age at death for right-handers (2018):", round(average_rh_age_2018, 2), "years")

# Printing the difference between the average ages (2018)
print("The difference in average ages is " + str(round(average_rh_age_2018 - average_lh_age_2018, 1)) + " years.")