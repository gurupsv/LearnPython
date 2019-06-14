import math, json, collections, itertools
import numpy as np
import matplotlib.pyplot as pp

#from mpl_toolkits.basemap import Basemap
import geopy

medal =  collections.namedtuple('medal',['year','athlete','team','event'])
medals = [medal(*line.strip().split('\t')) for line in open('goldmedals.txt','r')]

