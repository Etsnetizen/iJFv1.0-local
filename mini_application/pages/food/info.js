//pay_info.js
//获取应用实例
var app = getApp();
var WxParse = require('../../wxParse/wxParse.js');
var utils = require('../../utils/util.js');
Page({
    data: {
        autoplay: true,
        interval: 3000,
        duration: 1000,
        swiperCurrent: 0,
        hideShopPopup: true,
        buyNumber: 1,
        buyNumMin: 1,
        buyNumMax:1,
        canSubmit: false, //  选中时候是否允许加入购物车
        shopCarInfo: {},
        shopType: "addShopCar",//购物类型，加入购物车或立即购买，默认为加入购物车,
        id: 0,
        shopCarNum: 4,
        commentCount:2
    },
    onLoad: function ( e ) {
        var that = this;




        that.setData({
            id:e.id

        });


        that.setData({
            "info": {
                "id": 1,
                "name": "无法获取商品信息，请检查网络连接",
                "summary": '<p>多色可选的马甲</p><p><img src="http://www.timeface.cn/uploads/times/2015/07/071031_f5Viwp.jpg"/></p><p><br/>相当好吃了</p>',
                "total_count": 0,
                "comment_count": 0,
                "stock": 0,
                "price": "00.00",
                "main_image": "/images/food.jpg",
                "pics": [ '/images/food.jpg','/images/food.jpg' ]
            },
            buyNumMax:2,
            commentList: [
                {
                    "score": "好评",
                    "date": "2017-10-11 10:20:00",
                    "content": "非常好吃，一直在他们加购买",
                    "user": {
                        "avatar_url": "/images/more/logo.png",
                        "nick": "angellee 🐰 🐒"
                    }
                },
                {
                    "score": "好评",
                    "date": "2017-10-11 10:20:00",
                    "content": "非常好吃，一直在他们加购买",
                    "user": {
                        "avatar_url": "/images/more/logo.png",
                        "nick": "angellee 🐰 🐒"
                    }
                }
            ],

        });


        },
    onShow:function(){
        this.getInfo();//获取详情,没有必要写在onload里，因为在onshow既可以onload的时候触发，又可以每次显示这个页面时候再触发

    },
    goShopCar: function () {
        wx.reLaunch({
            url: "/pages/cart/index"
        });
    },
    toAddShopCar: function () {
        this.setData({
            shopType: "addShopCar"
        });
        this.bindGuiGeTap();//hideShopPopup: false
    },
    tobuy: function () {
        this.setData({
            shopType: "tobuy"
        });
        this.bindGuiGeTap();
    },
    addShopCar: function () {
        //添加到购物车函数
        var that = this;
        var data = {
            'id':that.data.info.id,
            'number':that.data.buyNumber//购买数量
        };
        wx.request({
            url:app.buildUrl('/cart/set'),
            header:app.getRequestHeader(),
            method:'POST',
            data:data,
            success:function ( res ) {
                var resp = res.data;
                app.alert({'content':resp.msg});
                that.setData({
                    hideShopPopup:true//隐藏加入购物车的那个小弹窗
                });
            }
        });

    },
    buyNow: function () {
        var data = {
          goods:[{
              'id':this.data.info.id,
              'price':this.data.info.price,
              'number':this.data.buyNumber,
          }]
        };
        this.setData({
                    hideShopPopup:true//隐藏加入购物车的那个小弹窗
                });
        wx.navigateTo({

            url: "/pages/order/index?data=" + JSON.stringify( data )
        });
    },
    /**
     * 规格选择弹出框
     */
    bindGuiGeTap: function () {
        this.setData({
            hideShopPopup: false
        })
    },
    /**
     * 规格选择弹出框隐藏
     */
    closePopupTap: function () {
        this.setData({
            hideShopPopup: true
        })
    },
    numJianTap: function () {
        if( this.data.buyNumber <= this.data.buyNumMin){
            return;
        }
        var currentNum = this.data.buyNumber;
        currentNum--;
        this.setData({
            buyNumber: currentNum
        });
    },
    numJiaTap: function () {
        if( this.data.buyNumber >= this.data.buyNumMax ){
            return;
        }
        var currentNum = this.data.buyNumber;
        currentNum++;
        this.setData({
            buyNumber: currentNum
        });
    },
    //事件处理函数
    swiperchange: function (e) {
        this.setData({
            swiperCurrent: e.detail.current
        })
    },
    getInfo:function () {
        var that = this;
        wx.request({
            url:app.buildUrl('/food/info'),
            header:app.getRequestHeader(),
            data:{
                id:that.data.id
            },
            success:function ( res ) {
                var resp = res.data;
                if(resp.code != 200){
                    app.alert({'content':resp.msg})

                }
                that.setData({
                   info:resp.data.info,//直接info里面的数据会自动匹配，不用一个个写出来
                   buyNumMax:resp.data.info.stock,
                    shopCarNum: resp.data.cart_number
                });
                WxParse.wxParse('article','html',that.data.info.summary,that,5);
            }
        });
    },
    onShareAppMessage:function (  ) {
        //微信分享函数https://www.jianshu.com/p/31e83ce4c389
        var that = this;
        return {
            title:that.data.info.name,//设置转发的标题
            path:'/page/food/info?id=' + that.data.info.id,
            success:function ( res ) {
                //转发成功的话
                wx.request({
                    url:app.buildUrl('/member/share'),
                    header:app.getRequestHeader(),
                    method:'POST',
                    data:{
                        url:utils.getCurrentPageUrlWithArgs()
                        //获取带参数的页面的url

                    },
                success:function () {
                        app.alert({'content':'感谢你转发'});
                    }
                    
                });
            },
            fail: function ( res ) {
                
            }
            
        }
    }
});
