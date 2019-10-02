#批量创建后台账号
"""
要求：
1.为xlsx文件
2.以某一列作为账号
3.以某一列作为密码
例如：
python Bath_account_creat.py -f 2019通讯录.xlsx -i 0 -u 2 -p 3 -n 5
意思时在此xls文件中取第0列作为用户名 第2列作为账号 以第3列中第5位开始作为密码 
"""
import xlrd,random,string
import sys,os
import getopt,hashlib,base64,time
from common.models.User import User
from common.libs.Helper import getCurrentDate
from application import db,app
def Get_xls_column(path,col,no=0):
    path = os.getcwd() + '\\' +path
    #print(path)
    data = xlrd.open_workbook(path,encoding_override='utf-8')
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    list = []
    for i in range(1,nrows):
        alldata = table.row_values(i)
        result = alldata[int(col)]
        if no == 0:
            list.append(result)
        else:
            list.append(str(result)[no:])
        #print(result)
    #print('返回' + str(list))
    return list,nrows
def geneSalt( length = 16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        salt = "".join(keylist)
        #print('取得密钥：' + salt + '\n')
        return (salt)
def Get_encrypt_pwd(len):
    #print(len)
    login_salt_list = []
    for i in range(0,len-1):
        login_salt_list.append(geneSalt())
        #print(login_salt_list)
    return login_salt_list
def Add_to_db(namelist,usernamelist,pwdlist,saltlist,mobile_list,num):
    # print('namelist' )
    # print(namelist)
    # print('userlist' )
    # print(usernamelist)
    # print('pwd_list')
    # print(pwdlist)
    # print('slatlist')
    # print(saltlist)
    # print(num)
    # print('mobilelist')
    # print(mobile_list)

    for i in range(0,num-1):
        m = hashlib.md5()
        str = "%s-%s" % (base64.encodebytes(pwdlist[i].encode('utf-8')),saltlist[i])
        m.update(str.encode('utf-8'))
        encrypt_pwd =  m.hexdigest()

        # print(namelist[i])
        # print(mobile_list[i])
        # print(usernamelist[i])
        # print(encrypt_pwd)
        # print(saltlist[i])



        print('INSERT INTO user (nickname, mobile,login_name,login_pwd,login_salt,status,updated_time,created_time) VALUES (\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\');'
                  .format(namelist[i],mobile_list[i],usernamelist[i],encrypt_pwd,saltlist[i],'-1',getCurrentDate(),getCurrentDate()))

    return True


 

def main():
    pre_time = time.time()
    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-i:-u:-p:-n:',['help','file','nickname','c_user','c_pwd','-no'])
    #print(opts)
    info_list = []
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            print('文件名 (用第几列作为用户名) (用第几列作为登陆名) (用第几列作为密码) (密码是这行的几位之后)')
            sys.exit()
        if opt_name in ('-f','--file'):
            print('即将开始')
            info_list.append(opt_value)#0
        if opt_name in ('-i', '--nickname'):
            info_list.append(opt_value)#1
        if opt_name in ('-u','--c_user'):
            info_list.append(opt_value)#2
        if opt_name in ('-p','--c_pwd'):
            info_list.append(opt_value)#3
        if opt_name in ('-n','--no'):
            info_list.append(opt_value)#4
    #print(info_list)
    print('**********正在获取姓名列表**********')
    name_list,num = Get_xls_column(info_list[0], info_list[1])
    print('**********获取成功，正在获取账号列表**********')
    mobile_list,num = Get_xls_column(info_list[0],info_list[3])
    int_mobile_list = []
    for i in mobile_list:
        int_mobile_list.append(int(i))
    str_username_list,num= Get_xls_column(info_list[0],info_list[2])
    int_username_list = []
    for i in str_username_list:
        int_username_list.append(int(i))
        #int_username_list.append(int(i))
    #print(int_username_list)
    print('**********获取成功，正在获取密码列表**********')
    str_pwd_list,num = Get_xls_column(info_list[0],info_list[3],int(info_list[4]))
    int_pwd_list = []
    for i in str_pwd_list:
        #print(i)
        tmp = int(float(i))
        #print(tmp)
        int_pwd_list.append(int(tmp))
        #print(type(i))
    #print(int_pwd_list)
    print('**********获取成功正在初始**********\n**********正在计算生成密钥**********')
    salt_list = Get_encrypt_pwd(num)
    print('**********密钥已生成，正在生成语句**********')
    username_list = [str(i) for i in int_username_list]
    pwd_list = [str(i) for i in int_pwd_list]
    mobile_list = [str(i) for i in int_mobile_list]
    print('**********请复制以下SQL语句**********')
    ret = Add_to_db(name_list,username_list,pwd_list,salt_list,mobile_list,num)
    cru_time = time.time()
    print('获取成功，耗时{:.3f} s'.format(cru_time-pre_time))
main()
