;
$(document).ready(function () {
    submit_report.init();
});
var submit_report = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        $(".wrap_report_stu_submit .stu_submit").click(function () {
            alert('111');
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")){
                alert("正在提交中");
                return;
            }
                var stu_name = $(".wrap_report_stu_submit input[name=stu_name]").val();
                var stu_num = $(".wrap_report_stu_submit input[name=stu_num]").val();
                var stu_class = $(".wrap_report_stu_submit input[name=stu_class]").val();
                var stu_mobile = $(".wrap_report_stu_submit input[name=stu_tel]").val();
                var stu_address = $(".wrap_report_stu_submit input[name=stu_adr]").val();
                var stu_description = $(".wrap_report_stu_submit input[name=stu_desc]").val();
                btn_target.addClass('disabled');
                var stu_data = {
                    name:stu_name,
                    student_id:stu_num,
                    class_name:stu_class,
                    mobile:stu_mobile,
                    address:stu_address,
                    description:stu_description,
                    attribute:$(".wrap_report_stu_submit input[name=stu_attribute]").val()
                };
                $.ajax({
                    url:common_ops.buildUrl("report"),
                    dataType:'json',
                    type:'POST',
                    data:stu_data,
                    success:function ( res ) {
                        btn_target.removeClass('disabled');
                        if( res.code == 200 ){
                            window.location.href = common_ops.buildUrl('/report/finish')
                        }
                        alert(res.msg);
                    }
                })

        });
        $(".wrap_report_tea_submit .tea_submit").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")){
                alert("正在提交中");
                return;
            }
                var tea_name = $(".wrap_report_tea_submit input[name=tea_name]").val();
                var tea_mobile = $(".wrap_report_tea_submit input[name=tea_tel]").val();
                var tea_address = $(".wrap_report_tea_submit input[name=tea_adr]").val();
                var tea_description = $(".wrap_report_tea_submit input[name=tea_desc]").val();
                /*
                if(tea_name.length < 1 ){
                    alert('请输入规范的姓名');
                    return;
                }
                if(tea_mobile.length < 8 ){
                    alert('请输入规范的手机号');
                    return;
                }
                if(tea_address.length < 2 ){
                    alert('请输入规范的地址');
                    return;
                }
                if(tea_description.length < 7 ){
                    alert('请输入规范的描述，不少于7个字符');
                    return;
                }*/
                btn_target.addClass('disabled');
                var data = {
                    name:tea_name,
                    mobile:tea_mobile,
                    address:tea_address,
                    description:tea_description,
                    attribute:$(".wrap_report_tea_submit input[name=tea_attribute]").val()
                };
                $.ajax({
                    url:common_ops.buildUrl("report"),
                    dataType:'json',
                    type:'POST',
                    data:data,
                    success:function ( res ) {
                        btn_target.removeClass('disabled');
                        if( res.code == 200 ){
                            window.location.href = common_ops.buildUrl('/report/finish')
                        }
                        alert(res.msg);
                    }
                })


        })
    }
};