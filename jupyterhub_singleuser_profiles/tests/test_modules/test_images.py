import pytest
from .. import mock_data, mock_openshift
from ... import images


mock_data_object = mock_data.Mockdata()

class TestImages:

    # CREATE THE IMAGE OBJECT HERE TO CHANGE THE OPENSHIFT OBJECT WITHIN!!!!!!

    #TODO: MOCK IMAGE DATA WITH YAML FILES
    #@pytest.fixture(autouse=True)
    #def prepare_test(self, get_image_object):
    #    self._image = get_image_object

    @pytest.fixture(autouse=True)
    # Openshift can be changed on creation without patch here
    def prepare_test(self):
        self._image = images.Images(mock_openshift, "default")

    def test_get(self):
        image_response = self._image.get()
        assert image_response[0].get('name') != None
        assert image_response[0]["order"] < image_response[3]["order"]
        assert isinstance(image_response[1]["content"]["software"], list) and image_response[1]["content"]["software"] != []
        assert isinstance(image_response[0]["content"]["software"], list) and image_response[0]["content"]["software"] == []

    def test_default(self):
        default_image_name = self._image.get_default()
        images = self._image.get()
        for image in images:
            if image["name"] == default_image_name:
                default_image = image
        assert images.index(default_image) == 0 or default_image["default"] == True
