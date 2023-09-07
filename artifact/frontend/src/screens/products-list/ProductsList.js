import React from 'react';
import { Alert, Col, Container, Row } from 'react-bootstrap';
import LoadingIndicator from '../../components/LoadingIndicator';
import Product from './components/Product';
import useProducts from './hooks/useProducts';
import { useLocation } from 'react-router-dom';
import SearchBar from '../../components/SearchBar';


export default function ProductsList() {

  const { search } = useLocation();
  console.log(search);
  const sp = new URLSearchParams(search);
  const query = sp.get('q');
  
  const { products, loading, error } = useProducts({}, query);

  return (
    <Container className="main-container">
      {loading ? (
        <LoadingIndicator className="align-content-center" />
      ) : error ? (
        <Alert variant="danger">{error}</Alert>
      ) : (
        <div>
          <h1>Products</h1>
        <Row style={{ width: '50vw', marginBottom: '1rem' }}>
        <SearchBar
          placeholder={query ? query : 'Search products'}
          ariaLabel="Search Products"
          currentPath="app/products"
        ></SearchBar>
      </Row>
          <Row>
            {products.map((product) => (
              <Col key={product.id} sm={6} md={4} lg={3} className="mb-3">
                <Product product={product}></Product>
              </Col>
            ))}
          </Row>
        </div>
      )}
    </Container>
  );
}
