import os

# automatically grab your total logical CPU count
n_cores = os.cpu_count()  # e.g. 8

os.environ["LOKY_MAX_CPU_COUNT"] = str(n_cores)

# import functions from preprocessing
import sys
sys.path.insert(0, "../pre_processing/")

# standard libraries
import numpy as np
import pandas as pd
import csv

# model libraries
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

# our own preprocessing script
import pre_processing_scripts_v2 as pp
from itertools import product

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


# GOAL:
# Make a function in which you can try a wide variety of parameters for BOTH preprocessing the data AND the model
# save a list of the accuracies, confusion matrices, and parameters used for the preporcessing and model


# this gets us the preprocessed data on each combination
def preprocess_combos():
    """
    input: none
    output: a list where each item in the list is the result of all the participants data on some particular parameter

    summary:
    create a combination of preprocessing parameters like n_components, min time, max time, response time, etc. 
    and preprocesses each participant with each combination
    """
    #region setup of variables and lists
    # make lists of paths
    eeg_paths = [irby_eeg_file_path_csv, sarah_eeg_file_path_csv, devin_eeg_file_path_csv, chengyi_eeg_file_path_csv, afnaan_eeg_file_path_csv, wei_eeg_file_path_csv, adalai_eeg_file_path_csv]
    psychopy_paths = [irby_psyhcopy_file_path_csv, sarah_psyhcopy_file_path_csv, devin_psyhcopy_file_path_csv, chengyi_psyhcopy_file_path_csv, afnaan_psyhcopy_file_path_csv, wei_psyhcopy_file_path_csv, adali_psyhcopy_file_path_csv]
    log_paths = [irby_log_path, sarah_log_path, devin_log_path, chengyi_log_path, afnaan_log_path, wei_log_path, adali_log_path]
    names = ["Irby", "Sarah", "Devin", "Chengyi", "Afnaan", "Wei", "Adali"]

    # a range of parameters to run the preprocessing with
    certainty_thresholds = np.linspace(0.25, 1.0, 5)
    n_components_list = np.arange(3,9)
    t_mins = np.linspace(0.0, 0.2, 5)
    t_maxs = np.linspace(0.3, 1.0, 5)

    # apply combinations to each name    
    settings = product(certainty_thresholds, n_components_list, t_mins, t_maxs)
    setting_list = list(settings)

    print("setting_list length: ", len(setting_list))

    #endregion

    # need a master list to store the output of each combination on the participants
    master_learned = []
    master_not_learned = []
    counter = 0

    # for each parameter
    for setting in setting_list[:2]:
        counter += 1
        print(f"Starting setting #{counter}")
        ct, comp, mini, maxi = setting

        # process first participant to get num_cols
        learned0, not_learned0 = pp.preprocessing(
            eeg_paths[0], log_paths[0], psychopy_paths[0], names[0],
            consider_certainty=True,
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
            eeg_paths[1:], log_paths[1:], psychopy_paths[1:], names[1:]
        ):
            learned_i, not_learned_i = pp.preprocessing(
                eeg_p, log_p, psycho_p, name,
                consider_certainty=True,
                certainty_threshold=ct,
                n_components=comp,
                t_min=mini,
                t_max=maxi
            )
            learned_chunks.append(learned_i)
            not_learned_chunks.append(not_learned_i)

        # now stack once per setting
        param_list_learned     = np.vstack(learned_chunks)
        param_list_not_learned = np.vstack(not_learned_chunks)

        master_learned.append(param_list_learned)
        master_not_learned.append(param_list_not_learned)
    
    # tests
    # print("len master_learned should be 2: ", len(master_learned))
    # print("len master_not_learned should be 2: ", len(master_not_learned))

    # print("shape of the first object in master learned", master_learned[0].shape)
    # print("shape of the first object in master_not_learned", master_not_learned[0].shape)

    # print("shape of the second object in master_learned", master_learned[1].shape)
    # print("shape of the second object in master_not_learned", master_not_learned[1].shape)

    return master_learned, master_not_learned, setting_list
    

