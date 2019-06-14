import pandas as pd
import collections

allmedals = pd.read_csv('medals-expanded.csv',
                        names=['Games','Year','Sport','Discipline',
                               'Athlete','Team','Gender','Event',
                               'Medal','Gold','Silver','Bronze'],header=1)

games = list(set(allmedals['Games']))
games.sort(key=lambda x: x.split()[-1])
with open('games.txt','w') as w:
    for game in games:
        w.write(game + '\n')

medal =  collections.namedtuple('medal',['year','athlete','team','event'])
medals = [medal(*line.strip().split('\t')) for line in open('goldmedals.txt','r')]


with open('goldmedals.txt','w') as out:
    for i,row in allmedals[(medals['Discipline'] == 'Athletics') & (medals['Gold'] == 1)].iterrows():
        out.write(str(row['Year']) + '\t' + row['Athlete'] + '\t' + row['Team'] + '\t' + row['Event'] + '\n')

