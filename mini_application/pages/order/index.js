//获取应用实例
var app = getApp();

Page({
    data: {
        goods_list: [
            /*
            {
                id:22,
                name: "小鸡炖蘑菇",
                price: "85.00",
                pic_url: "/images/food.jpg",
                number: 1,
            }*/],

        default_address: null/*{
            /*name: "编程浪子",
            mobile: "12345678901",
            detail: "上海市浦东新区XX",
            null
        }*/,
        yun_price: "0.00",
        pay_price: "0.00",
        total_price: "0.00",
        params: null
    },
    onShow: function () {
        var that = this;
        this.getOrderInfo();
    },
    onLoad: function (e) {
        var that = this;
        that.setData({
            params:JSON.parse( e.data )
        });
    },
    createOrder: function (e) {
        wx.showLoading();
        var that = this;
        var data = {
            type:this.data.params.type,
            goods:JSON.stringify(this.data.params.goods),
        };
        wx.request({
            url:app.buildUrl('/order/create'),
            header:app.getRequestHeader(),
            method:'POST',
            data:data,
            success:function ( res ) {
                wx.hideLoading();
            }
        });





        wx.navigateTo({
            url: "/pages/my/order_list"
        });

    },
    addressSet: function () {
        wx.navigateTo({
            url: "/pages/my/addressSet"
        });
    },
    selectAddress: function () {
        wx.navigateTo({
            url: "/pages/my/addressList"
        });
    },
    getOrderInfo:function () {
        var that = this;
        var data = {
            type:this.data.params.type,
            goods:JSON.stringify(this.data.params.goods),
        };
        wx.request({
            url:app.buildUrl('/order/info'),
            header:app.getRequestHeader(),
            method:'POST',
            data:data,
            success:function ( res ) {
                var resp = res.data;
                if(resp.code != 200){
                    app.alert({'content':resp.msg});
                    return;
                }
                that.setData({
                    goods_list:resp.data.food_list,
                    default_address: resp.data.default_address,
                    yum_price:resp.data.yun_price,
                    pay_price: resp.data.pay_price,
                    total_price: resp.data.total_price
                })
            }
        });

    }
});
