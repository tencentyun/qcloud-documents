
## 操作场景

本文档以 Java 语言为例，介绍客户端通过集成 Java 版本的数据上报 SDK 快捷地将数据上报到 Datahub 中的操作方法。

## 操作步骤

### 步骤1： 创建 HTTP 接入点

参见 [创建HTTP上报接入点 ](https://cloud.tencent.com/document/product/597/66017)在 Datahub 控制台创建一个 HTTP 接入点，获取到标识上报 EndPoint 的DatahubId。

### 步骤2：引入 Java SDK

参见 [SDK中心：Java](https://cloud.tencent.com/document/sdk/Java) 在 Java 项目通过 Maven、Gradle 等方式引入数据上报 SDK。

### 步骤3：数据上报

引入 SDK 后，可以通过调用 SDK 的 SendMessage 接口单条/批量上报数据，整体分为四步：

1. 实例化认证对象
2. 实例化 Client 对象
3. SendMessage 请求上报数据
4. 处理返回结果
<dx-codeblock>
:::  java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.ckafka.v20190819.CkafkaClient;
import com.tencentcloudapi.ckafka.v20190819.models.*;

public class SendMessage
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
            // 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
            Credential cred = new Credential("SecretId", "SecretKey");
            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("ckafka.tencentcloudapi.com");
            // 实例化一个client选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            CkafkaClient client = new CkafkaClient(cred, "ap-beijing", clientProfile);
            // 实例化一个请求对象,每个接口都会对应一个request对象
            SendMessageRequest req = new SendMessageRequest();
            req.setDataHubId("datahub-r6gkngy3");

            BatchContent[] batchContents1 = new BatchContent[2];
            BatchContent batchContent1 = new BatchContent();
            batchContent1.setBody("test1");
            batchContents1[0] = batchContent1;

            BatchContent batchContent2 = new BatchContent();
            batchContent2.setBody("test2");
            batchContents1[1] = batchContent2;

            req.setMessage(batchContents1);

            // 返回的resp是一个SendMessageResponse的实例，与请求对象对应
            SendMessageResponse resp = client.SendMessage(req);
            // 输出json格式的字符串回包
            System.out.println(SendMessageResponse.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
}
:::
</dx-codeblock>


### 步骤4：消息查询

数据发送成功后，可以在消息查询页面，查看数据是否发送成功，详情参见 [消息查询](https://cloud.tencent.com/document/product/597/53176)。





## 各语言 SDK 安装说明

参见 [SDK 中心](https://cloud.tencent.com/document/sdk/Description)。



## 源码 DEMO
<dx-codeblock>
:::  Java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.ckafka.v20190819.CkafkaClient;
import com.tencentcloudapi.ckafka.v20190819.models.*;

public class SendMessage
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
            // 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
            Credential cred = new Credential("SecretId", "SecretKey");
            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("ckafka.tencentcloudapi.com");
            // 实例化一个client选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            CkafkaClient client = new CkafkaClient(cred, "ap-beijing", clientProfile);
            // 实例化一个请求对象,每个接口都会对应一个request对象
            SendMessageRequest req = new SendMessageRequest();
            req.setDataHubId("datahub-r6gkngy3");

            BatchContent[] batchContents1 = new BatchContent[2];
            BatchContent batchContent1 = new BatchContent();
            batchContent1.setBody("test1");
            batchContents1[0] = batchContent1;

            BatchContent batchContent2 = new BatchContent();
            batchContent2.setBody("test2");
            batchContents1[1] = batchContent2;

            req.setMessage(batchContents1);

            // 返回的resp是一个SendMessageResponse的实例，与请求对象对应
            SendMessageResponse resp = client.SendMessage(req);
            // 输出json格式的字符串回包
            System.out.println(SendMessageResponse.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
}
:::
::: Python
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ckafka.v20190819 import ckafka_client, models
try:
    cred = credential.Credential("SecretId", "SecretKey")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ckafka.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ckafka_client.CkafkaClient(cred, "ap-beijing", clientProfile)

    req = models.SendMessageRequest()
    params = {
        "DataHubId": "datahub-r6gkngy3",
        "Message": [
            {
                "Body": "test1"
            },
            {
                "Body": "test2"
            }
        ]
    }
    req.from_json_string(json.dumps(params))

    resp = client.SendMessage(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
:::
::: Node.JS
// Depends on tencentcloud-sdk-nodejs version 4.0.3 or higher
const tencentcloud = require("tencentcloud-sdk-nodejs");

const CkafkaClient = tencentcloud.ckafka.v20190819.Client;

const clientConfig = {
  credential: {
    secretId: "SecretId",
    secretKey: "SecretKey",
  },
  region: "ap-beijing",
  profile: {
    httpProfile: {
      endpoint: "ckafka.tencentcloudapi.com",
    },
  },
};

const client = new CkafkaClient(clientConfig);
const params = {
    "DataHubId": "datahub-r6gkngy3",
    "Message": [
        {
            "Body": "test1"
        },
        {
            "Body": "test2"
        }
    ]
};
client.SendMessage(params).then(
  (data) => {
    console.log(data);
  },
  (err) => {
    console.error("error", err);
  }
);
:::
::: PHP
<?php
require_once 'vendor/autoload.php';
use TencentCloud\Common\Credential;
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Ckafka\V20190819\CkafkaClient;
use TencentCloud\Ckafka\V20190819\Models\SendMessageRequest;
try {

    $cred = new Credential("SecretId", "SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("ckafka.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $client = new CkafkaClient($cred, "ap-beijing", $clientProfile);

    $req = new SendMessageRequest();
    
    $params = array(
        "DataHubId" => "datahub-r6gkngy3",
        "Message" => array(
            array(
                "Body" => "test1"
            ),
            array(
                "Body" => "test2"
            )
        )
    );
    $req->fromJsonString(json_encode($params));

    $resp = $client->SendMessage($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
:::
::: GoLang
package main

import (
        "fmt"

        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
        "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
        ckafka "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ckafka/v20190819"
)

func main() {

        credential := common.NewCredential(
                "SecretId",
                "SecretKey",
        )
        cpf := profile.NewClientProfile()
        cpf.HttpProfile.Endpoint = "ckafka.tencentcloudapi.com"
        client, _ := ckafka.NewClient(credential, "ap-beijing", cpf)

        request := ckafka.NewSendMessageRequest()
        
        request.DataHubId = common.StringPtr("datahub-r6gkngy3")
        request.Message = []*ckafka.BatchContent {
                &ckafka.BatchContent {
                        Body: common.StringPtr("test1"),
                },
                &ckafka.BatchContent {
                        Body: common.StringPtr("test2"),
                },
        }

        response, err := client.SendMessage(request)
        if _, ok := err.(*errors.TencentCloudSDKError); ok {
                fmt.Printf("An API error has returned: %s", err)
                return
        }
        if err != nil {
                panic(err)
        }
        fmt.Printf("%s", response.ToJsonString())
} 
:::
:::  .Net
using System;
using System.Threading.Tasks;
using TencentCloud.Common;
using TencentCloud.Common.Profile;
using TencentCloud.Ckafka.V20190819;
using TencentCloud.Ckafka.V20190819.Models;

namespace TencentCloudExamples
{
    class SendMessage
    {
        static void Main(string[] args)
        {
            try
            {
                Credential cred = new Credential {
                    SecretId = "SecretId",
                    SecretKey = "SecretKey"
                };

                ClientProfile clientProfile = new ClientProfile();
                HttpProfile httpProfile = new HttpProfile();
                httpProfile.Endpoint = ("ckafka.tencentcloudapi.com");
                clientProfile.HttpProfile = httpProfile;

                CkafkaClient client = new CkafkaClient(cred, "ap-beijing", clientProfile);
                SendMessageRequest req = new SendMessageRequest();
                req.DataHubId = "datahub-r6gkngy3";
                BatchContent batchContent1 = new BatchContent();
                batchContent1.Body = "test1";

                BatchContent batchContent2 = new BatchContent();
                batchContent2.Body = "test2";
                req.Message = new BatchContent[] { batchContent1, batchContent2 };

                SendMessageResponse resp = client.SendMessageSync(req);
                Console.WriteLine(AbstractModel.ToJsonString(resp));
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            Console.Read();
        }
    }
}
:::
::: C++
#include <tencentcloud/core/Credential.h>
#include <tencentcloud/core/profile/ClientProfile.h>
#include <tencentcloud/core/profile/HttpProfile.h>
#include <tencentcloud/ckafka/v20190819/CkafkaClient.h>
#include <tencentcloud/ckafka/v20190819/model/SendMessageRequest.h>
#include <tencentcloud/ckafka/v20190819/model/SendMessageResponse.h>
#include <iostream>
#include <string>
#include <vector>

using namespace TencentCloud;
using namespace TencentCloud::Ckafka::V20190819;
using namespace TencentCloud::Ckafka::V20190819::Model;
using namespace std;

int main() {

        Credential cred = Credential("SecretId", "SecretKey");

        HttpProfile httpProfile = HttpProfile();
        httpProfile.SetEndpoint("ckafka.tencentcloudapi.com");

        ClientProfile clientProfile = ClientProfile();
        clientProfile.SetHttpProfile(httpProfile);
        CkafkaClient client = CkafkaClient(cred, "ap-beijing", clientProfile);

        SendMessageRequest req = SendMessageRequest();
        
        req.SetDataHubId("datahub-r6gkngy3");
        BatchContent batchContent1;
        batchContent1.SetBody("test1");
        BatchContent batchContent2;
        batchContent2.SetBody("test2");

        vector<BatchContent> batchContents1 = {batchContent1, batchContent2};
        req.SetMessage(batchContents1);

        auto outcome = client.SendMessage(req);
        if (!outcome.IsSuccess())
        {
            cout << outcome.GetError().PrintAll() << endl;
            return -1;
        }
        SendMessageResponse resp = outcome.GetResult();
        cout << resp.ToJsonString() << endl;
    
    return 0;
}
:::
</dx-codeblock>



