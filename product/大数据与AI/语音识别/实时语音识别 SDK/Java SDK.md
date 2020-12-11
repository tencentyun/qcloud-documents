本文介绍如何使用腾讯云语音实时识别服务提供的 Java SDK，包括 SDK 的安装方法及 SDK 代码示例。

## 依赖环境
1. 依赖环境：JDK 1.8版本及以上
2. 从 [腾讯云控制台](https://console.cloud.tencent.com/tts) 开通相应产品。
3. 获取 SecretID、SecretKey 。


## 获取安装
安装 Java SDK 前，先获取安全凭证。在第一次使用 SDK 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey，SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥，SecretKey 必须严格保管，避免泄露。


### 通过 Maven 安装
从 maven 服务器下载最新版本 SDK
```xml
<dependency>
    <groupId>com.tencentcloudapi</groupId>
    <artifactId>tencentcloud-speech-sdk-java</artifactId>
    <version>1.0.8</version>
</dependency>
```

## ASR SDK 说明
###  关键类说明

- SpeechClient  用于创建 SpeechRecognizer 语音识别器的客户端，通过 SpeechClient.newInstance 创建该实例，newInstance 为单例实现。
- SpeechRecognizer 语音识别器，通过客户端 speechClient.newSpeechRecognizer 创建实例。
- SpeechRecognitionRequest 用于配置请求参数，可通过 SpeechRecognitionRequest.initialize() 方法进行初始化。
- SpeechRecognitionResponse 请求响应。
- SpeechRecognitionListener 请求回调。包含识别开始，识别结束等回调方法。




### SDK 使用说明
1.创建 SpeechClient 实例。
2.创建 SpeechRecognitionRequest，这里配置请求相关参数包含切片大、引擎模型类型、文件格式等，具体参考官网[请求参数](https://cloud.tencent.com/document/product/1093/35799) 。
3.创建 SpeechRecognizer 实例，该实例是语音识别的处理者。
4.调用 SpeechRecognizer 的 start 方法，开始识别。
5.调用 SpeechRecognizer 的 write 方法开始发送语音数据。
6.调用 SpeechRecognizer 的 stop 方法，结束识别。

## 示例
#### [参考案例](https://github.com/TencentCloud/tencentcloud-speech-sdk-java-example)

```java
package com.tencentcloud.asr;

import com.tencent.SpeechClient;
import com.tencent.asr.model.*;
import com.tencent.asr.service.SpeechRecognitionListener;
import com.tencent.asr.service.SpeechRecognizer;
import com.tencent.core.model.GlobalConfig;
import com.tencent.core.utils.ByteUtils;
import com.tencent.core.utils.JsonUtil;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;
import java.util.Properties;

public class NewSpeechRecognitionHttpByteArrayExample {

    public static void main(String[] args) throws InterruptedException, IOException {
        GlobalConfig.ifLog = true;
        //默认使用 websocket 协议，可通过该配置指定协议类型
        //SpeechRecognitionSysConfig.requestWay= AsrConstant.RequestWay.Http;
        Properties props = new Properties();
        //从配置文件读取密钥
        props.load(new FileInputStream("../config.properties"));
        String appId = props.getProperty("appId");
        String secretId = props.getProperty("secretId");
        String secretKey = props.getProperty("secretKey");
        
        //1.创建 client 实例 client 为单例
        final SpeechClient speechClient = SpeechClient.newInstance(appId, secretId, secretKey);
        //2.创建 SpeechRecognizerRequest，这里配置请求相关参数包含切片大小、文件格式等
        final SpeechRecognitionRequest request = SpeechRecognitionRequest.initialize();
        //必须手动设置 EngineModelType
        request.setEngineModelType("16k_zh");
        //根据文件格式设置 VoiceFormat
        request.setVoiceFormat(1);
        //3.创建 SpeechRecognizer 实例，该实例是语音识别的处理者。
        SpeechRecognizer speechRecognizer = speechClient.newSpeechRecognizer(request, new MySpeechRecognitionListener());
        //案例使用文件模拟实时获取语音流，用户使用可直接调用 recognize(data) 传入字节数据
        FileInputStream fileInputStream = new FileInputStream(new File("8k.wav"));
        List<byte[]> speechData = ByteUtils.subToSmallBytes(fileInputStream, 3200);
        //4.调用 SpeechRecognizer 的 start 方法，开始识别。
        speechRecognizer.start();
        for (byte[] item : speechData) {
            // 休眠用于模拟语音时长，方便测试，休眠时间根据传输数据选择对应值。实际使用不用休眠
            // 参考时长：8k 3200字节 对应200ms  16k 6400字节对应200ms
            Thread.sleep(200);
            //5.调用 SpeechRecognizer 的 recognize 方法开始发送语音数据。
            speechRecognizer.write(item);
        }
        //6.调用 SpeechRecognizer 的 end 方法，结束识别。
        speechRecognizer.stop();
        fileInputStream.close();
    }

   

    public static class MySpeechRecognitionListener extends SpeechRecognitionListener {
        @Override
        public void onRecognitionResultChange(SpeechRecognitionResponse response) {
            //System.out.println("识别结果:"+JsonUtil.toJson(response));
        }

        @Override
        public void onRecognitionStart(SpeechRecognitionResponse response) {
            System.out.println("开始识别:" + JsonUtil.toJson(response));
        }

        @Override
        public void onSentenceBegin(SpeechRecognitionResponse response) {
            System.out.println("一句话开始:" + JsonUtil.toJson(response));
        }

        @Override
        public void onSentenceEnd(SpeechRecognitionResponse response) {
            System.out.println("一句话结束:" + JsonUtil.toJson(response));
        }

        @Override
        public void onRecognitionComplete(SpeechRecognitionResponse response) {
            System.out.println("识别结束:" + JsonUtil.toJson(response));
        }

        @Override
        public void onFail(SpeechRecognitionResponse response) {
            System.out.println("错误:" + JsonUtil.toJson(response));
        }
    }
}


```



