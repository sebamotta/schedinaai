import { useState } from "react";
import axios from "axios";

function App() {
  const [sport, setSport] = useState("");
  const [importo, setImporto] = useState("");
  const [rischio, setRischio] = useState("");
  const [risultato, setRisultato] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(
        `${import.meta.env.VITE_BACKEND_URL}/genera`,
        {
          sport,
          importo: parseFloat(importo),
          rischio: parseInt(rischio),
        }
      );
      setRisultato(res.data.schedina || "Errore nella risposta");
    } catch (err) {
      console.error("Errore nella fetch:", err);
      setRisultato("Errore nella comunicazione col backend");
    }
  };

  return (
    <div>
      <h1>Schedina AI</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="Sport" value={sport} onChange={(e) => setSport(e.target.value)} /><br />
        <input type="number" placeholder="Importo" value={importo} onChange={(e) => setImporto(e.target.value)} /><br />
        <input type="number" placeholder="Rischio" value={rischio} onChange={(e) => setRischio(e.target.value)} /><br />
        <button type="submit">Genera</button>
      </form>
      {risultato && (
        <div>
          <h2>Schedina generata:</h2>
          <pre>{JSON.stringify(risultato, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
