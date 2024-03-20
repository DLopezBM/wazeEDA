#!/usr/bin/env python
# coding: utf-8

# # **Waze Project**
# **Course 3 - Go Beyond the Numbers: Translate Data into Insights**

# Your team is still in the early stages of their user churn project. So far, you’ve completed a project proposal and used Python to inspect and organize Waze’s user data.
# 
# You check your inbox and notice a new message from Chidi Ga, your team’s Senior Data Analyst. Chidi is pleased with the work you have already completed and requests your assistance with exploratory data analysis (EDA) and further data visualization. Harriet Hadzic, Waze's Director of Data Analysis, will want to review a Python notebook that shows your data exploration and visualization.
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions and prepare an executive summary.

# # **Course 3 End-of-course project: Exploratory data analysis**
# 
# In this activity, you will examine data provided and prepare it for analysis.
# <br/>
# 
# **The purpose** of this project is to conduct exploratory data analysis (EDA) on a provided dataset.
# 
# **The goal** is to continue the examination of the data that you began in the previous Course, adding relevant visualizations that help communicate the story that the data tells.
# <br/>
# 
# 
# *This activity has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning
# 
# 
# **Part 3:** Building visualizations
# 
# **Part 4:** Evaluating and sharing results
# 
# <br/>
# 
# 
# Follow the instructions and answer the question below to complete the activity. Then, you will complete an executive summary using the questions listed on the [PACE Strategy Document ](https://docs.google.com/document/d/1iSHdbfQR6w8RClJNWai8oJXn9tQmYoTKn6QohuaK4-s/template/preview?resourcekey=0-ZIHnbxL1dd2u9A47iEVXvg).
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work.

# # **Visualize a story in Python**

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Plan stage.
# 
# 

# ### **Task 1. Imports and data loading**
# 
# For EDA of the data, import the data and packages that will be most helpful, such as pandas, numpy, and matplotlib.
# 
# 
# 

# In[1]:


### YOUR CODE HERE ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read in the data and store it as a dataframe object called df.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[2]:


# Load the dataset into a dataframe
df = pd.read_csv('waze_dataset.csv')

df.info()


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document and those below where applicable to complete your code:
# 1. Does the data need to be restructured or converted into usable formats?
# 
# 2. Are there any variables that have missing data?
# 

# 1. Taking a look at the data types, it seems that all variables are in the right Dtype
# 2. Running the info() method, it seems that "label" is missing in 700 rows.

# ### **Task 2. Data exploration and cleaning**
# 
# Consider the following questions:
# 
# 
# 
# 1.  Given the scenario, which data columns are most applicable?
# 
# 2.  Which data columns can you eliminate, knowing they won’t solve your problem scenario?
# 
# 3.  How would you check for missing data? And how would you handle missing data (if any)?
# 
# 4.  How would you check for outliers? And how would handle outliers (if any)?
# 
# 
# 
# 
# 
# 

# 1. The most applicable columns for this EDA would be sessions, drives and driven_km, all three related to "label" which have 700 rows with missing values.
# 2. I guess that total_navigations_fav1 and total_navigations_fav2 are not relevant and can be removed.
# 3. First, we can use the method info(). In this case, we can put that "label" column null data into a category "Unknown".
# 4. We can use the method describe() at first, and then making a box plot with all the relevant numeric columns.

# #### **Data overview and summary statistics**
# 
# Use the following methods and attributes on the dataframe:
# 
# * `head()`
# * `size`
# * `describe()`
# * `info()`
# 
# It's always helpful to have this information at the beginning of a project, where you can always refer back to if needed.

# In[3]:


### YOUR CODE HERE ###
df.head()


# In[4]:


### YOUR CODE HERE ###
df.size


# Generate summary statistics using the `describe()` method.

# In[5]:


### YOUR CODE HERE ###
df.describe()


# And summary information using the `info()` method.

# In[6]:


### YOUR CODE HERE ###
df.info()


# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# Consider the following questions as you prepare to deal with outliers:
# 
# 1.   What are some ways to identify outliers?
# 2.   How do you make the decision to keep or exclude outliers from any future models?

