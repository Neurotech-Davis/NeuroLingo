# import functions from preprocessing
import sys
sys.path.insert(0, "../pre_processing/")
import pre_processing_scripts_v2 as pp

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

# set parameters here
certainty_threshold = 0.5
n_components = 8
t_min = 0.0
t_max = 0.5


pp.preprocessing(wei_eeg_file_path_csv, wei_log_path, wei_psyhcopy_file_path_csv, "JoshuaWei", consider_certainty=True, certainty_threshold=certainty_threshold, n_components=n_components, t_min=t_min, t_max=t_max)
pp.preprocessing(irby_eeg_file_path_csv, irby_log_path, irby_psyhcopy_file_path_csv, "Irby", consider_certainty=True, certainty_threshold=certainty_threshold, n_components=n_components, t_min=t_min, t_max=t_max)
pp.preprocessing(sarah_eeg_file_path_csv, sarah_log_path, sarah_psyhcopy_file_path_csv, "Sarah", consider_certainty=True, certainty_threshold=certainty_threshold, n_components=n_components, t_min=t_min, t_max=t_max)
pp.preprocessing(devin_eeg_file_path_csv, devin_log_path, devin_psyhcopy_file_path_csv, "Devin", consider_certainty=True, certainty_threshold=certainty_threshold, n_components=n_components, t_min=t_min, t_max=t_max)
pp.preprocessing(chengyi_eeg_file_path_csv, chengyi_log_path, chengyi_psyhcopy_file_path_csv, "Chengyi", consider_certainty=True, certainty_threshold=certainty_threshold, n_components=n_components, t_min=t_min, t_max=t_max)
pp.preprocessing(afnaan_eeg_file_path_csv, afnaan_log_path, afnaan_psyhcopy_file_path_csv, "Afnaan", consider_certainty=True, certainty_threshold=certainty_threshold, n_components=n_components, t_min=t_min, t_max=t_max)
pp.preprocessing(adalai_eeg_file_path_csv, adali_log_path, adali_psyhcopy_file_path_csv, "Adali", consider_certainty=True, certainty_threshold=certainty_threshold, n_components=n_components, t_min=t_min, t_max=t_max)
