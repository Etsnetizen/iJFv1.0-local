var app = getApp();
Page({
    data: {
        statusType: ["全部","待处理", "处理中", "延期处理", "无法处理","已完成"],
        status:[ "10","-8","-7","-9","0","1" ],
        currentType: 0,
        tabClass: ["", "", "", "", "", ""]
    },
    statusTap: function (e) {
        var curType = e.currentTarget.dataset.index;
        this.data.currentType = curType;
        this.setData({
            currentType: curType
        });
        this.onShow();
    },
    onShow: function () {
        var that = this;
        /*that.setData({
            order_list: [
                {
					status: -8,
                    status_desc: "待支付",
                    date: "2018-07-01 22:30:23",
                    order_number: "20180701223023001",
                    note: "记得周六发货",
                    total_price: "85.00",
                    goods_list: [
                        {
                            pic_url: "/images/food.jpg"
                        },
                        {
                            pic_url: "/images/food.jpg"
                        }
                    ]
                }
            ]
        });*/
        this.getReportList();
    },
    getReportList:function () {
        wx.showLoading();
        var that = this;
        wx.request({
            url:app.buildUrl('/my/report'),
            header:app.getRequestHeader(),
            data:{
                status: that.data.status[that.data.currentType],
            },
            success:function ( res ) {
                var resp = res.data;
                if(resp.code != 200){
                    app.alert({'content':resp.msg});
                    return;
                }
                that.setData({
                    report_list:resp.data.report_list
                });
                wx.hideLoading();
            }
        })
    },
    reportCancel:function ( e ) {
        this.orderOps( e.currentTarget.dataset.id ,"cancel",'你确定要取消此报障？');
    }
});
