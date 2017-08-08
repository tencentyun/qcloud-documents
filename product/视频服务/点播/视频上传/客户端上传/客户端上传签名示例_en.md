## PHP

```php
<?php
// Determine the cloud API secret key for the App
$secret_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
$secret_key = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";

// Determine the current time and expiration time for the signature
$current = time();
$expired = $current + 86400;  // Validity period: 1 day

// Enter parameters into the parameter list
$arg_list = array(
	"secretId" => $secret_id,
	"currentTimeStamp" => $current,
	"expireTime" => $expired,
	"random" => rand());

// Calculate signature
$orignal = http_build_query($arg_list);
$signature = base64_encode(hash_hmac('SHA1', $orignal, $secret_key, true).$orignal);

echo $signature;
echo "\n";
?>
```
