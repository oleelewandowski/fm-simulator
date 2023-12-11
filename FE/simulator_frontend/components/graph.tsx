import React, { useEffect, useRef } from 'react';

interface GraphsInterface {
  title: string;
  signalAudio: string;
  signalGraph: string;
}

const Graph: React.FC<GraphsInterface> = ({
  title,
  signalAudio,
  signalGraph,
}) => {
  const audioRef = useRef<HTMLAudioElement>(null);

  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.volume = 0.02;
      audioRef.current.load();
    }
  }, [signalAudio]);

  return (
    <div className='box-border h-full border border-black rounded-sm'>
      <div className='flex flex-row justify-between p-1'>
        <h2 className='p-1 text-sm font-bold text-center'> {title} </h2>
        {signalAudio ? (
          <audio controls className='w-1/2 h-10' ref={audioRef}>
            <source
              src={`data:audio/wav;base64,${signalAudio}`}
              type='audio/wav'
            />
            Twoja przeglądarka nie wspiera odtwarzania audio.
          </audio>
        ) : (
          <audio controls className='w-1/2 h-10' aria-disabled></audio>
        )}
      </div>
      <div className='flex flex-col items-center justify-start mb-1 lg:flex-row'>
        {signalGraph ? (
          <div className='w-[70%] h-auto'>
            <img
              src={`data:image/png;base64,${signalGraph}`}
              alt='Modulated Signal Graph'
            />
          </div>
        ) : (
          <div className='w-[70%] h-auto p-4'>
            Kliknij &quot;Start&quot;, aby rozpocząć symulację
          </div>
        )}
      </div>
    </div>
  );
};

export default Graph;
