import pytest

from core.base import BaseProduct, BaseInstantiationError

SCOPE = "function"

class SampleBaseProduct(BaseProduct):
    pass

@pytest.fixture(scope=SCOPE)
def shared_sample_base_instance():
    instance = SampleBaseProduct('Sample Product', 'I love free samples')
    yield instance




class TestBaseProduct:
    def test_class_exists(self):
        assert globals().get('BaseProduct') == BaseProduct
    
    def test_base_product_instantiation_fails(self):
        with pytest.raises(BaseInstantiationError):
            base_product = BaseProduct('Product 1', desc='Good product')

    def test_base_add_images(self, shared_sample_base_instance):
        assert shared_sample_base_instance.name == 'Sample Product'
