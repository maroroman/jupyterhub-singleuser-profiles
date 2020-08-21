import connexion
import os
import json
import logging
from jupyterhub_singleuser_profiles.profiles import SingleuserProfiles

from functools import wraps
from urllib.parse import quote

from flask import Flask
from flask import redirect
from flask import request
from flask import Response

from jupyterhub.services.auth import HubAuth

_PROFILES = SingleuserProfiles(verify_ssl=False)
_PROFILES.load_profiles()
_PATH = "/opt/app-root/lib64/python3.6/site-packages"

_LOGGER = logging.getLogger(__name__)

prefix = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', '/')

auth = HubAuth(api_token=os.environ['JUPYTERHUB_API_TOKEN'], cache_max_age=60)

app = Flask(__name__)

def authenticated(f):
    """Decorator for authenticating with the Hub"""

    @wraps(f)
    def decorated(*args, **kwargs):
        cookie = request.cookies.get(auth.cookie_name)
        token = request.headers.get(auth.auth_header_name)
        if cookie:
            user = auth.user_for_cookie(cookie)
        elif token:
            user = auth.user_for_token(token)
        else:
            user = None
        if user:
            return f(user=user, *args, **kwargs)
        else:
            # redirect to login url on failed auth
            return redirect(auth.login_url + '?next=%s' % quote(request.path))

    return decorated

@authenticated
def whoami(user):
    return Response(
        json.dumps(user, indent=1, sort_keys=True), mimetype='application/json'
    )

@authenticated
def get_user_cm(user):
    cm = _PROFILES.get_user_profile_cm(user)
    return cm

@authenticated
def update_user_cm(user, body): 
    _PROFILES.update_user_profile_cm(user, data=body)
    return _PROFILES.get_user_profile_cm(user)

@authenticated
def get_sizes(pure_json=False, *args, **kwargs):
    _PROFILES.load_profiles()
    sizes_json = _PROFILES.get_sizes()
    if pure_json:
        return sizes_json
    response = []
    for size in sizes_json:
        response.append(size['name'])
    return response

@authenticated
def get_images(*args, **kwargs):
    _PROFILES.load_profiles()
    image_array = _PROFILES.get_images()
    return image_array

@authenticated
def get_size_by_name(sizeName, *args, **kwargs):
    _PROFILES.load_profiles()
    return _PROFILES.get_size(sizeName)

app = connexion.App(__name__, specification_dir='.', options={'swagger_ui':True})
app.add_api('swagger.yaml')
app.run(port=8181)
