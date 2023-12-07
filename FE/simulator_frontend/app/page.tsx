import ModulationForm from '@/components/modulation-form';

const HomePage = () => {
  return (
    <main className='border flex flex-col lg:flex-row p-8 min-h-screen gap-2 justify-start items-start'>
      <ModulationForm />
    </main>
  );
};

export default HomePage;
