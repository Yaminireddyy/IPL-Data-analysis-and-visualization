#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


balldf=pd.read_csv("IPL Ball-by-Ball 2008-2020.csv")
matchesdf=pd.read_csv("IPL Matches 2008-2020.csv")


# In[3]:


balldf.head(1)


# In[4]:


matchesdf.head(1)


# In[5]:


date=matchesdf["date"]
year=[]
for i in date:
    year.append(i[:4])
matchesdf["year"]=year 


# In[6]:


b_m_df=balldf.merge(matchesdf,on="id")
b_m_df.head(1)


# ### 1. Count of matches played in each season

# In[ ]:





# In[7]:


m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20=0,0,0,0,0,0,0,0,0,0,0,0,0
for i in matchesdf["year"]:
    if i=="2008":
        m8+=1
    elif i=="2009":
        m9+=1
    elif i=="2010":
        m10+=1
    elif i=="2011":
        m11+=1
    elif i=="2012":
        m12+=1
    elif i=="2013":
        m13+=1
    elif i=="2014":
        m14+=1
    elif i=="2015":
        m15+=1
    elif i=="2016":
        m16+=1
    elif i=="2017":
        m17+=1
    elif i=="2018":
        m18+=1
    elif i=="2019":
        m19+=1
    else:
        m20+=1


print("Matches played in Season-1  :",m8,"\nMatches played in Season-2  :",m9,
      "\nMatches played in Season-3  :",m10,"\nMatches played in Season-4  :",m11,
      "\nMatches played in Season-5  :",m12,"\nMatches played in Season-6  :",m13,
      "\nMatches played in Season-7  :",m14,"\nMatches played in Season-8 :",m15,
      "\nMatches played in Season-9 :",m16,"\nMatches played in Season-10 :",m17,
      "\nMatches played in Season-11 :",m18,"\nMatches played in Season-12 :",m19,
      "\nMatches played in Season-13 :",m20)
        



# #### Graph visualization

# In[8]:


y=np.array([m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20])
x=np.array(["1","2","3","4","5","6","7","8","9","10","11","12","13"])
plt.bar(x,y,color="black")
plt.xlabel("Seasons")
plt.ylabel("Num of matches")
plt.title("Count of matches played in each season")
plt.show()


# In[ ]:





# ### 2. Number of runs scored in each season 

# In[9]:


seasons={'2008':0,'2009':0,'2010':0,'2011':0,'2012':0,'2013':0,'2014':0,'2015':0,'2016':0,'2017':0,'2018':0,'2019':0,'2020':0}
for i in b_m_df.values:
    seasons[i[-1]]+=i[9]
print(seasons)
    
    


# #### Graphical visualization

# In[10]:


x=list(seasons.keys())
y=list(seasons.values())
plt.figure(figsize=(8,4))
plt.plot(x,y)
plt.xlabel("Seasons")
plt.ylabel("Num of Runs")
plt.title("Runs scored in each season")
plt.show()


# ### 3.What were the runs scored per match in diff seasons
# 

# In[11]:


for i in seasons.keys():
    


# ### 4.Who has Umpired the most

# In[12]:


umpires={}
umpires_lst1=(list(matchesdf['umpire1'].unique()))
umpires_lst2=(list(matchesdf['umpire2'].unique()))
umpires_lst=umpires_lst1+umpires_lst2
for i in umpires_lst:
    if i not in umpires:
        umpires[i]=0

for i in umpires.keys():
    c=0
    for j in matchesdf['umpire1']:
        if i==j:
            c+=1
    for k in matchesdf['umpire2']:
        if i==k:
            c+=1
    umpires[i]=c
    


# In[13]:


data=list(umpires.items())
matches_and_umpires=pd.DataFrame(data,columns=["ump","no_of_matches"])
#matches_and_umpires
matches_and_umpires=matches_and_umpires.sort_values(by="no_of_matches",ascending=False)
print(matches_and_umpires.iloc[:1])


