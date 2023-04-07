# HLS标准加密

视频加密是指对视频中的内容进行加密，可有效防止视频泄露和盗链问题，广泛用于在线教育及财经等领域。本文介绍数据万象HLS标准加密的原理和接入流程。

## 工作原理

COS服务采用信封数据加密的方式加密视频。业务方调用腾讯云密钥管理服务（KMS）生成数据密钥（DK）和信封数据密钥（EDK），然后利用数据密钥（DK）加密视频，并将加密后的文件和信封数据密钥（EDK）存储。播放器终端通过解密服务获取数据密钥（DK）请求解密播放视频。
数据万象视频加密流程如下：
![](https://qcloudimg.tencent-cloud.cn/raw/98568aaba384766c1c8ffb7e18747b58.png)

>?业务方开通腾讯云数据万象服务（CI）、存储服务（COS）、访问控制（CAM）、密钥管理服务（KMS）以及内容分发网络（CDN）（如未开通）。

### 加密流程

1. 用户业务侧将视频上传到对象存储后，请求 HLS 加密。
2. 数据万象收到加密请求后，向 KMS 请求加密密钥。
3. 数据万象通过转码功能对视频进行 HLS 加密。
4. 加密后，对象存储通过 CDN 分发加密后的 HLS 视频文件。

### 解密流程

1. 终端用户登录播放器终端，用户业务侧会对终端用户进行身份校验，校验通过后，会为播放终端分配一个 Token，并将带 Token 的播放地址返回给播放器端。
2. 用户播放终端解析返回的 m3u8 文件，得到 “URI” 内容，向 URI 请求密钥。
3. 用户业务侧的风控管理服务收到请求后，先根据用户逻辑自行判断合法性，再通过调用 KMS 服务的 API 查询密钥。
4. 密钥管理服务将返回的密钥返回给播放终端。播放终端通过获取的密钥对 m3u8 文件进行解密并播放。

## 业务方实现概览

### 接入准备

1. 开通腾讯云相关服务
2. 授权数据万象媒体处理访问KMS
3. 调用KMS服务的解密接口搭建解密服务，并将调用KMS接口获得的明文密钥Base64 Decode之后返回播放终端

### 加密视频

1. 登录 [数据万象控制台](https://console.cloud.tencent.com/ci)。
2. 在左侧导航栏中，单击**存储桶管理**，进入存储桶列表。
3. 找到您需要存储视频的存储桶，并单击右侧操作栏的**管理**，进入相应存储桶管理页面。
4. 单击左侧的**媒体处理**，选择**模板**页签，进入模板配置页面。
5. 选择**音视频转码**，单击**创建转码模板**，弹出创建转码模板窗口。
6. 在创建转码模板窗口中，配置如下信息：
   ![](https://main.qcloudimg.com/raw/447d05493505550ebf05cd9960822b21.png)

 - 模板名称：长度不超过64字符，仅支持中文、英文、数字、下划线`_`、中划线`-`和`*`。
 - 封装格式：选择 HLS。
 - 转码时长：可选为源视频时长、自定义配置时长。
 - 高级配置： 
   - 视频加密：开启视频加密。
   - UriKey：用户搭建的密钥管理服务的地址。

7. 单击**确定**，完成加密模板配置，后续选用此模板 [配置工作流](https://cloud.tencent.com/document/product/460/46488) 或 [配置任务](https://cloud.tencent.com/document/product/460/46489) 即可实现加密视频。

>? 可根据您使用的开发语言选择查看对应代码示例。



### 播放HLS加密视频

请按以下指引完成视频解密播放：
1. 搭建token服务。

>! token服务需要根据您的加密逻辑自行搭建，以达到更高的视频安全等级。

2. 搭建解密服务。
搭建一个本地HTTP服务，用于解密视频和获取解密密钥。

以下为PHP示例代码：

```java
<?php
/**
 * 需要用到 腾讯云开发者工具套件（SDK）3.0 获取地址 https://github.com/TencentCloud/tencentcloud-sdk-php
 * 万象控制台配置转码文件的 UriKey 之后，该接口的处理逻辑参考以下 demo
 * 1) 获取到密文 $_GET['Ciphertext']
 * 2) 请求 KMS Decrypt 接口，拿到响应后 进行 base64解码
 * 3) 接口返回 解码后的字符串
 */

require_once './tencentcloud-sdk-php/vendor/autoload.php';

use TencentCloud\Common\Credential;
use TencentCloud\Kms\V20190118\KmsClient;
use TencentCloud\Kms\V20190118\Models\DecryptRequest;
use TencentCloud\Common\Exception\TencentCloudSDKException;

$secretId = "";
$secretKey = "";
$ciphertext = $_GET['Ciphertext'];
$kmsRegion = $_GET['KMSRegion'];

try {
    $cred = new Credential($secretId, $secretKey);
    $kmsClient = new KmsClient($cred, $kmsRegion);

    $decryptRequest = new DecryptRequest();
    $decryptRequest->setCiphertextBlob($ciphertext);
    $resp = $kmsClient->Decrypt($decryptRequest);
    $plaintext = $resp->getPlaintext();
    $decodeStr = base64_decode($plaintext);

    echo $decodeStr;
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

java 示例代码如下：
[完整示例](https://github.com/563750789/HLS-video-demo/blob/master/src/main/java/com/qcloud/cos/hlsvideodemo/demo/example.m3u8)

```java
@RestController
@CrossOrigin("*")
public class KMSDecryptController {

    @RequestMapping("decrypt")
    public void decrypt(@RequestParam("Ciphertext") String ciphertext,@RequestParam("KMSRegion") String region, HttpServletResponse response) {
        try {
            // 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey,此处还需注意密钥对的保密
            // 密钥可前往 https://console.cloud.tencent.com/cam/capi 网站进行获取
            Credential cred = new Credential("", "");
            // 实例化 http
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("kms.tencentcloudapi.com");
            // 实例化一个 client 选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的 client 对象,clientProfile 是可选的
            KmsClient client = new KmsClient(cred, region, clientProfile);
            // 实例化一个请求对象,每个接口都会对应一个 request 对象
            DecryptRequest req = new DecryptRequest();
            //写入待解密数据
            req.setCiphertextBlob(ciphertext);
            // 返回的 resp 是一个 DecryptResponse 的实例，与请求对象对应
            DecryptResponse resp = client.Decrypt(req);
            String plaintext = resp.getPlaintext();
            //对秘钥进行 base64解密
            byte[] decode = Base64.getDecoder().decode(plaintext);
            //返回流
            ServletOutputStream outputStream = response.getOutputStream();
            outputStream.write(decode);
            outputStream.close();
        } catch (TencentCloudSDKException | IOException e) {
            System.out.println(e.toString());
        }
    }
}
```

3. 播放加密视频。
您可以使用自己的播放器或腾讯云播放器播放加密视频。

