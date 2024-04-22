from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    add_to_cart_endpoint: str


notebook = Product(
    name='14.1-inch Laptop',
    price=1590.00,
    add_to_cart_endpoint='/addproducttocart/details/31/1'
)
