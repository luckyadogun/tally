import pytest

from core.base import BaseProduct
from core.products import TangibleProduct, NoInstanceAccessError


class TestBaseProduct:
    def test_class_exists(self):
        assert globals().get('BaseProduct') == BaseProduct
    
    def test_base_fails_without_implementing_abstracts(self):
        with pytest.raises(TypeError):
            base_product = BaseProduct('Product 1', desc='Good product')


class TestTangibleProduct:
    def test_tangible_fails_without_fields(self):
        with pytest.raises(TypeError):
            instance = TangibleProduct('Sample Product', 'I love free samples')

    def test_tangible_passes_with_fields(self):
        instance = TangibleProduct('Sample Product', 1, 12, 22, 'Some sweeet sample')
        assert instance.name == 'Sample Product'
        assert instance.weight == 1
        assert instance.width == 12
        assert instance.height == 22
        assert instance.desc == 'Some sweeet sample'
        assert instance.id == 1

    def test_instance_cant_access_allproducts(self):
        with pytest.raises(NoInstanceAccessError):
            instance = TangibleProduct('Sample Product', 1, 12, 22, 'Some sweeet sample')
            instance.allproducts()

    def test_class_can_access_allproducts(self):
        TangibleProduct('Sample Product', 1, 12, 22, 'Some sweeet sample')
        assert len(TangibleProduct.allproducts()) > 0
         

    

