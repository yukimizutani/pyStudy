<div class="item_content">
<div id="item_list_title">アイテム一覧</div>
<p>対象バージョン：<br>
<select id="select_version" name="version">
<option value="0">全て</option>
<option value="1">第一弾</option>
<option value="2">第二弾</option>
</select></p>
<div id="item_list">
{% for key, items in codeDict.items() %}
<div class="item_column show">
{% for item in items %}
<img class="item" src="static/images/{{key}}/{{item}}" width="120" height="100"/>
{% endfor %}
</div>
{% endfor %}
</div>
<button type="button" id="save">保存</button>
<button type="button" id="reset">リセット</button>
<button type="button" id="initialize">初期化</button>
</div>
<style type="text/css">
.item_content {
    display: block;
    border: 1px dotted gray;
    font-size: 50px;
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
.item_column {
    display: block;
}
.item {
    display: inline-block;
    vertical-align: middle;
    text-align: center;
    color: #ffffff;
    width: 18%;
    height: 20%;
    border: 1px solid pink;
    filter: grayscale(100%);
}
.item:hover {
   background-color: #ccffff; /* 背景色 */
   border: 1px solid blue; /* 実線の枠を付ける(任意) */
}
.greyout {
    filter: grayscale(100%);
}
.blur {
   filter: blur(3px);
}
button, select {
    font-size: 50px;
}
.active {
    color: black;
}
#nav a {
    font-size: 50px;
}
option  {
    font-size: 50px;
}
}
</style>

<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<script language="javascript">

    function createNavigation(){
        $('#item_list').before('<div id="nav"></div>');
        $(".item_column.show").each(function () {
            if($(this).children(".item").length == $(this).children(".greyout").length){
                $(this).removeClass("show");
                $(this).addClass("empty");
            }
        });
        var rowsShown = 6;
        var rowsTotal = $(".item_column.show").length;
        var numPages = rowsTotal/rowsShown;
        for(i = 0;i < numPages;i++) {
            var pageNum = i + 1;
            $('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');
        }
        $("div:visible[class*='item_column']").hide();
        $(".item_column.show").slice(0, rowsShown).show();
        $('#nav a:first').addClass('active');
        $('#nav a').bind(clickEventType, function(){
            $('#nav a').removeClass('active');
            $(this).addClass('active');
            var currPage = $(this).attr('rel');
            var startItem = currPage * rowsShown;
            var endItem = startItem + rowsShown;
            $(".item_column.show").css('opacity','0.0').hide().slice(startItem, endItem).
            css('display','table-row').animate({opacity:1}, 300);
        });
    }

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
        createNavigation();
    });

    $('#save').on('click', function() {
        var selectedItems = $(".greyout");
        var images = [];
        selectedItems.each(function () {
            images.push( $(this).attr("src") );
        });

        $(document).ready(function() {
            $.ajax({
                type: "POST",
                data: JSON.stringify(images),
                contentType: "application/json; charset=utf-8",
                url: "http://localhost:8080/save_items"
            }).then(function(data) {
                selectedItems.each(function () {
                    $(this).hide();
                });
                $('#nav').remove();
                createNavigation();
            });
        });
    });

    $('#reset').on('click', function() {
        var allItems = $(".item");
        var images = [];
        allItems.each(function () {
            images.push( $(this).attr("src") );
        });
        var userInfo = {"usr":"admin"};
        userInfo["code"] = images;
        $(document).ready(function() {
            $.ajax({
                type: "POST",
                data: userInfo,
                contentType: "application/json; charset=utf-8",
                url: "http://localhost:8080/reset_items"
            }).then(function(data) {
                $(".greyout").each(function () {
                    $(this).removeClass(addclass);
                    $(this).show();
                });
                $(".empty").each(function () {
                    $(this).removeClass("empty");
                    $(this).addClass("show");
                    $(this).show();
                });
                $('#nav').remove();
                createNavigation();
            });
        });
    });

    $('#initialize').on('click', function() {
        var userInfo = {"usr":"admin"}
        $(document).ready(function() {
            $.ajax({
                type: "POST",
                data: userInfo,
                contentType: "application/json; charset=utf-8",
                url: "http://localhost:8080/initialize"
            }).then(function(data) {
                window.location.reload();
            });
        });
    });

    $(function($) {
        $('#select_version').change(function() {
            var str = $(this).val();
            console.log(str);
        });
    });
</script>