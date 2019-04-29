```php
<?php
// Step 1: Obtain required information for signature as follows
$secret_id = "AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv";
$secret_key = "bLcPnl88WU30VY57ipRhSePfPdOfSruK";

// Step 2: Set the validity period of the signature
$current = time();
$expired = $current + 86400;  // Validity period: 1 day

// Step 3: Assemble the parameter list according to the file information submitted by the client
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

// Step 3: Generate the signature
$orignal = http_build_query($arg_list);
$signature = base64_encode(hash_hmac('SHA1', $orignal, $secret_key, true).$orignal);

echo $signature;
echo "\n";
?>
```
