"""
Paquete pages que contiene todos los Page Objects del proyecto.

Este paquete implementa el patrón Page Object Model (POM) para
encapsular la interacción con las diferentes páginas de SauceDemo.
"""

from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage

__all__ = ['LoginPage', 'InventoryPage', 'CartPage']