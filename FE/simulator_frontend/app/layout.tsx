import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Symulator do demonstracji odbioru FM w warunkach zaników',
};

interface RootLayoutInterface {
  children: React.ReactNode;
}

const RootLayout: React.FC<RootLayoutInterface> = ({ children }) => {
  return (
    <html lang='pl'>
      <body className={inter.className}>{children}</body>
    </html>
  );
};

export default RootLayout;
