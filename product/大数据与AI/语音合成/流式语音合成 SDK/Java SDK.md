本文介绍如何使用腾讯云语音合成服务提供的 Java SDK，包括 SDK 的安装方法及 SDK 代码示例。

## 依赖环境
1. 依赖环境：JDK 1.8版本及以上。
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
    <version>1.0.7</version>
</dependency>
```

## TTS SDK 说明
###  关键类说明

- SpeechClient 通过 SpeechClient.newInstance 创建该实例，newInstance 为单例实现。
- SpeechSynthesizer 语音合成器，通过客户端 speechClient.newSpeechSynthesizer 创建实例。
- SpeechSynthesizerRequest 用于配置请求参数，可通过 SpeechSynthesizerRequest.initialize() 方法进行初始化。
- SpeechSynthesizerResponse 请求响应。
- SpeechSynthesizerListener 请求回调。包含 onMessage onComplete  onFail 回调方法。




### SDK 使用说明
1.创建 SpeechClient 实例。
2.创建 SpeechSynthesisRequest，这里配置请求相关参数，具体参考官网 [请求参数](https://cloud.tencent.com/document/product/1073/34093) 。
3.创建 SpeechSynthesizer 实例，该实例是语音识别的处理者。
4.调用 SpeechSynthesizer 的 synthesis 方法开始发送语音数据。

## 示例
#### [参考案例](https://github.com/TencentCloud/tencentcloud-speech-sdk-java-example)

```java
package com.tencentcloud.tts;

import com.tencent.SpeechClient;
import com.tencent.core.model.GlobalConfig;
import com.tencent.tts.model.*;
import com.tencent.tts.service.SpeechSynthesizer;
import com.tencent.tts.service.SpeechSynthesisListener;
import com.tencent.tts.utils.Ttsutils;

import java.io.*;
import java.util.Properties;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * 语音合成 example
 */
public class SpeechTtsExample {

    public static void main(String[] args) throws IOException {
        GlobalConfig.ifLog=true;
        //从配置文件读取密钥
        Properties props = new Properties();
        props.load(new FileInputStream("../config.properties"));
        String appId = props.getProperty("appId");
        String secretId = props.getProperty("secretId");
        String secretKey = props.getProperty("secretKey");


        //创建 SpeechSynthesizerClient 实例，目前是单例
        SpeechClient client = SpeechClient.newInstance(appId, secretId, secretKey);
        //初始化 SpeechSynthesizerRequest，SpeechSynthesizerRequest 包含请求参数
        SpeechSynthesisRequest request = SpeechSynthesisRequest.initialize();


        //使用客户端 client 创建语音合成实例
        SpeechSynthesizer speechSynthesizer = client.newSpeechSynthesizer(request, new SpeechTtsExample.MySpeechSynthesizerListener());
        //执行语音合成
        String ttsTextLong = "暖国的雨，向来没有变过冰冷的坚硬的灿烂的雪花。博识的人们觉得他单调，他自己也以为不幸否耶？江南的雪，可是滋润美艳之至了；" +
                "那是还在隐约着的青春的消息，是极壮健的处子的皮肤。雪野中有血红的宝珠山茶，白中隐青的单瓣梅花，深黄的磬口的蜡梅花；雪下面还有冷绿的杂草。" +
                "蝴蝶确乎没有；蜜蜂是否来采山茶花和梅花的蜜，我可记不真切了。但我的眼前仿佛看见冬花开在雪野中，有许多蜜蜂们忙碌地飞着，也听得他们嗡嗡地闹着。" +
                "孩子们呵着冻得通红，像紫芽姜一般的小手，七八个一齐来塑雪罗汉。因为不成功，谁的父亲也来帮忙了。罗汉就塑得比孩子们高得多，虽然不过是上小下大的一堆，" +
                "终于分不清是壶卢还是罗汉；然而很洁白，很明艳，以自身的滋润相粘结，整个地闪闪地生光。孩子们用龙眼核给他做眼珠，又从谁的母亲的脂粉奁中偷得胭脂来涂在嘴唇上。" +
                "这回确是一个大阿罗汉了。他也就目光灼灼地嘴唇通红地坐在雪地里。";
        speechSynthesizer.synthesis(ttsTextLong);
    }


    public static class MySpeechSynthesizerListener extends SpeechSynthesisListener {

        private AtomicInteger sessionId = new AtomicInteger(0);

        @Override
        public void onComplete(SpeechSynthesisResponse response) {
            System.out.println("onComplete");
            if (response.getSuccess()) {
                Ttsutils.printAndSaveResponse(16000, response.getAudio(), response.getSessionId());
            }
            System.out.println("结束：" + response.getSuccess() + " " + response.getCode() + " " + response.getMessage() + " " + response.getEnd());
        }

        //语音合成的语音二进制数据
        @Override
        public void onMessage(byte[] data) {
            System.out.println("onMessage:" + data.length);
            // Your own logic.
            String filePath = "logs/handler_" + "result_" + sessionId + ".pcm";
            //Ttsutils.saveResponseToFile(data, filePath);
            sessionId.incrementAndGet();
        }

        @Override
        public void onFail(SpeechSynthesisResponse response) {
            System.out.println("onFail");
        }
    }
}


```



