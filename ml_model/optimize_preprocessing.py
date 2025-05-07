# import functions from preprocessing
import sys
sys.path.insert(0, "../pre_processing/")

# standard libraries
import numpy as np

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

def preprocess_combos():
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

    # learned_data, not_learned_data = pp.preprocessing(eeg_paths[i], log_paths[i], psychopy_paths[i], names[i], consider_certainty=True, certainty_threshold, n_components, t_min, t_max)

    # master lists which are lists of lists
    master_learned = []
    master_not_learned = []

    # for each parameter
    for setting in setting_list[:2]:   # trying just two for now
        param_list_learned = []        # these will store the preprocessed data
        param_list_not_learned = []
        
        for i in range(0, 1):  # change to len(names) later
            # decompose setting into parts that can be passed into preprocessing function
            ct, comp, mini, maxi = setting
            learned, not_learned = pp.preprocessing(eeg_paths[i], log_paths[i], psychopy_paths[i], names[i], 
                                                    consider_certainty=True, certainty_threshold=ct, 
                                                    n_components=comp, t_min=mini, t_max=maxi)
            
            param_list_learned.append(learned)
            param_list_not_learned.append(not_learned)

        master_learned.append(param_list_learned)
        master_not_learned.append(param_list_not_learned)

    print("Master learned: ", master_learned)
    print("Master learned shape: ", len(master_learned))

preprocess_combos()