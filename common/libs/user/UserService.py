import hashlib,base64,string,random
class UserService():
    @staticmethod
    def geneAuthCode( user_info ):
        #获取授权码
        m = hashlib.md5()
        str = "%s-%s-%s-%s" %(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()
    @staticmethod
    def genePwd( pwd,salt ):
        m = hashlib.md5()
        str = "%s-%s" % (base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()