# 1. Talking about outliers...  To help you make the decision, you can start with these general guidelines:
# Delete them: If you are sure the outliers are mistakes, typos, or errors and the dataset will be used for modeling or machine learning, then you are more likely to decide to delete outliers. Of the three choices, you’ll use this one the least. 
# Reassign them: If the dataset is small and/or the data will be used for modeling or machine learning, you are more likely to choose a path of deriving new values to replace the outlier values. 
# Leave them: For a dataset that you plan to do EDA/analysis on and nothing else, or for a dataset you are preparing for a model that is resistant to outliers, it is most likely that you are going to leave them in.
# 
# 2. It depends on every case. Firstly I need to know the outliers in this data, and then think about them.

# ### **Task 3a. Visualizations**
# 
# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the Waze dataset.
# 
# **Question:** What type of data visualization(s) will be most helpful?
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 
# 

# I think that the most helpful visualization would be: Box plot, in order to know more about distribution and outliers, and bar chart in order to compare data.

# Begin by examining the spread and distribution of important variables using box plots and histograms.

# #### **`sessions`**
# 
# _The number of occurrence of a user opening the app during the month_

# In[7]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['sessions'])
 
# show plot
plt.show()


# In[8]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['sessions'],bins=30)


# The `sessions` variable is a right-skewed distribution with half of the observations having 56 or fewer sessions. However, as indicated by the boxplot, some users have more than 700.

# #### **`drives`**
# 
# _An occurrence of driving at least 1 km during the month_

# In[9]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['drives'], showmeans=True)
 
# show plot
plt.show()


# In[10]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['drives'],bins=30)


# The `drives` information follows a distribution similar to the `sessions` variable. It is right-skewed, approximately log-normal, with a median of 48. However, some drivers had over 400 drives in the last month.

# #### **`total_sessions`**
# 
# _A model estimate of the total number of sessions since a user has onboarded_

# In[11]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['total_sessions'])
 
# show plot
plt.show()


# In[12]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['total_sessions'],bins=30)


# The `total_sessions` is a right-skewed distribution. The median total number of sessions is 159.6. This is interesting information because, if the median number of sessions in the last month was 48 and the median total sessions was ~160, then it seems that a large proportion of a user's total drives might have taken place in the last month. This is something you can examine more closely later.

# #### **`n_days_after_onboarding`**
# 
# _The number of days since a user signed up for the app_

# In[13]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['n_days_after_onboarding'])
 
# show plot
plt.show()


# In[14]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['n_days_after_onboarding'],bins=20)


# The total user tenure (i.e., number of days since
# onboarding) is a uniform distribution with values ranging from near-zero to \~3,500 (\~9.5 years).

# #### **`driven_km_drives`**
# 
# _Total kilometers driven during the month_

# In[15]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['driven_km_drives'])
 
# show plot
plt.show()


# In[16]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['driven_km_drives'],bins=30)


# The number of drives driven in the last month per user is a right-skewed distribution with half the users driving under 3,495 kilometers. As you discovered in the analysis from the previous course, the users in this dataset drive _a lot_. The longest distance driven in the month was over half the circumferene of the earth.

# #### **`duration_minutes_drives`**
# 
# _Total duration driven in minutes during the month_

# In[17]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['duration_minutes_drives'])
 
# show plot
plt.show()


# In[18]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['duration_minutes_drives'],bins=30)


# The `duration_minutes_drives` variable has a heavily skewed right tail. Half of the users drove less than \~1,478 minutes (\~25 hours), but some users clocked over 250 hours over the month.

# #### **`activity_days`**
# 
# _Number of days the user opens the app during the month_

# In[19]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['activity_days'])
 
# show plot
plt.show()


# In[20]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['activity_days'],bins=31)


# Within the last month, users opened the app a median of 16 times. The box plot reveals a centered distribution. The histogram shows a nearly uniform distribution of ~500 people opening the app on each count of days. However, there are ~250 people who didn't open the app at all and ~250 people who opened the app every day of the month.
# 
# This distribution is noteworthy because it does not mirror the `sessions` distribution, which you might think would be closely correlated with `activity_days`.

# #### **`driving_days`**
# 
# _Number of days the user drives (at least 1 km) during the month_

# In[21]:


# Box plot
### YOUR CODE HERE ###
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(x=df['driving_days'])
 
# show plot
plt.show()


# In[22]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['driving_days'],bins=31)


