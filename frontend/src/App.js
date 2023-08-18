import logo from './logo.svg';
import './App.css';
import useFetch from './hooks/useFetch';

function App() {
  const { data: dataFromBackend, loading } = useFetch('http://localhost:5000/api/test');

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div className="App">
      <h1>React App</h1>
      <p>{dataFromBackend.message}</p>
    </div>
  );
}

export default App;
