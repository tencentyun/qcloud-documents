## CDB备份URL签名操作指南

提示：以下示例中的 secretId 以及签名值仅作示例，不可将其进行使用

### 1. 下载URL的获取
#### 方式一：通过页面控制台下载 URL
1. 在实例管理界面，单击【备份管理】，选择备份列表或Binlog列表。
![](//mc.qcloudimg.com/static/img/a3c43c4aed35725b567332edb9fdcff8/image.png)
2. 选择需要下载的备份，在操作里单击【下载】。（冷备数据可以选择【全部下载】下载整个数据库实例或者【部分下载】下载部分数据库、数据表）
![](//mc.qcloudimg.com/static/img/838eee5eecd37df2ec17318991e6e298/image.png)
3. 获取 URL。
![](//mc.qcloudimg.com/static/img/ddf7f77cdd088087228f5da010146e3e/image.png)

#### 方式二：通过API获取下载链接，[点击查看API文档说明](https://cloud.tencent.com/doc/api/253/5125)
获取到的URL格式如下（以下是样例）：
```
http://gz.dl.cdb.qcloud.com/c85be5fa579da84af33f0efd49b1b7cd?appid=8888888888&time=1478778522&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D
```

### 2.	选择一个API密钥用于对链接签名（以下密钥用于演示）
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx
secretkey: 7v64T1gUSB8hCazvDJUWxVxxxxxxxx

### 3.	对 URL 进行签名
以下签名演示使用上面的 URL、secretId、secretkey。

#### 步骤1
将 URL 的参数进行解析，并加入 secretId，得到如下格式的参数：
```
{
appid: 8888888888,
time: 1478778522,
sign: ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D,
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx
}
```

#### 步骤2 
对参数按照 key 降序排序拼接，得到如下格式的
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
采用 sha1 算法，以及 secretkey 密钥对上一步骤拼接的参数进行计算，得到签名，并将签名转为 base64 编码格式：
```
签名值（signature）：3wRBMgzkhnsCtDSR1Pb07Mxq%2FgA%3D
```

#### 步骤4 
生成新的下载链接，将 secretId 和生成的签名附加在原有的 URL 后面，完成签名：
```
http://gz.dl.cdb.qcloud.com/c85be5fa579da84af33f0efd49b1b7cd?appid=8888888888&time=1478778522&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D&secretId=AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx&signature=3wRBMgzkhnsCtDSR1Pb07Mxq%2FgA%3D
```

#### Nodejs 示例代码：
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
