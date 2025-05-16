##############################################################
# faster optimization using grid search and cross validation #
##############################################################

#region libraries
import numpy as np
import pandas as pd
import csv

import sys
sys.path.insert(0, "../pre_processing/")

import preprocessing_for_ml as pp

from sklearn.model_selection import ParameterGrid, cross_val_score, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from scipy.stats import randint
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.utils import shuffle

#endregion

def get_raw():
    #region paths
    # set paths
    irby_eeg_file_path_csv = '../../../Neurotech 24-25/EEG_data_new/EEG-20250317T232255Z-001/EEG/3_9_2025_JoshIrby_OpenBCI/OpenBCISession_2025-03-09_14-39-02/BrainFlow-RAW_2025-03-09_14-39-02_0.csv'
    irby_psyhcopy_file_path_csv = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_9_2025_JoshIrby_PsychoPy/6_finaltest_2025-03-09_14h42.58.498.csv'
    irby_log_path = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_9_2025_JoshIrby_PsychoPy/6_finaltest_2025-03-09_14h42.58.498.log'

    # Sarah
    sarah_eeg_file_path_csv = '../../../Neurotech 24-25/EEG_data_new/EEG-20250317T232255Z-001/EEG/3_9_2025_Sarah_OpenBCI/OpenBCISession_2025-03-09_13-24-49/BrainFlow-RAW_2025-03-09_13-24-49_0.csv'
    sarah_psyhcopy_file_path_csv ='../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_9_2025_Sarah_PsychoPy/138512_finaltest_2025-03-09_13h31.15.766.csv'
    sarah_log_path = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_9_2025_Sarah_PsychoPy/138512_finaltest_2025-03-09_13h31.15.766.log'

    # Devin
    devin_eeg_file_path_csv = '../../../Neurotech 24-25/EEG_data_new/EEG-20250317T232255Z-001/EEG/3_11_2025_Devin_OpenBCI/OpenBCISession_2025-03-11_17-07-21/BrainFlow-RAW_2025-03-11_17-07-21_1.csv'
    devin_psyhcopy_file_path_csv = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_11_2025_Devin_PsychoPy/devin_finaltest_2025-03-11_17h30.44.028.csv'
    devin_log_path = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_11_2025_Devin_PsychoPy/devin_finaltest_2025-03-11_17h30.44.028.log'

    # Chengyi
    chengyi_eeg_file_path_csv = '../../../Neurotech 24-25/EEG_data_new/EEG-20250317T232255Z-001/EEG/3_12_2025_Chengyi_OpenBCI/OpenBCISession_2025-03-12_17-07-49/BrainFlow-RAW_2025-03-12_17-07-49_1.csv'
    chengyi_psyhcopy_file_path_csv = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_12_2025_Chengyi_PsychoPy/69_finaltest_2025-03-12_17h33.18.370.csv'
    chengyi_log_path = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_12_2025_Chengyi_PsychoPy/69_finaltest_2025-03-12_17h33.18.370.log'

    # Afnaan
    afnaan_eeg_file_path_csv = '../../../Neurotech 24-25/EEG_data_new/EEG-20250317T232255Z-001/EEG/3_13_2025_Afnaan_OpenBCI/OpenBCISession_2025-03-13_22-03-16/BrainFlow-RAW_2025-03-13_22-03-16_0.csv'
    afnaan_psyhcopy_file_path_csv = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_13_2025_Afnaan_PsychoPy/69000_finaltest_2025-03-13_22h43.00.897.csv'
    afnaan_log_path = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_13_2025_Afnaan_PsychoPy/69000_finaltest_2025-03-13_22h43.00.897.log'

    # Joshua Wei
    wei_eeg_file_path_csv = '../../../Neurotech 24-25/EEG_data_new/EEG-20250317T232255Z-001/EEG/3_13_2025_JoshuaWei_OpenBCI/OpenBCISession_2025-03-13_19-40-36/BrainFlow-RAW_2025-03-13_19-40-36_0.csv'
    wei_psyhcopy_file_path_csv = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_13_2025_JoshuaWei_PsychoPy/42069_finaltest_2025-03-13_20h02.28.660.csv'
    wei_log_path = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/3_13_2025_JoshuaWei_PsychoPy/42069_finaltest_2025-03-13_20h02.28.660.log'

    # Adali
    adalai_eeg_file_path_csv = '../../../Neurotech 24-25/EEG_data_new/EEG-20250317T232255Z-001/EEG/4_13_2025_Adalai_OpenBCI/OpenBCISession_2025-04-13_19-18-26/BrainFlow-RAW_2025-04-13_19-18-26_0.csv'
    adali_psyhcopy_file_path_csv = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/4_13_2025_Adalai_PsychoPy/3333_finaltest_2025-04-13_19h36.14.933.csv'
    adali_log_path = '../../../Neurotech 24-25/psychoPy_data_new/PsychoPy-20250317T232226Z-001/PsychoPy/4_13_2025_Adalai_PsychoPy/3333_finaltest_2025-04-13_19h36.14.933.log'

    #endregion
    
    eeg_paths = [irby_eeg_file_path_csv, sarah_eeg_file_path_csv, devin_eeg_file_path_csv, chengyi_eeg_file_path_csv, afnaan_eeg_file_path_csv, wei_eeg_file_path_csv, adalai_eeg_file_path_csv]
    psychopy_paths = [irby_psyhcopy_file_path_csv, sarah_psyhcopy_file_path_csv, devin_psyhcopy_file_path_csv, chengyi_psyhcopy_file_path_csv, afnaan_psyhcopy_file_path_csv, wei_psyhcopy_file_path_csv, adali_psyhcopy_file_path_csv]
    log_paths = [irby_log_path, sarah_log_path, devin_log_path, chengyi_log_path, afnaan_log_path, wei_log_path, adali_log_path]
    names = ["Irby", "Sarah", "Devin", "Chengyi", "Afnaan", "Wei", "Adali"]

    # just use these to load in the appropriate files from each person
    # - use the functions in the preprocessing function in the preprocessing scripts
    # return a list of raw data
    # need to make it so that each particpants data is its own thing

    eeg_data = []
    psychopy_data = []
    log_data = []

    for name in range(len(names)):
        eeg_data.append(pp.load_eeg_data(eeg_paths[name]))
        psychopy_data.append(pp.load_psychopy_data(psychopy_paths[name]))
        log_data.append(pp.load_log_data(log_paths[name]))

    # each item in these lists is now a single participants raw data for the appropriate file

    return eeg_data, psychopy_data, log_data, names

