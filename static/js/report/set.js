;
var report_set_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        $(".wrap_report_set .save").click(function () {
            var btn_target = $(this);
            if(btn_target.hasClass('disabled')){
                common_ops.alert('正在处理中，请不要重复点击');
                return;
            }
            var remark = $(".wrap_report_set input[name=remark]").val();
            btn_target.addClass('disabled');
            var data  = {
                remark:remark,
                uid:$(".wrap_report_set input[name=uid]").val(),
                id:$(".wrap_report_set input[name=id]").val()
            };
            $.ajax({
                url:common_ops.buildUrl('/set'),
                type:'POST',
                data:data,
                dataType:'json',
                success:function ( res ) {
                    btn_target.removeClass('disabled');
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function () {
                            window.location.href = common_ops.buildUrl('/')
                        }
                    }
                    common_ops.alert(res.msg,callback)
                }
            });
        });
    }
};
$(document).ready(function () {
    report_set_ops.init();
});