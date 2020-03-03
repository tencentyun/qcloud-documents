## Composition of Returned Value
Unless otherwise specified, the returned values of each request contain the following fields:

<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th><th width="50"> <b>Required</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code on the result. 0: Successful; other values: Failed. For meanings of error codes, please see the <a href="/doc/api/258/错误码表" title="Error Codes">Error Codes</a> page
</td><td>Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Request result
</td><td>Yes
</td></tr></tbody></table>

For example:
Example requests that use common parameters:

```
 https://live/v2/index.php?Action=DescribeInstances&SecretId=xxxxxxx&Region=gz
 &Timestamp=1402992826&Nonce=345122&Signature=mysignature&instanceId=101
```


Possible returned result is as follows:

```
{
    "code":0,
    "message": "success",
    "instanceSet":
   [{
        "instanceId":"qcvm1234",
        "cpu":1,
        "mem":2,
        "disk":20,
        "bandwidth":65535,
        "os":"centos_62_64",
        "lanIp":"10.207.248.186",
        "wanIp":null,
        "status":0
   }]
}
```

## Error Codes
The error code in the response body summarizes the result of the calling and execution of a Tencent Cloud API.
Any error code other than 0 indicates the request is not properly executed. An error message describes the error in details. You can get the API execution result based on the error code.
On some terminals, such as browsers, message in Chinese is displayed in Unicode and needs to be decoded.

**The following error codes may be returned by Tencent Cloud APIs:**
<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Type</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> 4,000
</td><td> Invalid request parameter
</td><td> Required parameter is missing, or parameter value is not in a correct format. For relevant error message, please see the "message" field in error description.
</td></tr>
<tr>
<td> 4100
</td><td> Authentication failed
</td><td> Signature authentication failed. For more information, please see the Authentication section in the document.
</td></tr>
<tr>
<td> 4200
</td><td> Request expired
</td><td> The request has expired. For more information, please see the Request Validity Period section in the document.
</td></tr>
<tr>
<td> 4300
</td><td> Access denied
</td><td> Account is blocked or not within the user range of the API.
</td></tr>
<tr>
<td> 4400
</td><td> Quota is exceeded
</td><td> The number of requests has exceeded the quota limit. For more information, please see the Request Quota section in the document.
</td></tr>
<tr>
<td> 4500
</td><td> Replay attack
</td><td> The Nonce and Timestamp parameters can ensure that each request is executed only once on the server. Therefore, the Nonce value cannot be the same as last one, and the difference between Timestamp and Tencent server time cannot be greater than 2 hours.
</td></tr>
<tr>
<td> 4600
</td><td> Protocol is not supported
</td><td> The protocol is not supported. For more information, please see the relevant document.
</td></tr>
<tr>
<td> 5000
</td><td> Resource does not exist
</td><td> The instance corresponding to resource ID does not exist, or the instance has been returned, or another user's resource is accessed.
</td></tr>
<tr>
<td> 5100
</td><td> Resource operation failed
</td><td> The operation performed on the resource failed. For detailed error message, please see the "message" field in error description. Try again later or contact customer service for help.
</td></tr>
<tr>
<td> 5200
</td><td> Failed to purchase resource
</td><td> The resource purchase failed. This is may be caused by unsupported instance configuration or insufficient resource.
</td></tr>
<tr>
<td> 5300
</td><td> Failed to purchase resource
</td><td> The resource purchase failed because of insufficient balance.
</td></tr>
<tr>
<td> 5400
</td><td> Part of operations performed successfully
</td><td> Part of the batch operations have been performed successfully. For more information, please see the returned value of method.
</td></tr>
<tr>
<td> 5500
</td><td> User failed to pass identity verification
</td><td> Resource purchase failed because the user failed to pass identity verification.
</td></tr>
<tr>
<td> 6000
</td><td> Internal error on the server
</td><td> An internal error occurred on the server. Try again later or contact customer service personnel for help.
</td></tr>
<tr>
<td> 6100
</td><td> Not supported by the version
</td><td> The API is not supported by this version or is being maintained. Note: When this error occurs, first check whether the domain name of the API is correct. Different modules may have different domain names.
</td></tr>
<tr>
<td> 6200
</td><td> API is temporarily unavailable
</td><td> The API is under maintenance and is unavailable. Please try again later.
</td></tr></tbody></table>

