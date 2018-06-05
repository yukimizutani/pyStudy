<div class="boxContainer">
	<div class="box" onclick=show('top')>マイベージ</div>
	<div class="box" onclick=show("code")>マイコーデ</div>
	<div class="box" onclick=show("trade")>コーデトレード(Coming soon)</div>
    <div class="box" onclick=show("shop")>遊べるお店(Coming soon)</div>
</div>
<style type="text/css">
.boxContainer {
    display: table;
    table-layout: fixed;
    width: 100%;
    max-width: 100%;
    min-width: 480px;
    margin: 0 auto;
    padding: 0 30px;
    box-sizing: border-box;
}
.box {
    display: table-cell;
    vertical-align: middle;
    text-align: center;
    color: #ffffff;
    border: 1px dotted gray;
    text-color: black;
}
.box:hover {
   color: #000080; /* 文字色 */
   background-color: #ccffff; /* 背景色 */
   border: 1px solid blue; /* 実線の枠を付ける(任意) */
}

</style>