## 功能介绍
随着终端用户个性化的需求愈加丰富，简单的文字交互和图片上传已经不能满足展示与分享信息的诉求，UGC(User Generated Content)也就应运而生。腾讯视频云点播业务的UGC功能，即客户端上传视频功能，支持终端用户将一段短小的视频快速地上传到云端。另外，值得一提的是，依托于腾讯云的支持，后续也能做到播放流畅。

点播UGC上传SDK的能力包括：

1. 客户端本地视频上传；
2. 上传视频封面；
3. 分片并发上传；
4. 断点续传；
5. 获取上传进度。

目前腾讯云点播提供给如下平台的UGC上传SDK：

1. [iOS UGC SDK](/document/product/266/7836)；
2. [Android UGC SDK](/document/product/266/7837)。

## 业务流程
UGC视频上传的整体流程分为如下两部：

1. 客户端向服务端申请上传签名；
2. 调用腾讯云点播的UGC SDK，进行视频上传。

### 客户端申请上传签名
为了确保开发者在云点播的空间不被恶意使用，对于所有的UGC上传请求，点播服务端都会校验该请求的合法性。因此，客户端在发起视频上传之前，必须先向APP的后台申请签名。

获取上传文件签名的计算过程，可简单分为如下三个步骤：获取签名所需信息，拼接明文字符串，将明文字符串转化为签名。

**Step1：获取签名所需信息**

生成签名所需信息包括项目的Secret ID、Secret Key和待上传文件的文件名。可以在腾讯云管理中心控制台页面的**【云产品】**---**【监控与管理】**下的**【云 API 密钥】**页面查看到自己的Secret ID和Secret Key。

**Step2：拼接签名明文字符串**

签名明文字符串 Original 的格式如下：  

Original="s=[SecretID]&f=[FileName]&t=[currentTime]&e=[expiredTime]&r=[rand]"
 
签名明文串中各字段含义如下：

- s 	项目的Secret ID 
- f 	待上传文件的文件名称 
- t 	当前时间戳，是一个符合 Unix Epoch时间戳规范的数值，单位为秒 
- e 	签名的失效时刻，是一个符合Unix Epoch时间戳规范的数值，单位为秒。e的计算方式为e = t + 签名有效时长。签名有效时长最大取值为777600090天） 
- r 	随机串，无符号10进制整数，用户需自行生成，最长10位 

**Step3：将明文字符串转化为签名**

拼接好签名的明文字符串Original后，用已经获取的SecretKey对明文串进行**HMAC-SHA1**加密，得到SignTmp：
 
SignTmp = HMAC-SHA1(SecretKey, Original) 

将密文串SignTmp放在明文串Origin前面，拼接后进行**Base64Encode**算法，得到最终的签名Sign：
 
Sign = Base64(append(SignTmp, Original)) 

> 注意
> 
> 1. 此处使用的是标准的Base64编码，不是urlsafe的Base64编码。
> 2. 由于使用了HMAC算法，计算SignTmp的结果为二进制字符串，因此建议将算法写在同一函数中实现。单独输出SignTmp可能导致拼接后的字串有误。 

## 示例

### PHP示例
 
本节介绍生成签名的算法实例，实例中使用PHP语言（若开发者使用其他开发语言，请使用对应的函数）。 

#####1、获取签名所需信息获取得到的签名所需信息如下：
 
$secret_id = "AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv";
 
$secret_key = "bLcPnl88WU30VY57ipRhSePfPdOfSruK";
 
$current = time();
 
$expired = $current + 3600;
  
$rdm = rand();
 
$filename = "tencent_test.mp4";
 
#####2、拼接签名明文串
 
$orignal = 'k='.$secret_id.'&t='.$current.'&e='.$expired.'&f='.$filename.'&r='.$rdm;
 
#####3、生成签名
 
$signature=base64_encode(hash_hmac('SHA1',$orignal,$secret_key, true).$orignal);
 
echo $signature."\n";
  
如 original="s=AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv&f=tencent_test.mp4&t=1437995644&e=1437995704&r=2081660421"
 
最终得到的签名为：
 
IEmbRAPy5IgIAFnt7XPAToaY3RRzPUFLSURVZkxVRVVpZ1FpWHFtN0NWU3NwS0pudWFpSUt0eHFBdiZmPXRlbmNlbnRfdGVzdC5tcDQmdD0xNDM3OTk1NjQ0JmU9MTQzNzk5NTcwNCZyPTIwODE2NjA0MjE= 
