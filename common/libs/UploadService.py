from werkzeug.utils import secure_filename
from application import app,db
import os,stat,uuid,datetime
from common.libs.Helper import getCurrentDate
from common.models.Image import Image
from flask import g
import random,string
class UploadService():
    @staticmethod
    def uploadByFile( file ):
        config_upload = app.config['UPLOAD']
        resp = {'code':200,'msg':"操作成功",'data':{} }
        filename = secure_filename(file.filename)
        ext = filename.rsplit(".", 1)[1]  # 取切割之后的第一个，[0]是文件名
        if ext not in config_upload['ext']:
            resp['code'] = -1
            resp['msg'] = '不受支持的格式'
            return resp
        #上传
        root_path = os.getcwd() + config_upload['prefix_path']
        file_dir = datetime.datetime.now().strftime("%Y%m%d")
        save_dir = root_path + file_dir
        if not os.path.exists( save_dir ):
            os.mkdir( save_dir )
            os.chmod( save_dir ,stat.S_IRWXU | stat.S_IRGRP | stat.S_IRWXO)
            #https://www.runoob.com/python/os-chmod.html 权限分配
        file_name = str(uuid.uuid4()).replace("-", "") + "." + ext
        file.save("{0}/{1}".format(save_dir, file_name))


        model_image = Image()
        model_image.file_key = file_dir + "/" + file_name
        model_image.member_id = g.member_info.id
        model_image.random_code = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        model_image.created_time = getCurrentDate()
        db.session.add(model_image)
        db.session.commit()

        resp['data'] = {
            'file_key': model_image.file_key,
            'random_code':model_image.random_code
        }
        return resp

