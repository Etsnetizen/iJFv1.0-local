import time
from application import app

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        #版本管理url
        return path
    @staticmethod
    def buildStaticUrl( path ):
        release_version = app.config.get('RELEASE_VERSION')
        ver = "%s"%( int(time.time()) ) if not release_version else release_version
        path = '/static' + path + "?ver=" + ver
        return UrlManager.buildUrl( path )
