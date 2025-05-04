# library stuff
# Install
#!pip install mne
#!pip install pandas
#!pip install numpy

# Importing libraries
import mne
import pandas as pd
import numpy as np
from mne import Epochs, pick_types
from mne.preprocessing import ICA
from mne.io import concatenate_raws, read_raw_edf
from mne.datasets import eegbci
from mne.channels import make_standard_montage
from mne.decoding import UnsupervisedSpatialFilter
from mne.viz import plot_topomap
from datetime import datetime, timezone, timedelta
import pytz
from mne.decoding import UnsupervisedSpatialFilter
from sklearn.decomposition import PCA

def preprocessing(path_EEG_CSV, path_PsychoPy_log, path_PsychoPy_CSV, participantName, consider_certainty, certainty_threshold, n_components, t_min, t_max):
	
	# Helper functions to convert from UNIX time to UTC time
	# UNIX time is saved as an integer (seconds since 1/1/1970)
	# UTC time is saved as a string ("YYYY-MM-DDTHH:MM:SSZ")
	def unix_to_utc(unix_timestamp):
		utc_time = datetime.fromtimestamp(unix_timestamp, timezone.utc)
		local_timezone = pytz.timezone('America/Los_Angeles')
		local_time = utc_time.astimezone(local_timezone) # This gives our UTC time converted to PST
		return utc_time # This gives our raw UTC time
	def utc_to_unix(utc_time_str):
		utc_time = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%SZ")
		utc_time = utc_time.replace(tzinfo=timezone.utc)
		unix_timestamp = int(utc_time.timestamp())
		return unix_timestamp
	
	# Function to load the data. Simply enter a file path
	def load_eeg_data(file_path):

		# Create a dataframe from our data, replace NAs with 0s
		df = pd.read_csv(file_path, sep='\t', skiprows=2, header=None)
		df.fillna(0.0, inplace=True)

		# Extract EEG data
		trial_data = df.iloc[:, 1:24].values

		# Declares channel names and types of each set of data
		sfreq = 255  # sample rate in Hz
		ch_names = ['Channel {}'.format(i+1) for i in range(trial_data.shape[1])]
		ch_types = ['eeg' for i in range(trial_data.shape[1])]

		# Get the measurement date
		start_time_unix = trial_data[0][21] # This is where EEG start time is stored in UNIX time
		meas_date = unix_to_utc(start_time_unix) # However, MNE takes UTC time

		# Create info structures and RawArray objects for each set of data
		info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
		info.set_meas_date(meas_date)
		raw = mne.io.RawArray(trial_data.T, info)

		# Removing irrelevant channels
		ch_names = [raw.ch_names]
		ch_names_to_keep = [ch_names[0][0:8]]
		raw = raw.pick(ch_names_to_keep[0])

		# Return the RawArray object
		return raw
	
	# Feature extraction helper
	# def extract_features(raw):
	# 	data = raw.get_data()  # shape: (n_channels, n_times)
	# 	data = data[np.newaxis, ...]  # shape becomes (1, n_channels, n_times)
	# 	mean = np.mean(data, axis=2)
	# 	std = np.std(data, axis=2)
	# 	max_val = np.max(data, axis=2)
	# 	min_val = np.min(data, axis=2)
	# 	features = np.concatenate((mean, std, max_val, min_val), axis=2).flatten()
	# 	print("FEAUTRES HERE", features)
	# 	return features
	
	# Helper function, converts PsychoPy's timestamp into UNIX
	def psychopy_to_unix(psychopy_time):
		
		# Define the format of the input timestamp
		format_string = "%Y-%m-%d %Hh%M.%S.%f %z"

		# Parse the custom timestamp into a datetime object
		parsed_timestamp = datetime.strptime(psychopy_time, format_string)

		# Convert the datetime object to a Unix timestamp (floating-point for microseconds)
		unix_timestamp = parsed_timestamp.timestamp()

		# Print the Unix timestamp
		return unix_timestamp

	# Function to load psychopy data. Simply input the file path
	def load_psychopy_data(file_path):

		# Read psychopy data into a pandas dataframe
		psychopy_df = pd.read_csv(file_path, delimiter=',', skiprows=0, header=0)
		
		#create a new column for the unix time of psychopy stimuli
		psychopy_df = psychopy_df.dropna(subset=["expStart"])
		psychopy_df["expStart"] = psychopy_df["expStart"].astype(str)
		psychopy_df["unix_time"] = psychopy_df["expStart"].apply(psychopy_to_unix)
		
		return psychopy_df
	
	# Function to load log data
	def load_log_data(file_path):
		log_df = pd.read_csv(file_path, sep="\t", header=None, encoding="utf-8")
		log_df = log_df.rename(columns={0: "time", 1: "type", 2: "action"}) # Renames columns for easier access
		return log_df
	
	action_practice_training = ["practice_amharicc: autoDraw = True",
							"amharic_practice2: autoDraw = True"]
	action_practice_testing = ["textAmharic_9: autoDraw = True"]
	action_correctness = ["textCheck: text = '✓'", 
						"textXmark: text = '✗'"]
	action_training = ["amharics1: autoDraw = True", 
						"amharics1_2: autoDraw = True", 
						"amharics2: autoDraw = True", 
						"amharics2_2: autoDraw = True", 
						"amharics3: autoDraw = True", 
						"amharics3_2: autoDraw = True", 
						"amharics4: autoDraw = True", 
						"amharics4_2"]
	action_testing = ["textAmharic_5: autoDraw = True", 
					"textAmharic_6: autoDraw = True", 
					"textAmharic_7: autoDraw = True", 
					"textAmharic_8: autoDraw = True"]
	action_english = ["textOptionA_5: autoDraw = True",
					"textOptionB_5: autoDraw = True",
					"textOptionC_5: autoDraw = True",
					"textOptionD_5: autoDraw = True",
					"textOptionA_6: autoDraw = True",
					"textOptionB_6: autoDraw = True",
					"textOptionC_6: autoDraw = True",
					"textOptionD_6: autoDraw = True",
					"textOptionA_7: autoDraw = True",
					"textOptionB_7: autoDraw = True",
					"textOptionC_7: autoDraw = True",
					"textOptionD_7: autoDraw = True",
					"textOptionA_8: autoDraw = True",
					"textOptionB_8: autoDraw = True",
					"textOptionC_8: autoDraw = True",
					"textOptionD_8: autoDraw = True"]
	action_keypress = ["Keypress: left",
					"Keypress: right",
					"Keypress: up",
					"Keypress: down",
					"Keypress: space"]
	action_diamond = ["textDiamond_8: autoDraw = True", 
					"textDiamond_3: autoDraw = True", 
					"textDiamond_5: autoDraw = True",
					"textDiamond_6: autoDraw = True",
					"textDiamond_7: autoDraw = True",]

	raw = load_eeg_data(path_EEG_CSV)
	psychopy_df = load_psychopy_data(path_PsychoPy_CSV)
	log_df = load_log_data(path_PsychoPy_log)

	filtered_actions = action_testing + action_correctness
	pattern = "|".join(filtered_actions)
	sub_df = log_df[log_df["action"].str.contains(pattern, na=False, regex=True)]
	sub_df.index = range(len(sub_df)) # Renaming row indices for easier iteration

	filtered_certainty = action_keypress + action_diamond + action_practice_testing + action_testing + action_correctness
	certainty_pattern = "|".join(filtered_certainty)
	certainty_df = log_df[log_df["action"].str.contains(certainty_pattern, na=False, regex=True)]
	certainty_df.index = range(len(certainty_df)) # Renaming row indices for easier iteration

	certainty_timestamps = []
	for index in range(len(certainty_df)): # Certainty timestamps
		if ("textAmharic" in certainty_df["action"][index]): 
			certainty = float(certainty_df["time"][index+2] - certainty_df["time"][index+1])
			if certainty < certainty_threshold:
				timestamp, correctness = float(certainty_df["time"][index]), certainty_df["action"][index+3][-2]
				certainty_timestamps.append((timestamp, correctness))
		
	def extract_rows(df, check_symbol, pattern):
		"""
		Extract rows where the 'action' contains 'textAmharic' and the next row's 'action'
		contains the specified check symbol.
		
		Parameters:
			df (pd.DataFrame): The DataFrame containing the data.
			check_symbol (str): The symbol to look for in the next row's action.
			
		Returns:
			learned_list (list): List of rows (as pd.Series) that meet the criteria.
		"""
		list = []
		check_symbol_exists = (check_symbol != "")
		
		# Loop through all rows
		for i in range(len(df)):
			current_action = df.iloc[i]["action"]
			if (check_symbol_exists) and (i < len(df) - 1):
				next_action = df.iloc[i + 1]["action"]
				if str(pattern) in current_action and check_symbol in next_action:
					list.append(df.iloc[i]["time"])
			else:
				if str(pattern) in current_action:
					list.append(df.iloc[i]["time"])
		return list


	learned_list = extract_rows(sub_df, check_symbol="✓", pattern="textAmharic")
	not_learned_list = extract_rows(sub_df, check_symbol="✗", pattern="textAmharic")

	# lists are a bunch of np.float64, convert these all to standard floats
	def np_float_to_float(np_float64_list):
		new_list = []

		for i in range(0,len(np_float64_list)):
			new_list.append(float(np_float64_list[i]))
		
		return new_list


	# now we have lists of just the times
	learned_list_times = np_float_to_float(learned_list)
	not_learned_list_times = np_float_to_float(not_learned_list)
	certainty_list_times = []
	for timestamp, correctness in certainty_timestamps:
		if (correctness == "✓"): 
			certainty_list_times.append(timestamp)

	duration = t_max - t_min
	if (consider_certainty):
		length = len(certainty_list_times) + len(not_learned_list_times) 
		not_learned_tags = ["not_learned"] * len(not_learned_list_times)
		certainty_tags = ["certainly_learned"] * len(certainty_list_times)
		final_onsets = certainty_list_times + not_learned_list_times
		final_description = certainty_tags + not_learned_tags
	else:
		length = len(learned_list_times) + len(not_learned_list_times)
		not_learned_tags = ["not_learned"] * len(not_learned_list_times)
		learned_tags = ["learned"] * len(learned_list_times)
		final_onsets = learned_list_times + not_learned_list_times
		final_description = learned_tags + not_learned_tags
	duration_list = [duration] * length

	buffer = psychopy_df.loc[0, 'unix_time'] - utc_to_unix(raw.info['meas_date'].strftime("%Y-%m-%dT%H:%M:%SZ"))
	new_orig_time = (raw.info['meas_date'] + timedelta(seconds=buffer)).strftime("%Y-%m-%d %H:%M:%S.%f")

	later_annot = mne.Annotations(
		onset = final_onsets,
		duration = duration_list,
		description = final_description,
		orig_time=new_orig_time,
	)

	raw = raw.copy().set_annotations(later_annot)
	#raw.compute_psd(fmin=0,fmax=50).plot()
	f_low = 0.1
	f_high = 30
	data_cleaned = raw.filter(f_low, f_high, fir_design="firwin", skip_by_annotation="edge")   
	#low and high pass filter, fir_design can be changed to match what lit review did

	#notch filter for electrical noise
	data_cleaned.notch_filter(60)
	picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude="bads")  

	ica = ICA(n_components=n_components, random_state=97, method="fastica")

	ica.fit(raw)   
	#raw cleaned has been through filtering
	#clean will have gone through ica

	data_cleaned = ica.apply(raw)

	# Extract events from annotations
	events, event_id = mne.events_from_annotations(data_cleaned)

	# Define the epoch time window (start and end in seconds relative to event onset)
	tmin, tmax = t_min, t_max  # for example, 200ms before and 500ms after each event, original: -0.2, 1

	#mne expects event ID to be ints and not strings, so we need to change our annotations via dictionary

	# Create epochs
	if (consider_certainty):
		event_epochs = mne.Epochs(
			data_cleaned,                # Variable that contains our data
			events,                      # Events we want to investigate, remember we changed T1 and T2 to this
			event_id={"certainly_learned": 1, "not_learned": 2},
			tmin=tmin,                   # Start time relative to event, creating a buffer of how many seconds around event we want
			tmax=tmax,                   # End time relative to event
			proj=True,                   # Re-references data after everything we've done so far
			picks=picks,                 # Only use channels specified in 'picks' (AKA EEG)
			baseline=None,               # No baseline correction
			preload=True                 # Load the epochs into memory for faster access
		)
		

		# make different epochs for each label
		certainly_learned_event_epochs = mne.Epochs(
			data_cleaned,                # Variable that contains our data
			events,                      # Events we want to investigate, remember we changed T1 and T2 to this
			event_id={"certainly_learned": 1},
			tmin=tmin,                   # Start time relative to event, creating a buffer of how many seconds around event we want
			tmax=tmax,                   # End time relative to event
			proj=True,                   # Re-references data after everything we've done so far
			picks=picks,                 # Only use channels specified in 'picks' (AKA EEG)
			baseline=None,               # No baseline correction
			preload=True                 # Load the epochs into memory for faster access
		)

		not_learned_event_epochs = mne.Epochs(
			data_cleaned,                # Variable that contains our data
			events,                      # Events we want to investigate, remember we changed T1 and T2 to this
			event_id={"not_learned": 2},
			tmin=tmin,                   # Start time relative to event, creating a buffer of how many seconds around event we want
			tmax=tmax,                   # End time relative to event
			proj=True,                   # Re-references data after everything we've done so far
			picks=picks,                 # Only use channels specified in 'picks' (AKA EEG)
			baseline=None,               # No baseline correction
			preload=True                 # Load the epochs into memory for faster access
		)
	else: 
		event_epochs = mne.Epochs(
			data_cleaned,                # Variable that contains our data
			events,                      # Events we want to investigate, remember we changed T1 and T2 to this
			event_id={"learned": 1, "not_learned": 2},
			tmin=tmin,                   # Start time relative to event, creating a buffer of how many seconds around event we want
			tmax=tmax,                   # End time relative to event
			proj=True,                   # Re-references data after everything we've done so far
			picks=picks,                 # Only use channels specified in 'picks' (AKA EEG)
			baseline=None,               # No baseline correction
			preload=True                 # Load the epochs into memory for faster access
		)
		

		# make different epochs for each label
		learned_event_epochs = mne.Epochs(
			data_cleaned,                # Variable that contains our data
			events,                      # Events we want to investigate, remember we changed T1 and T2 to this
			event_id={"learned": 1},
			tmin=tmin,                   # Start time relative to event, creating a buffer of how many seconds around event we want
			tmax=tmax,                   # End time relative to event
			proj=True,                   # Re-references data after everything we've done so far
			picks=picks,                 # Only use channels specified in 'picks' (AKA EEG)
			baseline=None,               # No baseline correction
			preload=True                 # Load the epochs into memory for faster access
		)

		not_learned_event_epochs = mne.Epochs(
			data_cleaned,                # Variable that contains our data
			events,                      # Events we want to investigate, remember we changed T1 and T2 to this
			event_id={"not_learned": 2},
			tmin=tmin,                   # Start time relative to event, creating a buffer of how many seconds around event we want
			tmax=tmax,                   # End time relative to event
			proj=True,                   # Re-references data after everything we've done so far
			picks=picks,                 # Only use channels specified in 'picks' (AKA EEG)
			baseline=None,               # No baseline correction
			preload=True                 # Load the epochs into memory for faster access
		)


	# Step 1: Get epoch data
	X_epochs = event_epochs.get_data()
	#print(f"Original shape: {X_epochs.shape}")  # Shape: (epochs, channels, times) times is the amount of samples. 

	# repeat for the other epochs
	if (consider_certainty):
		certainly_learned_epochs = certainly_learned_event_epochs.get_data()
		#print(f"Original shape: {certainly_learned_epochs.shape}")
	else:
		learned_epochs = learned_event_epochs.get_data()
		#print(f"Original shape: {learned_epochs.shape}")


	not_learned_epochs = not_learned_event_epochs.get_data()
	#(f"Original shape: {not_learned_epochs.shape}")

	# Step 2: Apply PCA
	pca_mne = UnsupervisedSpatialFilter(PCA(n_components=n_components), average=False)
	X_pca = pca_mne.fit_transform(X_epochs)
	#print(f"After PCA shape: {X_pca.shape}")  # Shape: (epochs, components, times)

	# repeat
	if (consider_certainty):
		certainly_learned_pca = pca_mne.fit_transform(certainly_learned_epochs)
	
		#print(f"After PCA shape: {certainly_learned_pca.shape}")
	else:
		learned_pca = pca_mne.fit_transform(learned_epochs)
		#print(f"After PCA shape: {learned_pca.shape}")

	not_learned_pca = pca_mne.fit_transform(not_learned_epochs)
	#print(f"After PCA shape: {not_learned_pca.shape}")
	# Step 3: Reshape data for machine learning
	X_flat = X_pca.reshape(X_pca.shape[0], -1)  # Shape: (epochs, components * times)
	#print(f"Flattened shape: {X_flat.shape}")
	#print(X_flat)

	if (consider_certainty):
		certainly_learned_flat = certainly_learned_pca.reshape(certainly_learned_pca.shape[0], -1)  # Shape: (epochs, components * times)
		#print(f"Flattened shape: {certainly_learned_flat.shape}")
		#print(certainly_learned_flat)
	else:
		learned_flat = learned_pca.reshape(learned_pca.shape[0], -1)  # Shape: (epochs, components * times)
		#print(f"Flattened shape: {learned_flat.shape}")
		#print(learned_flat)

	not_learned_flat = not_learned_pca.reshape(not_learned_pca.shape[0], -1)  # Shape: (epochs, components * times)
	#print(f"Flattened shape: {not_learned_flat.shape}")
	#print(not_learned_flat)

	# return the data
	return certainly_learned_flat, not_learned_flat


