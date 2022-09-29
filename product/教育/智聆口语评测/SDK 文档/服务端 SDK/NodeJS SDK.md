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
安装 NODEJS 10.0.0 版本及以上。
2. 下载 SDK
从 github 下载 [tencentcloud-sdk-nodejs](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)。或者在终端输入 git 命令：
```
git clone https://github.com/TencentCloud/tencentcloud-sdk-nodejs.git
```
如果无法使用git或不清楚如何使用，可以单击 [这里](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/archive/refs/heads/master.zip) 下载。

3. 获取安装
	- 通过 Npm 安装
通过 npm 获取安装是使用 NODEJS SDK 的推荐方法，npm 是 NODEJS 的包管理工具。关于 npm 详细可参考 [npm 官网](https://www.npmjs.com/ )。
		1. 执行以下安装命令：npm install tencentcloud-sdk-nodejs --save
		2. 在您的代码中引用对应模块代码，可参考示例。
		3. 如上引用方式会将腾讯云所有产品 sdk 下载到本地，可以将 `tencentcloud-sdk-nodejs` 换成 `tencentcloud-sdk-nodejs-cvm/cbs/vpc` 等，即可引用特定产品的 sdk，代码中可将 `require("tencentcloud-sdk-nodejs")` 改为 `require("tencentcloud-sdk-nodejs-cvm/cbs/vpc")`，其余不变，可参考示例，可大大节省存储空间。
	- 通过源码包安装
		1. 前往 [Github 仓库](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 或者 [Gitee 仓库](https://gitee.com/tencentcloud/tencentcloud-sdk-nodejs) 下载源码压缩包。
		2. 解压源码包到您项目合适的位置。
		3. 在您的代码中引用对应模块代码，可参考示例。
4. 运行项目
进入 `examples/soe/v20180903/init_oral_process.js`，填入SecretId 和 SecretKey。
![](https://qcloudimg.tencent-cloud.cn/raw/ed32a9b683396f5eadf2004171071344.png)
填入请求参数，参考 [InitOralProcess](https://cloud.tencent.com/document/product/884/19319)，运行项目，进行评测。
![](https://qcloudimg.tencent-cloud.cn/raw/f690c747ad881743081940f4b88bdd68.png)
获取评测结果，参考 [数据结构](https://cloud.tencent.com/document/product/884/19320)。

## SDK 使用方法
### 临时密钥（推荐）
客户端为了密钥安全性，需要考虑在服务端使用临时密钥，对密钥进行加密处理。NodeJS 临时密钥参考如下（填入密钥信息使用）：
```
// Depends on tencentcloud-sdk-nodejs version 4.0.3 or higher
const tencentcloud = require("tencentcloud-sdk-nodejs");

const StsClient = tencentcloud.sts.v20180813.Client;

// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
// 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
const clientConfig = {
  credential: {
    secretId: "",
    secretKey: "",
  },
  region: "ap-beijing",
  profile: {
    httpProfile: {
      endpoint: "sts.tencentcloudapi.com",
    },
  },
};

// 实例化要请求产品的client对象,clientProfile是可选的
const client = new StsClient(clientConfig);
const policy = {
    version: '2.0',
    statement: {
      effect: 'allow',
      action: ['soe:TransmitOralProcessWithInit'],
      resource: '*'
    }
  };

const params = {
    "Name": "soe",
    "Policy": encodeURIComponent(JSON.stringify(policy))
};
client.GetFederationToken(params).then(
  (data) => {
    console.log(data);
  },
  (err) => {
    console.error("error", err);
  }
);
```
### 内部签名（推荐）
#### 发音数据传输接口附带初始化过程(推荐)
[TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口使用示例：
需要安装 `node-uuid : npm install node-uuid`。
```
const tencentcloud = require("tencentcloud-sdk-nodejs");

//导入对应产品模块的client models。
const SoeClient = tencentcloud.soe.v20180724.Client;

const fs = require('fs');
const path = require('path');
const mineType = require('mime-types');


// console.log(data);

// 获取uuid
var uuid = require('node-uuid');
let SessionId = uuid.v1();


const clientConfig = {
    credential: {
      secretId: "",
      secretKey: "",
    },
    region: "",
    profile: {
      httpProfile: {
        endpoint: "soe.tencentcloudapi.com",
      },
    },
  };
  
  // 实例化要请求产品的client对象,clientProfile是可选的
  const client = new SoeClient(clientConfig);
  // 获取base64数据
  let PKG_SIZE = 10 * 1024;
  let filePath = path.resolve(''); //本地音频文件
  let data = fs.readFileSync(filePath);
  let pkgNum = Math.ceil(data.length / PKG_SIZE);
  for (let i = 1; i <= pkgNum; i++) {
    let lastIndex = i * PKG_SIZE;
    if (i == pkgNum) {
        lastIndex = data.length;
    }
    let buf = data.slice((i - 1) * PKG_SIZE, lastIndex)

    data = buf.toString('base64');
    if (i == pkgNum) {
        IsEnd = 1;
    } else {
        IsEnd = 0;
    }
    const params = {
        "SeqId": i,
        "IsEnd": IsEnd,
        "VoiceFileType": 2,
        "VoiceEncodeType": 1,
        "UserVoiceData": data,
        "SessionId": SessionId,
        "RefText": "hello",
        "WorkMode": 0,
        "EvalMode": 0,
        "ScoreCoeff": 1
    };
    client.TransmitOralProcessWithInit(params).then(
      (data) => {
        console.log(data);
      },
      (err) => {
        console.error("error", err);
      }
    );
  }

```

#### 发音评估初始化和发音数据传输接口
[InitOralProcess](https://cloud.tencent.com/document/api/884/19319) 和 [TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318) 组合使用示例：
```
const tencentcloud = require("tencentcloud-sdk-nodejs");

//导入对应产品模块的client models。
const SoeClient = tencentcloud.soe.v20180724.Client;

const fs = require('fs');
const path = require('path');
const mineType = require('mime-types');

let filePath = path.resolve(''); //本地音频文件
let data = fs.readFileSync(filePath);

data = new Buffer.from(data).toString('base64');
// console.log(data);

var uuid = require('node-uuid');
let SessionId = uuid.v1();

const clientConfig = {
credential: {
    secretId: "",
    secretKey: "",
},
region: "",
profile: {
    httpProfile: {
    endpoint: "soe.tencentcloudapi.com",
    },
},
};
  
// 实例化要请求产品的client对象,clientProfile是可选的
const client = new SoeClient(clientConfig);
const params = {
    "SessionId": SessionId,
    "RefText": "hello",
    "WorkMode": 1,
    "EvalMode": 1,
    "ScoreCoeff": 1
};
client.InitOralProcess(params).then(
(data) => {
    console.log(data);
},
(err) => {
    console.error("error", err);
}
);

client.TransmitOralProcess(
{
    SessionId: SessionId,
    VoiceFileType: 2,
    SeqId: 1,
    VoiceEncodeType: 1,
    IsEnd: 1,
    UserVoiceData:data},
function (err, response) {
    // 请求异常返回，打印异常信息
    if (err) {
    console.log(err)
    return
    }
    // 请求正常返回，打印response对象
    console.log(response)
}
)
```

#### 关键词评测
[KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 接口使用示例：
```
// Depends on tencentcloud-sdk-nodejs version 4.0.3 or higher
const tencentcloud = require("tencentcloud-sdk-nodejs");

const SoeClient = tencentcloud.soe.v20180724.Client;
const fs = require('fs');
const path = require('path');
const mineType = require('mime-types');

// 获取base64数据
let filePath = path.resolve(''); //本地音频文件地址
let data = fs.readFileSync(filePath);
data = new Buffer.from(data).toString('base64');
// console.log(data);

// 获取uuid
var uuid = require('node-uuid');
let SessionId = uuid.v1();

// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
// 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
const clientConfig = {
  credential: {
    secretId: "",
    secretKey: "",
  },
  region: "",
  profile: {
    httpProfile: {
      endpoint: "soe.tencentcloudapi.com",
    },
  },
};

// 实例化要请求产品的client对象,clientProfile是可选的
const client = new SoeClient(clientConfig);
const params = {
    "SeqId": 1,
    "IsEnd": 1,
    "VoiceFileType": 2,
    "VoiceEncodeType": 1,
    "UserVoiceData": data,
    "SessionId": SessionId,
    "Keywords": [
        {
            "RefText": "hello",
            "EvalMode": 0,
            "ServerType": 0,
            "ScoreCoeff": 1
        },
        {
            "RefText": "我",
            "EvalMode": 0,
            "ServerType": 1,
            "ScoreCoeff": 1
        }
    ]
};
client.KeywordEvaluate(params).then(
  (data) => {
    console.log(data);
  },
  (err) => {
    console.error("error", err);
  }
);

```

### 外部签名（不推荐）
使用 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口演示：
1. 生成 curl
```
const crypto = require('crypto');
const { mainModule } = require('process');
var request = require("request");

function sha256(message, secret = '', encoding) {
    const hmac = crypto.createHmac('sha256', secret)
    return hmac.update(message).digest(encoding)
}
function getHash(message, encoding = 'hex') {
    const hash = crypto.createHash('sha256')
    return hash.update(message).digest(encoding)
}
function getDate(timestamp) {
    const date = new Date(timestamp * 1000)
    const year = date.getUTCFullYear()
    const month = ('0' + (date.getUTCMonth() + 1)).slice(-2)
    const day = ('0' + date.getUTCDate()).slice(-2)
    return `${year}-${month}-${day}`
}
function main(){
    // 密钥参数
    const SECRET_ID = ""
    const SECRET_KEY = ""

    const endpoint = "soe.tencentcloudapi.com"
    const service = "soe"
    const region = "ap-guangzhou"
    const action = "TransmitOralProcessWithInit"
    const version = "2018-07-24"
    const timestamp =  parseInt(new Date().getTime()/1000);
    console.log(timestamp)
    // const timestamp = 1551113065
    //时间处理, 获取世界时间日期
    const date = getDate(timestamp)
    console.log(date)

    // ************* 步骤 1：拼接规范请求串 *************
    const signedHeaders = "content-type;host"

    const payload = "{\"SeqId\": 1, \"IsEnd\": 1, \"VoiceFileType\": 3, \"VoiceEncodeType\": 1, \"UserVoiceData\": \"//MoxAALuN4gAUkwAYQh1xWKzZAAMDZPRAKCRiYoJEEP/c4jHPJk0zAGA02ghGPERnaPZARHP8f+BkQQ/CqjfIxQLhkl2RAz//MoxAwPgNqoAZp4ADtQSTWOF1F+AEmTEImdt6jsb6WhXxTCvtkfiVUSLYdfX7hHvulYVqRfAZ+XOecxF//ph/+HbmNezSs8//MoxAkO4Oq4y9pQACMIy2HqbczDokotX71inxey/+udQMhypprA6IdjTWZWb0/QeaAFihx9/dr6NrdmgLOhat/++GIFmkGq//MoxAgOOO7UAHvKcD4u3EwOF9XNMK99Nu9Malj/0ERAqKi6tqYOCnGMAYuPg4il3/+fNB4QBhqZkYLEFC36InsC0mtHtEHf//MoxAoNYPLQAIPScBN69jsHpVNf/FFkPLf/UQ5X6QoAgm+QLisHkaUGoJEMFc///21mX2f9aRil/+KtwSkZ0XEtUWAzE23n//MoxA8Q4OrAAHvecHuoXU9pmuMRsAAl5kxR+iGa25Xy5K5DZndk+5GjFi4ruA3Po3Y////6CJMIhNvYgUhIGXFlFdljblAF//MoxAYOOLcWXmrSTqAB3RCZhvPpqgorarEywEZfpMLiImr/EbP9oFSJ/tRkmWkyCqSB7////ZGIiBim4gD60h/bQ8PAPWCj//MoxAgNMK7dlGveTCGa8yD4Mq/3dFs2/HPQW1XSttIJyKLf22MNsUyxqRmPUuHgi0b////9eQ9wkusmAPBsncNhPkwKoUqn//MoxA4MyK7IAGteTC6OJRT0Ugvx6Ur7OCiUV3r9HnSoYlWVg6oBkf////vLEFNRFMnV8nAFvQwtRZv2MBA4/bybO662jmbd//MoxBUMWNrIAGvMcOK8QpNEgWIosuBaLtuJf9k8M////7UF2StBPfNK6hDgnRvqAyTP/SiQH8hU31/HJqzWg1N61Y0lmoYI//MoxB4NINbEAGvQcGCCb5XfJDJD///1PwmCwKnlG36HrNEa6iqFSihJgRArUoxkzNS9Nr7hnHzGj4peHNfx0dx3LDJ2SFjN//MoxCQMcMrEAIvMcFl0ir////A6xOIktb+mtyEzawnALISGYieXWnFQ5AFCGKxU3XkVteSTc2uUS0oUBAWA0eU+W/t/9QVD//MoxC0NKMa8KmIEcEDQPB2WBqDVr/8/52mU2Dx0NTL1rqQqpzzbAf/0iBIOu37LJ1HPQzcM7dkKXYXETT9ZXqET//UHZbrV//MoxDMMkN6QUNJEcCkoBAN01mbKkI1yPAyqjxXtZltKeAxYa4aAqf+eSGHFlLlKD6m2O9vnhi9qmO////s/+lVRTMnty4ke//MoxDsM0Dp4H1kQABcA/8JwUE/8ciCyT/8YceY5ETf/8RgchQJAcBKf/5OGEHIPMwJQTP//83QGHJdyTGHHmQP///yTJceB//MoxEIXmxqkAYdoAdL49B6EoTBLB4BaP////wtAwA80jQvqY+XDQvrKtXQiaPYkjALhtQTGjWUR4g9zGdfMjohS5vsRp3Xo//MoxB4UcuLQAYcoAb+onWzt9f+RhpFP7qevrbvcyIFMkVE+uYqgxxbzTrFaiZ27KGnYnMR+UYQwfHKYo78ih2r+1cO1qvRa//MoxAcNkp68AYIoAHv6P9ef7/qHBTqpfQWY1u230+YsSHE+2/2RH7SlnoAx0+tLJ/r6CcvMYWMVd9n66oKbdTGxwbruYXOO//MoxAsOchKQAYI4ACXC5rVY5PHD9jnod+arRqj5hL80xXnzl9f+sgPH/uPP/+3lHRircOlTv5Fm0l+qx+zHquq7CjCgJhQE//MoxAwNqSGQA8MQAEkzN/+hjPq1W//qygIlAICFKAnvBpZ0sWPCV1WCpU6DQ87/Ue6vyUGiwNVMQU1FMy45OS41VVVVVVVV\", \"SessionId\": \"test_1432543\", \"RefText\": \"bick sdfad\", \"WorkMode\": 1, \"EvalMode\": 1, \"ScoreCoeff\": 1}"

    const hashedRequestPayload = getHash(payload);
    const httpRequestMethod = "POST"
    const canonicalUri = "/"
    const canonicalQueryString = ""
    const canonicalHeaders = "content-type:application/json; charset=utf-8\n" + "host:" + endpoint + "\n"

    const canonicalRequest = httpRequestMethod + "\n"
                            + canonicalUri + "\n"
                            + canonicalQueryString + "\n"
                            + canonicalHeaders + "\n"
                            + signedHeaders + "\n"
                            + hashedRequestPayload
    console.log(canonicalRequest)
    // console.log("----------------------------")

    // ************* 步骤 2：拼接待签名字符串 *************
    const algorithm = "TC3-HMAC-SHA256"
    const hashedCanonicalRequest = getHash(canonicalRequest);
    const credentialScope = date + "/" + service + "/" + "tc3_request"
    const stringToSign = algorithm + "\n" +
                    timestamp + "\n" +
                    credentialScope + "\n" +
                    hashedCanonicalRequest
    // console.log(stringToSign)
    // console.log("----------------------------")

    // ************* 步骤 3：计算签名 *************
    const kDate = sha256(date, 'TC3' + SECRET_KEY)
    const kService = sha256(service, kDate)
    const kSigning = sha256('tc3_request', kService)
    const signature = sha256(stringToSign, kSigning, 'hex')
    // console.log(signature)
    // console.log("----------------------------")

    // ************* 步骤 4：拼接 Authorization *************
    const authorization = algorithm + " " +
                    "Credential=" + SECRET_ID + "/" + credentialScope + ", " +
                    "SignedHeaders=" + signedHeaders + ", " +
                    "Signature=" + signature
    // console.log(authorization)
    // console.log("----------------------------")

    const Call_Information = 'curl -X POST ' + "https://" + endpoint
                            + ' -H "Authorization: ' + authorization + '"'
                            + ' -H "Content-Type: application/json; charset=utf-8"'
                            + ' -H "Host: ' + endpoint + '"'
                            + ' -H "X-TC-Action: ' + action + '"'
                            + ' -H "X-TC-Timestamp: ' + timestamp.toString() + '"'
                            + ' -H "X-TC-Version: ' + version + '"'
                            + ' -H "X-TC-Region: ' + region + '"'
                            + " -d '" + payload + "'"
    console.log(Call_Information)

    
}
main()

```

2. 根据签名信息，使用进行调用
```
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://soe.tencentcloudapi.com',
  'headers': {
    'Authorization': authorization,
    'Content-Type': 'application/json; charset=utf-8',
    'Host': 'soe.tencentcloudapi.com',
    'X-TC-Action': 'TransmitOralProcessWithInit',
    'X-TC-Timestamp': timestamp.toString(),
    'X-TC-Version': '2018-07-24',
    'X-TC-Region': 'ap-guangzhou'
  },
  body: payload
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

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