# The number of days users drove each month is almost uniform, and it largely correlates with the number of days they opened the app that month, except the `driving_days` distribution tails off on the right.
# 
# However, there were almost twice as many users (\~1,000 vs. \~550) who did not drive at all during the month. This might seem counterintuitive when considered together with the information from `activity_days`. That variable had \~500 users opening the app on each of most of the day counts, but there were only \~250 users who did not open the app at all during the month and ~250 users who opened the app every day. Flag this for further investigation later.

# #### **`device`**
# 
# _The type of device a user starts a session with_
# 
# This is a categorical variable, so you do not plot a box plot for it. A good plot for a binary categorical variable is a pie chart.

# In[23]:


# Pie chart
### YOUR CODE HERE ###

device_counts = df['device'].value_counts()
labels=device_counts.index.values

plt.pie(device_counts, labels=device_counts.index.values, autopct='%1.1f%%')
plt.show()


# There are nearly twice as many iPhone users as Android users represented in this data.

# #### **`label`**
# 
# _Binary target variable (“retained” vs “churned”) for if a user has churned anytime during the course of the month_
# 
# This is also a categorical variable, and as such would not be plotted as a box plot. Plot a pie chart instead.

# In[24]:


# Pie chart
### YOUR CODE HERE ###
df['label'] = df['label'].fillna('Unknown')

label_counts = df['label'].value_counts()


plt.pie(label_counts, labels=label_counts.index.values, autopct='%1.1f%%')
plt.show()


# Less than 18% of the users churned.

# #### **`driving_days` vs. `activity_days`**
# 
# Because both `driving_days` and `activity_days` represent counts of days over a month and they're also closely related, you can plot them together on a single histogram. This will help to better understand how they relate to each other without having to scroll back and forth comparing histograms in two different places.
# 
# Plot a histogram that, for each day, has a bar representing the counts of `driving_days` and `activity_days`.

# In[25]:


# Histogram
### YOUR CODE HERE ###
plt.hist([df['driving_days'],df['activity_days']],bins=31, label=['Driving Days', 'Activity Days'])
plt.legend(loc='upper right')
plt.show()


# As observed previously, this might seem counterintuitive. After all, why are there _fewer_ people who didn't use the app at all during the month and _more_ people who didn't drive at all during the month?
# 
# On the other hand, it could just be illustrative of the fact that, while these variables are related to each other, they're not the same. People probably just open the app more than they use the app to drive&mdash;perhaps to check drive times or route information, to update settings, or even just by mistake.
# 
# Nonetheless, it might be worthwile to contact the data team at Waze to get more information about this, especially because it seems that the number of days in the month is not the same between variables.
# 
# Confirm the maximum number of days for each variable&mdash;`driving_days` and `activity_days`.

# In[26]:


### YOUR CODE HERE ###
print(df['driving_days'].max())
print(df['activity_days'].max())


# It's true. Although it's possible that not a single user drove all 31 days of the month, it's highly unlikely, considering there are 15,000 people represented in the dataset.
# 
# One other way to check the validity of these variables is to plot a simple scatter plot with the x-axis representing one variable and the y-axis representing the other.

# In[27]:


# Scatter plot
### YOUR CODE HERE ###
plt.scatter(df['activity_days'],df['driving_days'])

# Labels
plt.xlabel('Activity days')  # Añade una etiqueta al eje X
plt.ylabel('Driving days')   # Añade una etiqueta al eje Y

# Title
plt.title('Relación entre Días de Actividad y Días Conduciendo')

# (Opcional) Añadir leyenda
plt.legend(['Actividad vs. Conducción'])

# Mostrar el gráfico
plt.show()


# Notice that there is a theoretical limit. If you use the app to drive, then by definition it must count as a day-use as well. In other words, you cannot have more drive-days than activity-days. None of the samples in this data violate this rule, which is good.

# #### **Retention by device**
# 
# Plot a histogram that has four bars&mdash;one for each device-label combination&mdash;to show how many iPhone users were retained/churned and how many Android users were retained/churned.

# In[28]:


# Histogram
### YOUR CODE HERE ###

df_grouped = df.groupby(['device','label'], as_index=False)['ID'].count()


# Crear un gráfico de barras
ax = sns.barplot(x='device', y='ID', hue='label', data=df_grouped)

