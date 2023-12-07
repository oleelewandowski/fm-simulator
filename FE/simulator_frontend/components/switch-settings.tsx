'use client';

import { Settings } from 'lucide-react';
import React, { Dispatch, SetStateAction, useEffect, useState } from 'react';

import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover';
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from '@/components/ui/tooltip';
import { Button } from './ui/button';
import { Label } from './ui/label';
import { Switch } from './ui/switch';

interface SwitchSettingsProps {
  switchSettings: {
    baseband: boolean;
    carrier: boolean;
    modulated: boolean;
    demodulatedWithoutFadings: boolean;
    demodulatedWithFadings: boolean;
  };
  setSwitchSettings: Dispatch<
    SetStateAction<{
      baseband: boolean;
      carrier: boolean;
      modulated: boolean;
      demodulatedWithoutFadings: boolean;
      demodulatedWithFadings: boolean;
    }>
  >;
}

const SwitchSettings: React.FC<SwitchSettingsProps> = ({
  switchSettings,
  setSwitchSettings,
}) => {
  // NOTE: Avoid hydration error
  const [isMounted, setIsMounted] = useState(false);
  useEffect(() => {
    setIsMounted(true);
  }, []);

  if (!isMounted) return null;

  return (
    <Popover>
      <PopoverTrigger>
        <TooltipProvider>
          <Tooltip>
            <TooltipTrigger>
              <Button variant='link'>
                <Settings />
              </Button>
            </TooltipTrigger>
            <TooltipContent>
              <p> Modyfikuj Wyświetlone Wykresy</p>
            </TooltipContent>
          </Tooltip>
        </TooltipProvider>
      </PopoverTrigger>
      <PopoverContent className='space-y-4'>
        <div className='flex items-center space-x-4'>
          <Switch
            checked={switchSettings.baseband}
            onCheckedChange={(newState) =>
              setSwitchSettings((prevState) => ({
                ...prevState,
                baseband: newState,
              }))
            }
            id='baseband'
          />
          <Label htmlFor='baseband' className='text-md'>
            Sygnał Modulujący
          </Label>
        </div>
        <div className='flex items-center space-x-4'>
          <Switch
            checked={switchSettings.carrier}
            onCheckedChange={(newState) =>
              setSwitchSettings((prevState) => ({
                ...prevState,
                carrier: newState,
              }))
            }
            id='carrier'
          />
          <Label htmlFor='carrier' className='text-md'>
            Sygnał Nośny
          </Label>
        </div>
        <div className='flex items-center space-x-4'>
          <Switch
            checked={switchSettings.modulated}
            onCheckedChange={(newState) =>
              setSwitchSettings((prevState) => ({
                ...prevState,
                modulated: newState,
              }))
            }
            id='modulated'
          />
          <Label htmlFor='modulated' className='text-md'>
            Sygnał Zmodulowany FM
          </Label>
        </div>
        <div className='flex items-center space-x-4'>
          <Switch
            checked={switchSettings.demodulatedWithoutFadings}
            onCheckedChange={(newState) =>
              setSwitchSettings((prevState) => ({
                ...prevState,
                demodulatedWithoutFadings: newState,
              }))
            }
            id='demodulatedWithoutFadings'
          />
          <Label htmlFor='demodulatedWithoutFadings' className='text-md'>
            Sygnał Zdemodulowany FM bez zaników
          </Label>
        </div>
        <div className='flex items-center space-x-4'>
          <Switch
            checked={switchSettings.demodulatedWithFadings}
            onCheckedChange={(newState) =>
              setSwitchSettings((prevState) => ({
                ...prevState,
                demodulatedWithFadings: newState,
              }))
            }
            id='demodulatedWithFadings'
          />
          <Label htmlFor='demodulatedWithFadings' className='text-md'>
            Sygnał Zdemodulowany FM z zanikami
          </Label>
        </div>
      </PopoverContent>
    </Popover>
  );
};

export default SwitchSettings;
