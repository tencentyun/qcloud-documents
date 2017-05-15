## 1 初始化 

调用示例：
```
QALHttpRequest.init();
```

## 2 设置cache大小
设置Http的缓存大小，缓存get请求的结果。空闲空间不足时将通过LRU淘汰数据。参数size为缓存大小，单位为字节，填0表示关闭Cache.
调用示例： 
```
QALHttpRequest.setCacheMaxSize(10*1024*1024);
```

## 3 发送请求 

GET调用示例： 
```
QALHttpRequest request = new QALHttpRequest("http://www.qq.com");
request.setRequestMethod(http.GET);
request.setContentType("text/html");            
Log.i(TAG,"request:" + url );
request.request(new QALHttpValueCallBack(){                        
	@Override
	public void onFailed(int arg0, String arg1) {
		Log.e(TAG,"http request error:" + arg0 +":" + arg1);
	}

	@Override
	public void onFinished(QALHttpResponse arg0) {                         
	   Log.i(TAG,"http rsp status:" +  arg0.getStatus() +"|len:" + arg0.getBody().length  +"|costTime:" + use_time );
	}
						 
});
```

POST调用示例： 
```
String url = "http://stat.m.jd.com/stat/access";
QALHttpRequest request = new QALHttpRequest(url);
request.setRequestMethod(http.POST);
request.setContentType("text/html");	
Map<String,String> formData = new HashMap<String,String>();
formData.put("key1", "value1");
formData.put("key2", "value2");
request.setFormData("charset=utf-8", formData);

final long startTime = System.currentTimeMillis();
request.request(new QALHttpValueCallBack(){

	@Override
	public void onFailed(int arg0, String arg1) {
		Log.e(TAG,"http request error:" + arg0 +":" + arg1);
	}

	@Override
	public void onFinished(QALHttpResponse arg0) {
		long use_time = System.currentTimeMillis() - startTime;
		Log.d(TAG,"http rsp status:" +  arg0.getStatus() +"|len:" + arg0.getBody().length  +"|costTime:" + use_time );
	}
});
```

## 4 错误码

<table class="table table-bordered">
<tr><td width="21%">错误码</td><td>含义</td><td width="34%">是否需要app处理</td></tr>
<tr><td>1001</td><td>请求回包失败</td><td>否</td></tr>
<tr><td>1002</td><td>请求没有响应，超时</td><td>否</td></tr>
<tr><td>-21022</td><td>回包包体Protobuf解包失败</td><td>否</td></tr>
<tr><td>-21021</td><td>回包字符串解码失败</td><td>否</td></tr>
<tr><td>-21020</td><td>回包解析Json格式失败</td><td>否</td></tr>
<tr><td>-21017</td><td>回包分片不完整</td><td>否</td></tr>
<tr><td>-21016</td><td>回包包体解压缩失败</td><td>否</td></tr>
</table>

