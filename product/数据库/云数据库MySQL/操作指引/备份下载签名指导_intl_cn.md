## CDB备份URL签名操作指南

提示：以下示例中的secretId以及签名值仅作示例，不可将其进行使用

### 1.	下载URL的获取
方式一：通过页面控制台下载URL
![](https://mc.qcloudimg.com/static/img/92773c7d8ce9498440c7c7d280926e57/url.png)

方式二：通过API获取下载链接,[点击查看API文档说明](https://www.qcloud.com/doc/api/253/5125)

获取到的URL格式如下(以下是样例)：
```
http://gz.dl.cdb.qcloud.com/c85be5fa579da84af33f0efd49b1b7cd?appid=8888888888&time=1478778522&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D
```

### 2.	选择一个API密钥用于对链接签名（以下密钥用于演示）
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx
secretkey: 7v64T1gUSB8hCazvDJUWxVxxxxxxxx

### 3.	对URL进行签名
以下签名演示使用上面的URL secretId secretkey

#### 步骤1
将URL的参数进行解析，并加入secretId，得到如下格式的参数：
```
{
appid: 8888888888,
time: 1478778522,
sign: ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D,
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx
}
```

#### 步骤2 
对参数按照key降序排序拼接，得到如下格式的
排序：
```
{
appid: 8888888888,
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx,
sign: ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D,
time: 1478778522
}
```

拼接：
```
appid=8888888888&secretId=AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D&time=1478778522
```

#### 步骤3 
采用sha1算法，以及secretkey密钥对上一步骤拼接的参数进行计算，得到签名，并将签名转为base64编码格式：
```
签名值（signature）：3wRBMgzkhnsCtDSR1Pb07Mxq%2FgA%3D
```

#### 步骤4 
生成新的下载链接，将secretId和生成的签名附加在原有的URL后面，完成签名：
```
http://gz.dl.cdb.qcloud.com/c85be5fa579da84af33f0efd49b1b7cd?appid=8888888888&time=1478778522&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D&secretId=AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx&signature=3wRBMgzkhnsCtDSR1Pb07Mxq%2FgA%3D
```

#### Nodejs示例代码：
```
var libUrl = require('url');
var crypto = require('crypto');
var libQuery = require('querystring');

function sign(url, SecretId, secretKey){
	//下载URL解析
	url += '&secretId=' + SecretId;
	var uinfo = libUrl.parse(url);
	var param = libQuery.parse(uinfo.query);
	
	//参数排序
	var keys = Object.keys(param).sort();
	var sortUrl = [];
	for(var i in keys){
		sortUrl.push(keys[i] + '=' +param[keys[i]]);
	}
	sortUrl = sortUrl.join('&');

	//签名计算
	var hmac = crypto.createHmac('sha1', secretKey);
	param['signature'] = hmac.update(new Buffer(sortUrl, 'utf8')).digest('base64');
	
	//生成新的下载URL
	var newUrl = 'http://' + uinfo.host + uinfo.pathname + '?';
	sortUrl = [];
	for(var i in param){
		sortUrl.push(i + '=' + encodeURIComponent(param[i]));
	}
	newUrl += sortUrl.join('&');
	return newUrl;
}
```