# Añadir etiquetas y título
plt.xlabel('Device')
plt.ylabel('Number of users')
plt.title('Users Retained/Churn by Device')

leg = ax.get_legend()

# Cambiar el título de la leyenda
leg.set_title('Legend')


# Mostrar el gráfico
plt.show()


# The proportion of churned users to retained users is consistent between device types.

# #### **Retention by kilometers driven per driving day**
# 
# In the previous course, you discovered that the median distance driven last month for users who churned was 8.33 km, versus 3.36 km for people who did not churn. Examine this further.
# 
# 1. Create a new column in `df` called `km_per_driving_day`, which represents the mean distance driven per driving day for each user.
# 
# 2. Call the `describe()` method on the new column.

# In[29]:


# 1. Create `km_per_driving_day` column
### YOUR CODE HERE ###
df['km_per_driving_day']=df['driven_km_drives'] / df['driving_days']

# 2. Call `describe()` on the new column
### YOUR CODE HERE ###
df.describe()


# What do you notice? The mean value is infinity, the standard deviation is NaN, and the max value is infinity. Why do you think this is?
# 
# This is the result of there being values of zero in the `driving_days` column. Pandas imputes a value of infinity in the corresponding rows of the new column because division by zero is undefined.
# 
# 1. Convert these values from infinity to zero. You can use `np.inf` to refer to a value of infinity.
# 
# 2. Call `describe()` on the `km_per_driving_day` column to verify that it worked.

# In[30]:


# 1. Convert infinite values to zero
### YOUR CODE HERE ###
df['km_per_driving_day'] = df['km_per_driving_day'].replace([np.inf, -np.inf], 0)

# 2. Confirm that it worked
### YOUR CODE HERE ###
df['km_per_driving_day'].describe()


# The maximum value is 15,420 kilometers _per drive day_. This is physically impossible. Driving 100 km/hour for 12 hours is 1,200 km. It's unlikely many people averaged more than this each day they drove, so, for now, disregard rows where the distance in this column is greater than 1,200 km.
# 
# Plot a histogram of the new `km_per_driving_day` column, disregarding those users with values greater than 1,200 km. Each bar should be the same length and have two colors, one color representing the percent of the users in that bar that churned and the other representing the percent that were retained. This can be done by setting the `multiple` parameter of seaborn's [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html) function to `fill`.

# In[31]:


# Histogram
### YOUR CODE HERE ###
# Filtrar el DataFrame para incluir solo aquellos registros con 'km_per_driving_day' <= 1200
df_filtered = df[df['km_per_driving_day'] <= 1200]

# Crear el histograma
sns.histplot(data=df_filtered, x='km_per_driving_day', hue='label', stat='percent', multiple='fill', binwidth=100, palette=['red', 'green', 'grey'])

# Añadir etiquetas y título al gráfico
plt.xlabel('Driven Km. per Driving Day')
plt.ylabel('Percentage')
plt.title('Comparison of users retained vs. churned considering Driven Km. per day')

# Mostrar el gráfico
plt.show()


# The churn rate tends to increase as the mean daily distance driven increases, confirming what was found in the previous course. It would be worth investigating further the reasons for long-distance users to discontinue using the app.

# #### **Churn rate per number of driving days**
# 
# Create another histogram just like the previous one, only this time it should represent the churn rate for each number of driving days.

# In[32]:


# Histogram
### YOUR CODE HERE ###

# Crear el histograma
sns.histplot(data=df, x='driving_days', hue='label', stat='percent', multiple='fill', bins=31, palette=['red', 'green', 'grey'])

# Añadir etiquetas y título al gráfico
plt.xlabel('Driving Days')
plt.ylabel('Percentage of churned users')
plt.title('Comparison of users retained vs. churned per Driving day')

# Mostrar el gráfico
plt.show()


# The churn rate is highest for people who didn't use Waze much during the last month. The more times they used the app, the less likely they were to churn. While 40% of the users who didn't use the app at all last month churned, nobody who used the app 30 days churned.
# 
# This isn't surprising. If people who used the app a lot churned, it would likely indicate dissatisfaction. When people who don't use the app churn, it might be the result of dissatisfaction in the past, or it might be indicative of a lesser need for a navigational app. Maybe they moved to a city with good public transportation and don't need to drive anymore.

