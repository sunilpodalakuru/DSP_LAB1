import numpy as np
import scipy.io.wavfile as wav
from scipy.fft import fft, ifft

# Load audio file
rate, data = wav.read('/home/rguktrkvalley/vowelssam.wav')
print(rate)
# Convert to floating-point
data = data / np.max(np.abs(data))

# Perform FFT
data_fft = fft(data)

# Estimate noise (assume noise is in the first few seconds)
noise_estimate = np.mean(np.abs(data_fft[:int(rate * 2)]))

# Spectral subtraction
cleaned_fft = np.maximum(np.abs(data_fft) - noise_estimate, 0) * np.sign(data_fft)

# Inverse FFT to get the cleaned signal
cleaned_signal = ifft(cleaned_fft).real

# Save cleaned audio
cleaned_signal= (cleaned_signal* 32767).astype(np.int16)  # Convert back to 16-bit PCM
wav.write('cleaned_audio.wav', rate, cleaned_signal)

