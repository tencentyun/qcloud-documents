# 预签名 URL

 SDK 提供了获取对象 URL ，计算签名，获取请求预签名 URL 接口.

## 获取对象 URL 
```C#
string GetAccessURL(CosRequest request);
```
## 计算签名
```C#
string GenerateSign(string method, string path, Dictionary<string, string> queryParameters, Dictionary<string, string> headers, long signDurationSecond)；
```
## 获取请求预签名 URL 
```C#
string GenerateSignURL(PreSignatureStruct preSignatureStruct);
```
### 参数说明
|参数名称|类型|描述|
|-----|-----|----|
|request|CosRequest|请求对象|
|preSignatureStruct|PreSignatureStruct|预签名 URL 实例|
|method|string|http 请求方法|
|path|string|http 请求路径,即 对象键|
|headers|`Dictionary<string, string>`|签名是否校验header|
|queryParameters|`Dictionary<string, string>`|签名是否校验请求url中查询参数|
|signDurationSecond|long|签名有效时间，单位为秒|

### 上传请求示例
```C#
try
{
	string requestSignURL = "http://example-1253653367.cos.ap-beijing.myqcloud.com/audio/audio.mp3?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDIrtxB8LEvM53HjbAKEP62SLRZLkBiMFD%26q-sign-time%3D1546048753%3B1546055954%26q-key-time%3D1546048753%3B1546055954%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D1d44b1785e95803d463a88832b95f22c3ae2c4c2%26x-cos-security-token%3Dff07a1003f7a0145fee74b63526425b2223b506930001"; //上传预签名 URL (使用临时密钥方式计算的签名 URL )
	string srcPath = @"F:\audio.mp3"；//本地文件路径
	PutObjectRequest request = new PutObjectRequest(null, null, srcPath);
	//设置上传请求预签名 UR L
	request.RequestURLWithSign = requestSignURL;
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
	});
	//执行请求
	PutObjectResult result = cosXml.PutObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}
```

### 下载请求示例
```C#
try
{
	string requestSignURL = "http://example-1253653367.cos.ap-beijing.myqcloud.com/audio/audio.mp3?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDPiqmW3qcgXVSKN8jngPzRhvxzYyDL5qP%26q-sign-time%3D1546049824%3B1546050424%26q-key-time%3D1546049824%3B1546050424%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D012b0f151f5e0b83f6e38f9f8808a0b3e79cbcc2"; //下载请求预签名 URL (使用永久密钥计算的签名 URL )
	string localDir = @"F:\audio"；//下载到本地指定文件夹
	string localFileName = "audio_download.mp3"; //指定本地保存的文件名
	GetObjectRequest request = new GetObjectRequest(null, null, localDir, localFileName);
	//设置下载请求预签名 UR L
	request.RequestURLWithSign = requestSignURL;
	//设置进度回调
	request.SetCosProgressCallback(delegate(long completed, long total)
	{
		Console.WriteLine(String.Format("progress = {1:##.##}%", completed * 100.0 / total));
	});
	//执行请求
	GetObjectResult result = cosXml.GetObject(request);
	//请求成功
	Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{	
	//请求失败
 	Console.WriteLine("CosClientException: " + clientEx.Message);
}
catch (COSXML.CosException.CosServerException serverEx)
{
	//请求失败
	Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}
```
