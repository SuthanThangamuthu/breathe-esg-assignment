import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [company, setCompany] = useState("");
  const [sourceType, setSourceType] = useState("SAP");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("file", file);
    formData.append("company", company);
    formData.append("source_type", sourceType);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/upload/",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      console.log(data);
      if (response.ok) 
      {
      setMessage(data.message || "Upload successful");
      } 
    } catch (error) {
      console.error(error);
      setMessage("Error uploading file");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Emission Upload System</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Company Name:</label>
          <br />
          <input
            type="text"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            required
          />
        </div>

        <br />

        <div>
          <label>Source Type:</label>
          <br />
          <select
            value={sourceType}
            onChange={(e) => setSourceType(e.target.value)}
          >
            <option value="SAP">SAP</option>
            <option value="UTILITY">Utility</option>
            <option value="TRAVEL">Travel</option>
          </select>
        </div>

        <br />

        <div>
          <label>CSV File:</label>
          <br />
          <input
            type="file"
            accept=".csv"
            onChange={(e) => setFile(e.target.files[0])}
            required
          />
        </div>

        <br />

        <button type="submit">Upload CSV</button>
      </form>

      <br />

      <h3>{message}</h3>
    </div>
  );
}

export default App;