def split_data(learned_data, not_learned_data):
    random_state = 42

    # 1. DataFrame conversion
    learned_df     = pd.DataFrame(learned_data)
    not_learned_df = pd.DataFrame(not_learned_data)

    # 2. Undersample the majority class to match minority size
    n = min(len(learned_df), len(not_learned_df))
    learned_trimmed     = learned_df.sample(n=n, random_state=random_state)
    not_learned_trimmed = not_learned_df.sample(n=n, random_state=random_state)

    # 3. Concatenate and create labels
    X_df = pd.concat([learned_trimmed, not_learned_trimmed], axis=0)
    y    = np.concatenate([np.zeros(n), np.ones(n)])

    # 4. Shuffle in unison
    X_df, y = shuffle(X_df, y, random_state=random_state)

    # 5. Scale
    scaler = StandardScaler()
    X = scaler.fit_transform(X_df)

    return X, y


def preprocess(raw_eeg_list, psychopy_data, log_data, names, setting):
    """
    input: raw eeg, psychopy, log data, list of names, and a preprocessing setting
    output: X, y
    """

    # define the paramters from the setting
    ct = setting['certainty_thresholds']
    comp = setting['n_components']
    mini = setting['t_mins']
    maxi = setting['t_maxs']
    certainty = setting['consider_certainty']

    # process first participant to get num_cols
    learned0, not_learned0 = pp.preprocessing(
        raw_eeg_list[0], log_data[0], psychopy_data[0], names[0],
        consider_certainty=certainty,
        certainty_threshold=ct,
        n_components=comp,
        t_min=mini,
        t_max=maxi
    )

    # collect each participant’s data in lists
    learned_chunks     = [learned0]
    not_learned_chunks = [not_learned0]

    # process the rest
    for eeg_p, log_p, psycho_p, name in zip(
        raw_eeg_list[1:], log_data[1:], psychopy_data[1:], names[1:]
    ):
        learned_i, not_learned_i = pp.preprocessing(
            eeg_p, log_p, psycho_p, name,
            consider_certainty=certainty,
            certainty_threshold=ct,
            n_components=comp,
            t_min=mini,
            t_max=maxi
        )
        learned_chunks.append(learned_i)
        not_learned_chunks.append(not_learned_i)

    # now stack once per setting
    learned     = np.vstack(learned_chunks)
    not_learned = np.vstack(not_learned_chunks)

    # now split this into X and y to give to ml models
    X, y = split_data(learned, not_learned)

    return X, y

