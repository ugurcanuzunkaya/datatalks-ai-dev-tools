import React, { useState, useEffect, useRef } from 'react';
import Editor from '@monaco-editor/react';
import io from 'socket.io-client';

const socket = io('http://localhost:8000');

function App() {
  const [code, setCode] = useState("# Write your Python code here\nprint('Hello, World!')");
  const [output, setOutput] = useState("");
  const [roomId, setRoomId] = useState("interview-room-1");
  const pyodideRef = useRef(null);

  useEffect(() => {
    // Join room
    socket.emit('join_room', roomId);

    // Listen for code updates
    socket.on('code_update', (newCode) => {
      setCode(newCode);
    });

    // Load Pyodide
    async function loadPyodide() {
      if (window.loadPyodide && !pyodideRef.current) {
        pyodideRef.current = await window.loadPyodide();
        console.log("Pyodide loaded");
      }
    }
    loadPyodide();

    return () => {
      socket.off('code_update');
    };
  }, [roomId]);

  const handleEditorChange = (value) => {
    setCode(value);
    socket.emit('code_change', { room_id: roomId, code: value });
  };

  const runCode = async () => {
    if (!pyodideRef.current) {
      setOutput("Pyodide is still loading...");
      return;
    }
    try {
      // Capture stdout
      pyodideRef.current.setStdout({ batched: (msg) => setOutput((prev) => prev + msg + "\n") });
      setOutput(""); // Clear previous output
      await pyodideRef.current.runPythonAsync(code);
    } catch (error) {
      setOutput((prev) => prev + "\nError:\n" + error.message);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', backgroundColor: '#1e1e1e', color: 'white' }}>
      <div style={{ padding: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #333' }}>
        <h3>Coding Interview Platform</h3>
        <button onClick={runCode} style={{ padding: '8px 16px', backgroundColor: '#28a745', color: 'white', border: 'none', cursor: 'pointer', borderRadius: '4px' }}>
          Run Code
        </button>
      </div>
      <div style={{ display: 'flex', flex: 1, overflow: 'hidden' }}>
        <div style={{ flex: 1, borderRight: '1px solid #333' }}>
          <Editor
            height="100%"
            defaultLanguage="python"
            theme="vs-dark"
            value={code}
            onChange={handleEditorChange}
            options={{ minimap: { enabled: false }, fontSize: 14 }}
          />
        </div>
        <div style={{ flex: 1, padding: '10px', overflowY: 'auto', fontFamily: 'monospace', whiteSpace: 'pre-wrap', backgroundColor: '#0d0d0d' }}>
          <div style={{ color: '#888', marginBottom: '10px' }}>OUTPUT:</div>
          {output}
        </div>
      </div>
    </div>
  );
}

export default App;
