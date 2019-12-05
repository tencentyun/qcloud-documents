## 初始化 

**示例：**

```
QALHttpRequest.init();
```

## 设置 Cache 大小

设置 HTTP 的缓存大小，缓存 GET 请求的结果。空闲空间不足时将通过 LRU 淘汰数据。参数 `size` 为缓存大小，单位为字节，填 0 表示关闭 Cache。

**示例：**

```
QALHttpRequest.setCacheMaxSize(10*1024*1024);
```

## 发送请求 

**GET 调用示例： **

```
QALHttpRequest request = new QALHttpRequest("http://www.qq.com");
request.setRequestMethod(http.GET);
request.setContentType("text/html");            
Log.i(TAG,"request:" + url );
request.request(new QALHttpValueCallBack(){                        
	@Override
	public void onFailed(int arg0, String arg1) {
		// TODO Auto-generated method stub
		Log.e(TAG,"http request error:" + arg0 +":" + arg1);
	}
	@Override
	public void onFinished(QALHttpResponse arg0) {
		// TODO Auto-generated method stub                                    
	   Log.i(TAG,"http rsp status:" +  arg0.getStatus() +"|len:" + arg0.getBody().length  +"|costTime:" + use_time );
	}
});
```

**POST 调用示例： **

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
		// TODO Auto-generated method stub
		Log.e(TAG,"http request error:" + arg0 +":" + arg1);
	}
	@Override
	public void onFinished(QALHttpResponse arg0) {
		// TODO Auto-generated method stub
		long use_time = System.currentTimeMillis() - startTime;
		Log.d(TAG,"http rsp status:" +  arg0.getStatus() +"|len:" + arg0.getBody().length  +"|costTime:" + use_time );
	}
});
```

## 错误码

| 错误码 | 含义 | 是否需要 App 处理 |
| --- | --- | --- |
| 1001 | 请求回包失败 | 否 |
| 1002 | 请求没有响应，超时 | 否 |
| -21022 | 回包包体 Protobuf 解包失败 | 否 |
| -21021 | 回包字符串解码失败 | 否 |
| -21020 | 回包解析 JSON 格式失败 | 否 |
| -21017 | 回包分片不完整 | 否 |
| -21016 | 回包包体解压缩失败 | 否 |