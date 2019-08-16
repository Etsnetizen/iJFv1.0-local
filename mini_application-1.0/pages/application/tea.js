// pages/application/stu.js

var app = getApp();

Page({
    data:{
      id:-1,
      tempFilePaths:[],
      random_code:0
    },
  formSubmit: function (e) {
      wx.showLoading();
    //console.log('form发生了submit事件，携带数据为：', e.detail.value)
      var that = this;
      var name = e.detail.value.name;
      var mobile = e.detail.value.phone;
      var address = e.detail.value.address;
      var description = e.detail.value.discribe;


      if (name.length < 1){
          wx.showToast({
            title: '姓名填写有误',
            icon: 'none',
            duration: 2000
          })
      }
      if (mobile.length < 11){
          wx.showToast({
            title: '手机号填写有误',
            icon: 'none',
            duration: 2000
          })
      }
      if (address.length < 1){
          wx.showToast({
            title: '地址填写有误',
            icon: 'none',
            duration: 2000
          })
      }
      if (description.length < 3){
          wx.showToast({
            title: '请详细描述你的问题',
            icon: 'none',
            duration: 2000
          })
      }


      var data = {
          attribute:1,
          name:name,
          mobile:mobile,
          address:address,
          description:description,
          random_code:that.data.random_code
      };
      wx.request({
            url:app.buildUrl('/submit'),
            header:app.getRequestHeader(),
            method:'POST',
            data:data,
            success:function ( res ) {
                var resp = res.data;
                if(resp.code != 200){
                    app.alert({'content':resp.msg});
                    return;
                }
                wx.hideLoading();
                wx.redirectTo({
                    url: 'finish'
                })
            }
        });




  },
  formReset: function () {
    //console.log('form发生了reset事件')
  },

  onLoad:function ( e ) {
      var that = this;
      that.setData({
        id:e.id
      })
  },
  upload: function () {
    let that = this;
    wx.chooseImage({
      count: 1, // 默认9
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function ( res ) {
          wx.showToast({
            title: '正在上传...',
            icon: 'loading',
            mask: true,
            duration: 1000
          });
          // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
          let tempFilePaths = res.tempFilePaths;
          that.setData({
              tempFilePaths:tempFilePaths
          });
          console.log(tempFilePaths);



          /**
         * 上传完成后把文件上传到服务器
         */
          var count = 0;
          //上传文件
              wx.uploadFile({
                  url: app.buildUrl('/submit/upload'),
                  filePath: tempFilePaths[0],
                  name: 'upfile',
                  header:app.getRequestHeader(),
              success: function (res) {
                      console.log(1110111);
                      console.log(res);
                      console.log(res.data);
                      console.log(22222);
                  count++;
              //如果是最后一张,则隐藏等待中
                  if ( res.statusCode == 200) {
                      wx.showToast({
                        title: '上传成功',
                        icon: 'none',
                        duration: 2000
                      });
                      var resp = JSON.parse(res.data);//!!!!! wocao!!踩坑踩好久！！
                      //python穿过来的是json，要转换为字典！！！！

                      console.log(1111);
                      console.log(resp);
                      console.log(resp.data);
                      console.log(2222);
                      console.log(resp.data.random_code);
                      console.log(3333);
                      that.setData({
                          random_code: resp.data.random_code
                      })
                  }
              },
              fail: function (res) {
                  wx.hideToast();
                  wx.showModal({
                    title: '错误提示',
                    content: '上传图片失败',
                    showCancel: false,
              })
            }
          });

    }});


  },


















  /**右上角分享
   */
  onShareAppMessage: function () {

  }
});