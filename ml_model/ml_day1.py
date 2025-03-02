import numpy as np
import mne
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score


np.random.seed(69)

# --- Create Fake Continuous EEG Data ---
# Parameters for the fake data
sfreq = 100.0        # Sampling frequency in Hz
n_channels = 8       # Number of EEG channels
n_seconds = 60       # Total duration in seconds
n_samples = int(sfreq * n_seconds)

# Generate random data (n_channels x n_samples)
data = np.random.randn(n_channels, n_samples)

# Create channel names and types
ch_names = [f'EEG{i+1}' for i in range(n_channels)]
ch_types = ['eeg'] * n_channels

# Create an MNE Info object (metadata for the channels)
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)

# Create a RawArray object with the fake data
raw = mne.io.RawArray(data, info)

# # Get the raw EEG data (shape: n_channels x n_samples)
# eeg_data = raw.get_data()

# # Transpose so that each row is a sample and each column is a channel
# df = pd.DataFrame(eeg_data.T, columns=ch_names)

# # Save to CSV
# df.to_csv("eeg_data.csv", index=False)


# ------- MAKING THE FAKE DATA --------
onsets_L = np.random.uniform(0, n_seconds, 100)
onsets_NL = np.random.uniform(0, n_seconds, 100)

durations_L = np.ones(100)
durations_NL = np.ones(100)

onsets = np.concatenate([onsets_L, onsets_NL])
durations = np.concatenate([durations_L, durations_NL])
descriptions = np.array(['L'] * 100 + ['NL'] * 100)

# Create the Annotations object
annotations = mne.Annotations(onset=onsets, duration=durations, description=descriptions)

# Attach the annotations to the raw data
raw.set_annotations(annotations)

# annotations_df = pd.DataFrame({
#     'onset': raw.annotations.onset,
#     'duration': raw.annotations.duration,
#     'description': raw.annotations.description
# })
# annotations_df.to_csv("annotations.csv", index=False)


# --- Convert Annotations to Events ---
events, event_id = mne.events_from_annotations(raw)
#{'L': 1, 'NL': 2}

# ------- Getting Epochs (-0.2 to 0.5) From Annotations -------
epochs = mne.Epochs(raw, events, event_id=event_id, tmin= -0.2, tmax= 0.5, 
                    baseline=(None, 0), preload=True, event_repeated= "drop")

# ------ Data is 3D -> list in list in list -> changed to 2D -> list in list --------

X = epochs.get_data()
# inner most = the data points over the duration of epoch, len (71)
# middle = the amount of channels in my data, len(8)
# outer most = the amount of working epochs I have, len(192)

X_flat = X.reshape(len(X), -1)
#outer list = number of epochs, len (192)
#inner list = num channels X number of samples, len(8 * 71 = 568)

#------ Change L and NL to 1 and 0 respectively -----
y_binary = (epochs.events[:, -1] == 1).astype(int)  
#{'L': 1, 'NL': 0} -> booleans

#Model 1 -> Cross Validation
svm_classifier = SVC(kernel='linear', C = 1.0)
cv_scores = cross_val_score(svm_classifier, X_flat, y_binary, cv=5)
print("Cross-validated accuracy (%):", np.mean(cv_scores) * 100)

#Model 2 -> Specific Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X_flat, y_binary, test_size=0.2)
svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
print("Train/Test accuracy (%):", accuracy_score(y_test, y_pred) * 100)
