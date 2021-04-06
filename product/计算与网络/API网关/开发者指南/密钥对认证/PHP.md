## 操作场景

该任务指导您使用 PHP 语言，通过密钥对鉴权来对您的 API 进行认证管理。

## 操作步骤
1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“密钥对鉴权”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台密钥管理界面创建密钥对。
4. 在控制台使用计划界面创建使用计划，并将使用计划与已创建的密钥对绑定（参考 [使用计划示例](https://cloud.tencent.com/document/product/628/11816)）。
5. 将使用计划与 API 或 API 所在服务进行绑定。
6. 参考 [示例代码](#example)，使用 PHP 语言生成签名内容。

## 注意事项
- 最终发送的 HTTP 请求内至少包含两个 Header：Date 和 X-Date 二选一以及 Authorization，可以包含更多 header。如果使用 Date Header，服务端将不会校验时间；如果使用 X-Date Header，服务端将校验时间。
- Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Fri, 09 Oct 2015 00:00:00 GMT。
- X-Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Mon, 19 Mar 2018 12:08:40 GMT。X-Date Header 里的时间和当前时间的差值不能超过15分钟。
- 如果是微服务 API，Header 中需要添加 “X-NameSpace-Code” 和 “X-MicroService-Name” 两个字段，通用 API 不需要添加，Demo 中默认添加了这两个字段。

<span id="example"></span>
## 示例代码
```
<?php

$dateTime = gmdate("D, d M Y H:i:s T");
$SecretId = 'your SecretId'; # 密钥对的 SecretId
$SecretKey = 'your SecretKey'; # 密钥对的 SecretKey
$srcStr = "date: ".$dateTime."\n"."source: "."xxxxxx"; # 签名水印值，可填写任意值
$Authen = 'hmac id="'.$SecretId.'", algorithm="hmac-sha1", headers="date source", signature="';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $SecretKey, true));
# echo $signStr;
$Authen = $Authen.$signStr."\"";
echo $Authen;
# echo '</br>';

$url = 'http://service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com/release/yousa'; # 用户 API 的访问路径
$headers = array( 
	'Host:service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com', # 用户 API 所在服务的域名
	'Accept:text/html, */*; q=0.01',
	'Source: xxxxxx',
	'Date: '.$dateTime,
	'Authorization: '.$Authen,
	'X-Requested-With: XMLHttpRequest',
	# 'Accept-Encoding: gzip, deflate, sdch',
	
	# 如果是微服务 API，Header 中需要添加'X-NameSpace-Code'、'X-MicroService-Name'两个字段，通用 API 不需要添加。
	'X-NameSpace-Code: testmic',
	'X-MicroService-Name: provider-demo'
);
$ch = curl_init(); 
curl_setopt($ch, CURLOPT_URL,$url); 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
curl_setopt($ch, CURLOPT_TIMEOUT, 60); 
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); 
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");

$data = curl_exec($ch); 

if (curl_errno($ch)) { 
	print "Error: " . curl_error($ch); 
} else { 
	# Show me the result 
	var_dump($data); 
	curl_close($ch); 
} 

?>
```

