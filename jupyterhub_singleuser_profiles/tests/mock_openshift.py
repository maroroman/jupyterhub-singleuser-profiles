import yaml
import os
import sys
from openshift.dynamic.resource import ResourceInstance

def get_imagestreams(label=None):
    with open(os.path.join(sys.path[0], "jupyterhub_singleuser_profiles/tests/mock_images.yaml"), "r") as f:
        # The "client" attribute is unneccessary so "foo" is in its' place
        return ResourceInstance("foo", yaml.load(f))