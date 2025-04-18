import React from "react";
import { Route, Routes } from "react-router-dom";
import { SCREEN_PATH } from "./routes";
import LandingPage from "../pages/landing";
import ManageProducts from "../pages/manage-products";

function RootNavigation() {
  return (
    <Routes>
      <Route path={SCREEN_PATH.HOME} element={<LandingPage />} />
      <Route path={SCREEN_PATH.MANAGE_PRODUCTS} element={<ManageProducts />} />
    </Routes>
  );
}

export default RootNavigation;
