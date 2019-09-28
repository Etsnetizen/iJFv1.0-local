# iJF小程序（本地调试环境配置）
## 本地环境配置

### pip安装以下库
    flask
    flask-sqlalchemy
    flask-debugtoolbar
    mysqlclient
    flask_script
    requests
    
### 导入数据库
    iJF_database.sql
    
### 修改配置
#### config/base_setting.py 
- 修改sql地址
    - SQLALCHEMY_DATABASE_URI = 'mysql://root:yourpwd@127.0.0.1/jfbz'
- 修改domain
    - APP = {
    'domain':'http://192.168.199.224:9000'
       }
 - 修改appkey\appid
    - MINA_APP = {
        'appid':'xxxx',
        'appkey':'xxxx'
      }
       
### 小程序开发者工具
    选择application-1.0目录
    
## 功能
1.小程序
   1. 报障页面
      1. 教师/学生报障功能
   2. 更多功能
      1. 后续版本发布
   3.  个人中心
      1. 查看我的报障单
2. 网页后台
    1. 对报障单的操作
       1. '处理完成'
       2. '无法处理'
       3. '延期处理'
       4. '待处理'
       5. '处理中'
    2. 对报障单添加备注方便处理（内部添加）
    3. 撤销报障单已完成状态
    4. 查看报障单（含图片）
    5. 查看报障单的处理记录
    
## 说明
    1. 后台目前只完成报障单查看、处理功能，其他功能待后续
    2. 在后台页面的报障展示页面，操作栏目的小图标分别为：
        1. 查看详情
        2. 添加备注
        3. 完成
        4. 无法完成
        5. 延期完成
        6. 处理中
        
## 更新
    1. 2019.9.28
        1. 增加了官网首页、报障页面、关于页面、工作人员入口
        2. 网页端报障与小程序端实现数据库同步(但网页端报障并不能在小程序端中查看报障进度)
        3. 完成了查询报障进度的页面
    
    
## 启动
* python manage.py runserver

**此为本地调试，无法承受更多并发，请勿部署在公网服务器。**
