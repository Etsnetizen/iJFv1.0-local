from application import app
from common.libs.Helper import ops_render
from common.libs.LogService import LogService
@app.errorhandler( 404 )
def error_404( e ):
    LogService.addErrorLog(str(e) )
    return ops_render('error/error.html',context={'error':404,'msg':'页面正在开发，现在无法访问'})
