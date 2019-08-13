//获取应用实例
var app = getApp();
Page({
    data: {},
    onLoad() {

    },
    onShow() {
        /*let that = this;
        that.setData({
            user_info: {
                nickname: "编程浪子",
                avatar_url: "/images/more/logo.png"
            },
        })*/
        this.getInfo();
    },
    getInfo:function () {
        var that = this;
        wx.request({
            url:app.buildUrl('/member/info'),
            header:app.getRequestHeader(),
            success:function ( res ) {
                var resp = res.data;
                if( resp.code != 200){
                    app.alert({'content':resp.msg})
                    return;
                }
                that.setData({
                    user_info:resp.data.info
                });
            }
        });
    }
});