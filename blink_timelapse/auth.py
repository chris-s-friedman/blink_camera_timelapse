from blinkpy.auth import Auth
from blinkpy.blinkpy import Blink
from blinkpy.helpers.util import json_load


def blink_session(user=None, password=None, credential_file=None):
    if user is not None and password is not None:
        auth = Auth({"username": user, "password": password}, no_prompt=True)
    elif credential_file is not None:
        auth = Auth(json_load(credential_file))
    else:
        raise ValueError(
            "Must supply either username and password or "
            "supply a credential file"
        )
    blink = Blink()
    # Can set no_prompt when initializing auth handler
    blink.auth = auth
    blink.start()
    return blink