## Format of Returned Results for Asynchronous Task APIs
### 1. Format of returned results for common asynchronous task interfaces
This refers to the asynchronous task API in which only one resource can be operated for each request, for example, creating load balancer or resetting OS for server.
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th><th> <b>Required</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code on the result. 0: Successful; other values: Failed.
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message on the result
</td><td> No
</td></tr>
<tr>
<td> requestId
</td><td> String
</td><td> Task ID
</td><td> Yes
</td></tr></tbody></table>

### 2. Format of returned results for batch asynchronous task APIs
This refers to the asynchronous task API in which multiple resources can be operated for each request, for example, changing passwords, starting or shutting down machines.
<table class="t">
<tbody><tr>
<th> <b>Name</b>
</th><th> <b>Type</b>
</th><th> <b>Description</b>
</th><th> <b>Required</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> Error code on the result. 0: Successful; other values: Failed.
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> Error message on the result
</td><td> No
</td></tr>
<tr>
<td> detail
</td><td> Array
</td><td> The code, message, and requestId for an operation performed on the resource based on the resource ID (key).
</td><td> Yes
</td></tr></tbody></table>

For example:

```
{
        "code":0,
        "message": "success",
        "detail":
        {
             "qcvm6a456b0d8f01d4b2b1f5073d3fb8ccc0":
            {
             "code":0,
             "message":"",
             "requestId":"1231231231231":,
            }
              "qcvm6a456b0d8f01d4b2b1f5073d3fb8ccc0":
            {
              "code":0,
              "message":"",
              "requestId":"1231231231232":,
            }
        }
}
```
>Note:
If all operations performed on the resource are successful, the outermost code is 0
If all operations performed on the resource fail, the outermost code is 5100
If part of operations performed on the resource fail, the outermost error code is 5400
In the third case, the terminal can obtain the information about the failed operations via "detail" field.

