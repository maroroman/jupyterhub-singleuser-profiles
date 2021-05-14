import pytest
import mock_data

Mock = mock_data.Mockdata()

class TestImages:

    #TODO: MOCK IMAGE DATA WITH YAML FILES
    @pytest.fixture(autouse=True)
    def prepare_test(self, get_image_object):
        self._image = get_image_object

    def test_get(self):
        assert self._image.get() == Mock._IMAGES

    def test_default(self):
        assert self._image.get_default() == "s2i-generic-data-science-notebook:v0.0.2"