# #### **Proportion of sessions that occurred in the last month**
# 
# Create a new column `percent_sessions_in_last_month` that represents the percentage of each user's total sessions that were logged in their last month of use.

# In[33]:


### YOUR CODE HERE ###
df['percent_sessions_in_last_month']=(df['sessions'] / df['total_sessions'])*100

#Si el valor es mayor que 100 es que este mes se ha dado de alta, sustituimos valores mayores que 100 por 100

df['percent_sessions_in_last_month'] = np.where(df['percent_sessions_in_last_month'] > 100, 100, df['percent_sessions_in_last_month'])


# What is the median value of the new column?

# In[34]:


### YOUR CODE HERE ###
df['percent_sessions_in_last_month'].describe()


# Now, create a histogram depicting the distribution of values in this new column.

# In[35]:


# Histogram
### YOUR CODE HERE ###
plt.hist(df['percent_sessions_in_last_month'])
plt.show()


# Check the median value of the `n_days_after_onboarding` variable.

# In[36]:


### YOUR CODE HERE ###
df['n_days_after_onboarding'].describe()


# Half of the people in the dataset had 40% or more of their sessions in just the last month, yet the overall median time since onboarding is almost five years.
# 
# Make a histogram of `n_days_after_onboarding` for just the people who had 40% or more of their total sessions in the last month.

# In[37]:


# Histogram
### YOUR CODE HERE ###


# The number of days since onboarding for users with 40% or more of their total sessions occurring in just the last month is a uniform distribution. This is very strange. It's worth asking Waze why so many long-time users suddenly used the app so much in the last month.

# ### **Task 3b. Handling outliers**
# 
# The box plots from the previous section indicated that many of these variables have outliers. These outliers do not seem to be data entry errors; they are present because of the right-skewed distributions.
# 
# Depending on what you'll be doing with this data, it may be useful to impute outlying data with more reasonable values. One way of performing this imputation is to set a threshold based on a percentile of the distribution.
# 
# To practice this technique, write a function that calculates the 95th percentile of a given column, then imputes values > the 95th percentile with the value at the 95th percentile.  such as the 95th percentile of the distribution.
# 
# 

# In[38]:


### YOUR CODE HERE ###
def change_95 (row):
    ninetyfifth_percentile = np.percentile(row,95)
    
    ret = np.where(row > ninetyfifth_percentile, ninetyfifth_percentile, row)
    
    return ret


# Next, apply that function to the following columns:
# * `sessions`
# * `drives`
# * `total_sessions`
# * `driven_km_drives`
# * `duration_minutes_drives`

# In[43]:


### YOUR CODE HERE ###

df['sessions']=change_95(df['sessions'])
df['drives']=change_95(df['drives'])
df['total_sessions']=change_95(df['total_sessions'])
df['driven_km_drives']=change_95(df['driven_km_drives'])
df['duration_minutes_drives']=change_95(df['duration_minutes_drives'])


# Call `describe()` to see if your change worked.

# In[44]:


### YOUR CODE HERE ###
df.describe()


# #### **Conclusion**
# 
# Analysis revealed that the overall churn rate is \~17%, and that this rate is consistent between iPhone users and Android users.
# 
# Perhaps you feel that the more deeply you explore the data, the more questions arise. This is not uncommon! In this case, it's worth asking the Waze data team why so many users used the app so much in just the last month.
# 
# Also, EDA has revealed that users who drive very long distances on their driving days are _more_ likely to churn, but users who drive more often are _less_ likely to churn. The reason for this discrepancy is an opportunity for further investigation, and it would be something else to ask the Waze data team about.

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Execute stage.

# ### **Task 4a. Results and evaluation**
# 
# Having built visualizations in Python, what have you learned about the dataset? What other questions have your visualizations uncovered that you should pursue?
# 
# **Pro tip:** Put yourself in your client's perspective. What would they want to know?
# 
# Use the following code fields to pursue any additional EDA based on the visualizations you've already plotted. Also use the space to make sure your visualizations are clean, easily understandable, and accessible.
# 
# **Ask yourself:** Did you consider color, contrast, emphasis, and labeling?
# 
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# I have learned this month the application has been used extensively compared to the past looking at the sessions this month.
# There are lots of users who drive a lot. The more days a user drive, the highest posibilities of retaining. But, the most km. driven the most churning rate.
# 
# My other questions are how many users have been landed this month.
# 
# My client would likely want to know how the churning rate changes between new users vs. user with more than 6 months.
# 
# 
# 

