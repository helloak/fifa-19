#libraries used
import numpy as np #data manipulation
import pandas as pd #data manipulation
import matplotlib.pyplot as plt #data visualisation
import seaborn as sns #data visualisation
import pycountry #for maps
import geopandas as gpd #for maps
import datetime


#display conditions
pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',100)

from math import pi
from IPython.display import display, HTML #for display in Jupyter

df_fifa = pd.read_csv('data.csv')

#analysing the data
df_fifa.head()
df_fifa.info()
df_fifa.describe()
df_fifa.shape
df_fifa.nunique()
df_fifa.columns

chosen_columns = [
    'Name',
    'Age',
    'Nationality',
    'Overall',
    'Potential',
    'Special',
    'Acceleration',
    'Aggression',
    'Agility',
    'Balance',
    'BallControl',
    'Body Type',
    'Composure',
    'Crossing',
    'Curve',
    'Club',
    'Dribbling',
    'FKAccuracy',
    'Finishing',
    'GKDiving',
    'GKHandling',
    'GKKicking',
    'GKPositioning',
    'GKReflexes',
    'HeadingAccuracy',
    'Interceptions',
    'International Reputation',
    'Jersey Number',
    'Jumping',
    'Joined',
    'LongPassing',
    'LongShots',
    'Marking',
    'Penalties',
    'Position',
    'Positioning',
    'Preferred Foot',
    'Reactions',
    'ShortPassing',
    'ShotPower',
    'Skill Moves',
    'SlidingTackle',
    'SprintSpeed',
    'Stamina',
    'StandingTackle',
    'Strength',
    'Value',
    'Vision',
    'Volleys',
    'Wage',
    'Weak Foot',
    'Work Rate'
]

df = pd.DataFrame(df_fifa, columns = chosen_columns)
df.sample(5)
plt.rcParams['figure.figsize']=(25,16)
hm=sns.heatmap(df[['Age', 'Overall', 'Potential', 'Value', 'Wage',
                'Acceleration', 'Aggression', 'Agility', 'Balance', 'BallControl',
                'Body Type','Composure', 'Crossing','Dribbling', 'FKAccuracy', 'Finishing',
                'HeadingAccuracy', 'Interceptions','International Reputation',
                'Joined', 'Jumping', 'LongPassing', 'LongShots',
                'Marking', 'Penalties', 'Position', 'Positioning',
                'ShortPassing', 'ShotPower', 'Skill Moves', 'SlidingTackle',
                'SprintSpeed', 'Stamina', 'StandingTackle', 'Strength', 'Vision',
                'Volleys']].corr(), annot = True, linewidths=.5, cmap='Blues')
hm.set_title(label='Heatmap of dataset', fontsize=30)
hm;

plt.show()
