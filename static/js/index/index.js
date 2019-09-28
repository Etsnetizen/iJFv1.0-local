;
$(document).ready(function () {
    index_ops.init()
});
var index_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        var that = this;
        $(".wrap_index_search .index_search").click(function () {
                    $(".wrap_index_search").submit();
        });
    }
};