# preprocess now returns an X and y to do a split on for EACH setting
# preprocess(ParameterGrid(preprocess_grid)[0])

def optimization(raw_eeg_data, psychopy_data, log_data, names):
    # grid is as it sounds, creates grid of combinations, basically same thing as nested for loops
    # TODO: make this a grid search with scikit learn
    # TODO: make a pipeline to make stuff easier to scale
    # BUT this code can run as of now, the steps above likely won't improve run time by much but are just valuable skills to learn

    preprocess_grid = {   # creates hundreds of combinations
        'certainty_thresholds' : np.linspace(0.25, 1.0, 5),
        'n_components' : np.arange(3,9),
        't_mins' : np.linspace(0.0, 0.2, 3),
        't_maxs' : np.linspace(0.3, 1.0, 5),
        'consider_certainty': [True, False]
    }

    MODEL_FACTORIES = {
    'svm_rbf':      lambda: SVC(kernel='rbf', random_state=42, cache_size=200),
    'svm_linear':   lambda: SVC(kernel='linear', random_state=42, cache_size=200),
    'svm_poly':     lambda: SVC(kernel='poly', random_state=42, cache_size=200),
    'kNN':          lambda: KNeighborsClassifier(n_neighbors=11, n_jobs=-1),
    'RandomForest': lambda: RandomForestClassifier(random_state=42, n_jobs=-1),
    'LDA':          LinearDiscriminantAnalysis,
    'NeuralNet':    lambda: MLPClassifier(
                          hidden_layer_sizes=(64,32),
                          activation='relu',
                          solver='adam',
                          max_iter=500,
                          random_state=42
                      ),
    }

    model_list = ['svm_rbf', 'svm_linear', 'svm_poly', 'kNN', 'RandomForest', 'LDA', 'NeuralNet']

    # main list to store everything and be sorted later
    main_list = []

    count = 0
    # for each setting run it through preprocessing to get the X and Y
    for setting in ParameterGrid(preprocess_grid):
        count += 1
        print("count is: ", count)

        # just X and y, cross val score will handle the rest
        X, y = preprocess(raw_eeg_data, psychopy_data, log_data, names, setting)

        # note: seems to be skipping the svm models
        for model in model_list:
            # sublist of parameters and model and accuracy
            sub_list = []
            sub_list.append(setting)

            factory = MODEL_FACTORIES[model]
            estimator = factory()
            # print("model: ", estimator)
            # cv is how many folds/times the model runs on the data, we want the mean of it
            scores = cross_val_score(estimator, X, y, scoring='accuracy', cv=5, n_jobs=-1)
            y_pred = cross_val_predict(estimator, X, y, cv = 5, n_jobs=-1)
            cm = confusion_matrix(y, y_pred)
            mean_accuracy = scores.mean()
            sub_list.append(model)            # add model to sublist
            sub_list.append(mean_accuracy)    # add the mean accuracy
            sub_list.append(cm)               # add the confusion matrix
            main_list.append(sub_list)        # add this SUBLIST to the main list
        
    return main_list

def to_csv(mylist, title):

    filename = title
    with open(filename,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(mylist)

def main():
    raw_eeg_data, psychopy_data, log_data, names = get_raw() # do this in main so that we only read in the data ONCE

    results_list = optimization(raw_eeg_data, psychopy_data, log_data, names)
    results_list.sort(key=lambda sublist: -sublist[2])
    to_csv(results_list, 'optimized_list.csv')

if __name__ == "__main__":
    main()
