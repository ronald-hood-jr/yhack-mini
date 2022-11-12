import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Header } from './components/header';
import { Footer } from './components/footer';
import { Table } from './components/table';
function App() {
  return (
    <div className='flex flex-col h-screen justify-between'>
      <Header/>
      <Table/>
      <Footer/>
    </div>
    
  );
}

export default App;
