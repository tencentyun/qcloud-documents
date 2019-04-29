```php
<?php
// 确定APP的云API密钥
$secret_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
$secret_key = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";

// 确定签名的当前时间和失效时间
$current = time();
$expired = $current + 86400;  // 签名有效期：1天

// 向参数列表填入参数
$arg_list = array(
	"secretId" => $secret_id,
	"currentTimeStamp" => $current,
	"expireTime" => $expired,
	"random" => rand());

// 计算签名
$orignal = http_build_query($arg_list);
$signature = base64_encode(hash_hmac('SHA1', $orignal, $secret_key, true).$orignal);

echo $signature;
echo "\n";
?>
```