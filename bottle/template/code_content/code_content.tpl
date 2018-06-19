<div class="item_content">
<div id="item_list_title">アイテム一覧</div>
<p>対象バージョン：<br>
<select id="select_version" name="version">
<option value="0">全て</option>
<option value="1">第一弾</option>
<option value="2">第二弾</option>
<option value="3">第三弾</option>
</select></p>
<div id="item_list">
{% for key, items in codeDict.items() %}
<div id="item_column">
{% for item in items %}
<img class="item" src="static/images/{{key}}/{{item}}" width="120" height="100"/>
{% endfor %}
</div>
{% endfor %}
</div>
<button type="button" id="save">保存</button>
<button type="button" id="reset">リセット</button>
</div>
<style type="text/css">
.item_content {
    display: block;
    border: 1px dotted gray;
}
#select_version {
}
#item_list_title {
    position: relative;
    display: block;
}
#item_list {
    position: relative;
    height: 100%;
    border: 5px double;
    margin: 5px;
    display: block;
    table-layout: fixed;
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
    padding: 0 30px;
    box-sizing: border-box;
}
#item_column {
    display: block;
}
.item {
    display: inline-block;
    vertical-align: middle;
    text-align: center;
    color: #ffffff;
    width: 20%;
    height: 25%;
    border: 1px solid pink;
    filter: grayscale(100%);
}
.item:hover {
   background-color: #ccffff; /* 背景色 */
   border: 1px solid blue; /* 実線の枠を付ける(任意) */
}
.greyout {
    filter: blur(3px);
}
.blur {
    filter: blur(3px);
}
#buttons {

}
}
</style>

<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<script language="javascript">
    var clickEventType=((window.ontouchstart!==null)?'click':'touchstart');
    var addclass = 'greyout';
    $('.item').bind(clickEventType, function(){
        if ($(this).hasClass(addclass)){
            $(this).removeClass(addclass);
        } else {
            $(this).addClass(addclass);
        }
    });
    var addclass2 = 'blur';
    var dblClickEvent=((window.ontouchstart!==null)?'dblclick':'taphold');
   $('.item').bind(dblClickEvent, function(){
        if ($(this).hasClass(addclass2)){
            $(this).removeClass(addclass2);
        } else {
            $(this).addClass(addclass2);
        }
    });

    $(document).ready(function(){
    $('#item_list').before('<div id="nav"></div>');
    var rowsShown = 6;
    var rowsTotal = $("div:visible[id*='item_column']").length;
    var numPages = rowsTotal/rowsShown;
    for(i = 0;i < numPages;i++) {
        var pageNum = i + 1;
        $('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');
    }
    $("div:visible[id*='item_column']").hide();
    $("[id*='item_column']").slice(0, rowsShown).show();
    $('#nav a:first').addClass('active');
    $('#nav a').bind(clickEventType, function(){
        $('#nav a').removeClass('active');
        $(this).addClass('active');
        var currPage = $(this).attr('rel');
        var startItem = currPage * rowsShown;
        var endItem = startItem + rowsShown;
        $("[id*='item_column']").css('opacity','0.0').hide().slice(startItem, endItem).
        css('display','table-row').animate({opacity:1}, 300);
    });
    });

    $('#save').on('click', function() {
        var selectedItems = $(".greyout");

    });
</script>