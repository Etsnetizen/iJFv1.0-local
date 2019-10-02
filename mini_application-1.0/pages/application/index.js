//index.js
//获取应用实例
var app = getApp();
Page({
   data:{
        isConnect:false,
        attribute:{
            '0':'正在获取',
            '1':'正在获取'
        },
       maxsize_report_index:false
   },
   onLoad:function(){
       this.ConnectToDataBase();
       this.CheckMaxsizeReport()
    },
   onShow:function () {
        var that = this;
        this.ConnectToDataBase()
    },
   ConnectToDataBase:function () {
        wx.showLoading();
        var that = this;
        wx.request({
            url:app.buildUrl('/index/connect'),
            header:app.getRequestHeader(),
            success:function ( res ) {
                var resp = res.data;
                if( resp.code != 200 ){
                    app.alert({'content':resp.msg} );
                    wx.hideLoading();
                    return;
                }
                that.setData({
                    isConnect:true,
                    attribute:resp.data.attribute
                });
                wx.hideLoading();
            }
        });
    },
   toStuReportPage:function ( e ) {
       wx.navigateTo({
           url:'/pages/application/stu?id=' + e.currentTarget.dataset.id
       })
   },
   toTeaReportPage:function ( e ) {
       wx.navigateTo({
           url:'/pages/application/tea?id=' + e.currentTarget.dataset.id
       })
   },
   CheckMaxsizeReport:function () {
        wx.showLoading();
        var that = this;
        wx.request({
            url:app.buildUrl('/index/check'),
            header:app.getRequestHeader(),
            success:function ( res ) {
                var resp = res.data;
                if( resp.code == 200 ){
                    that.setData({
                        maxsize_report_index:true
                    })
                }
                wx.hideLoading();
            }
        });
    }
});


