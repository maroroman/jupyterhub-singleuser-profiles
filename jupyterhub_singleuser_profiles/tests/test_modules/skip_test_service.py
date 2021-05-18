import pytest
from .. import mock_data
import yaml
import requests

Mock = mock_data.Mockdata()

class TestService:
    
    def test_get_service_reference_config_map(self, get_service_object, requests_mock):
        requests_mock.get('https://api.cluster-fdc5.fdc5.sandbox1237.opentlc.com:6443/api/v1/namespaces/default/configmaps?limit=500', body=Mock._SERVICE_REF_CM)
        assert yaml.load(get_service_object.get_service_reference_config_map("opentlc-mgr")) == Mock._SERVICE_REF_CM

    def test_get_template(self):
        pass

    def test_process_template(self):
        pass

    def test_get_owner_references(self):
        pass

    def test_deploy_services(self):
        pass

    def test_submit_resource(self):
        pass

    def test_delete_reference_cm(self):
        pass
