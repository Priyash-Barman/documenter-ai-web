import { BrowserRouter } from "react-router-dom";
import RootNavigation from "./navigation";
import Header from "./components/common/header";

function App() {
  return (
    <>
      <BrowserRouter basename={"/"}>
        <Header />
        <RootNavigation />
      </BrowserRouter>
    </>
  );
}

export default App;
