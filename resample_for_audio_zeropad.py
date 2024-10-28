import librosa
import soundfile as sf

# Load the WAV file
duration=0.1
data, original_fs = librosa.load('input.wav', sr=None,duration=duration)

# Resample to the desired rate
desired_fs = 8000  # Example: resample to 16 kHz
resampled_data = librosa.resample(data, orig_sr=original_fs, target_sr=desired_fs)

# Save the resampled WAV file
sf.write('resampled_output.wav', resampled_data, desired_fs)
