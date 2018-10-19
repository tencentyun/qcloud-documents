本文档介绍web端如何请求服务端，通过js调用腾讯云万象优图REST API进行图片的上传、下载、查询、复制和删除。其中签名需要向开发者服务器请求，开发者服务器鉴权服务部署参考鉴权服务部署示例。

1. web前端部署与代码示例
将web前端部署在与服务端同域下，web前端代码可以参考以下示例，示例页面参见web示例页面。
```
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr">
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<title>腾讯云万象优图 - 示例程序</title>
<script type="text/javascript" src="../jquery-2.1.4.min.js"></script>
<script type="text/javascript" src="../jquery.form.min.js"></script>
</head>

<div>
	<h2>腾讯云万象优图 - 示例程序</h2>
    <form id="uploadForm">
    	<input type="file" name="FileContent"></input>
    	<input id="subbtn" type="submit">
    </form> 

 	<div id="downloadRet" style="display:none">
 		<h3>下载链接</h3>
 		<span id="downloadUrl"></span><input id="downloadBtn" type="button" value="下载"><br/>
 		<img id="downloadImg" src=""></img>
 		<h3>文件ID</h3>
 		<div id="fileid"></div>
 		<h3>管理URL</h3>
 		<span id="url"></span>  
                <input id="queryBtn" type="button" value="查询">  
                <input id="deleteBtn" type="button" value="删除">  
                <input id="copyBtn" type="button" value="复制"><br/>
 		<span id="imgInfo"></span>
 	</div>
</div>


<script type="text/javascript">

$(document).ready(function() {
	initUploadForm();
});

$('input[name=FileContent]').change(function () {
	initUploadForm();
});

$('body').on('click', '#downloadBtn', function(){
	$('#downloadImg').attr('src', $('#downloadUrl').text());
});

$('body').on('click', '#deleteBtn', function(){
	var manageUrl = $('#url').text();
	if (!manageUrl) {
		alert('尚未获取管理url');
		return false;
	}
	manageUrl = manageUrl + '/del';
	// 请将以下获取签名的链接换成您部署好的服务端http url
	// 建议通过业务登录态检查来增强安全性，避免签名被非法获取
	$.getJSON('http://203.195.194.28/php/getsign.php?type=delete&url='+encodeURIComponent(manageUrl), 
              function(data) {
		var sign = data.sign,
			url = manageUrl + '?sign=' + encodeURIComponent(sign);
		$.ajax({
		    type: "POST",
		    url: url,
		    data: {},
		    success: function() {
		  	    alert('删除成功');
		    },
		    contentType:"multipart/form-data",
		    dataType: 'json'
		});
	});
});

$('body').on('click', '#copyBtn', function(){
	var manageUrl = $('#url').text();
	if (!manageUrl) {
		alert('尚未获取管理url');
		return false;
	}
	manageUrl = manageUrl + '/copy';
	// 请将以下获取签名的链接换成您部署好的服务端http url
	// 建议通过业务登录态检查来增强安全性，避免签名被非法获取
	$.getJSON('http://203.195.194.28/php/getsign.php?type=copy&url='+encodeURIComponent(manageUrl), 
             function(data) {
		var sign = data.sign,
			url = manageUrl + '?sign=' + encodeURIComponent(sign);
		$.ajax({
		    type: "POST",
		    url: url,
		    data: {},
		    success: function(ret) {
		  	    alert('复制成功');
		    },
		    contentType:"multipart/form-data",
		    dataType: 'json'
		});
	});
});

$('body').on('click', '#queryBtn', function(){
	var manageUrl = $('#url').text();
	if (!manageUrl) {
		alert('尚未获取管理url');
		return false;
	}
	$.ajax({
	    type: "GET",
	    url: manageUrl,
	    data: {},
	    success: function(data) {
	  	    $('#imgInfo').text(JSON.stringify(data));
	    },
	    error:function(ret) {
	    	$('#imgInfo').text(ret.responseText);
	    },
	    dataType: 'json'
	});
});

function initUploadForm () {
	// 请将以下获取签名的链接换成您部署好的服务端http url
	// 建议通过业务登录态检查来增强安全性，避免签名被非法获取
	$.getJSON('http://203.195.194.28/php/getsign.php', function(data) {
		var sign = data.sign,
		    url = data.url + '?sign=' + encodeURIComponent(sign);

		var options = { 
                    type: 'post',
                    url: url,
                    dataType: 'json',
                    contentType:"multipart/form-data",
		    success:function(ret) { 
		    	$('#downloadUrl').html(ret.data.download_url);
		    	$('#fileid').text(ret.data.fileid);
		    	$('#url').text(ret.data.url);
		    	$('#downloadRet').show();
		    },
		    error:function (ret) {
		    	alert(ret.responseText);
		    }
		}; 
		 
		// pass options to ajaxForm 
		$('#uploadForm').ajaxForm(options);
	});
}

</script>
</body>
```
2. 测试
访问 web 前端入口，进行测试调用，验证各种操作能够正常执行。