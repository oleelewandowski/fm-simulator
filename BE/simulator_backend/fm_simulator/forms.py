from django import forms

class SignalForm(forms.Form):
    freq = forms.FloatField(min_value=0.1, max_value=2000.0, required=False, initial=280.0, help_text="Częstotliwość sygnału bazowego w Hz")
    duration = forms.FloatField(min_value=0.1, max_value=10.0, required=False, initial=3.0, help_text="Czas trwania sygnału w sekundach")
    sample_rate = forms.IntegerField(min_value=1, max_value=176000.4, required=False, initial=44100, help_text="Częstotliwość próbkowania w próbkach/sekundę")
    carrier_freq = forms.FloatField(min_value=0.1, max_value=20000.0, required=False, initial=2200.0, help_text="Częstotliwość nośna w Hz")
    modulation_index = forms.FloatField(min_value=0.0, max_value=50.0, required=False, initial=3.0, help_text="Indeks modulacji dla FM")
    scale = forms.FloatField(min_value=0.0, max_value=1.0, required=False, initial=0.02, help_text="Skala rozkładu Rayleigha, wpływająca na zmienność zaników")
    fading_floor = forms.FloatField(min_value=0.0, max_value=1.0, required=False, initial=0.5, help_text="Minimalny poziom sygnału po zaniku, zapobiegający całkowitej utracie sygnału")

    def clean(self):
        # Wykorzystanie super do dodania logiki metody clean klasy nadrzędnej
        cleaned_data = super().clean()
        # Ustawienie wartości domyślnych, jeśli pola są puste
        cleaned_data.setdefault('freq', self.fields['freq'].initial)
        cleaned_data.setdefault('duration', self.fields['duration'].initial)
        cleaned_data.setdefault('sample_rate', self.fields['sample_rate'].initial)
        cleaned_data.setdefault('carrier_freq', self.fields['carrier_freq'].initial)
        cleaned_data.setdefault('modulation_index', self.fields['modulation_index'].initial)
        cleaned_data.setdefault('scale', self.fields['scale'].initial)
        cleaned_data.setdefault('fading_floor', self.fields['fading_floor'].initial)
        return cleaned_data
