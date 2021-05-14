import yaml
import sys
import os

class Mockdata:

    def __init__(self):

        self._SIZES = [{'name': 'Small',
            'resources': {'requests': {'memory': '1Gi', 'cpu': 1},
            'limits': {'memory': '2Gi', 'cpu': 2}}},
            {'name': 'Medium',
            'resources': {'requests': {'memory': '2Gi', 'cpu': 2},
            'limits': {'memory': '4Gi', 'cpu': 4}}},
            {'name': 'Large',
            'resources': {'requests': {'memory': '4Gi', 'cpu': 4},
            'limits': {'memory': '8Gi', 'cpu': 8}}}]
        
        self._IMAGES = [
                        {
                            "content": {
                            "dependencies": [
                                {
                                "name": "Boto3",
                                "version": "1.17.11"
                                },
                                {
                                "name": "Kafka-Python",
                                "version": "2.0.2"
                                },
                                {
                                "name": "Matplotlib",
                                "version": "3.1.3"
                                },
                                {
                                "name": "Numpy",
                                "version": "1.20.2"
                                },
                                {
                                "name": "Pandas",
                                "version": "1.2.3"
                                },
                                {
                                "name": "Scipy",
                                "version": "1.6.2"
                                }
                            ],
                            "software": [
                                {
                                "name": "Python",
                                "version": "v3.8.3"
                                }
                            ]
                            },
                            'default': False,
                            "description": "Jupyter notebook image with a set of data science libraries that advanced AI/ML notebooks will use as a base image to provide a standard for libraries avialable in all notebooks",
                            "display_name": "Standard Data Science",
                            "name": "s2i-generic-data-science-notebook:v0.0.2",
                            "url": "https://github.com/thoth-station/s2i-generic-data-science-notebook"
                        },
                        {
                            "content": {
                            "dependencies": [],
                            "software": []
                            },
                            'default': False,
                            "description": "Jupyter notebook image with Elyra-AI installed",
                            "display_name": "Elyra Notebook Image",
                            "name": "s2i-lab-elyra:v0.0.8",
                            "url": "https://github.com/thoth-station/s2i-lab-elyra"
                        },
                        {
                            "content": {
                            "dependencies": [],
                            "software": []
                            },
                            'default': False,
                            "description": "Jupyter notebook image with minimal dependency set to start experimenting with Jupyter environment.",
                            "display_name": "Minimal Notebook Image",
                            "name": "s2i-minimal-notebook:v0.0.7",
                            "url": "https://github.com/thoth-station/s2i-minimal-notebook"
                        },
                        {
                            "content": {
                            "dependencies": [],
                            "software": []
                            },
                            'default': False,
                            "description": "Jupyter notebook image containing basic dependencies for data science and machine learning work.",
                            "display_name": "SciPy Notebook Image",
                            "name": "s2i-scipy-notebook:v0.0.2",
                            "url": "https://github.com/thoth-station/s2i-minimal-notebook"
                        },
                        {
                            "content": {
                            "dependencies": [],
                            "software": []
                            },
                            'default': False,
                            "description": None,
                            "display_name": None,
                            "name": "s2i-spark-minimal-notebook:py36-spark2.4.5-hadoop2.7.3",
                            "url": None
                        },
                        {
                            "content": {
                            "dependencies": [],
                            "software": []
                            },
                            'default': False,
                            "description": None,
                            "display_name": None,
                            "name": "s2i-spark-scipy-notebook:3.6",
                            "url": None
                        },
                        {
                            "content": {
                            "dependencies": [],
                            "software": []
                            },
                            'default': False,
                            "description": "Jupyter notebook image containing dependencies for training Tensorflow models.",
                            "display_name": "Tensorflow Notebook Image",
                            "name": "s2i-tensorflow-notebook:v0.0.2",
                            "url": "https://github.com/thoth-station/s2i-tensorflow-notebook"
                        }
                        ]
        with open(os.path.join(sys.path[0], "./mock_yamls/service_ref_cm.yaml"), "r") as service_ref_cm:
            self._SERVICE_REF_CM = yaml.load(service_ref_cm)