
import jwt
import datetime
import logging

from functools import wraps
from flask import abort, request
from common.utils.web_key import PRIVATE_WEB_KEY
from common.utils.web_key_pub import PUBLIC_WEB_KEY
from passlib.hash import pbkdf2_sha256


TOKEN_ALGO = 'RS512'
TEN_YEARS = 60 * 60 * 24 * 7 * 52 * 10
ONE_YEARS = 60 * 60 * 24 * 7 * 52

decorator_with_args = lambda decorator: lambda *args, **kwargs: lambda func: decorator(func, *args, **kwargs)

LOG = logging.getLogger(__name__)

def extract_payload(token):
    try:
        payload = jwt.decode(token, PUBLIC_WEB_KEY, algorithm=TOKEN_ALGO)
        return payload
    except jwt.ExpiredSignatureError as e:
        print((str(e) + " ExpiredSignatureError"))
        raise
    except jwt.InvalidTokenError as e:
        print((str(e) + " InvalidTokenError"))
        raise
    except Exception as e:
        print((str(e) + " Error"))
        raise
    return False


def authentication_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        LOG.info("===>")
        # return f(user={}, *args, **kwargs)
        if 'Authorization' not in request.headers:
            abort(403, 'User not logged or no token received')
        token = request.headers['Authorization']
        token = token.split('Bearer ')
        LOG.info("===> split")
        if len(token) > 1:
            token = token[1]
        else:
            abort(403, 'Empty token')
        try:
            payload = extract_payload(token)
            LOG.info("===> extract")
        except Exception as e:
            LOG.info("===> exct")
            abort(403, 'User not logged or session expired ' + str(e))
        else:
            LOG.info("===>return")
            return f(user=payload, *args, **kwargs)
    return decorated_function


@decorator_with_args
def permissions(f, permissions=None):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_permission = kwargs['user'].get('permission', '')
        if not permissions:
            return f(*args, **kwargs)
        perms = permissions
        if not isinstance(permissions, tuple):
            perms = (permissions, )
        if user_permission not in perms:
            abort(403, 'User has not enough privilege')
        else:
            return f(*args, **kwargs)
    return decorated_function


def generate_user_token(data):
    now = datetime.datetime.utcnow()
    delta = datetime.timedelta(seconds=ONE_YEARS)

    payload = {
        # Reserved claims
        'iat': now,
        'nbf': now,
        'exp': now + delta,
        'iss': 'AIO',
        # 'aud': audience
    }
    payload.update(data)
    # flask_log(jwt.encode(payload, PRIVATE_WEB_KEY, algorithm=TOKEN_ALGO))
    return jwt.encode(payload, PRIVATE_WEB_KEY, algorithm=TOKEN_ALGO)


def hash_password(password):
    return pbkdf2_sha256.encrypt(password, rounds=1000000, salt_size=16)


def verify_password(xhash, password):
    return pbkdf2_sha256.verify(password, xhash)
