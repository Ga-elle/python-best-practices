#! /usr/bin/env python3
# coding: utf-8

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SetOfParliamentMembers:
  
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "SetOfParliamentMember: {} members".format(len(self.dataframe))
   
  def __len__(self):
        return self.number_of_mps()

  def __getitem__(self, index):
      try:
        result = dict(self.dataframe.iloc[index])
      except:
          if index < 0:
              raise Exception("Please select a positive index")
          elif index >= len(self.dataframe):
              raise Exception("There are only {} MPs!".format(len(self.dataframe)))
          else:
              raise Exception("Wrong index")
      return result
                                
  def __iter__(self):
    self.iterator_state = 0
    return self
  
  def __next__(self):
    if self.iterator_state >= len(self):
      raise StopIteration()
    result = self[self.iterator_state]
    self.iterator_state += 1
    return result
  
  def data_from_csv(self, csv_file):
    self.dataframe = pd.read_csv(csv_file, sep=";")
    
  def data_from_dataframe(self, dataframe):
    self.dataframe = dataframe
    
  def display_chart(self):
    data = self.dataframe
    female_mps = data[data.sexe == "F"]
    male_mps = data[data.sexe == "H"]
    
    counts = [len(female_mps), len(male_mps)]
    counts = np.array(counts)
    nb_mps = counts.sum()
    proportions = counts / nb_mps
    
    labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]
    
    fix, ax = plt.subplots()
    ax.axis("equal")
    ax.pie(
        proportions,
        labels=labels,
        autopct="1%.1f pourcents")
    plt.title("{} ({} MPs)".format(self.name, nb_mps))
    plt.show()
  
  def split_by_political_party(self):
    result = {}
    data = self.dataframe
    
    all_parties = data['parti_ratt_financier'].dropna().unique()
    
    for party in all_parties:
      data_subset = data[data.parti_ratt_financier == party]
      subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
      subset.data_from_dataframe(data_subset)
      result[party] = subset
      
    return result
    

  def number_of_mps(self):
    return len(self.dataframe)
    
    
def launch_analysis(data_file, by_party = False, info = False):
  sopm = SetOfParliamentMembers("All MPs")
  sopm.data_from_csv(os.path.join("data", data_file))
  
  if info:
    print(sopm.number_of_mps())
    
  sopm.display_chart()
  if by_party:
    for party, s in sopm.split_by_political_party().items():
      s.display_chart()
  
  for mp in sopm:
    print(mp['nom'], mp['emails'])

if __name__ == "__main__":
  launch_analysis('current_mps.csv')