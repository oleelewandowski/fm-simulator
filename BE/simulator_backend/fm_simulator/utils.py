import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from scipy.io.wavfile import write

def create_plot_and_audio(signal, sample_rate, title, num_samples=1000):
    """
    Tworzy wykres i audio dla danego sygnału.

    :param signal: Sygnał do wygenerowania wykresu i audio.
    :param sample_rate: Częstotliwość próbkowania używana dla sygnału.
    :param title: Tytuł wykresu.
    :param num_samples: Liczba próbek do uwzględnienia na wykresie.
    :return: Ciągi zakodowane w Base64 dla obrazu wykresu i audio WAV.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(signal[:num_samples])  # Rysuje tylko pierwsze num_samples dla przejrzystości
    plt.title(title)
    plt.xlabel('Próbki')
    plt.ylabel('Amplituda')
    plt.grid(True)
    
    # Zapisuje wykres do obrazu PNG
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    # Kodowanie obrazu PNG do ciągu base64
    image_base64 = base64.b64encode(image_png).decode('utf-8')
    
    # Generowanie zawartości pliku WAV
    wav_output = BytesIO()
    scaled_signal = np.int16(signal / np.max(np.abs(signal)) * 32767)
    write(wav_output, sample_rate, scaled_signal)
    wav_output.seek(0)
    wav_file_content = wav_output.read()
    wav_output.close()
    
    # Kodowanie pliku WAV do ciągu base64
    wav_base64 = base64.b64encode(wav_file_content).decode('utf-8')
    
    return image_base64, wav_base64

def normalize_signal(signal):
    """
    Normalizuje sygnał do zakresu od -1 do 1.

    :param signal: Wejściowy sygnał (tablica numpy).
    :return: Znormalizowany sygnał jako tablica numpy.
    """
    # Znajdowanie maksymalnej wartości bezwzględnej w sygnale
    max_val = np.max(np.abs(signal))
    
    # Unikanie dzielenia przez zero, jeśli sygnał jest całkowicie cichy
    if max_val == 0:
        return signal
    
    # Normalizacja sygnału
    normalized_signal = signal / max_val
    
    return normalized_signal
