//获取应用实例
var app = getApp();
Page({
    data: {},
    onLoad() {

    },
    onShow() {
        this.getInfo();
    },
    getInfo:function () {
        var that = this;
        wx.request({
            url:app.buildUrl('/member/info'),
            header:app.getRequestHeader(),
            success:function ( res ) {
                var resp = res.data;
                if( resp.code != 200 ){
                    wx.showToast({
                        title: '上传成功',
                        icon: 'none',
                        duration: 2000
                      });
                }
                that.setData({
                    user_info:resp.data.info
                });
            }
        });
    },
    toMyReport:function () {
        wx.navigateTo({
           url:'/pages/my/order_list'
       })
    }

});