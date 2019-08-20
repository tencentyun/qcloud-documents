## 接入准备
### SDK获取
一句话语音识别 Java SDK 安装及相关环境说明 [Java SDK 安装及相关环境说明>>](https://cloud.tencent.com/document/sdk/Java)

### 接入须知
开发者在调用前请先查看一句话语音识别的[ 接口说明]()，了解接口的**使用要求**和**使用步骤**。

## 快速接入
以下分别是通过**语音URL**和**本地语音上传**请求方式的demo，来帮助客户快速接入。

+ **通过语音URL方式请求**

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Base64;
import com.tencentcloudapi.asr.v20190614.AsrClient;
import com.tencentcloudapi.asr.v20190614.models.SentenceRecognitionRequest;
import com.tencentcloudapi.asr.v20190614.models.SentenceRecognitionResponse;

public class SentenceRecognition
{
    public static void main(String [] args) throws IOException {
    	 // 采用语音URL方式调用
        try{
    		  //重要：<Your SecretId>、<Your SecretKey>需要替换成客户自己的账号信息
    		  //请参考接口说明中的使用步骤1进行获取。 
            Credential cred = new Credential("Your SecretId", "Your SecretKey");
            
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("asr.tencentcloudapi.com");

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);            
            
            AsrClient client = new AsrClient(cred, "ap-shanghai", clientProfile);
            
            String params = "{\"ProjectId\":0,\"SubServiceType\":2,\"EngSerViceType\":\"16k\",\"SourceType\":0,\"Url\":\"http://ttsgz-1255628450.cos.ap-guangzhou.myqcloud.com/20190813/cbf318cd-273e-4b7c-bab0-50a1885c9b96.wav\",\"VoiceFormat\":\"wav\",\"UsrAudioKey\":\"session-123\"}";
            SentenceRecognitionRequest req = SentenceRecognitionRequest.fromJsonString(params, SentenceRecognitionRequest.class);
            
            SentenceRecognitionResponse resp = client.SentenceRecognition(req);
            
            System.out.println(SentenceRecognitionRequest.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
                System.out.println(e.toString());
        }
    }
    
}
```

+ **通过本地语音上传方式请求**

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Base64;

import com.tencentcloudapi.asr.v20190614.AsrClient;

import com.tencentcloudapi.asr.v20190614.models.SentenceRecognitionRequest;
import com.tencentcloudapi.asr.v20190614.models.SentenceRecognitionResponse;

public class SentenceRecognition
{
    public static void main(String [] args) throws IOException {
        
        //采用本地语音上传方式调用
    	try{
    		  //重要：<Your SecretId>、<Your SecretKey>需要替换成客户自己的账号信息
    		  //请参考接口说明中的使用步骤1进行获取。 
            Credential cred = new Credential("Your SecretId", "Your SecretKey");
            
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("asr.tencentcloudapi.com");

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);            
            
            AsrClient client = new AsrClient(cred, "ap-shanghai", clientProfile);
            
            String params = "{\"ProjectId\":0,\"SubServiceType\":2,\"EngSerViceType\":\"16k\",\"SourceType\":1,\"Url\":\"\",\"VoiceFormat\":\"wav\",\"UsrAudioKey\":\"session-123\"}";
            SentenceRecognitionRequest req = SentenceRecognitionRequest.fromJsonString(params, SentenceRecognitionRequest.class);
       
            File file = new File("/Users/ruskinli/eclipse-workspace/TencentSentence/src/test.wav");
            FileInputStream inputFile = new FileInputStream(file);
            byte[] buffer = new byte[(int)file.length()];
            req.setDataLen(file.length());
            inputFile.read(buffer);
            inputFile.close();
            String encodeData = Base64.getEncoder().encodeToString(buffer);
            req.setData(encodeData);
            
            SentenceRecognitionResponse resp = client.SentenceRecognition(req);
            
            System.out.println(SentenceRecognitionRequest.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
                System.out.println(e.toString());
        }

    }
    
}
```

