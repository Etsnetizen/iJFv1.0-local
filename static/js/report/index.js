;
var report_index_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        var that = this ;
        $(".wrap_search .search").click(function () {
                $(".wrap_search").submit();
        });
        $(".finish").click(function () {
                that.ops("finish",$(this).attr("data"))
        });
        $(".unfinished").click(function () {
                that.ops("unfinished",$(this).attr("data"))
        });
        $(".delay").click(function () {
                that.ops("delay",$(this).attr("data"))
        });
        $(".processing").click(function () {
                that.ops("processing",$(this).attr("data"))
        });
        $(".recover").click(function () {
                that.ops("recover",$(this).attr("data"))
        });

    },
    ops:function (act,id) {
        var callback = {
            'ok':function () {
                $.ajax({
                    url:common_ops.buildUrl('/ops'),
                    type:'POST',
                    data:{
                        act:act,
                        uid:$(".reference-box input[name=uid]").val(),
                        id:id,

                    },
                    dataType:'json',
                    success:function ( res ) {
                        var callback = null;
                        if( res.code == 200 ){
                            callback = function () {
                                window.location.href = window.location.href;
                            }
                        }
                        common_ops.alert(res.msg,callback )
                    }
                });
            },
            'cancel':null
        };
        common_ops.confirm("确认执行此操作？",callback)
    }
};
$(document).ready(function () {
    report_index_ops.init();
});