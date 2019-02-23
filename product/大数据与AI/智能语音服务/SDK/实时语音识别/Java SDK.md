## 开发准备
### 相关环境
实时语音识别 [Java SDK 下载地址>>](https://main.qcloudimg.com/raw/870ef507ac3ffc62c34e28670015ba98/RASRjavasdk.zip)

### 环境依赖
JDK1.8 及以上。

### 安装 SDK
**源码安装**
根据下载地址下载源码，解压获得的压缩包得到如下图的文件和文件夹。
![](https://main.qcloudimg.com/raw/f3ae2e90e822e0abda0b401456074a79.png)
本 SDK 源码放在 src 文件夹中：RASRsdk.java，您只需将本文件及其相关依赖放在项目中即可使用本 SDK。
您可以直接使用 RASRtest.java 文件，对本 SDK 进行测试，也可以直接修改 RASRtest.java。
test.wav 为测试音频，大小为8k16bit。

### 卸载 SDK
删除相关文件与依赖文件即可卸载本 SDK。

## 快速入门
```
public class RASRtest {
    public static void main(String[] args) {
        //用户需修改为自己的secretid，secret_key,appid
        String secret_key = "kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP";
        String secretid = "AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8";
        String appid = "1255628450";

        //识别引擎 8k_0 or 16k_0
        String engine_model_type = "8k_0";

        //结果返回方式 0：同步返回 or 1：尾包返回
        String res_type = "0";

        // 识别结果文本编码方式 0:UTF-8,1:GB2312,2:GBK,3:BIG5
        String result_text_format = "0";

        // 语音编码方式 1:wav 4:sp 6:skill
        String voice_format = "1";

        String filepath = "D:\\test.wav";

        // 语音切片长度 cutlength<200000
        int cutlength = 6400;
        //调用setConfig函数设置相关参数
        int res = RASRsdk.setConfig(secret_key, secretid, appid, engine_model_type, res_type, result_text_format, voice_format, filepath, cutlength);
        if (res < 0) {
            return;
        }
        //调用sendVoice函数获得音频识别结果
        RASRsdk.sendVoice();
    }
}

```
				
				
				
