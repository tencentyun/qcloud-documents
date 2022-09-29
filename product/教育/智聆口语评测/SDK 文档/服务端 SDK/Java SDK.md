## 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。
Tencent Cound API 3.0 SDK，封装了腾讯云的 SDK，通过集成SDK，可以快速接入相关产品功能，如智聆口语评测，数学作业批改，英文作文批改。本文档介绍 [智聆口语评测](https://cloud.tencent.com/document/product/884/19309) 相关说明。

## 流程图
流程图请参见 [服务模式](https://cloud.tencent.com/document/product/884/33697)。

## SDK 集成准备
1. 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在访问管理 > 访问密钥 > [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取该凭证。
>! 密钥属于敏感信息，正式密钥仅可在调试使用，线上环境情况下，为了防止他人盗取，推荐使用 [临时签名](https://cloud.tencent.com/document/product/884/31888#SecretKey)，具体请参考 [签名](https://cloud.tencent.com/document/product/884/31888#SecretKey) 相关内容。
>
![](https://qcloudimg.tencent-cloud.cn/raw/3049463174ada47857762086690e7c26.png)
2. 设备准备
准备一台电脑。

## SDK DEMO 使用流程
1. 安装依赖环境
JDK 7 版本及以上。

2. 下载 SDK
从 github 下载 [tencentcloud-sdk-java](https://github.com/TencentCloud/tencentcloud-sdk-java)。或者在终端输入 git 命令：
```
git clone https://github.com/TencentCloud/tencentcloud-sdk-java.git
```
3. 获取安装
	- 通过 Maven 安装（推荐）
从 3.1.500 版本开始，本项目使用 [KonaJDK](https://github.com/Tencent/TencentKona-8) 编译发布。
通过 Maven 获取安装是使用 Java SDK 的推荐方法，Maven 是 Java 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 Maven 详细可参考 Maven 官网。
		1. 请访问 [Maven 官网](https://maven.apache.org/) 下载对应系统 Maven 安装包进行安装。
		2. 为您的项目添加 Maven 依赖项，只需在 Maven pom.xml 添加以下依赖项即可。注意这里的版本号只是举例，您可以在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 上找到最新的版本(最新版本是3.1.561)
		3. maven仓库中显示的4.0.11是废弃版本，我们已经联系maven官方删除jar包，但maven索引无法清除，请勿使用;
		4. 引用方法可参考示例。
```
<dependency>
    <groupId>com.tencentcloudapi</groupId>
    <artifactId>tencentcloud-sdk-java</artifactId>
    <!-- go to https://search.maven.org/search?q=tencentcloud-sdk-java and get the latest version. -->
    <!-- 请到https://search.maven.org/search?q=tencentcloud-sdk-java查询所有版本，最新版本如下 -->
    <version>3.1.561</version>
</dependency>
```
		5. 如上引用方式会将腾讯云所有产品 sdk 下载到本地，可以将 artifactId 换成 tencentcloud-sdk-java-cvm/cbs/vpc 等，即可引用特定产品的 sdk，代码中使用方式和大包相同，可参考示例。最新版本也可在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 查询，可大大节省存储空间。
		6. 中国大陆地区的用户可以使用镜像源加速下载，编辑 maven 的 settings.xml 配置文件，在 mirrors 段落增加镜像配置：
```
<mirror>
  <id>tencent</id>
  <name>tencent maven mirror</name>
  <url>https://mirrors.tencent.com/nexus/repository/maven-public/</url>
  <mirrorOf>*</mirrorOf>
</mirror>

```
	- 通过源码包进行安装
		1. 前往 [Github 仓库](https://github.com/tencentcloud/tencentcloud-sdk-java) 或者 [Gitee 仓库](https://gitee.com/tencentcloud/tencentcloud-sdk-java) 下载源码压缩包。
		2. 解压源码包到您项目合适的位置。
		3. 需要将 vendor目 录下的 jar 包放在 Java 的可找到的路径中。
		4. 引用方法可参考示例。
4. 运行项目
进入 `examples/soe/v20180903/InitOralProcess.java` ，填入本地音频文件路径、SecretId 和 SecretKey。
![](https://qcloudimg.tencent-cloud.cn/raw/acab51d9ef0d8cb001697035ffbd5f18.png)
填入请求参数，参考 [InitOralProcess](https://cloud.tencent.com/document/product/884/19319)，运行项目，进行评测。
![](https://qcloudimg.tencent-cloud.cn/raw/4a175ae4fa6550f349c0ddf0d2ce9cbe.png)
获取评测结果，参考 [数据结构](https://cloud.tencent.com/document/product/884/19320)。

## SDK 使用方法
### 临时密钥（推荐）
客户端为了密钥安全性，需要考虑在服务端使用临时密钥，对密钥进行加密处理。Java 临时密钥参考如下（填入密钥信息使用）：
```
package sts.v20180813;

import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.sts.v20180813.StsClient;
import com.tencentcloudapi.sts.v20180813.models.GetFederationTokenRequest;
import com.tencentcloudapi.sts.v20180813.models.GetFederationTokenResponse;


public class GetFederationToken {
    public static void main(String[] args)throws Exception {
        try {
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setReqMethod("POST"); // post请求(默认为post请求)
            httpProfile.setConnTimeout(60); // 请求连接超时时间，单位为秒(默认60秒)
            httpProfile.setEndpoint("sts.tencentcloudapi.com"); // 指定接入地域域名(默认就近接入)

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setUnsignedPayload(true);
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            StsClient client = new StsClient(cred, "ap-beijing",clientProfile);

            GetFederationTokenRequest req = new GetFederationTokenRequest();

            req.setName("soe");
            req.setPolicy("{\"version\": \"2.0\",\"statement\": {\"effect\": \"allow\", \"action\": [\"soe:TransmitOralProcessWithInit\"], \"resource\": \"*\"}}");

            GetFederationTokenResponse resp = client.GetFederationToken(req);

            // 输出json格式的字符串回包
            System.out.println(GetFederationTokenResponse.toJsonString(resp));


        } catch (TencentCloudSDKException e) {
            e.printStackTrace();
        }
    }
}

```

### 内部签名（推荐）
#### 发音数据传输接口附带初始化过程(推荐)
[TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口使用示例。
采用语音输入模式：流式分片。
```
package soe.v20180724;

import java.nio.file.Files;
import java.nio.file.Paths;

import java.util.UUID;
import java.util.Arrays;
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.soe.v20180724.SoeClient;
import com.tencentcloudapi.soe.v20180724.models.TransmitOralProcessWithInitRequest;
import com.tencentcloudapi.soe.v20180724.models.TransmitOralProcessWithInitResponse;


public class TransmitOralProcessWithInit {

    public static void main(String[] args) throws Exception {
        try {
            String file = ""; //本地音频文件
            int PKG_SIZE = 2 * 1024; //分片大小
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
            Credential cred = new Credential("", "");

            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setReqMethod("POST"); // post请求(默认为post请求)
            httpProfile.setConnTimeout(60); // 请求连接超时时间，单位为秒(默认60秒)
            httpProfile.setEndpoint("soe.ap-beijing.tencentcloudapi.com"); // 指定接入地域域名(默认就近接入)

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setUnsignedPayload(true);
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            SoeClient client = new SoeClient(cred, "", clientProfile);
            String sessionId = UUID.randomUUID().toString();

            TransmitOralProcessWithInitRequest req = new TransmitOralProcessWithInitRequest();

            req.setVoiceEncodeType(1L);  //语音数据类型1:pcm
            req.setVoiceFileType(3L); //语音文件类型
            req.setSessionId(sessionId); //唯一标识
            req.setRefText("book"); //文本
            req.setWorkMode(0L); //0,流式分片,1一次性评测
            req.setEvalMode(0L); //评估模式,0,单词.1,句子,2,段落,3自由说,4单词纠错
            req.setScoreCoeff(1.0f); //评估难度
            req.setServerType(0L); //服务类型.0英文,1中文
            req.setIsAsync(0L); //异步
            req.setIsQuery(0L); //轮询
            req.setTextMode(0L); //文本格式.0普通文本 1,音素结构
            
            //将文件装换成base64
            byte[] data = Files.readAllBytes(Paths.get(file));
            int pkgNum = (int) Math.ceil((double) data.length/PKG_SIZE);
            for(int i = 1;i<=pkgNum;i++){
                int lastIndex = i * PKG_SIZE;
                if (i == pkgNum) {
                    lastIndex = data.length;
                }
                byte[] buf = Arrays.copyOfRange(data, (i - 1) * PKG_SIZE, lastIndex);
                String base64Str = new sun.misc.BASE64Encoder().encode(buf);
                req.setUserVoiceData(base64Str);
                req.setSeqId((long) i);
                if (i == pkgNum) {
                    req.setIsEnd(1L);
                } else {
                    req.setIsEnd(0L);
                }

                TransmitOralProcessWithInitResponse resp = client.TransmitOralProcessWithInit(req);

                // 输出json格式的字符串回包
                System.out.println(TransmitOralProcessWithInitResponse.toJsonString(resp));
                // 也可以取出单个值。
                // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
                System.out.println(resp.getPronAccuracy());
            }
        } catch (TencentCloudSDKException e) {
            System.out.println(e);
        }
    }
}

```

#### 发音评估初始化和发音数据传输接口
[InitOralProcess](https://cloud.tencent.com/document/api/884/19319) 和 [TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318) 组合使用示例：
```
package soe.v20180724;

import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.soe.v20180724.SoeClient;
import com.tencentcloudapi.soe.v20180724.models.InitOralProcessRequest;
import com.tencentcloudapi.soe.v20180724.models.TransmitOralProcessRequest;
import com.tencentcloudapi.soe.v20180724.models.InitOralProcessResponse;
import com.tencentcloudapi.soe.v20180724.models.TransmitOralProcessResponse;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.UUID;

public class InitAndTransmitOralProcess {

    public static void main(String[] args) {
        try {
            String file = ""; //本地音频文件
            String sessionId = UUID.randomUUID().toString();
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
            Credential cred = new Credential("secretId", "secretId");

            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setReqMethod("POST"); // post请求(默认为post请求)
            httpProfile.setConnTimeout(60); // 请求连接超时时间，单位为秒(默认60秒)
            httpProfile.setEndpoint("soe.ap-beijing.tencentcloudapi.com"); // 指定接入地域域名(默认就近接入)

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setUnsignedPayload(true);
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            SoeClient client = new SoeClient(cred, "", clientProfile);
            InitOralProcessRequest req = new InitOralProcessRequest();
            req.setSessionId(sessionId);
            req.setRefText("bike");
            req.setWorkMode(1L);
            req.setEvalMode(0L);
            req.setScoreCoeff(1.0f);
            req.setServerType(0L);

            InitOralProcessResponse res = client.InitOralProcess(req);

            // 输出json格式的字符串回包
            System.out.println(InitOralProcessResponse.toJsonString(res));
            // 也可以取出单个值。
            // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
            System.out.println(res.getRequestId());
            TransmitOralProcessRequest transreq = new TransmitOralProcessRequest();

            transreq.setIsEnd(1L);
            transreq.setSeqId(1L);
            transreq.setSessionId(sessionId);
            // base64编码数据
            byte[] buf = Files.readAllBytes(Paths.get(file));
            String base64Str = new sun.misc.BASE64Encoder().encode(buf);

            transreq.setUserVoiceData(base64Str);
            transreq.setVoiceEncodeType(1L);
            transreq.setVoiceFileType(3L);

            TransmitOralProcessResponse transres = client.TransmitOralProcess(transreq);

            // 输出json格式的字符串回包
            System.out.println(TransmitOralProcessResponse.toJsonString(transres));
            // 也可以取出单个值。
            // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
            System.out.println(transres.getPronAccuracy());
        } catch (TencentCloudSDKException | IOException e) {
            e.printStackTrace();
        }
    }

}
```

#### 关键词评测
[KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 接口使用示例：
```
package soe.v20180724;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.UUID;

import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.soe.v20180724.SoeClient;
import com.tencentcloudapi.soe.v20180724.models.InitOralProcessResponse;
import com.tencentcloudapi.soe.v20180724.models.KeywordEvaluateRequest;
import com.tencentcloudapi.soe.v20180724.models.Keyword;
import com.tencentcloudapi.soe.v20180724.models.KeywordEvaluateResponse;

public class KeywordEvaluate {
    public static final String AUDIO_FOR_ONCE = "";

    public static void main(String [] args) throws IOException {
        try{
            String file = ""; //本地音频文件
            String sessionId = UUID.randomUUID().toString();
            Credential cred = new Credential("", "");

            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("soe.tencentcloudapi.com");

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);

            SoeClient client = new SoeClient(cred, "", clientProfile);

            KeywordEvaluateRequest req = new KeywordEvaluateRequest();
            req.setSeqId(1L);
            req.setIsEnd(1L);
            req.setVoiceFileType(3L);
            req.setVoiceEncodeType(1L);
            req.setSessionId(sessionId);
            byte[] buf = Files.readAllBytes(Paths.get(AUDIO_FOR_ONCE));
            String base64Str = new sun.misc.BASE64Encoder().encode(buf);
            req.setUserVoiceData(base64Str);

            Keyword[] keywords1 = new Keyword[2];
            Keyword keyword1 = new Keyword();
            keyword1.setRefText("bike");
            keyword1.setEvalMode(0L);
            keyword1.setServerType(0L);
            keyword1.setScoreCoeff(1.0f);
            keyword1.setTextMode(0L);
            keywords1[0] = keyword1;

            Keyword keyword2 = new Keyword();
            keyword2.setRefText("bick");
            keyword2.setEvalMode(0L);
            keyword2.setServerType(0L);
            keyword2.setScoreCoeff(1.0f);
            keyword2.setTextMode(0L);
            keywords1[1] = keyword2;

            req.setKeywords(keywords1);

            KeywordEvaluateResponse resp = client.KeywordEvaluate(req);
            System.out.println(KeywordEvaluateResponse.toJsonString(resp));

        } catch (TencentCloudSDKException | IOException e) {
            System.out.println(e.toString());
        }
    }
}
```

### 外部签名（不推荐）
使用 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口演示：
1. 生成 curl
```
package soe.v20180724;

import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;
import java.util.TreeMap;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class TencentCloudAPITC3Demo {
    private final static Charset UTF8 = StandardCharsets.UTF_8;
    private final static String SECRET_ID = "";
    private final static String SECRET_KEY = "";
    private final static String CT_JSON = "application/json; charset=utf-8";

    public static byte[] hmac256(byte[] key, String msg) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKeySpec = new SecretKeySpec(key, mac.getAlgorithm());
        mac.init(secretKeySpec);
        return mac.doFinal(msg.getBytes(UTF8));
    }

    public static String sha256Hex(String s) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] d = md.digest(s.getBytes(UTF8));
        return DatatypeConverter.printHexBinary(d).toLowerCase();
    }

    public static void main(String[] args) throws Exception {

        String service = "soe";
        String host = "soe.tencentcloudapi.com";
        String region = "ap-guangzhou";
        String action = "TransmitOralProcessWithInit";
        String version = "2018-07-24";
        String algorithm = "TC3-HMAC-SHA256";
//        String timestamp = "1551113065";
        String timestamp = String.valueOf(System.currentTimeMillis() / 1000);
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        // 注意时区，否则容易出错
        sdf.setTimeZone(TimeZone.getTimeZone("UTC"));
        String date = sdf.format(new Date(Long.valueOf(timestamp + "000")));

        // ************* 步骤 1：拼接规范请求串 *************
        String httpRequestMethod = "POST";
        String canonicalUri = "/";
        String canonicalQueryString = "";
        String canonicalHeaders = "content-type:application/json; charset=utf-8\n" + "host:" + host + "\n";
        String signedHeaders = "content-type;host";
//        String AUDIO_FOR_ONCE = "bike.mp3";
//        byte[] buf = Files.readAllBytes(Paths.get(AUDIO_FOR_ONCE));
//        String base64Str = new sun.misc.BASE64Encoder().encode(buf);
        String payload = "{\"SeqId\": 1, \"IsEnd\": 1, \"VoiceFileType\": 3, \"VoiceEncodeType\": 1, \"UserVoiceData\": \"//MoxAALuN4gAUkwAYQh1xWKzZAAMDZPRAKCRiYoJEEP/c4jHPJk0zAGA02ghGPERnaPZARHP8f+BkQQ/CqjfIxQLhkl2RAz//MoxAwPgNqoAZp4ADtQSTWOF1F+AEmTEImdt6jsb6WhXxTCvtkfiVUSLYdfX7hHvulYVqRfAZ+XOecxF//ph/+HbmNezSs8//MoxAkO4Oq4y9pQACMIy2HqbczDokotX71inxey/+udQMhypprA6IdjTWZWb0/QeaAFihx9/dr6NrdmgLOhat/++GIFmkGq//MoxAgOOO7UAHvKcD4u3EwOF9XNMK99Nu9Malj/0ERAqKi6tqYOCnGMAYuPg4il3/+fNB4QBhqZkYLEFC36InsC0mtHtEHf//MoxAoNYPLQAIPScBN69jsHpVNf/FFkPLf/UQ5X6QoAgm+QLisHkaUGoJEMFc///21mX2f9aRil/+KtwSkZ0XEtUWAzE23n//MoxA8Q4OrAAHvecHuoXU9pmuMRsAAl5kxR+iGa25Xy5K5DZndk+5GjFi4ruA3Po3Y////6CJMIhNvYgUhIGXFlFdljblAF//MoxAYOOLcWXmrSTqAB3RCZhvPpqgorarEywEZfpMLiImr/EbP9oFSJ/tRkmWkyCqSB7////ZGIiBim4gD60h/bQ8PAPWCj//MoxAgNMK7dlGveTCGa8yD4Mq/3dFs2/HPQW1XSttIJyKLf22MNsUyxqRmPUuHgi0b////9eQ9wkusmAPBsncNhPkwKoUqn//MoxA4MyK7IAGteTC6OJRT0Ugvx6Ur7OCiUV3r9HnSoYlWVg6oBkf////vLEFNRFMnV8nAFvQwtRZv2MBA4/bybO662jmbd//MoxBUMWNrIAGvMcOK8QpNEgWIosuBaLtuJf9k8M////7UF2StBPfNK6hDgnRvqAyTP/SiQH8hU31/HJqzWg1N61Y0lmoYI//MoxB4NINbEAGvQcGCCb5XfJDJD///1PwmCwKnlG36HrNEa6iqFSihJgRArUoxkzNS9Nr7hnHzGj4peHNfx0dx3LDJ2SFjN//MoxCQMcMrEAIvMcFl0ir////A6xOIktb+mtyEzawnALISGYieXWnFQ5AFCGKxU3XkVteSTc2uUS0oUBAWA0eU+W/t/9QVD//MoxC0NKMa8KmIEcEDQPB2WBqDVr/8/52mU2Dx0NTL1rqQqpzzbAf/0iBIOu37LJ1HPQzcM7dkKXYXETT9ZXqET//UHZbrV//MoxDMMkN6QUNJEcCkoBAN01mbKkI1yPAyqjxXtZltKeAxYa4aAqf+eSGHFlLlKD6m2O9vnhi9qmO////s/+lVRTMnty4ke//MoxDsM0Dp4H1kQABcA/8JwUE/8ciCyT/8YceY5ETf/8RgchQJAcBKf/5OGEHIPMwJQTP//83QGHJdyTGHHmQP///yTJceB//MoxEIXmxqkAYdoAdL49B6EoTBLB4BaP////wtAwA80jQvqY+XDQvrKtXQiaPYkjALhtQTGjWUR4g9zGdfMjohS5vsRp3Xo//MoxB4UcuLQAYcoAb+onWzt9f+RhpFP7qevrbvcyIFMkVE+uYqgxxbzTrFaiZ27KGnYnMR+UYQwfHKYo78ih2r+1cO1qvRa//MoxAcNkp68AYIoAHv6P9ef7/qHBTqpfQWY1u230+YsSHE+2/2RH7SlnoAx0+tLJ/r6CcvMYWMVd9n66oKbdTGxwbruYXOO//MoxAsOchKQAYI4ACXC5rVY5PHD9jnod+arRqj5hL80xXnzl9f+sgPH/uPP/+3lHRircOlTv5Fm0l+qx+zHquq7CjCgJhQE//MoxAwNqSGQA8MQAEkzN/+hjPq1W//qygIlAICFKAnvBpZ0sWPCV1WCpU6DQ87/Ue6vyUGiwNVMQU1FMy45OS41VVVVVVVV\", \"SessionId\": \"test_1432543\", \"RefText\": \"bick sdfad\", \"WorkMode\": 1, \"EvalMode\": 1, \"ScoreCoeff\": 1}";
        String hashedRequestPayload = sha256Hex(payload);
        String canonicalRequest = httpRequestMethod + "\n" + canonicalUri + "\n" + canonicalQueryString + "\n"
                + canonicalHeaders + "\n" + signedHeaders + "\n" + hashedRequestPayload;
        System.out.println(canonicalRequest);

        // ************* 步骤 2：拼接待签名字符串 *************
        String credentialScope = date + "/" + service + "/" + "tc3_request";
        String hashedCanonicalRequest = sha256Hex(canonicalRequest);
        String stringToSign = algorithm + "\n" + timestamp + "\n" + credentialScope + "\n" + hashedCanonicalRequest;
        System.out.println(stringToSign);

        // ************* 步骤 3：计算签名 *************
        byte[] secretDate = hmac256(("TC3" + SECRET_KEY).getBytes(UTF8), date);
        byte[] secretService = hmac256(secretDate, service);
        byte[] secretSigning = hmac256(secretService, "tc3_request");
        String signature = DatatypeConverter.printHexBinary(hmac256(secretSigning, stringToSign)).toLowerCase();
        System.out.println(signature);

        // ************* 步骤 4：拼接 Authorization *************
        String authorization = algorithm + " " + "Credential=" + SECRET_ID + "/" + credentialScope + ", "
                + "SignedHeaders=" + signedHeaders + ", " + "Signature=" + signature;
        System.out.println(authorization);

        TreeMap<String, String> headers = new TreeMap<String, String>();
        headers.put("Authorization", authorization);
        headers.put("Content-Type", CT_JSON);
        headers.put("Host", host);
        headers.put("X-TC-Action", action);
        headers.put("X-TC-Timestamp", timestamp);
        headers.put("X-TC-Version", version);
        headers.put("X-TC-Region", region);

        StringBuilder sb = new StringBuilder();
        sb.append("curl -X POST https://").append(host)
                .append(" -H \"Authorization: ").append(authorization).append("\"")
                .append(" -H \"Content-Type: application/json; charset=utf-8\"")
                .append(" -H \"Host: ").append(host).append("\"")
                .append(" -H \"X-TC-Action: ").append(action).append("\"")
                .append(" -H \"X-TC-Timestamp: ").append(timestamp).append("\"")
                .append(" -H \"X-TC-Version: ").append(version).append("\"")
                .append(" -H \"X-TC-Region: ").append(region).append("\"")
                .append(" -d '").append(payload).append("'");
        System.out.println(sb.toString());
    }
}
```

2. 根据签名信息，进行调用
```
OkHttpClient client = new OkHttpClient().newBuilder().build();
MediaType mediaType = MediaType.parse("application/json; charset=utf-8");
RequestBody body = RequestBody.create(mediaType, payload);
Request request = new Request.Builder()
  .url("https://soe.tencentcloudapi.com")
  .method("POST", body)
  .addHeader("Authorization", authorization)
  .addHeader("Content-Type", "application/json; charset=utf-8")
  .addHeader("Host", host)
  .addHeader("X-TC-Action",action)
  .addHeader("X-TC-Timestamp", timestamp)
  .addHeader("X-TC-Version", region)
  .addHeader("X-TC-Region", payload)
  .build();
Response response = client.newCall(request).execute();
```

## 参数说明
### 请求参数说明

| 接口名称 | 接口功能 | 
|---------|---------|
| [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 	| 发音数据传输接口附带初始化过程（常用实践）| 
| [InitOralProcess](https://cloud.tencent.com/document/api/884/19319)	| 发音评估初始化| 
| [KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 	| 关键词评测| 
|[TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318)	|发音数据传输接口|
 
### 返回结果说明
参考 API 文档 [数据结构](https://cloud.tencent.com/document/api/884/19320)。

## 错误码
参考 API 文档 [错误码](https://cloud.tencent.com/document/api/884/30658)。

## 常见问题
参考 [常见问题](https://cloud.tencent.com/document/product/884/32593)。 






