import axios from "axios";

const api = axios.create({
  baseURL: "https://fakestoreapi.com", // Change this to your API base URL
  timeout: 10000, // Request timeout in milliseconds
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
