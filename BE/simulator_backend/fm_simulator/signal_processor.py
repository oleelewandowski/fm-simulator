import numpy as np
from scipy.signal import hilbert

def generate_sine_wave(freq, duration, sample_rate):
    """
    Generuje sygnał w postaci fali sinusoidalnej.
    
    :param freq: Częstotliwość fali sinusoidalnej w Hz.
    :param duration: Czas trwania sygnału w sekundach.
    :param sample_rate: Liczba próbek na sekundę.
    :return: Fala sinusoidalna jako tablica numpy.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def fm_modulate(modulating_freq, carrier_freq, modulation_index, sample_rate, duration):
    """
    Moduluje sygnał bazowy przy użyciu modulacji częstotliwości (FM).

    :param modulating_freq: Częstotliwość sygnału modulującego w Hz.
    :param carrier_freq: Częstotliwość sygnału nośnego w Hz.
    :param modulation_index: Indeks modulacji, reprezentujący czułość modulacji.
    :param sample_rate: Liczba próbek na sekundę (częstotliwość próbkowania).
    :param duration: Czas trwania generowanego sygnału FM w sekundach.
    :return: Sygnał zmodulowany częstotliwościowo jako tablica numpy.
    """
    # Tworzenie tablicy czasu dla określonego czasu trwania
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Generowanie sygnału FM
    modulated_wave = np.sin(2 * np.pi * carrier_freq * t + 
                            modulation_index * np.sin(2 * np.pi * modulating_freq * t))
    
    # Normalizacja zmodulowanego sygnału do zakresu [-1, 1]
    modulated_wave /= np.max(np.abs(modulated_wave))
    
    return modulated_wave

def fm_demodulate_hilbert(fm_signal, sample_rate):
    """
    Demoduluje sygnał FM za pomocą transformacji Hilberta.

    :param fm_signal: Wejściowy sygnał FM (tablica numpy).
    :param sample_rate: Liczba próbek na sekundę (częstotliwość próbkowania).
    :return: Zdemodulowany sygnał jako tablica numpy.
    """
    # Tworzenie sygnału analitycznego z rzeczywistego sygnału FM
    analytic_signal = hilbert(fm_signal)
    
    # Obliczanie natychmiastowej fazy sygnału analitycznego
    instantaneous_phase = np.unwrap(np.angle(analytic_signal))
    
    # Różniczkowanie natychmiastowej fazy, aby uzyskać natychmiastową częstotliwość
    instantaneous_frequency = np.diff(instantaneous_phase) / (2.0 * np.pi) * sample_rate
    
    # Interpolacja ostatniej wartości
    if len(instantaneous_frequency) > 1:
        last_value = 2 * instantaneous_frequency[-1] - instantaneous_frequency[-2]
    else:
        last_value = instantaneous_frequency[-1]
    demodulated_signal = np.append(instantaneous_frequency, last_value)

    return demodulated_signal

def simulate_rayleigh_fading(fm_signal, scale, fading_floor):
    """
    Symuluje zanik Rayleigha na zmodulowanym sygnale FM, z możliwością regulacji skali i minimalnego poziomu zaniku.

    :param fm_signal: Zmodulowany sygnał FM (tablica numpy).
    :param scale: Skala rozkładu Rayleigha, wpływająca na zmienność zaników.
    :param fading_floor: Minimalny poziom sygnału po zaniku, zapobiegający całkowitej utracie sygnału.
    :return: Sygnał FM z zastosowanym zanikiem Rayleigha.
    """
    # Generowanie sekwencji losowej o rozkładzie Rayleigha
    fading_samples = np.random.rayleigh(scale, size=len(fm_signal))
    
    # Zapewnienie, że zanik nigdy nie powoduje całkowitej utraty sygnału
    fading_samples = fading_samples * (1 - fading_floor) + fading_floor

    # Stosowanie sekwencji zaniku do sygnału FM
    faded_fm_signal = fm_signal * fading_samples
    
    return faded_fm_signal

