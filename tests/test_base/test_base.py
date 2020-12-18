import pytest

from core.base import BaseProduct, BaseInstantiationError

class TestBaseProduct:
    def test_class_exists(self):
        assert globals().get('BaseProduct') == BaseProduct
    
    def test_base_product_instantiation_fails(self):
        with pytest.raises(BaseInstantiationError):
            base_product = BaseProduct('Product 1', desc='Good product')
