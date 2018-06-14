<div class="item_content">
<div id="item_list_title">アイテム一覧</div>
<p>対象バージョン：<br>
<select name="version">
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
</div>
<style type="text/css">
.item_content {
    position: relative;
    display: block;
    border: 1px dotted gray;
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
    min-width: 480px;
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
    border: 1px solid pink;
}
.item:hover {
   color: #000080; /* 文字色 */
   background-color: #ccffff; /* 背景色 */
   border: 1px solid blue; /* 実線の枠を付ける(任意) */
}
.greyout {
    filter: grayscale(100%);
}
.blur {
    filter: blur(3px);
}
</style>

<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<script language="javascript">
    var addclass = 'greyout';
    var $cols = $('.item').click(function(e) {
        if ($(this).hasClass(addclass)){
            $(this).removeClass(addclass);
        } else {
            $(this).addClass(addclass);
        }
    });
    var addclass2 = 'blur';
    $('.item').dblclick(function(e) {
        if ($(this).hasClass(addclass2)){
            $(this).removeClass(addclass2);
        } else {
            $(this).addClass(addclass2);
        }
    });
</script>