qcloudapi-sdk-php 是为了让 PHP 开发者能够在自己的代码里更快捷方便的使用腾讯云的 API 而开发的 SDK 工具包。

### 快速入门
1. 申请安全凭证。
在第一次使用云 API 之前，首先需要在腾讯云网站上申请安全凭证，安全凭证包括 SecretId 和 SecretKey，SecretId 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
2. 使用 SDK
下载 SDK，放入到程序目录，使用方法请参考下面的示例。
 ```
    <?php
    require_once './src/QcloudApi/QcloudApi.php';

    $config = array('SecretId'       => '您的secretId',
                    'SecretKey'      => '您的secretKey',
                    'RequestMethod'  => 'GET',
                    'DefaultRegion'  => '区域参数');

    // 第一个参数表示使用哪个域名
    // 已有的模块列表：
    // QcloudApi::MODULE_CVM      对应   cvm.api.qcloud.com
    // QcloudApi::MODULE_CDB      对应   cdb.api.qcloud.com
    // QcloudApi::MODULE_LB       对应   lb.api.qcloud.com
    // QcloudApi::MODULE_TRADE    对应   trade.api.qcloud.com
    // QcloudApi::MODULE_SEC      对应   csec.api.qcloud.com
    // QcloudApi::MODULE_IMAGE    对应   image.api.qcloud.com
    // QcloudApi::MODULE_MONITOR  对应   monitor.api.qcloud.com
    // QcloudApi::MODULE_CDN      对应   cdn.api.qcloud.com
    $service = QcloudApi::load(QcloudApi::MODULE_CVM, $config);

    // 请求参数，请参考 wiki 文档上对应接口的说明
    $package = array('offset' => 0,
                     'limit' => 3,
                     // 'Region' => 'gz', // 当 Region 不是上面配置的 DefaultRegion 值时，可以重新指定请求的 Region
                     'SignatureMethod' => 'HmacSHA256',//指定所要用的签名算法，可选 HmacSHA256 或 HmacSHA1，默认为 HmacSHA1
                     );
                     
    // 请求前可以通过下面四个方法重新设置请求的 secretId/secretKey/region/method 参数
    // 重新设置 secretId
    $secretId = '您的secretId';
    $service->setConfigSecretId($secretId);
    // 重新设置 secretKey
    $secretKey = '您的secretKey';
    $service->setConfigSecretKey($secretKey);
    // 重新设置 region
    $region = 'sh';
    $service->setConfigDefaultRegion($region);
    // 重新设置 method
    $method = 'POST';
    $service->setConfigRequestMethod($method);

    // 请求方法为对应接口的接口名，请参考 wiki 文档上对应接口的接口名
    $a = $service->DescribeInstances($package);

    // 生成请求的 URL，不发起请求
    $a = $service->generateUrl('DescribeInstances', $package);

    if ($a === false) {
        // 请求失败，解析错误信息
        $error = $service->getError();
        echo "Error code:" . $error->getCode() . ' message:' . $error->getMessage();

        // 对于异步任务接口，可以通过下面的方法获取对应任务执行的信息
        $detail = $error->getExt();
    } else {
        // 请求成功
        var_dump($a);
    }
 ```
