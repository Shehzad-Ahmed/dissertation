import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ProductsList from './screens/products-list/ProductsList';
import ProductDetails from './screens/products-detail/ProductDetails';
import ShoppingCart from './screens/shopping-cart/ShoppingCart';
import Login from './screens/login/Login';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Home from './screens/home/Home';
import Registration from './screens/registration/Registration';
import FAQs from './screens/faqs/FAQs';
import ContactUs from './screens/contact-us/ContactUs';

function App() {
  return (
    <BrowserRouter>
      <div className="d-flex flex-column site-container">
        <ToastContainer position="bottom-center" limit={1} />
        <header>
          <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
          ></link>
          <Navbar></Navbar>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<ProductsList />}></Route>
            <Route path="app/home/" element={<Home />}></Route>
            <Route path="app/products/" element={<ProductsList />}></Route>
            <Route path="app/login/" element={<Login />}></Route>
            <Route path="app/register/" element={<Registration />}></Route>
            <Route path="app/product/:id" element={<ProductDetails />}></Route>
            <Route path="app/cart/" element={<ShoppingCart />}></Route>
            <Route path="app/faqs/" element={<FAQs />}></Route>
            <Route path="app/contact-us" element={<ContactUs />}></Route>
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
