## How to Sign the CDB Backup URL

Note: The secretId and signature in the example below are only for reference, and cannot be used in practice

### 1.	Getting the Download URL
Method 1: Get the download URL on the console
![](https://mc.qcloudimg.com/static/img/92773c7d8ce9498440c7c7d280926e57/url.png)

Method 2: Get the download URL via API. [Click to view the API Documentation](https://www.qcloud.com/doc/api/253/5125)

The obtained URL is as follows (sample):
```
http://gz.dl.cdb.qcloud.com/c85be5fa579da84af33f0efd49b1b7cd?appid=8888888888&time=1478778522&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D
```

### 2. Selecting an API Key for Signing the URL (The following key is only used as an example)
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx
secretkey: 7v64T1gUSB8hCazvDJUWxVxxxxxxxx

### 3. Signing the URL
The following signature example uses the above URL, secretId and secretkey

#### Step 1
Resolve the URL parameters and add secretId to get the following parameters:
```
{
appid: 8888888888,
time: 1478778522,
sign: ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D,
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx
}
```

#### Step 2 
Sort the parameters in descending order based on key to get the following 
Sorting result:
```
{
appid: 8888888888,
secretId: AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx,
sign: ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D,
time: 1478778522
}
```

After combining the parameters:
```
appid=8888888888&secretId=AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D&time=1478778522
```

#### Step 3 
Use sha1 algorithm and secretkey to compute the combination of the parameters in Step 2 to get the signature, then encode it with Base64:
```
Signature:3wRBMgzkhnsCtDSR1Pb07Mxq%2FgA%3D
```

#### Step 4 
Append the secretId and the generated signature to the end of the original URL to generate a new download URL and complete the signature:
```
http://gz.dl.cdb.qcloud.com/c85be5fa579da84af33f0efd49b1b7cd?appid=8888888888&time=1478778522&sign=ZDxBCfRuFXDITwXY4C7%2BkTDAlDE%3D&secretId=AKID1agWVShCU7cQxKh33n9w98kwxxxxxxx&signature=3wRBMgzkhnsCtDSR1Pb07Mxq%2FgA%3D
```

#### Nodejs Sample Codes
```
var libUrl = require('url');
var crypto = require('crypto');
var libQuery = require('querystring');

function sign(url, SecretId, secretKey){
	//Resolve the download URL
	url += '&secretId=' + SecretId;
	var uinfo = libUrl.parse(url);
	var param = libQuery.parse(uinfo.query);
	
	//Sort the parameters
	var keys = Object.keys(param).sort();
	var sortUrl = [];
	for(var i in keys){
		sortUrl.push(keys[i] + '=' +param[keys[i]]);
	}
	sortUrl = sortUrl.join('&');

	//Compute the signature
	var hmac = crypto.createHmac('sha1', secretKey);
	param['signature'] = hmac.update(new Buffer(sortUrl, 'utf8')).digest('base64');
	
	//Generate the new download URL
	var newUrl = 'http://' + uinfo.host + uinfo.pathname + '?';
	sortUrl = [];
	for(var i in param){
		sortUrl.push(i + '=' + encodeURIComponent(param[i]));
	}
	newUrl += sortUrl.join('&');
	return newUrl;
}
```
