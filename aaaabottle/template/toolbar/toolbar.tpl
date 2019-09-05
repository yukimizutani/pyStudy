<form class="content_type_boxContainer" method="GET" action="/">
    <button class="content_type_box" name='contentType' value='top'>Top</button>
	<button class="content_type_box" name='contentType' value='myPage'>マイページ</button>
	<button class="content_type_box" name='contentType' value='code'>マイコーデ</button>
	<button class="content_type_box" name='contentType' value='trade'>コーデトレード(Coming soon)</button>
    <button class="content_type_box" name='contentType' value='shop'>遊べるお店(Coming soon)</button>
</form>
<style type="text/css">
.content_type_boxContainer {
    display: table;
    table-layout: fixed;
    width: 100%;
    box-sizing: border-box;
}
.content_type_box {
    display: inline-block;
    vertical-align: middle;
    text-align: center;
    text-color: black;
    width: 20%;
    height: 100%;
    max-height: 42px;
    background-color: #F28CBB;
    font-size: 1em;
    overflow: hidden;
}
.content_type_box:hover {
   color: #000080; /* 文字色 */
   background-color: #ccffff; /* 背景色 */
   border: 1px solid blue; /* 実線の枠を付ける(任意) */
}
</style>