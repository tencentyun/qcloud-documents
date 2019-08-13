## 开发准备
### 相关环境
一句话语音识别[ Java SDK下载地址>>](https://main.qcloudimg.com/raw/1ebec980474c7bf16e7cbfb79d1bc559/SASRjavasdk.zip)

### 环境依赖
JDK 1.8 及以上。

### 安装 SDK
**源码安装**
根据下载地址下载源码，解压获得的压缩包得到如下图的文件和文件夹。
![](https://main.qcloudimg.com/raw/3a1c7d927c915636ce6d8f3af78f50fd.png)
本 SDK 源码放在 src 文件夹中：SASRsdk.java，用户可将本文件即其相关依赖放在项目中即可使用本 SDK。
若想使用本 SDK 直接测试，可使用 SASRtest.java 文件进行测试，用户可以直接修改 SASRtest.java。
test.wav 为测试音频，8k16bit。
### 卸载 SDK
卸载方式即删除相关 cpp 文件与静态库文件即可。
## 快速入门
```
public class SASRtest {
    public static void main(String[] args) {

        //用户需修改为自己的SecretId，SecretKey
        String SecretId = "AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8";
        String SecretKey = "kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP";

        // 识别引擎 8k or 16k
        String EngSerViceType = "8k";

        // 语音数据来源 0:语音url or 1:语音数据bodydata(data数据大小要小于800k)
        String SourceType = "0";

        //音频格式 wav，mp3
        String VoiceFormat = "wav";

        // 语音数据地址
        //String fileURI = "D:\\test.wav";
        String fileURI="http://liqiansunvoice-1255628450.cosgz.myqcloud.com/30s.wav";

        //调用setConfig函数设置相关参数
        int res = SASRsdk.setConfig(SecretId, SecretKey, EngSerViceType, SourceType, VoiceFormat, fileURI);
        if (res < 0) {
            return;
        }

        //调用sendVoice函数获得音频识别结果
       try{ 
            SASRsdk.sendVoice(); 
       }catch (Exception e){ 
          e.printStackTrace(); 
       } 
       }
       }
  ```

