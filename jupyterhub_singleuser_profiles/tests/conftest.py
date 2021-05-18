import pytest
import pytest_mock
import requests
import requests_mock
from . import mock_openshift
from mock import Mock, patch

from .. import profiles, sizes, service, images

@pytest.fixture(scope="module")
def get_adapter():
  pass

@patch.object(profiles.SingleuserProfiles, 'openshift', mock_openshift)
@pytest.fixture(scope="module")
def get_profiles():
  return profiles.SingleuserProfiles(namespace="default", verify_ssl=False)

@pytest.fixture(scope="module")
def loaded_profiles(get_profiles):
    _profiles = get_profiles
    _profiles.load_profiles()
    return _profiles

@pytest.fixture(scope="module")
def get_image_object(get_profiles):
  get_profiles.load_profiles()
  return images.Images(get_profiles.openshift, get_profiles.namespace)

@pytest.fixture(scope="module")
def get_service_object(get_profiles):
  get_profiles.load_profiles()
  return service.Service(get_profiles.openshift, get_profiles.namespace)

@pytest.fixture(scope="module")
def get_size_object(get_profiles):
  get_profiles.load_profiles()
  return sizes.Sizes(get_profiles.sizes)