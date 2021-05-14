import pytest
import mock_data
import yaml

Mock = mock_data.Mockdata()

class TestService:
    
    def test_get_service_reference_config_map(self, get_service_object):
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