## Sample Codes
### 1. Download SDK codes
**[Sample Codes in PHP](https://mc.qcloudimg.com/static/pdf/5ef6e2f7fece68bb862ad281e2c878e2/docfile.pdf)**
**[Sample Codes in JAVA](https://mc.qcloudimg.com/static/pdf/61b3958a8ee12cd5781571569907657c/docfile.pdf)**
**[Sample Codes in Python](https://mc.qcloudimg.com/static/pdf/b3cfda9f251c2ef703a21d9bf8ef4e7e/docfile.pdf)**
**[Sample Codes in .NET](https://mc.qcloudimg.com/static/pdf/988e25376805ad8b52ac68dd090e1a3a/docfile.pdf)**

Replace the YOUR_SECRET_ID and YOUR_SECRET_KEY in the sample codes with the actual SecretId and SecretKey. 
The sample codes are for reference only. Please use the codes based on your actual needs.

### 2. Sample codes in PHP

```
<?php


/***************In reality, the following parameters should be changed based on the APIs called*********************************/
/***************The DescribeInstances is provided here as an example to describe how to obtain the VM with the specified instanceId**********/

/*The URL of the DescribeInstances API is cvm.api.qcloud.com, which can be obtained from the "1. API Description" chapter*/
$HttpUrl="cvm.api.qcloud.com";

/*All APIs other than MultipartUploadVodFile support GET and POST methods unless specified otherwise*/
$HttpMethod="GET"; 

/*Most APIs are based on HTTPS protocol, except a small number of APIs such as MultipartUploadVodFile*/
$isHttps =true;

/*Your key is required. You can obtain SecretId and $SecretKey from https://console.cloud.tencent.com/capi*/
$secretKey='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';


/*The following five parameters are the common parameters of all APIs. For some APIs that are not region-specific (e.g. DescribeDeals), the Region parameter is not required*/
$COMMON_PARAMS = array(
        'Nonce'=> rand(),
        'Timestamp'=>time(NULL),
        'Action'=>'DescribeInstances',
        'SecretId'=> 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'Region' =>'gz',
);

/*The following two parameters are the ones specific to DescribeInstances API and are used to query specific VM list.*/
$PRIVATE_PARAMS = array(
        'instanceIds.0'=> 'qcvm00001',
        'instanceIds.1'=> 'qcvm00002',
);


/***********************************************************************************/


CreateRequest($HttpUrl,$HttpMethod,$COMMON_PARAMS,$secretKey, $PRIVATE_PARAMS, $isHttps);


function CreateRequest($HttpUrl,$HttpMethod,$COMMON_PARAMS,$secretKey, $PRIVATE_PARAMS, $isHttps)
{
    $FullHttpUrl = $HttpUrl."/v2/index.php";
    
    /***************Sort the request parameters in ascending lexicographical order by their names (case-sensitive)*************/
    $ReqParaArray = array_merge($COMMON_PARAMS, $PRIVATE_PARAMS);
    ksort($ReqParaArray);
    
    /**********************************Generate original signature text**********************************
     * Combine the request method, URI address, and sorted request parameters into the following format to generate the original signature text. In this example, the original signature text is as follows: 
     * GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=345122&Region=gz
     * &SecretId=AKIDz8krbsJ5yKBZQ	·1pn74WFkmLPx3gnPhESA&Timestamp=1408704141
     * &instanceIds.0=qcvm12345&instanceIds.1=qcvm56789
     * ****************************************************************************/
    $SigTxt = $HttpMethod.$FullHttpUrl."?";
    
    $isFirst = true;
    foreach ($ReqParaArray as $key => $value)
    {
        if (!$isFirst) 
        { 
            $SigTxt = $SigTxt."&";
        }
        $isFirst= false;
        
        /*In the combination of original signature text, any "_" in a parameter name should be replaced with "."*/
        if(strpos($key, '_'))
        {
            $key = str_replace('_', '.', $key);
        }
        
        $SigTxt=$SigTxt.$key."=".$value;
    }
    
    /*********************Generate a Signature based on the original signature string $SigTxt******************/
    $Signature = base64_encode(hash_hmac('sha1', $SigTxt, $secretKey, true));

    
    /***************Join the request strings together. The request parameters and Signature string need to be encoded using urlencode********************/
    $Req = "Signature=".urlencode($Signature);
    foreach ($ReqParaArray as $key => $value)
    {
        $Req=$Req."&".$key."=".urlencode($value);
    }
    
    /*********************************Send request********************************/
    if($HttpMethod === 'GET')
    {
        if($isHttps === true)
        {
            $Req="https://".$FullHttpUrl."?".$Req;
        }
        else
        {
            $Req="http://".$FullHttpUrl."?".$Req;
        }
        
        $Rsp = file_get_contents($Req);
        
    }
    else
    {
        if($isHttps === true)
        {
        	$Rsp= SendPost("https://".$FullHttpUrl,$Req,$isHttps);
        }
        else
        {
        	$Rsp= SendPost("http://".$FullHttpUrl,$Req,$isHttps);
        }
    }
    
    var_export(json_decode($Rsp,true));
}

function SendPost($FullHttpUrl,$Req,$isHttps)
{
	
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $Req);
        
        curl_setopt($ch, CURLOPT_URL, $FullHttpUrl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        if ($isHttps === true) {
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER,  false);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST,  false);
        }
        
        $result = curl_exec($ch);
        
        return $result;
}
```

