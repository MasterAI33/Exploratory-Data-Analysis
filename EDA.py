#Importing Required Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#Data Cleaning and Organizing
file_path = "palmerpenguins_extended.csv"
df = pd.read_csv(file_path)
df.drop(["year"], axis=1, inplace=True)
df.drop(["diet"], axis=1, inplace=True)
df.rename(columns={"species": "Species", "island": "Island", "bill_length_mm": "Bill Length (mm)", "flipper_length_mm": "Flipper Length (mm)", "bill_depth_mm": "Bill Depth (mm)", "body_mass_g": "Body Mass (g)", "sex": "Sex", "life_state":"Age", "health_metrics": "Health", "life_stage": "Life Stage"}, inplace=True)

# print(len(df['Species']))
without = df.copy()

#filtering out other penguin types
for i in range(len(without['Species'])):
  if (without.iloc[i, 0]) != 'Adelie':
    df.drop(i, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

without = df.copy()
#filtering out male penguins
for i in range(len(without['Sex'])):
  if (without.iloc[i, 6]) != 'female':
    df.drop(i, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

without = df.copy()
# filtering out the non-juvenile penguins
for i in range(len(without['Life Stage'])):
  if (without.iloc[i, 7]) != 'juvenile':
    df.drop(i, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

df.drop(['Life Stage', 'Sex', 'Species'], axis = 1, inplace=True)
df
# df['Health'].unique()



#Visualization #1: Island and Bill Length
#Data Aggregation for Island and Bill Length
Biscoe_Bill_len = []
Torgensen_Bill_len = []
Dream_Bill_len = []

for i in range(len(df['Island'])):
  if df.iloc[i, 0] == 'Biscoe':
    Biscoe_Bill_len.append(df.iloc[i, 1])
  elif df.iloc[i,0] == 'Torgensen':
    Torgensen_Bill_len.append(df.iloc[i,1])
  else:
    Dream_Bill_len.append(df.iloc[i,1])
biscoe = sum(Biscoe_Bill_len)/len(Biscoe_Bill_len)
print(biscoe)
torgensen = sum(Torgensen_Bill_len)/len(Torgensen_Bill_len)
print(torgensen)
dream = sum(Dream_Bill_len)/len(Dream_Bill_len)
print(dream)

#Rendering the Data
bill_len = pd.DataFrame(
    {
        'Island': ['Biscoe', 'Torgensen', 'Dream'],
        'Average Bill Length (mm)': [biscoe, torgensen, dream]
    }
)
plt.figure(figsize=(8, 7))
plt.title('Average Bill Length (mm) by Island')
sns.barplot(x='Island', y='Average Bill Length (mm)', data=bill_len, palette='inferno')



#Visualization #2: Island and Bill Depth (mm)
#Data Aggregation for Island and Bill Depth
Biscoe_Bill_depth = []
Torgensen_Bill_depth = []
Dream_Bill_depth = []

for i in range(len(df['Island'])):
  if df.iloc[i, 0] == 'Biscoe':
    Biscoe_Bill_depth.append(df.iloc[i, 2])
  elif df.iloc[i,0] == 'Torgensen':
    Torgensen_Bill_depth.append(df.iloc[i,2])
  else:
    Dream_Bill_depth.append(df.iloc[i,2])
biscoe2 = sum(Biscoe_Bill_depth)/len(Biscoe_Bill_depth)
print(biscoe2)
torgensen2 = sum(Torgensen_Bill_depth)/len(Torgensen_Bill_depth)
print(torgensen2)
dream2 = sum(Dream_Bill_depth)/len(Dream_Bill_depth)
print(dream2)

#Rendering the Data
bill_depth = pd.DataFrame(
    {
        'Island': ['Biscoe', 'Torgensen', 'Dream'],
        'Average Bill Depth (mm)': [biscoe2, torgensen2, dream2]
    }
)
bill_depth
plt.figure(figsize=(8, 7))
plt.title('Average Bill Depth (mm) by Island')
sns.barplot(x='Island', y='Average Bill Depth (mm)', data=bill_depth, palette='magma')



#Visualization #3: Island and Flipper Length (mm)
#Data Aggregation for Island and Flipper Length
Biscoe_flipper_len = []
Torgensen_flipper_len = []
Dream_flipper_len = []

for i in range(len(df['Island'])):
  if df.iloc[i, 0] == 'Biscoe':
    Biscoe_flipper_len.append(df.iloc[i, 3])
  elif df.iloc[i,0] == 'Torgensen':
    Torgensen_flipper_len.append(df.iloc[i,3])
  else:
    Dream_flipper_len.append(df.iloc[i,3])
biscoe3 = sum(Biscoe_flipper_len)/len(Biscoe_flipper_len)
print(biscoe3)
torgensen3 = sum(Torgensen_flipper_len)/len(Torgensen_flipper_len)
print(torgensen3)
dream3 = sum(Dream_flipper_len)/len(Dream_flipper_len)
print(dream3)

#Rendering the Data
flipper_length = pd.DataFrame(
    {
        'Island': ['Biscoe', 'Torgensen', 'Dream'],
        'Average Flipper Length (mm)': [biscoe3, torgensen3, dream3]
    }
)
flipper_length

plt.figure(figsize=(8, 7))
plt.title('Average Flipper Length (mm) by Island')
sns.barplot(x='Island', y='Average Flipper Length (mm)', data=flipper_length, palette='cividis')



#Visualization #4: Island and Body Mass (g)
#Data Aggregation for Island and Body Mass
Biscoe_mass = []
Torgensen_mass = []
Dream_mass = []

for i in range(len(df['Island'])):
  if df.iloc[i, 0] == 'Biscoe':
    Biscoe_mass.append(df.iloc[i, 4])
  elif df.iloc[i,0] == 'Torgensen':
    Torgensen_mass.append(df.iloc[i,4])
  else:
    Dream_mass.append(df.iloc[i,4])
biscoe4 = sum(Biscoe_mass)/len(Biscoe_mass)
print(biscoe4)
torgensen4 = sum(Torgensen_mass)/len(Torgensen_mass)
print(torgensen4)
dream4 = sum(Dream_mass)/len(Dream_mass)
print(dream4)

#Rendering the Data
body_mass = pd.DataFrame(
    {
        'Island': ['Biscoe', 'Torgensen', 'Dream'],
        'Average Body Mass (g)': [biscoe4, torgensen4, dream4]
    }
)
flipper_length

plt.figure(figsize=(8, 7))
plt.title('Average Body Mass (g) by Island')
sns.barplot(x='Island', y='Average Body Mass (g)', data=body_mass, palette='viridis')



#Hypothesis Testing for Visualization #1
test_stat = biscoe - torgensen
biscoe_bill_lengths = df[df['Island'] == 'Biscoe']['Bill Length (mm)']
torgensen_bill_lengths = df[df['Island'] == 'Torgensen']['Bill Length (mm)']
biscoe_bill_lengths.reset_index(drop=True)
torgensen_bill_lengths.reset_index(drop=True)
combined_col = pd.concat([df[df['Island'] == 'Biscoe']['Bill Length (mm)'], df[df['Island'] == 'Torgensen']['Bill Length (mm)']])
combined_col.reset_index(drop=True)
biscoe_count = len(biscoe_bill_lengths)
torgensen_count = len(torgensen_bill_lengths)
# print(len(combined_col), biscoe_count, torgensen_count)

labels = np.array(['Biscoe']*biscoe_count + ['Torgensen']*torgensen_count)
histogram_data = []

n = 15000
for i in range(n):
  np.random.shuffle(labels)
  shuffled = pd.DataFrame(
      {
          'Bill_Length (mm)': combined_col.values,
          'Island': labels
      }
  )
  new_biscoe = shuffled[shuffled['Island'] == 'Biscoe']['Bill_Length (mm)']
  new_torgensen = shuffled[shuffled['Island'] == 'Torgensen']['Bill_Length (mm)']
  curr_mean = new_biscoe.mean() - new_torgensen.mean()
  histogram_data.append(curr_mean)
print(histogram_data)

plt.figure(figsize=(8, 7))
plt.xlabel('Bins of Mean Differences')
plt.ylabel('Frequency of Each Bin')
sns.histplot(histogram_data, bins=50, kde=True, color='orange', label='Differences in Mean')
plt.title('Difference in Mean between Biscoe and Torgensen Bill Lengths (mm) after Shuffling')

#Calculating p-value
significance_level = 0.05
p_value = np.sum(np.abs(histogram_data) >= np.abs(test_stat)) / n
print(p_value)

print(f"The p-value is {p_value} and is greated than the significance level cutoff which is {0.05}. Therefore, it can be concluded that we fail to reject the null hypothesis and that there is minimal effect of the island between the average bill lengths of the penguins tested.")