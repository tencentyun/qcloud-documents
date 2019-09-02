```php
<?php
// Step 1：获取签名所需信息获取得到的签名所需信息，如下
$secret_id = "AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv";
$secret_key = "bLcPnl88WU30VY57ipRhSePfPdOfSruK";

// Step 2：设置签名有效时间
$current = time();
$expired = $current + 86400;  // 签名有效期：1天

// Step 3：根据客户端所提交的文件信息，拼装参数列表
$file_name = "tencent_test.mp4";
$file_sha = "a9993e364706816aba3e25717850c26c9cd0d89d";
$uid="1234";

$arg_list = array(
	"s" => $secret_id,
	"t" => $current,
	"e" => $expired,
	"f" => $file_name,
	"fs" => $file_sha,
	"ft" => $file_type,
	"uid" => $uid,
	"r" => rand());

// Step 4：生成签名
$orignal = http_build_query($arg_list);
$signature = base64_encode(hash_hmac('SHA1', $orignal, $secret_key, true).$orignal);

echo $signature;
echo "\n";
?>
```