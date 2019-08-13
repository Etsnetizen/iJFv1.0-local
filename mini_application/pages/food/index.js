//pay_info.js
//获取应用实例
var app = getApp();
Page({
    data: {
        indicatorDots: true,
        autoplay: true,
        interval: 3000,
        duration: 1000,
        loadingHidden: false, // loading
        swiperCurrent: 0,
        categories: [],
        activeCategoryId: 0,
        goods: [],
        scrollTop: "0",
        loadingMoreHidden: true,
        searchInput: '',
        p:1,//记录分页页数
        processing:false//是否正在处理
    },
    onLoad: function () {
        var that = this;

        wx.setNavigationBarTitle({
            title: app.globalData.shopName
        });


        this.getBannerAndCat();
    },
    onShow:function(){
      //onShow:微信方法，每次显示这个页面时都会触发
        this.getBannerAndCat();
    },
    scroll: function (e) {
        var that = this, scrollTop = that.data.scrollTop;
        that.setData({
            scrollTop: e.detail.scrollTop
        });
    },
    //事件处理函数
    swiperchange: function (e) {
        this.setData({
            swiperCurrent: e.detail.current
        })
    },
	listenerSearchInput:function( e ){
	        this.setData({
	            searchInput: e.detail.value
	        });
	 },
	 toSearch:function( e ){
	        this.setData({
	            p:1,
	            goods:[],
	            loadingMoreHidden:true
	        });
	        this.getFoodList();
	},
    tapBanner: function (e) {
        if (e.currentTarget.dataset.id != 0) {
            wx.navigateTo({
                url: "/pages/food/info?id=" + e.currentTarget.dataset.id
            });
        }
    },
    toDetailsTap: function (e) {
        //前往详情页面的函数
        wx.navigateTo({
            url: "/pages/food/info?id=" + e.currentTarget.dataset.id
        });
    },
    getBannerAndCat:function () {
        var that = this;
        wx.request({
            url:app.buildUrl('/food/index'),
            header:app.getRequestHeader(),
            success:function (res) {
                var resp = res.data;
                if( resp.code != 200 ){
                    app.alert({'content':resp.msg} );
                    return;
                }
                that.setData({
                    banners:resp.data.banner_list,
                    categories:resp.data.cat_list
                });
                that.getFoodList()
            }
        });
    },
    catClick:function( e ){
        this.setData({
            activeCategoryId:e.currentTarget.id,
            p:1,
            goods:[],
            loadingMoreHidden:true
        });
        this.getFoodList();

    },
    onReachBottom:function(){
        //这是微信的翻页方法，在翻页的时候会自动触发，十分简单
        var that = this;
        setTimeout(function () {
            that.getFoodList();
        },500);
    },
    getFoodList:function () {
        var that = this;

        if(that.data.processing){
            return;
        }
        if(!that.data.loadingMoreHidden ){
            return;
        }
        that.setData({
            processing:true
        });

        wx.request({
            url:app.buildUrl('/food/search'),
            header: app.getRequestHeader(),
            data:{
                    cat_id:that.data.activeCategoryId,
                    mix_kw:that.data.searchInput,
                    p:that.data.p
            },
            success:function ( res ) {
                var resp = res.data;
                if( resp.code != 200){
                    app.alert({'content':resp.msg});
                    return;
                }
                var goods = resp.data.list;
                that.setData({
                    goods:that.data.goods.concat(goods),
                    //如果直接goods:goods，则翻页的时候会替换掉原来的内容，必须加上新的内容才可以
                    //goods在data（data是页面配置）里定义了
                    p:that.data.p + 1,
                    processing:false
                });

                if(resp.data.has_more == 0){
                    that.setData({
                        loadingMoreHidden:false//取消隐藏，即把那个底线显示出来
                    });
                }
            }
        });
    }

});
