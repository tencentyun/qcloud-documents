## 1 Signature and Authentication

Tencent mobile service makes use of the signature to verify the legitimacy of the request. Developers allow the client to upload, download, and manage the specified resources by authorizing the signature to the client. The signature consists of **multiple-time signature** and **one-time signature**:

**Multiple-time signature**: The signature will not bind the fileid of the file. You need to set a validity period later than the current time. This signature can be used multiple times within the validity period, and the maximum validity period can be set for three months.

**One-time signature**: The signature will bind the fileid of the file. The valid period must be set to 0. This signature can only be used once, and can only be applied to the bound file.

For specific applicable scenario, refer to [Applicable Scenarios for Signatures](http://cloud.tencent.com/doc/product/227/%E7%AD%BE%E5%90%8D%E7%AE%97%E6%B3%95#4-签名适用场景).



## 2 Signature Algorithm



### 2.1	Required Information for Obtaining Signature

The information required to generate the signature includes the project ID (appid), space name (bucket, the organization management unit of file resources), and the Secret ID and Secret Key of the project. The above information can be obtained as follows:

1) Login [Cloud Object Storage](http://console.cloud.tencent.com/cos), and enter the cloud object storage space;

2) If the developer does not create such a space, you can add a space on your own. Space name (bucket) can be inputted by the user;

3) Click "Obtain secretKey" to get Appid, Secret ID and Secret Key;



### 2.2. Joining the Signature Strings

Join the multiple-time signature strings:

a=[appid]&b=[bucket]&k=[SecretID]&e=[expiredTime]&t=[currentTime]&r=[rand]&f=

Join the one-time signature strings:

a=[appid]&b=[bucket]&k=[SecretID]&e=[expiredTime]&t=[currentTime]&r=[rand]&f=[fileid]

The meanings of fields in signature strings are as follows:

| **Field** | **Description**                                   |
| ------ | ---------------------------------------- |
| a      | Developers' project ID. It is the unique ID identifying the project produced by the system when it accesses Cloud Object Storage to create space, that is, Appid |
| b      | Space name bucket                               |
| k      | Secret ID of the project                             |
| e      | Validity period of the signature (in seconds). It is a value that aligns with the UNIX Epoch timestamp specifications. **When it is a one-time signature, e must be set to 0** |
| t      | Current timestamp (in seconds). It is a value that aligns with the UNIX Epoch timestamp specifications. **When it is a multiple-time signature, e should be greater than t** |
| r      | Random string. It is an unsigned decimal integer. Users need to generate the random string by themselves, and it is up to ten digits              |
| fileid | Unique identifier for the stored resources. The format is "/appid/bucketname/user-defined path or resource name", **and requires urlencode encoding for non-'/' characters** |



**Note: **

**When the signature strings are joined for a one-time signature, the expiration time e must be set to 0 to ensure that the signature can only be used for fixed resources and can only be used once;**

**The one-time signature must be used when deleting a file;**

**The multiple-time signature must be used when uploading a file;**

For specific applicable scenario, refer to [Applicable Scenarios for Signatures](http://cloud.tencent.com/doc/product/227/%E7%AD%BE%E5%90%8D%E7%AE%97%E6%B3%95#4-签名适用场景).


### 2.3	Generating Signature

\1. Cloud Object Storage (COS) uses HMAC-SHA1 algorithm to sign the request;

\2. The signature string shall be encoded with Base64.

The formula for generating the signature is as follows:

**SignTmp = HMAC-SHA1(SecretKey, orignal)**

**Sign = Base64(SignTmp.orignal)**

In the formula, SecretKey is the project Secret Key obtained in Section 2.1, while the original is the signature string joined in Section 2.2. First, generate a signature for original using HMAC-SHA1 algorithm, then add the original to the end of signature result, and perform BASE64 decoding to get the final sign.

**Note: Please note that the Base64 encoding used here is standard Base64 encoding, not urlsafe Base64 encoding.**



## 3 Instances

This section describes the instances of algorithms generating signatures which use PHP language. If the developer uses other languages for developing, please use the corresponding algorithm.



### 3.1 Required Information for Obtaining Signature

The required information for obtaining signature is as follows.

Project ID: 200001

Space name (bucket): newbucket

Secret ID: AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv

Secret Key: bLcPnl88WU30VY57ipRhSePfPdOfSruK



### 3.2. Joining the Signature Strings

The joined multiple-time signature string is as follows:

a=200001&b=newbucket&k=AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv&e=1438669115&t=1436077115&r=11162&f=

The joined one-time signature string is as follows:

a=10001290&b=tencentyun&k=AKIDgaoOYh2kOmJfWVdH4lpfxScG2zPLPGoK&e=0&t=1436077115&r=11162&f=tencentyunSignTest

``` 
$appid = "200001";
$bucket = "newbucket";
$secret_id = "AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv";
$secret_key = "bLcPnl88WU30VY57ipRhSePfPdOfSruK";
$expired = time() + 60;
$onceExpired = 0;
$current = time();
$rdm = rand();
$userid = "0";
$fileid = "/200001/newbucket/tencent_test.jpg";

$srcStr = 'a='.$appid.'&b='.$bucket.'&k='.$secret_id.'&e='.$expired.'&t='.$current.'&r='.$rdm.'&f=';

$srcStrOnce= 'a='.$appid.'&b='.$bucket.'&k='.$secret_id.'&e='.$onceExpired .'&t='.$current.'&r='.$rdm
.'&f='.$fileid;


```





### 3.3 Generating Signature

``` 
$signStr = base64_encode(hash_hmac('SHA1', $srcStr, $secret_key, true).$srcStr);

$signStrOnce = base64_encode(hash_hmac('SHA1',$srcStrOnce,$secret_key, true).$srcStrOnce);

echo $signStr."\n"; 

echo $signStrOnce."\n";

```



The final obtained multiple-time signature is:

vxzLR6vzMNhBMUVzMTWKUB+LMeVhPTIwMDAwMSZrPUFLSURVZkxVRVVpZ1FpWHFtN0 NWU3NwS0pudWFpSUt0eHFBdiZlPTE0Mzc5OTU3MDQmdD0xNDM3OTk1NjQ0JnI9MjA4 MTY2MDQyMSZmPSZiPW5ld2J1Y2tldA==



The one-time signature is:

f11dDSuw86CR02Ko1INzsZstbRlhPTIwMDAwMSZrPUFLSURVZkxVRVVpZ1FpWHFtN0 NWU3NwS0pudWFpSUt0eHFBdiZlPTAmdD0xNDM3OTk1NjQ1JnI9MTE2NjcxMDc5MiZm PS8yMDAwMDEvbmV3YnVja2V0L3RlbmNlbnRfdGVzdC5qcGcmYj1uZXdidWNrZXQ=





## 4 Applicable Scenarios for Signatures

Cloud Object Storage (COS) limits the applicable scenario for signature as follows:

| **Scenario**          | **Applicable Signature**   |
| --------------- | ---------- |
| Download (token hotlink protection is disabled) | No signature verification      |
| Upload              | **Multiple-time signature** |
| Query directories and files         |     Multiple-time signature      |
| Create directories            |     Multiple-time signature      |
| Download (token hotlink protection is enabled)  |      Multiple-time signature      |
| Delete directories and files         | **One-time signature** |
| Update directories and files         |       One-time signature     |


