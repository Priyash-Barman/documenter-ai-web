import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getProducts } from "../../services/api";
import { setProducts } from "../../services/redux/slices/product.slice";

function ManageProducts() {
  const dispatch = useDispatch();
  const productList = useSelector((state) => state.product.products);
  const [product, setProduct] = useState([]);

  useEffect(() => {
    setProduct(productList);
  }, [productList]);

  useEffect(() => {
    const prod = getProducts();
    prod.then((res) => {
      dispatch(setProducts(res));
    });
  }, [dispatch]);

  return (
    <>
      <div className="container">
        <h4 className="text-center my-4">Products</h4>
        <table className="table table-bordered">
          <thead className="table-dark">
            <tr>
              <th>id</th>
              <th>title</th>
              <th>price</th>
            </tr>
          </thead>
          <tfoot className="table-dark">
            <tr>
              <td colSpan={3} className="text-center">
                Products by fakestore
              </td>
            </tr>
          </tfoot>
          <tbody>
            {product.map((prod) => (
              <tr key={prod.id}>
                <td>{prod.id}</td>
                <td>{prod.title}</td>
                <td>{prod.price}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default ManageProducts;
