import { useEffect, useReducer } from 'react';
import apiCallReducer from '../../../utils/apiCallReducer';
import axios from 'axios';

const useProducts = (defaultValue, searchQuery) => {
  const [{ loading, error, data: products }, dispatch] = useReducer(
    apiCallReducer,
    {
      data: [],
      loading: true,
      error: '',
    }
  );
  useEffect(() => {
    dispatch({ type: 'FETCH_REQUEST' });
    const getProducts = async () => {
      try {
        const results = await axios.get(`/api/inventory/products/search/?q=${searchQuery ? searchQuery : ''}`);

        dispatch({
          type: 'FETCH_SUCCESS',
          payload: results.data.results.map((data) => transformData(data)),
        });
      } catch (error) {
        dispatch({ type: 'FETCH_FAIL', error: error.message });
      }
    };
    const transformData = (data) => {
      return {
        id: data.id,
        name: data.name,
        price: data.actual_price,
        imageUrl: data.images.length? data.images[0]: "",
      };
    };
    getProducts();
  }, [searchQuery]);

  return { products, loading, error };
};

export default useProducts;
