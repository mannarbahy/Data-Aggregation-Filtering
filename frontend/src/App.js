import { useEffect, useState } from "react";
import "./App.css";
function App() {
  // use data to display the fetched transactions
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const response = await fetch("http://127.0.0.1:5000/customer_details");
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const fetchedData = await response.json();
    const dataArray = Object.entries(fetchedData).map(([customer_id, total_revenue]) => ({
      customer_id,
      total_revenue
    }));
    setData(dataArray);
  };
  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="continer">
      <h1>Welcome to UR-Store Assessment</h1>
     
      <ul className="customer-list">
  {data.map((customer, index) => (
    <li key={index}>
      Customer ID: {customer.customer_id} - Revenue: {customer.total_revenue}
    </li>
  ))}
    


      </ul>

    </div>
  );
}

export default App;
