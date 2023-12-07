import React from 'react';
import Graph from '@/components/graph';

interface GraphsInterface {
  data: {
    sine_signal_audio: string;
    sine_signal_graph: string;
    carrier_signal_audio: string;
    carrier_signal_graph: string;
    modulated_signal_audio: string;
    modulated_signal_graph: string;
    demodulated_signal_audio: string;
    demodulated_signal_graph: string;
    demodulated_signal_with_fading_graph: string;
    demodulated_signal_with_fading_audio: string;
  };
  switchSettings: {
    baseband: boolean;
    carrier: boolean;
    modulated: boolean;
    demodulatedWithoutFadings: boolean;
    demodulatedWithFadings: boolean;
  };
}

const Graphs: React.FC<GraphsInterface> = ({ data, switchSettings }) => {
  return (
    <div className='box-border grid flex-1 w-full grid-cols-1 gap-2 p-2'>
      {switchSettings.baseband && (
        <Graph
          signalAudio={data?.sine_signal_audio}
          signalGraph={data?.sine_signal_graph}
          title='Sygnał Modulujący'
        />
      )}
      {switchSettings.carrier && (
        <Graph
          signalAudio={data?.carrier_signal_audio}
          signalGraph={data?.carrier_signal_graph}
          title='Sygnał Nośny'
        />
      )}
      {switchSettings.modulated && (
        <Graph
          signalAudio={data?.modulated_signal_audio}
          signalGraph={data?.modulated_signal_graph}
          title='Sygnał Zmodulowany FM'
        />
      )}
      {switchSettings.demodulatedWithoutFadings && (
        <Graph
          signalAudio={data?.demodulated_signal_audio}
          signalGraph={data?.demodulated_signal_graph}
          title='Sygnał Zdemodulowany FM bez zaników'
        />
      )}
      {switchSettings.demodulatedWithFadings && (
        <Graph
          signalAudio={data?.demodulated_signal_with_fading_audio}
          signalGraph={data?.demodulated_signal_with_fading_graph}
          title='Sygnał Zdemodulowany FM z zanikami'
        />
      )}
    </div>
  );
};

export default Graphs;
