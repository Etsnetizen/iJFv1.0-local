from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
class Application ( Flask ):
    def __init__(self,import_name,root_path = None):
        super(Application, self).__init__( import_name ,root_path = root_path,static_folder = None )
        self.config.from_pyfile( 'config/base_setting.py' )
        # if 'ops_config' in os.environ:
        # self.config.from_pyfile('config/%s.py' % os.environ['ops_config'])

        db.init_app( self )

db = SQLAlchemy()
app = Application(__name__,root_path=os.getcwd() )
manager = Manager(app)


from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')#注册一个全局的模板urlmanager，可在所有文件中使用，包括html
app.add_template_global(UrlManager.buildUrl,'buildUrl')
app.add_template_global(UrlManager.buildImageUrl,'buildImageUrl')
