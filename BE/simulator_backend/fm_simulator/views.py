import json
import matplotlib
matplotlib.use('Agg')  # Ustawienie backendu przed zaimportowaniem pyplot
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .forms import SignalForm
from .signal_processor import generate_sine_wave, fm_modulate, fm_demodulate_hilbert, simulate_rayleigh_fading
from .utils import create_plot_and_audio, normalize_signal

@csrf_exempt
@require_http_methods(["POST"])
def simulate_fm_modulation(request):
    data = json.loads(request.body)
    form = SignalForm(data)
    if form.is_valid():
        freq = form.cleaned_data.get('freq') or 280.0
        duration = form.cleaned_data.get('duration') or 3.0
        sample_rate = form.cleaned_data.get('sample_rate') or 44100
        carrier_freq = form.cleaned_data.get('carrier_freq') or 2200.0
        modulation_index = form.cleaned_data.get('modulation_index') or 3.0
        scale = form.cleaned_data.get('scale') or 0.02
        fading_floor = form.cleaned_data.get('fading_floor') or 0.5

        # Generowanie podstawowych składowych sygnału
        baseband = generate_sine_wave(freq, duration, sample_rate)
        carrier_signal = generate_sine_wave(carrier_freq, duration, sample_rate)
        modulated_signal = fm_modulate(freq, carrier_freq, modulation_index, sample_rate, duration)
        faded_modulated_signal = simulate_rayleigh_fading(modulated_signal, scale, fading_floor)
        demodulated_signal = fm_demodulate_hilbert(modulated_signal, sample_rate)
        demodulated_signal = normalize_signal(demodulated_signal)
        demodulated_signal_with_fading = fm_demodulate_hilbert(faded_modulated_signal, sample_rate) 
        demodulated_signal_with_fading = normalize_signal(demodulated_signal_with_fading)

        # Generowanie wykresu i dźwięku sygnału bazowego
        sine_image_base64, sine_wav_base64 = create_plot_and_audio(
            baseband, sample_rate, 'Sygnał modulujący', 1000)
        
        # Generowanie wykresu i dźwięku sygnału nośnego
        carrier_image_base64, carrier_wav_base64 = create_plot_and_audio(
            carrier_signal, sample_rate, 'Sygnał nośny', 1000)
        
        # Generowanie wykresu i dźwięku sygnału zmodulowanego FM
        mod_image_base64, mod_wav_base64 = create_plot_and_audio(
            modulated_signal, sample_rate, 'Sygnał zmodulowany FM', 1000)
        
        # Generowanie wykresu i dźwięku sygnału zdemodulowanego FM bez zaników
        demodulated_image_base64, demod_wav_base64 = create_plot_and_audio(
            demodulated_signal, sample_rate, 'Sygnał zdemodulowany FM bez zaników', 1000)
        
        # Generowanie wykresu i dźwięku sygnału zdemodulowanego FM z zanikami
        demodulated_with_fading_image_base64, demod_with_fading_wav_base64 = create_plot_and_audio(
            demodulated_signal_with_fading, sample_rate, 'Sygnał zdemodulowany FM z zanikami', 1000)
    
        # Tworzenie danych odpowiedzi z zmodulowanym sygnałem, jego obrazem i plikiem audio
        response_data = {
            'sine_signal_graph': sine_image_base64,
            'sine_signal_audio': sine_wav_base64,
            'carrier_signal_graph': carrier_image_base64,
            'carrier_signal_audio': carrier_wav_base64,
            'modulated_signal_graph': mod_image_base64,
            'modulated_signal_audio': mod_wav_base64,
            'demodulated_signal_graph': demodulated_image_base64,
            'demodulated_signal_audio': demod_wav_base64,
            'demodulated_signal_with_fading_graph': demodulated_with_fading_image_base64,
            'demodulated_signal_with_fading_audio': demod_with_fading_wav_base64
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'Errors': form.errors}, status=400)
