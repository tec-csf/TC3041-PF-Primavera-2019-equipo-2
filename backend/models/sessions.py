import redis
from . import config
import hashlib, uuid

class Sessions(object):

    def __init__(self):
        if config.REDIS_PASSWORD:
            self.instance = redis.StrictRedis(
                host=config.REDIS_HOST,
                port=config.REDIS_PORT,
                password=config.REDIS_PASSWORD)
        else:
            self.instance = redis.StrictRedis(
                host= config.REDIS_HOST,
                port=config.REDIS_PORT)

    def hashed_pass(self,password):
        """ Hash Pass """
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        return hashed_password

    def set_user(self,user,password):

        self.instance.hset(user,"password",Sessions.hashed_pass(self,password))

    def get_user_password(self,user):

        password=self.instance.hget(user,"password")

        return password

    def get_active_sessions(self):
        """ Regresa las sesiones activas en Redis """

        size = self.instance.dbsize()

        return size

    def add(self, id):
        """ Crea una nueva sesion en Redis """

        result = self.instance.set(id, 1)

        return result
