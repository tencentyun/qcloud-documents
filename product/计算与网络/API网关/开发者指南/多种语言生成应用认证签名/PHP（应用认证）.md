## 操作场景

该任务指导您使用 PHP 语言，通过应用认证来对您的 API 进行认证管理。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“应用认证”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台 [应用管理](https://console.cloud.tencent.com/apigateway/app) 界面创建应用。
4. 在应用列表中选中已经创建好的应用，单击【绑定API】，选择服务和 API 后单击【提交】，即可将应用与 API 建立绑定关系。
5. 参考 [示例代码](#示例代码)，使用 PHP 语言生成签名内容。

## 环境依赖
- 本示例代码支持 PHP 7 版本，其他 PHP 版本可能需要您适当修改。
- API 网关提供 JSON 请求方式和 form 请求方式的示例代码，请您根据自己业务的实际情况合理选择。

## 注意事项

- 应用生命周期管理，以及 API 向应用授权、应用绑定 API 等操作请您参考 [应用管理](https://cloud.tencent.com/document/product/628/55087)。
- 应用生成签名过程请您参考 [应用认证方式](https://cloud.tencent.com/document/product/628/55088)。

## 示例代码[](id:示例代码)

### JSON 请求方式示例代码
<dx-codeblock>
:::  php
<?php

/**
Sort the given query string in alphabetical order

- @param string $queryStr
- @return string sorted query string
*/
function sortQueryParameters($queryStr) {
    if (is_null($queryStr) || empty($queryStr)) {
        return "";
    }

    parse_str($queryStr, $arr);
    if (empty($arr)) {
        return "";
    }
    ksort($arr);

    $sortedQueryArr = array();
    foreach($arr as $k => $v) {
        $tmp = $k;
        if (!empty($v)) {
            $tmp .= ("=" . $v);
        }
        array_push($sortedQueryArr, $tmp);
    }

    return join('&', $sortedQueryArr);
}

// ==========================================================
// Note: Update the customized variables based on your API
// ==========================================================
$apiAppKey = '<your_apiAppKey>';
$apiAppSecret = '<your_apiAppSecret>';
$httpMethod = "POST";
$acceptHeader = "application/json"; // accept header for your request
$url = 'https://service-xxxx-xxxx.gz.apigw.tencentcs.com/testmock?b=1&a=2';

// ContentType and contentMd5 should be empty if request body is not present
$reqBody = "{\"code\":1, \"msg\":\"ok\"}";
$contentType = "application/json";
$contentMD5 = base64_encode(md5($reqBody));

// ==========================================================
// customized parameter ends here
// ==========================================================

$parsedUrl = parse_url($url);
$xDateHeader = gmstrftime('%a, %d %b %Y %T %Z', time());

// Note:
// 1. parameters should be in alphabetical order
// 2. form parameter should also append to $pathAndParam
$pathAndParam = $parsedUrl['path'];
if ($parsedUrl['query']) {
    $pathAndParam = $pathAndParam . '?' . sortQueryParameters($parsedUrl['query']);
}

// Generate the string to sign
$strToSign = sprintf("x-date: %s\n%s\n%s\n%s\n%s\n%s",
    $xDateHeader, $httpMethod, $acceptHeader, $contentType, $contentMD5, $pathAndParam);
// echo "strToSign: $strToSign\n";

// Encode the string with HMAC and base64
$sign = base64_encode(hash_hmac('sha1', $strToSign, $apiAppSecret, TRUE));
$authHeader = sprintf('hmac id="%s", algorithm="hmac-sha1", headers="x-date", signature="%s"',
    $apiAppKey, $sign);

// Generate the request headers
$headers = array(
    'Host:' . $parsedUrl['host'],
    'Accept:' . $acceptHeader,
    'X-Date:' . $xDateHeader,
    'Content-Type:' . $contentType,  // only required if request body is present
    'Content-MD5:' . $contentMD5,    // only required if request body is present
    'Authorization:' . $authHeader,
);
// var_dump($headers);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_TIMEOUT, 60);
curl_setopt($ch, CURLOPT_POSTFIELDS, $reqBody); // only required if request body is present
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $httpMethod);
$data = curl_exec($ch);

if (curl_errno($ch)) {
    print "Error: " . curl_error($ch);
} else {
    var_dump($data);
    curl_close($ch);
}
:::
</dx-codeblock>



### form 请求方式示例代码
<dx-codeblock>
:::  php
<?php

/**
 * Generate a sorted query parameter string from parameter array.
 * such as array('b' => 1, 'a' => 2) to "a=1&b=2"
 *
 * @param array $paramArr
 * @return string sorted query string
 */
function getSortedParameterStr($paramArr) {
    ksort($paramArr);
    $tmpArr = array();
    foreach($paramArr as $k => $v) {
        $tmp = $k;
        if (!empty($v)) {
            $tmp .= ("=" . $v);
        }
        array_push($tmpArr, $tmp);
    }

    return join('&', $tmpArr);
}


// ==========================================================
// Note: Update the customized variables based on your API
// ==========================================================
$apiAppKey = '<your_apiappkey>';
$apiAppSecret = '<your_apiappsecret>';
$httpMethod = "POST";
$acceptHeader = "application/json"; // accept header for your request
$url = 'https://service-xxxx-xxxx.gz.apigw.tencentcs.com/testmock?b=1&a=2';

$formParam = array(
    'id' => 1,
    'name' => 'tencent'
);

$reqBody = getSortedParameterStr($formParam);
$contentType = "application/x-www-form-urlencoded";
// ContentMd5 should be empty for form request
$contentMD5 = "";

// ==========================================================
// customized parameter ends here
// ==========================================================

$parsedUrl = parse_url($url);
$xDateHeader = gmstrftime('%a, %d %b %Y %T %Z', time());

// Note:
// 1. parameters should be in alphabetical order
// 2. form parameter should also append to $pathAndParam
$paramArr = array();
if (!is_null($parsedUrl['query']) && !empty($parsedUrl['query'])) {
    parse_str($parsedUrl['query'], $paramArr);
}
if (!empty($formParam)) {
    $paramArr = array_merge($paramArr, $formParam);
}

$pathAndParam = $parsedUrl['path'];
if (!empty($paramArr)){
    $pathAndParam = $pathAndParam . '?' . getSortedParameterStr($paramArr);
}

// Generate the string to sign
$strToSign = sprintf("x-date: %s\n%s\n%s\n%s\n%s\n%s",
    $xDateHeader, $httpMethod, $acceptHeader, $contentType, $contentMD5, $pathAndParam);
// echo "strToSign: $strToSign\n";

// Encode the string with HMAC and base64
$sign = base64_encode(hash_hmac('sha1', $strToSign, $apiAppSecret, TRUE));
$authHeader = sprintf('hmac id="%s", algorithm="hmac-sha1", headers="x-date", signature="%s"',
    $apiAppKey, $sign);

// Generate the request headers
$headers = array(
    'Host:' . $parsedUrl['host'],
    'Accept:' . $acceptHeader,
    'X-Date:' . $xDateHeader,
    'Content-Type:' . $contentType,  // only required if request body is present
    //'Content-MD5:' . $contentMD5,    // only required if request body is present and not form
    'Authorization:' . $authHeader,
);
// var_dump($headers);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_TIMEOUT, 60);
curl_setopt($ch, CURLOPT_POSTFIELDS, $reqBody); // only required if request body is present
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $httpMethod);
$data = curl_exec($ch);

if (curl_errno($ch)) {
    print "Error: " . curl_error($ch);
} else {
    var_dump($data);
    curl_close($ch);
}
:::
</dx-codeblock>
