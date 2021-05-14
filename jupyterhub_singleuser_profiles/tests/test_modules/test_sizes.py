from mock_data import Mockdata
import pytest

Mock = Mockdata()

size_param = [("Small", Mock._SIZES[0]),("Medium", Mock._SIZES[1]),("Large", Mock._SIZES[2])]

class TestSizes:

    def test_get_sizes(self,loaded_profiles):
        assert loaded_profiles.get_sizes() == Mock._SIZES

    @pytest.mark.parametrize("size, expected", size_param)
    def test_get_size(self,size, expected, loaded_profiles):
        assert loaded_profiles.get_size(size) == expected

    def test_parse(self,get_size_object):
        assert get_size_object._parse(Mock._SIZES[0]) == Mock._SIZES[0]