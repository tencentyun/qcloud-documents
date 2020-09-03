## 接入准备
### SDK获取
录音文件识别 Java SDK 获取，请参考：[Java SDK 依赖环境及获取安装](https://cloud.tencent.com/document/sdk/Java)。

### 接入须知
开发者在调用前请先查看录音文件语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37823)，了解接口的**使用要求**和**使用步骤**。

## 快速接入
以下分别是通过**语音 URL** 和**本地语音上传**请求方式的 demo 以及**轮询**识别结果的 demo ，来帮助客户快速接入。 

+ **通过语音 URL 方式请求**

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

import com.tencentcloudapi.asr.v20190614.models.CreateRecTaskRequest;
import com.tencentcloudapi.asr.v20190614.models.CreateRecTaskResponse;

public class CreateRecTask
{
    public static void main(String [] args) throws IOException {
        //采用音频 URL 方式
        try{
            //重要，此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息，获取方法：
    	   //请参考接口说明（https://cloud.tencent.com/document/product/1093/37139）中的使用步骤 1 进行获取。
            Credential cred = new Credential("Your SecretId", "Your SecretKey");
            
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("asr.tencentcloudapi.com");

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);            
            
            AsrClient client = new AsrClient(cred, "ap-shanghai", clientProfile);
            
            String params = "{\"EngineModelType\":\"16k_zh\",\"ChannelNum\":1,\"ResTextFormat\":0,\"SourceType\":0,\"Url\":\"https://asr-audio-1300466766.cos.ap-nanjing.myqcloud.com/test16k.wav\"}";
            CreateRecTaskRequest req = CreateRecTaskRequest.fromJsonString(params, CreateRecTaskRequest.class);
            
            CreateRecTaskResponse resp = client.CreateRecTask(req);
            
            System.out.println(CreateRecTaskRequest.toJsonString(resp));
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

import com.tencentcloudapi.asr.v20190614.models.CreateRecTaskRequest;
import com.tencentcloudapi.asr.v20190614.models.CreateRecTaskResponse;

public class CreateRecTask
{
    public static void main(String [] args) throws IOException {
        //通过本地音频方式
        try{
             //重要，此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息，获取方法：
    	    //请参考接口说明（https://cloud.tencent.com/document/product/1093/37139）中的使用步骤 1 进行获取。
            Credential cred = new Credential("Your SecretId", "Your SecretKey");
            
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("asr.tencentcloudapi.com");

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);            
            
            AsrClient client = new AsrClient(cred, "ap-shanghai", clientProfile);
            
            String params = "{\"EngineModelType\":\"16k_zh\",\"ChannelNum\":1,\"ResTextFormat\":0,\"SourceType\":1}";
            CreateRecTaskRequest req = CreateRecTaskRequest.fromJsonString(params, CreateRecTaskRequest.class);

            File file = new File("/Users/ruskinli/eclipse-workspace/TencentSentence/src/test.wav");
            FileInputStream inputFile = new FileInputStream(file);
            byte[] buffer = new byte[(int)file.length()];
            req.setDataLen(file.length());
            inputFile.read(buffer);
            inputFile.close();
            String encodeData = Base64.getEncoder().encodeToString(buffer);
            req.setData(encodeData);
            CreateRecTaskResponse resp = client.CreateRecTask(req);
            System.out.println(CreateRecTaskRequest.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
                System.out.println(e.toString());
        }

    }
    
}
```

+ **查询录音文件语音识别结果**

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;

import com.tencentcloudapi.asr.v20190614.AsrClient;

import com.tencentcloudapi.asr.v20190614.models.DescribeTaskStatusRequest;
import com.tencentcloudapi.asr.v20190614.models.DescribeTaskStatusResponse;

public class DescribeTaskStatus
{
    public static void main(String [] args) {
        try{

            //重要，此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息，获取方法：
    	   //请参考接口说明（https://cloud.tencent.com/document/product/1093/37139）中的使用步骤 1 进行获取。
            Credential cred = new Credential("Your SecretId", "Your SecretKey");
            
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("asr.tencentcloudapi.com");

            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);            
            
            AsrClient client = new AsrClient(cred, "ap-shanghai", clientProfile);
            
            String params = "{\"TaskId\":123456}";
            DescribeTaskStatusRequest req = DescribeTaskStatusRequest.fromJsonString(params, DescribeTaskStatusRequest.class);
            
            DescribeTaskStatusResponse resp = client.DescribeTaskStatus(req);
            
            System.out.println(DescribeTaskStatusRequest.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
                System.out.println(e.toString());
        }

    }
    
}
```

