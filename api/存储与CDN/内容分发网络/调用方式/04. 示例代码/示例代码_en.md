## Sample Download Links

CDN provides the following sample codes:

+ PHP: [Get Code](https://github.com/QCloudCDN/CDN_API_SDK/tree/master/Qcloud_CDN_API/php)
+ Python: [Get Code](https://github.com/QCloudCDN/CDN_API_SDK/tree/master/Qcloud_CDN_API/python)
+ Java: [Get Code](https://github.com/QCloudCDN/CDN_API_SDK/tree/master/Qcloud_CDN_API/java/cdn_openapi_demo/src)
+ Go: [Get Code](https://github.com/QCloudCDN/CDN_API_SDK/tree/master/Qcloud_CDN_API/go)

The sample codes are for reference only. Please use the codes based on your actual needs.

## Sample Code (PHP)

Take [DescribeCdnHosts](https://cloud.tencent.com/doc/api/231/查询域名信息) as an example:
```
<?php
/*Your key is required. You can obtain SecretId and $secretKey from https://console.cloud.tencent.com/capi*/
$secretKey='YOUR_SECRET_KEY';
$secretId='YOUR_SECRET_ID';
$action='DescribeCdnHosts';

$HttpUrl="cdn.api.qcloud.com";

/*All APIs other than MultipartUploadVodFile support GET and POST methods unless specified otherwise*/
$HttpMethod="POST";

/*Most APIs are based on HTTPS protocol, except a small number of APIs such as MultipartUploadVodFile*/
$isHttps =true;

/*The following five parameters are the common parameters of all APIs. For some APIs that are not region-specific (e.g. DescribeDeals), the Region parameter is not required*/
$COMMON_PARAMS = array(
                'Nonce' => rand(),
                'Timestamp' =>time(NULL),
                'Action' =>$action,
                'SecretId' => $secretId
                );

$PRIVATE_PARAMS = array();

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
         * &SecretId=AKIDz8krbsJ5yKBZQ    ·1pn74WFkmLPx3gnPhESA&Timestamp=1408704141
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

                /*In the combination of original signature text, any "_" in the parameter names should be replaced with "."*/
                if(strpos($key, '_'))
                {
                        $key = str_replace('_', '.', $key);
                }

                $SigTxt=$SigTxt.$key."=".$value;
        }

        /*********************Generate a Signature based on the original signature string $SigTxt******************/
        $Signature = base64_encode(hash_hmac('sha1', $SigTxt, $secretKey, true));


        /***************Combine the request strings. The request parameters and signature string need to be encoded using urlencode********************/
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

function SendPost($FullHttpUrl, $Req, $isHttps)
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


