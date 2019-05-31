```javascript
var querystring = require("querystring");
var crypto = require('crypto');

// Step 1：获取签名所需信息获取得到的签名所需信息，如下
var secret_id = "AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv";
var secret_key = "bLcPnl88WU30VY57ipRhSePfPdOfSruK";

// Step 2：设置签名有效时间
var current = parseInt((new Date()).getTime() / 1000)
var expired = current + 86400;  // 签名有效期：1天

// Step 3：根据客户端所提交的文件信息，拼装参数列表
var file_name = "tencent_test.mp4";
var file_sha = "a9993e364706816aba3e25717850c26c9cd0d89d";
var uid="1234";
var ft="AVI";

var arg_list = {
	s : secret_id,
	t : current,
	e : expired,
	f : file_name,
	fs : file_sha,
	ft : file_type,
	r : Math.round(Math.random() * Math.pow(10, 10)),
	uid : uid
}

// Step 4：生成签名
var orignal = querystring.stringify(arg_list);
var orignal_buffer = new Buffer(orignal, "utf8");

var hmac = crypto.createHmac("sha1", secret_key);
var hmac_buffer = hmac.update(orignal_buffer).digest();

var signature = Buffer.concat([hmac_buffer, orignal_buffer]).toString("base64");

console.log(signature);
```