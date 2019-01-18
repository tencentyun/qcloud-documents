## Sample Code (PHP)

The API in this example is [DescribeCdnHosts](https://cloud.tencent.com/doc/api/231/查询域名信息).
```
<?php
/*Your key is required. You can obtain SecretId and $SecretKey from https://console.cloud.tencent.com/capi*/
$secretKey='YOUR_SECRET_KEY';
$secretId='YOUR_SECRET_ID';
$action='DescribeCdnHosts';

$HttpUrl="cdn.api.qcloud.com";

/*Unless otherwise specified, all APIs other than MultipartUploadVodFile support GET and POST methods. */
$HttpMethod="POST";

/*Most APIs are based on HTTPS protocol, except such APIs as MultipartUploadVodFile.*/
$isHttps =true;

/*The following five parameters are the common parameters of all APIs. For some APIs that are not region-specific (e.g. DescribeDeals), the Region parameter is not required.*/
$COMMON_PARAMS = array(
                'Nonce' => rand(),
                'Timestamp' =>time(NULL),
                'Action' =>$action,
                'SecretId' => $secretId,
                'SignatureMethod' => 'HmacSHA256'
                );

$PRIVATE_PARAMS = array();

/***********************************************************************************/


CreateRequest($HttpUrl,$HttpMethod,$COMMON_PARAMS,$secretKey, $PRIVATE_PARAMS, $isHttps);

function CreateRequest($HttpUrl,$HttpMethod,$COMMON_PARAMS,$secretKey, $PRIVATE_PARAMS, $isHttps)
{
        $FullHttpUrl = $HttpUrl."/v2/index.php";

        /***************Sort the request parameters in ascending lexicographical order by their names on a case-sensitive basis.*************/
        $ReqParaArray = array_merge($COMMON_PARAMS, $PRIVATE_PARAMS);
        ksort($ReqParaArray);

        /**********************************Generate original signature text**********************************
         * Combine the request method, URL, and sorted request parameters into the following format to generate the original signature text. In this example, the original signature text is as follows: 
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

                /*In the construction of original signature text, any "_" in a parameter name should be replaced with "."
                if(strpos($key, '_'))
                {
                        $key = str_replace('_', '.', $key);
                }

                $SigTxt=$SigTxt.$key."=".$value;
        }

        /*********************Generate a Signature based on the original signature string $SigTxt.******************/
        $Signature = base64_encode(hash_hmac('sha256', $SigTxt, $secretKey, true));


        /***************Join the request strings together. The request parameters and Signature string need to be encoded with urlencode********************/
        $Req = "Signature=".urlencode($Signature);
        foreach ($ReqParaArray as $key => $value)
        {
                $Req=$Req."&".$key."=".urlencode($value);
        }

        /*********************************Send requests********************************/
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


