## 1. Downloading SDK Codes
**[Sample Codes in PHP] (https://github.com/QcloudApi/qcloudapi-sdk-php)**
**[Sample Codes in Java] (https://github.com/QcloudApi/qcloudapi-sdk-java)**
**[Sample Codes in Python] (https://github.com/QcloudApi/qcloudapi-sdk-python)**
**[Sample Codes in .NET ] (https://github.com/QcloudApi/qcloudapi-sdk-dotnet)**

Replace the YOUR_SECRET_ID and YOUR_SECRET_KEY in the sample codes with the actual SecretId and SecretKey. 
The sample codes are for reference only. Please use the codes based on your actual needs.

## 2. Sample Codes in PHP

```
<?php


/***************In reality, the following parameters should be changed based on the APIs called.*********************************/
/***************The DescribeInstances is provided here as an example to describe how to obtain the VM with the specified instanceId.**********/

/*The URL of the DescribeInstances API is cvm.api.qcloud.com, which can be obtained from the "1. API Description" chapter.*/
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
