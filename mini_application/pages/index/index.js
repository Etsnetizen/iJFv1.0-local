//login.js
//获取应用实例
var app = getApp();
Page({
  data: {
    remind: '加载中',
    angle: 0,
    userInfo: {},
      regFlag:true
  },
  goToIndex:function(){
    wx.switchTab({//witchTab为转换页面
      url: '/pages/food/index',
    });
  },
  //onload是加载小程序，第一步
  onLoad:function(){
    wx.setNavigationBarTitle({
      title: app.globalData.shopName
    });
    this.checkLogin()//检查是否已经登陆
  },

  onReady: function(){
    var that = this;
    setTimeout(function(){
      that.setData({
        remind: ''
      });
    }, 1000);
    wx.onAccelerometerChange(function(res) {
      var angle = -(res.x*30).toFixed(1);
      if(angle>14){ angle=14; }
      else if(angle<-14){ angle=-14; }
      if(that.data.angle !== angle){
        that.setData({
          angle: angle
        });
      }
    });
  },
    checkLogin:function(){
        var that = this;
         wx.login({
             success:function( res ){
                 if( !res.code ){
                    app.alert( { 'content':'登录失败，请再次点击~~' } );
                    return;
                 }
                 wx.request({//这个是微信的方法
                    url:app.buildUrl( '/member/check-reg' ),
                    header:app.getRequestHeader(),////如果不加这句，发送类型为json类型，并不是表单提交，之前后台网址都是js提交，注意区分
                    method:'POST',
                    data:{ code:res.code },
                    success:function( res ){
                        if( res.data.code != 200 ){//wx的request 返回的data才是开发者服务器返回的数据，所以要加data
                            that.setData({
                                regFlag:false
                            });
                            return;
                        }
                        app.setCache("token",res.data.data.token);
                        //that.goToIndex();
                    }
                });
             }
         });
    },
  login: function ( e ) {//根据官方文档会传过来参数e
      //app.console( e );//看看e是什么鬼
      //app.console("test");
      var that = this;
    if(!e.detail.userInfo){
      app.alert({"content":"登陆失败！"});
      return;
    }

    //如果授权成功，发送form
    var data = e.detail.userInfo;
    wx.login({//res为微信后台传过来的数据，与py后台无关
      success:function ( res ) {
        if(!res.code){
          app.alert({'content':"登陆失败"});
          return;
        }
        data['code'] = res.code;
        wx.request({
              url:app.buildUrl('/member/login'),
              header:app.getRequestHeader(),//如果不加这句，发送类型为json类型，并不是表单提交，之前后台网址都是js提交，注意区分
              method:'POST',
              data:data,
        success:function ( res ) {
              //app.alert({'content':'登陆成功！！！'})
            if( res.data.code != 200){
                app.alert({'content':res.data.msg});
                return;
            }
            app.setCache("token",res.data.data.token);
            that.goToIndex();

      }
    });
      }
    });




  }
});