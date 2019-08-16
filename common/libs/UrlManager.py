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

    """图片上传url地址管理，url地址为：域名+图片前缀（prefix_url+file_key）"""

    @staticmethod
    def buildImageUrl(path):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD']['prefix_url'] + path
        return url

