## 操作场景

该任务指导您使用 PHP 语言，通过应用认证来对您的 API 进行认证管理。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“应用认证”（参见 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参见 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台 [应用管理](https://console.cloud.tencent.com/apigateway/app) 界面创建应用。
4. 在应用列表中选中已经创建好的应用，单击**绑定 API**，选择服务和 API 后单击**提交**，即可将应用与 API 建立绑定关系。
5. 参见 [示例代码](#示例代码)，使用 PHP 语言生成签名内容。

## 环境依赖

- 本示例代码支持 PHP 7 版本，其他 PHP 版本可能需要您适当修改。
- API 网关提供 JSON 请求方式和 form 请求方式的示例代码，请您根据自己业务的实际情况合理选择。

## 注意事项

- 应用生命周期管理，以及 API 向应用授权、应用绑定 API 等操作请您参见 [应用管理](https://cloud.tencent.com/document/product/628/55087)。
- 应用生成签名过程请您参见 [应用认证方式](https://cloud.tencent.com/document/product/628/55088)。

## 示例代码[](id:示例代码)
<dx-accordion>
::: 基础代码
<dx-codeblock>
:::  php
<?php

const FORM_URLENCODED = "application/x-www-form-urlencoded";

/**
 * Generate a sorted query parameter string from parameter array.
 * such as array('b' => 1, 'a' => 2) to "a=1&b=2"
 *
 * @param array $paramArr
 * @return string sorted query string
 */
function getSortedParameterStr($paramArr)
{
    ksort($paramArr);
    $tmpArr = array();
    foreach ($paramArr as $k => $v) {
        $tmp = $k;
        if (!empty($v)) {
            $tmp .= ("=" . $v);
        }
        array_push($tmpArr, $tmp);
    }

    return join('&', $tmpArr);
}

/**
 * Send a HTTP request with App Authorization
 *
 * @param $apiAppKey string API App Key
 * @param $apiAppSecret string API App Secret
 * @param $method string HTTP Method of API
 * @param $url string Request URL of API, note that environment path (/release) is not allowed
 * @param $contentType string Request Content-Type header, set empty if request body is not needed
 * @param $acceptHeader string Accept HTTP request header
 * @param $reqBody string Request Body, set null if request body is not needed
 * @param $formParam array form parameters array, set null if not form request
 * @param $algorithm string Encryption algorithm: sha1, sha256, sha384, sha512, SM3, default to sha1
 * @param $customHeaders array Custom HTTP Headers, such as `array('x-header-a' => 1)`
 */
function sendRequestWithAppAuth($apiAppKey, $apiAppSecret, $method, $url, $contentType, $acceptHeader,
                                $reqBody=null, $formParam=null, $algorithm=null, $customHeaders=null)
{
    $contentMD5 = "";
    $isForm = ($contentType == FORM_URLENCODED);
    // Note: ContentMd5 is empty for application/x-www-form-urlencoded request
    if ($isForm) {
        assert(!is_null($formParam), "formParam is required for form request");
        // generate request body from form parameters
        $reqBody = getSortedParameterStr($formParam);
    } elseif (!is_null($reqBody)) {
        // get content md5 for signing the request later
        $contentMD5 = base64_encode(md5($reqBody));
    }

    if (null === $algorithm) {
        $algorithm = "sha1";
    }

    // ===================================
    // STEP 1: Generate the string to sign
    // ===================================

    echo "1. URL:\n $url\n";

    // Note:
    // 1. parameters needs to be sorted in alphabetical order
    // 2. parameters include both query parameters and form parameters
    $paramArr = array();
    $parsedUrl = parse_url($url);
    if (!is_null($parsedUrl['query']) && !empty($parsedUrl['query'])) {
        parse_str($parsedUrl['query'], $paramArr);
    }
    if (!empty($formParam)) {
        $paramArr = array_merge($paramArr, $formParam);
    }

    $pathAndParam = $parsedUrl['path'];
    if (!empty($paramArr)) {
        $pathAndParam = $pathAndParam . '?' . getSortedParameterStr($paramArr);
    }

    $xDateHeader = gmstrftime('%a, %d %b %Y %T %Z', time());
    $strToSign = sprintf("x-date: %s\n%s\n%s\n%s\n%s\n%s",
        $xDateHeader, $method, $acceptHeader, $contentType, $contentMD5, $pathAndParam);

    // Print stringToSign for debugging if authorization failed with 401
    $strToSignDebug = str_replace("\n", "#", $strToSign);
    echo "2. StringToSign:\n $strToSignDebug\n";

    // ===============================================================================
    // STEP 2: generate the signature (Authorization header) based on the stringToSign
    // ===============================================================================

    // Encode the string with HMAC and base64.
    $sign = base64_encode(hash_hmac($algorithm, $strToSign, $apiAppSecret, TRUE));
    $authHeader = sprintf(
        'hmac id="%s", algorithm="hmac-%s", headers="x-date", signature="%s"',
        $apiAppKey, $algorithm, $sign
    );

    $headers = array(
        'Host:' . $parsedUrl['host'],
        'Accept:' . $acceptHeader,
        'X-Date:' . $xDateHeader,
        'Authorization:' . $authHeader,
    );
    if (!empty($contentType)) {
        array_push($headers, "Content-Type:" . $contentType);
    }
    if (!empty($contentMD5)) {
        array_push($headers, "Content-MD5:" . $contentMD5);
    }
    if (!is_null($customHeaders) && is_array($customHeaders)) {
        foreach ($customHeaders as $k => $v) {
            array_push($headers, $k . ":" . $v);
        }
    }

    echo "3. Request Headers:\n";
    var_dump($headers);

    // ============================
    // STEP 3: send the API request
    // ============================

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_TIMEOUT, 60);
    if (!empty($reqBody)) {
        curl_setopt($ch, CURLOPT_POSTFIELDS, $reqBody); // only required if request body is present
    }
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
    $data = curl_exec($ch);
    if (curl_errno($ch)) {
        print "Error: " . curl_error($ch);
    } else {
        echo "Response: \n";
        var_dump($data);
        curl_close($ch);
    }
}
:::
</dx-codeblock>
:::
::: GET 请求示例
<dx-codeblock>
:::  php
// ==========================================================
// Example 1: send a GET request without a request body
// ==========================================================
$apiAppKey = '<your_app_key>';
$apiAppSecret = '<your_app_secret>';

$httpMethod = "GET";
$acceptHeader = "application/json";

// Note: environment path, such as `/release`, is not supported with App Authorization
$url = 'https://service-xxxx-xxxx.gz.apigw.tencentcs.com/testmock?b=1&a=2';
sendRequestWithAppAuth($apiAppKey, $apiAppSecret, $httpMethod, $url, "", $acceptHeader);
:::
</dx-codeblock>
:::
::: POST JSON 请求示例
<dx-codeblock>
:::  php
// ==========================================================
// Example 2: send a POST request with JSON request body
// ==========================================================
$apiAppKey = '<your_app_key>';
$apiAppSecret = '<your_app_secret>';

$httpMethod = "POST";
$acceptHeader = "application/json";
$contentType = "application/json";

// Note: environment path, such as `/release`, is not supported with App Authorization
$url = 'https://service-xxxx-xxxx.gz.apigw.tencentcs.com/testmock?b=1&a=2';
$jsonBody = "{\"data\":1}";
sendRequestWithAppAuth($apiAppKey, $apiAppSecret, $httpMethod, $url,
    $contentType, $acceptHeader, $jsonBody);
:::
</dx-codeblock>
:::
::: POST form-urlencoded 请求示例
<dx-codeblock>
:::  php
$apiAppKey = '<your_app_key>';
$apiAppSecret = '<your_app_secret>';

$httpMethod = "POST";
$acceptHeader = "application/json";
$contentType = "application/x-www-form-urlencoded";

// Note: environment path, such as `/release`, is not supported with App Authorization
$url = 'https://service-xxxx-xxxx.gz.apigw.tencentcs.com/testmock?b=1&a=2';
$customHeaders = array("x-custom-header" => 1);
$formParam = array('id' => 1, 'name' => 'tencent');
sendRequestWithAppAuth($apiAppKey, $apiAppSecret, $httpMethod, $url,
    $contentType, $acceptHeader, null, $formParam, null, $customHeaders);
:::
</dx-codeblock>
:::
</dx-accordion>