# Store our EEG data path in a variable

# Aaron's relative file paths

# Josh Irby
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

# Chengyi's files
# eeg_file_path_csv = 'C:/Users/cheng/OneDrive/Desktop/Data Collection (OpenBCI & PsychoPy)-20250404T031700Z-001/Data Collection (OpenBCI & PsychoPy)/EEG/3_13_2025_JoshuaWei_OpenBCI/OpenBCISession_2025-03-13_19-40-36/BrainFlow-RAW_2025-03-13_19-40-36_0.csv'
# psyhcopy_file_path_csv = 'C:/Users/cheng/OneDrive/Desktop/Data Collection (OpenBCI & PsychoPy)-20250404T031700Z-001/Data Collection (OpenBCI & PsychoPy)\PsychoPy/3_13_2025_JoshuaWei_PsychoPy/42069_finaltest_2025-03-13_20h02.28.660.csv'
# log_path = 'C:/Users/cheng/OneDrive/Desktop/Data Collection (OpenBCI & PsychoPy)-20250404T031700Z-001/Data Collection (OpenBCI & PsychoPy)/PsychoPy/3_13_2025_JoshuaWei_PsychoPy/42069_finaltest_2025-03-13_20h02.28.660.log'

#Combine CSV files into one function

import glob
import os

def combine_csv_into_one(directory_path):
    
    pattern = os.path.join(directory_path, "clean*.csv")
    csv_files = glob.glob(pattern)

    all_dfs = []
    for file in csv_files:
        df = pd.read_csv(file, header = None)
        all_dfs.append(df)

    combined_df = pd.concat(all_dfs, ignore_index=True)
    return combined_df

def combiner():
    learned_path = "../clean_learned_EEG"
    not_learned_path = "../clean_not_learned_EEG"

    learned_df = combine_csv_into_one(learned_path)
    not_learned_df = combine_csv_into_one(not_learned_path)

    learned_output_path = os.path.join(learned_path, "combined_learned.csv")
    learned_df.to_csv(learned_output_path, index=False)

    not_learned_output_path = os.path.join(not_learned_path, "combined_not_learned.csv")
    not_learned_df.to_csv(not_learned_output_path, index=False)

def test_print():
	print("import works!")