# Use the following two code blocks (add more blocks if you like) to do additional EDA you feel is important based on the given scenario.

# In[46]:


### YOUR CODE HERE ###
#Filtering by n_days_after_onboarding < 30 -> New users
df_new_users = df[df['n_days_after_onboarding']<=30]
#df_new_users.head(20)

#It's expected that users with days after onboarding <= 30 to have percent_sessions_in_last_month in 100%
#We see that it's not the case, which can mean that "total_sessions" has been modeled with data we don't know.

#Let's check the churn rate among people with n_days_after_onboarding in this month
label_counts = df_new_users['label'].value_counts()

plt.pie(label_counts, labels=label_counts.index.values, autopct='%1.1f%%')
plt.show()

#We see that churn rate is 23.6% much higher that the whole dataset


# In[49]:


### YOUR CODE HERE ###
#Filtering by n_days_after_onboarding > 180 -> Old users (more than 6 months after onboarding)
df_old_users = df[df['n_days_after_onboarding'] > 180]


#Let's check the churn rate among people with n_days_after_onboarding in this month
label_counts_old = df_old_users['label'].value_counts()

plt.pie(label_counts_old, labels=label_counts_old.index.values, autopct='%1.1f%%')
plt.show()

#We see that churn rate is 16.5% similar to the whole dataSet


# In[50]:


print("Número de usuarios nuevos")
print(label_counts)

print("Número de usuarios antiguos")
print(label_counts_old)


# ### **Task 4b. Conclusion**
# 
# Now that you've explored and visualized your data, the next step is to share your findings with Harriet Hadzic, Waze's Director of Data Analysis. Consider the following questions as you prepare to write your executive summary. Think about key points you may want to share with the team, and what information is most relevant to the user churn project.
# 
# **Questions:**
# 
# 1. What types of distributions did you notice in the variables? What did this tell you about the data?
# 
# 2. Was there anything that led you to believe the data was erroneous or problematic in any way?
# 
# 3. Did your investigation give rise to further questions that you would like to explore or ask the Waze team about?
# 
# 4. What percentage of users churned and what percentage were retained?
# 
# 5. What factors correlated with user churn? How?
# 
# 6. Did newer uses have greater representation in this dataset than users with longer tenure? How do you know?
# 

# 1. What types of distributions did you notice in the variables? What did this tell you about the data?
# Todas las variables importantes tienen una gran desviación hacia la derecha. Esto indica que hay muchos usuarios que conducen muchas horas y muchos kilómetros.
# 
# 2. Was there anything that led you to believe the data was erroneous or problematic in any way?
# Sí. Hemos encontrado que hay algunos outliers que no son creíbles. Como el número de horas de conducción que no son físicamente posible.
# Además, Hemos localizado que los usuarios con "days after onboarding" menor de 30 días (que implica usuarios que se han dado de alta en el último mes) tiene "total sessions" que representa una estimación del número total de sesiones (más allá de este mes) que no cuadra, ya que total_sessions debería ser igual o muy similar a "sessions"
# 
# 3. Did your investigation give rise to further questions that you would like to explore or ask the Waze team about?
# Necesitamos saber cómo se ha obtenido el dato "total sessions" también el significado real de "n_days_after_onboarding"
# 
# 4. What percentage of users churned and what percentage were retained?
# En el total del dataset el % de churn es de 16.9% y el de retained 78.4%, siendo desconocido el 4.7%
# 
# 5. What factors correlated with user churn? How?
# Parece que los usuarios que conducen más km. al día tienen mayor incidencia de churn.
# Además, los usuarios que conducen menor número de días tienen también mayor incidencia de churn.
# 
# 6. Did newer uses have greater representation in this dataset than users with longer tenure? How do you know?
# Al principio parece que viendo el porcentaje de sesiones en el último mes comparado con el porcenta de sesiones totales, la mayoría de los usuarios han usado la aplicación este último mes.
# Mirando a través de "days after onboarding", el % de usuarios nuevos es muy pequeño, como era de esperar.
# 
# 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
