# import functions from preprocessing
import sys
sys.path.insert(0, "../pre_processing/")

# standard libraries
import numpy as np
import pandas as pd

# model libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from scipy.stats import randint
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


# Optimizing
# from tpot import TPOTClassifier
from sklearn import tree


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
    certainty_thresholds = np.linspace(0.25, 1.0, 10)
    n_components_list = np.arange(3,9)
    t_mins = np.linspace(0.0, 0.2, 5)
    t_maxs = np.linspace(0.3, 1.0, 5)

    # apply combinations to each name    
    settings = product(certainty_thresholds, n_components_list, t_mins, t_maxs)
    setting_list = list(settings)

    #endregion

    # need a master list to store the output of each combination on the participants
    master_learned = []
    master_not_learned = []

    # for each parameter
    for setting in setting_list[:2]:   # trying just two for now

        # need to process one participant first to get num_cols, then might as well add it to param_list
        ct, comp, mini, maxi = setting
        learned, not_learned = pp.preprocessing(eeg_paths[0], log_paths[0], psychopy_paths[0], names[0], 
                                                    consider_certainty=True, certainty_threshold=ct, 
                                                    n_components=comp, t_min=mini, t_max=maxi)
        
        num_cols = learned.shape[1]

        # empty storage for the data
        param_list_learned = np.empty((0, num_cols))        
        param_list_not_learned = np.empty((0, num_cols))

        # adding the first participant to the data
        param_list_learned = np.vstack((param_list_learned, learned))
        param_list_not_learned = np.vstack((param_list_not_learned, not_learned))
        
        for i in range(1, 2):  # SKIP the first one bc it's already been processed
            # decompose setting into parts that can be passed into preprocessing function
            learned, not_learned = pp.preprocessing(eeg_paths[i], log_paths[i], psychopy_paths[i], names[i], 
                                                    consider_certainty=True, certainty_threshold=ct, 
                                                    n_components=comp, t_min=mini, t_max=maxi)
            
            # add processed data
            param_list_learned = np.vstack((param_list_learned, learned))
            param_list_not_learned = np.vstack((param_list_not_learned, not_learned))

        # now param_list is filled with the preprocessed data of each participant
        # we need to store this in a master list
        master_learned.append(param_list_learned)
        master_not_learned.append(param_list_not_learned)
    
    # tests
    print("len master_learned should be 2: ", len(master_learned))
    print("len master_not_learned should be 2: ", len(master_not_learned))

    print("shape of the first object in master learned", master_learned[0].shape)
    print("shape of the first object in master_not_learned", master_not_learned[0].shape)

    print("shape of the second object in master_learned", master_learned[1].shape)
    print("shape of the second object in master_not_learned", master_not_learned[1].shape)

    return master_learned, master_not_learned, setting_list
    

# helper function for data splitting
def split_data(learned_data, not_learned_data, scalar=True):
    
    # convert data into dataframes
    learned_data = pd.DataFrame(learned_data)
    not_learned_data = pd.DataFrame(not_learned_data)

    # checking how much data for each category
    print(f"original learned shape: {learned_data.shape}")
    print(f"original not_learned shape: {not_learned_data.shape}")

    # make them equal to remove bias
    learned_data = learned_data.sample(frac=1, random_state=42).reset_index(drop=True)
    not_learned_data = not_learned_data.sample(frac=1, random_state=42).reset_index(drop=True)

    # get length 
    learned_length = learned_data.shape[0]
    not_learned_length = not_learned_data.shape[0]

    new_learned_data = learned_data.drop(index=range(not_learned_length, learned_length))
    new_not_learned_data = not_learned_data.drop(index=range(learned_length, not_learned_length))

    # print results
    print(f"new learned shape: {new_learned_data.shape}")
    print(f"new not_learned shape: {not_learned_data.shape}")
    
    X_learned = new_learned_data
    X_not_learned = new_not_learned_data

    # make the label vector y
    '''
    to indicate which epochs go to which condition
    y vector label should be as long as x matrix is long

    zeros = learned
    ones = not learned
    '''
    y_learned = np.zeros(X_learned.shape[0])
    y_not_learned = np.ones(X_not_learned.shape[0])

    # combine the data and labels
    # learned + not learned 
    # learned labels + not learned labels
    X = np.concatenate([X_learned, X_not_learned], axis=0)
    y = np.concatenate([y_learned, y_not_learned], axis=0)

    # scaling
    if(scalar):   
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = X

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

    return X_train, X_test, y_train, y_test


## mini functions for testing each model
# each one should take the training data as input and output a list of the model used, accuracy, cm, and preprocessing paramaters
def test_ml(X_train, X_test, y_train, y_test, model_type):
    # empty results list
    results = []
    random = 42

    if(model_type == 'svm_rbf'):
        model = SVC(kernel='rbf', random_state=random)

    elif(model_type == 'svm_linear'):
        model = SVC(kernel='linear', random_state=random)

    elif(model_type == 'svm_poly'):
        model = SVC(kernel='poly', random_state=random)

    elif(model_type == 'kNN'):
        model = KNeighborsClassifier(n_neighbors=11)

    elif(model_type == 'RandomForest'):
        model = RandomForestClassifier(random_state=random)

    # TODO: add neural net

    # train the data using fit
    model.fit(X_train, y_train)

    # make predictions based on the testing data from before
    y_pred = model.predict(X_test)

    # evauluate the performance of the SVM model by caclulating confusino matrix
    # and the accuracy score
    cm = confusion_matrix(y_test, y_pred)
    results.append(cm)
    svm_accuracy = accuracy_score(y_test, y_pred)
    results.append(svm_accuracy)

    return results
    

# now repeat the process with ML models
def ml_optimization(master_learned, master_not_learned, setting_list):
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
        X_train, X_test, y_train, y_test = split_data(master_learned[i], master_not_learned[i], scalar=True)

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

    print("results list length", len(results_list))
    print("results list object one: ", results_list[0])
    print("results list object two: ", results_list[1])

    return 0

def main():
    # pre process data on a bunch of combos
    master_learned, master_not_learned, setting_list = preprocess_combos()

    # give that data to the ml_optimizer to try differnet models on each one
    optimized_list = ml_optimization(master_learned, master_not_learned, setting_list)

    # sort the optimized list by accuracy

    

if __name__ == "__main__":
    main()
