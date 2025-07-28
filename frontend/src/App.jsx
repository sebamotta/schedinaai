
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [sport, setSport] = useState('calcio');
  const [importo, setImporto] = useState(10);
  const [rischio, setRischio] = useState(2);
  const [schedina, setSchedina] = useState(null);

  const generaSchedina = async () => {
    try {
      const res = await axios.post('http://localhost:8000/genera', {
        sport,
        importo,
        rischio
      });
      setSchedina(res.data.schedina);
    } catch (err) {
      console.error('Errore nella richiesta:', err);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>SchedinaAI</h1>
      <div>
        <label>Sport: </label>
        <input value={sport} onChange={(e) => setSport(e.target.value)} />
      </div>
      <div>
        <label>Importo: </label>
        <input
          type="number"
          value={importo}
          onChange={(e) => setImporto(parseFloat(e.target.value))}
        />
      </div>
      <div>
        <label>Rischio: </label>
        <input
          type="number"
          value={rischio}
          onChange={(e) => setRischio(parseInt(e.target.value))}
        />
      </div>
      <button onClick={generaSchedina} style={{ marginTop: '1rem' }}>
        Genera schedina
      </button>
      {schedina && (
        <div style={{ marginTop: '1rem' }}>
          <strong>Schedina:</strong> {schedina.join(', ')}
        </div>
      )}
    </div>
  );
}

export default App;
