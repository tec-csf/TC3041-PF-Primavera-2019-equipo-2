import redis
import hashlib, uuid
from backend import config

class Login(object):

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

        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        return hashed_password

    def set_user(self,user,password):

        self.instance.hset(user,"password",Login.hashed_pass(self,password))


    def get_user_password(self,user):

        password=self.instance.hget(user,"password")

        return password
