import numpy as np
import mne

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

# --- Convert Annotations to Events ---
# This converts annotations into an events array and an event_id dictionary.
# For example, event_id might look like: {'L': 1, 'NL': 2}
events, event_id = mne.events_from_annotations(raw)

# Display the events and event mapping
print("Events:")
print(events)
print("\nEvent IDs:")
print(event_id)
