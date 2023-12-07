'use client';

import * as z from 'zod';

import { Button } from '@/components/ui/button';
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { zodResolver } from '@hookform/resolvers/zod';
import axios from 'axios';
import { Fragment, useState } from 'react';
import { useForm } from 'react-hook-form';
import Graphs from './graphs';
import SwitchSettings from './switch-settings';

const formSchema = z.object({
  freq: z.string(),
  duration: z.string(),
  sample_rate: z.string(),
  carrier_freq: z.string(),
  modulation_index: z.string(),
  scale: z.string(),
  fading_floor: z.string(),
});

const ModulationForm = () => {
  const [loading, setLoading] = useState(false);
  const [switchSettings, setSwitchSettings] = useState({
    baseband: true,
    carrier: true,
    modulated: true,
    demodulatedWithoutFadings: true,
    demodulatedWithFadings: true,
  });
  const [data, setData] = useState({
    sine_signal_audio: '',
    sine_signal_graph: '',
    carrier_signal_audio: '',
    carrier_signal_graph: '',
    modulated_signal_audio: '',
    modulated_signal_graph: '',
    demodulated_signal_audio: '',
    demodulated_signal_graph: '',
    demodulated_signal_with_fading_graph: '',
    demodulated_signal_with_fading_audio: '',
  });

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      freq: '280',
      duration: '3',
      sample_rate: '44100',
      carrier_freq: '2200',
      modulation_index: '3',
      scale: '0.02',
      fading_floor: '0.5',
    },
  });

  const onSubmit = async (inputValues: z.infer<typeof formSchema>) => {
    const parsedValues = {
      freq: parseFloat(inputValues.freq),
      duration: parseFloat(inputValues.duration),
      sample_rate: parseFloat(inputValues.sample_rate),
      carrier_freq: parseFloat(inputValues.carrier_freq),
      modulation_index: parseFloat(inputValues.modulation_index),
      scale: parseFloat(inputValues.scale),
      fading_floor: parseFloat(inputValues.fading_floor),
    };

    setLoading(true);
    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/signal_processor/simulate_fm/',
        parsedValues,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      setData(response.data);
    } catch (error) {
      console.log('[SUBMIT]: Błąd podczas wysyłania formularza');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Fragment>
      <section className='flex flex-col w-full rounded-md lg:w-1/3 h-3/5 lg:h-full'>
        <h1 className='justify-start p-1 text-2xl font-bold'> Parametry </h1>
        <div className='p-1 grid-1'>
          <Form {...form}>
            <form
              onSubmit={form.handleSubmit(onSubmit)}
              className='grid grid-cols-2 gap-1 lg:grid-cols-1'
            >
              <FormField
                name='freq'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Częstotliwość Sygnału Modulującego </FormLabel>
                    <FormControl>
                      <Input disabled={loading} {...field} type='number' />
                    </FormControl>
                    <FormDescription>
                      Częstotliwość sygnału modulującego w Hz
                    </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                name='duration'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Czas Trwania </FormLabel>
                    <FormControl>
                      <Input disabled={loading} {...field} type='number' />
                    </FormControl>
                    <FormDescription>
                      Czas trwania sygnału w sekundach
                    </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                name='sample_rate'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Częstotliwość Próbkowania </FormLabel>
                    <FormControl>
                      <Input disabled={loading} {...field} type='number' />
                    </FormControl>
                    <FormDescription>
                      Częstotliwość próbkowania w próbkach/sekundę
                    </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                name='carrier_freq'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Częstotliwość Sygnału Nośnego </FormLabel>
                    <FormControl>
                      <Input disabled={loading} {...field} type='number' />
                    </FormControl>
                    <FormDescription>
                      Częstotliwość sygnału nośnego w Hz
                    </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                name='modulation_index'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Indeks Modulacji </FormLabel>
                    <FormControl>
                      <Input disabled={loading} {...field} type='number' />
                    </FormControl>
                    <FormDescription> Indeks modulacji dla FM </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                name='scale'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Skala Rozkładu Rayleigha </FormLabel>
                    <FormControl>
                      <Input
                        disabled={loading}
                        {...field}
                        type='number'
                        step={0.01}
                      />
                    </FormControl>
                    <FormDescription>
                      Skala rozkładu Rayleigha, wpływająca na zmienność zaników
                    </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                name='fading_floor'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel> Minimalny Poziom Sygnału Po Zaniku </FormLabel>
                    <FormControl>
                      <Input
                        disabled={loading}
                        {...field}
                        type='number'
                        step={0.01}
                      />
                    </FormControl>
                    <FormDescription>
                      Minimalny poziom sygnału po zaniku, zapobiegający
                      całkowitej utracie sygnału
                    </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <Button type='submit' className='w-full mt-4' disabled={loading}>
                Start
              </Button>
            </form>
          </Form>
        </div>
      </section>
      <section className='flex flex-col w-full h-full rounded-md '>
        <div className='flex flex-row justify-between'>
          <div>
            <h1 className='p-2 text-2xl font-bold'>
              Wykresy oraz możliwość odsłuchu
            </h1>
          </div>
          <div className='flex items-center justify-center'>
            <SwitchSettings
              setSwitchSettings={setSwitchSettings}
              switchSettings={switchSettings}
            />
          </div>
        </div>
        <Graphs data={data} switchSettings={switchSettings} />
      </section>
    </Fragment>
  );
};

export default ModulationForm;
