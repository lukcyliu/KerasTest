import tensorflow as tf
import matplotlib as plt
import numpy as np
import time
import csv
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense,Activation,Dropout
from keras.layers.recurrent import LSTM
np.random.seed(2017)

def get_data(path_to_dataset='bick_rnn.csv',sequence_length=20):
    max_values = 45949
    with open(path_to_dataset) as f:
        data = csv.reader(f,delimiter = ",")
        bike = []
        nb_of_values = 0
        for line in data:
            try:
                bike.append(float(line[0]))
                nb_of_values += 1
            except ValueError:
                pass
            if nb_of_values >= max_values:
                break

              