# ### 5.Which team has won the most tosses

# In[14]:


teams=list(b_m_df["toss_winner"].unique())
teams_tosses={}
for i in teams:
    teams_tosses[i]=0
for i in matchesdf["toss_winner"]:
    teams_tosses[i]+=1


# ### Graphical representation

# In[15]:


x=teams_tosses.keys()
y=teams_tosses.values()
plt.figure(figsize=(30,5))
plt.bar(x,y,width=0.5,color="green")
plt.show()


# ### 6.What does the team decide after winning the toss

# In[16]:


tossdec=list(matchesdf['toss_decision'].unique())
toss_dec={}
for i in tossdec:
    toss_dec[i]=0
for j in matchesdf["toss_decision"]:
    toss_dec[j]+=1
print(toss_dec)


# In[17]:


x=toss_dec.keys()
y=toss_dec.values()
label=["field","bat"]
plt.pie(y,labels=label)
plt.show()


# In[ ]:






# ### Does winning the toss imply winning the game

# In[18]:


total_no_of_matches=m8+m9+m10+m11+m12+m13+m14+m15+m16+m17+m18+m19+m20
c=0
for i in matchesdf.values:
    if i[8]==i[10]:
        c+=1
res=(c/total_no_of_matches)*100
if res>80:
    print("YES ! Winning the toss imply winning the game")
else:
    print("NO ! Winning the toss doesn't imply winning the game")


# ### how many times has the chasing team won the match

# In[19]:


c_field=0
for i in matchesdf.values:
    if i[9]=="field":
        if i[8]==i[10]:
            c_field+=1
    else:
        if i[8]!=i[10]:
            c_field+=1
print("Chasing team has Won ",c_field," Matches out of ",total_no_of_matches)
            


# ### which all teams had won this  the tournment

# In[20]:


teams_won=list(matchesdf['winner'].unique())
teams_won


# ### Which team has won the most number of matches

# In[21]:


teams_matches={}
for i in teams:
    teams_matches[i]=0
#print(teams_matches)
for i in matchesdf["winner"]:
    if i in teams:
        teams_matches[i]+=1


# ### Graphical visualization

# In[22]:


x=teams_matches.keys()
y=teams_matches.values()
plt.figure(figsize=(30,5))
plt.bar(x,y,width=0.5,color="yellow")
plt.show()


# ### Which team has the highest winning percentage

# In[45]:


teams_matches_won={}
for i in teams:
    teams_matches_won[i]=[0,0,0.0]
# total num of matches played by each team
for j in matchesdf["team1"]:
    teams_matches_won[j][0]+=1
for k in matchesdf["team2"]:
    teams_matches_won[k][0]+=1
# total num of matches won by each team
for x in matchesdf["winner"]:
    if x in teams:
        teams_matches_won[x][1]+=1
#calculating team winning percentage
for y in teams:
    teams_matches_won[y][2]=(teams_matches_won[y][1]/teams_matches_won[y][0])*100


# In[46]:


games_played=[]
games_won=[]
winning_perc=[]
for i in teams:
    games_played.append(teams_matches_won[i][0])
    games_won.append(teams_matches_won[i][1])
    winning_perc.append(teams_matches_won[i][2])
data=pd.DataFrame(teams)
data["games_played"]=games_played
data["games_won"]=games_won
data["winning_perc"]=winning_perc
data=data.sort_values(by='winning_perc',ascending=False)
print(data.iloc[0:1])


# ### Which stadium has hosted most no of matches

# In[66]:


venues=list(matchesdf["venue"].unique())
venue_matches={}
for i in venues:
    venue_matches[i]=0
for j in matchesdf["venue"]:
    venue_matches[j]+=1
data=pd.DataFrame(venue_matches.values())
data["venues"]=venue_matches.keys()
data.drop([0],axis=1)
data["matches"]=venue_matches.values()
data=data.sort_values(by="matches",ascending=False)
data


# In[ ]:





# In[ ]:




