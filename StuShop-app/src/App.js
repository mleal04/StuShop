import './App.css';
import { useEffect } from 'react';

function App() {
  useEffect(() => {
    // This runs once when the component mounts
    fetch("http://db8:5000/orders")
      .then(res => res.json())
      .then(data => {
        console.log(data);  // prints the data from your Flask backend
      })
      .catch(err => console.error(err));
  }, []); // empty dependency array = run once

  return (
    <div className="App">
      <p>Welcome to the StuShop App!</p>
      <p>Check the console for fetched orders.</p>
    </div>
  );
}

export default App;