# helper function for data splitting
def split_data(learned_data, not_learned_data, scalar=True, test_size=0.2, random_state=42):
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

    # 5. Scale if requested
    if scalar:
        scaler = StandardScaler()
        X = scaler.fit_transform(X_df)
    else:
        X = X_df.values

    # 6. Stratified train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test

## mini functions for testing each model
# each one should take the training data as input and output a list of the model used, accuracy, cm, and preprocessing paramaters
def test_ml(X_train, X_test, y_train, y_test, model_type):
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

    
    results = []

    factory = MODEL_FACTORIES[model_type]
    model   = factory()
    model.fit(X_train, y_train)
    y_pred  = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    results.append(cm)
    accuracy = accuracy_score(y_test, y_pred)
    results.append(accuracy)  
    results.append(model_type)

    return results
    

# now repeat the process with ML models
def ml_optimization(master_learned, master_not_learned, setting_list, scalar_status):
    # save hyperparameter tuning for later, this function should just try different models
    # with different preprocessing strategies

    # at this point the ith item in master_learned, master_not_learned corresponds to the ith setting

    # create ultimate_list, which should be a list where each item is:
    # - a list containing accuracy score, cm, preprocessing settings, model used
    results_list = []

    # for each piece of data need run model on it
    n = len(master_learned)
    for i in range(n):

        # split data, note this has been coded to test_size = 0.2, can change it by going into split_data function
        X_train, X_test, y_train, y_test = split_data(master_learned[i], master_not_learned[i], scalar=scalar_status, test_size=0.2)

        # test SVM linear
        svm_linear_results = test_ml(X_train, X_test, y_train, y_test, 'svm_linear')
        svm_linear_results.append(setting_list[i])
        results_list.append(svm_linear_results)

        # test SVM poly
        svm_poly_results = test_ml(X_train, X_test, y_train, y_test, 'svm_poly')
        svm_poly_results.append(setting_list[i])
        results_list.append(svm_poly_results)

        # test SVM rbf
        svm_rbf_results = test_ml(X_train, X_test, y_train, y_test, 'svm_rbf')
        svm_rbf_results.append(setting_list[i])
        results_list.append(svm_rbf_results)

        # test knn
        kNN_results = test_ml(X_train, X_test, y_train, y_test, 'kNN')
        kNN_results.append(setting_list[i])
        results_list.append(kNN_results)

        # test Random Forest
        rf_results = test_ml(X_train, X_test, y_train, y_test, 'RandomForest')
        rf_results.append(setting_list[i])
        results_list.append(rf_results)

        # test LDA
        LDA_results = test_ml(X_train, X_test, y_train, y_test, 'LDA')
        LDA_results.append(setting_list[i])
        results_list.append(LDA_results)

        # test NerualNet
        NeuralNet_results = test_ml(X_train, X_test, y_train, y_test, 'NeuralNet')
        NeuralNet_results.append(setting_list[i])
        results_list.append(NeuralNet_results)

    # print("results list length", len(results_list))
    # print("results list object one: ", results_list[0])
    # print("results list object two: ", results_list[1])

    return results_list

def print_list_list(list_list, n):
    for sublist in list_list[:n]:
        print(sublist)

def to_csv(list_list, title):

    filename = title
    with open(filename,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list_list)
        


def main():
    # pre process data on a bunch of combos
    master_learned, master_not_learned, setting_list = preprocess_combos()

    # give that data to the ml_optimizer to try differnet models on each one
    scalar_optimized_list = ml_optimization(master_learned, master_not_learned, setting_list, scalar_status=True)
    non_scalar_optimized_list = ml_optimization(master_learned, master_not_learned, setting_list, scalar_status=False)


    # sort the optimized list by accuracy
    scalar_optimized_list.sort(key=lambda sublist: -sublist[1])
    non_scalar_optimized_list.sort(key=lambda sublist: -sublist[1])

    # prints the top 5 most accurate results
    print_list_list(scalar_optimized_list, 5)
    to_csv(scalar_optimized_list, 'scalar_optimized_list.csv')
    print_list_list(non_scalar_optimized_list, 5)
    to_csv(non_scalar_optimized_list, 'non_scalar_optimized_list.csv')


if __name__ == "__main__":
    main()

