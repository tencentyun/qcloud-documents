## 临时密钥

临时密钥是通过 CAM 云 API 提供的接口，获取到权限受限的密钥。<br>
 COS API 可以使用临时密钥计算签名，用于发起 COS API 请求。<br>
 COS API 请求使用临时密钥计算签名时，需要用到获取临时密钥接口返回的信息中三个字段，分别如下：
- `tmpSecretId` 
- `tmpSecretKey` 
- `sessionToken` 

## 使用临时密钥的优势

Web、iOS、Android 使用 COS 的场景时，通过固定密钥计算签名方式不能有效地控制权限，同时把永久密钥放到客户端代码中有极大的泄露风险。如若通过临时密钥方式，则可以方便、有效地解决权限控制问题。
例如，在申请临时密钥过程中，可以通过设置权限策略 [policy](https://cloud.tencent.com/document/product/436/31923#policy) 字段，限制操作和资源，将权限限制在指定的范围内。

有关 COS API 授权策略，请查看：
- [COS API 临时密钥授权策略指引](https://cloud.tencent.com/document/product/436/31923)
- [常见场景的临时密钥权限策略示例](https://cloud.tencent.com/document/product/436/31923#.E5.B8.B8.E8.A7.81.E5.9C.BA.E6.99.AF.E6.8E.88.E6.9D.83.E7.AD.96.E7.95.A5)

## 获取临时密钥

获取临时密钥，可以通过提供的 [COS STS SDK](https://github.com/tencentyun/qcloud-cos-sts-sdk) 方式获取，也可以直接请求 STS 云 API 的方式获取。

### COS STS SDK 

COS 针对 STS 提供了 SDK 和样例，目前已有 Java、Nodejs、PHP、Python 等多种语言的样例。
具体内容请参考 [COS STS SDK](https://github.com/tencentyun/qcloud-cos-sts-sdk)。各个 SDK 的使用说明请参考 Github 上的 README 和 样例。

以 COS STS SDK 提供的 [Java SDK](https://github.com/tencentyun/qcloud-cos-sts-sdk/tree/master/java) 为例，获取临时密钥示例如下：

```java
import com.qcloud.Utilities.Json.JSONObject;

public class Demo {
    public static void main(String[] args) {
        TreeMap<String, Object> config = new TreeMap<String, Object>();

		try {
		    // 固定密钥
		    config.put("SecretId", "AKIDXXXXXXXXXXXXXXXXX");
		    // 固定密钥
		    config.put("SecretKey", "XXXXXXXXXXXXXXXXX");
		
		    // 临时密钥有效时长，单位是秒
		    config.put("durationSeconds", 1800);
		
		    // 换成您的 bucket
		    config.put("bucket", "examplebucket-appid");
		    // 换成 bucket 所在地区
		    config.put("region", "ap-guangzhou");
		
		    // 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的目录，例子：* 或者 a/* 或者 a.jpg
		    config.put("allowPrefix", "*");
		
		    // 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
		    String[] allowActions = new String[] {
		            // 简单上传
		            "name/cos:PutObject",
		            // 分片上传
		            "name/cos:InitiateMultipartUpload",
		            "name/cos:ListMultipartUploads",
		            "name/cos:ListParts",
		            "name/cos:UploadPart",
		            "name/cos:CompleteMultipartUpload"
		    };
		    config.put("allowActions", allowActions);
		
		    JSONObject credential = CosStsClient.getCredential(config);
		    System.out.println(credential);
		} catch (Exception e) {
		    throw new IllegalArgumentException("no valid secret !");
		}
    }
}
```

### 使用临时密钥访问 COS

 COS API 使用临时密钥访问 COS 服务时，通过 `x-cos-security-token` 字段来传递临时 `sessionToken` ；通过临时 `SecretId` 和 `SecretKey` 来计算签名。

以 COS Java SDK 为例，使用临时密钥访问 COS 示例如下：
> 单击 [此处](https://github.com/tencentyun/cos-java-sdk-v5) ，从 Github 下载 Java SDK 安装包。

```java
public class Demo {
    public static void main(String[] args) throws Exception {

        // 用户基本信息
        String tmpSecretId = "AKIDxxxxxx";
        String tmpSecretKey = "xxxxxx";
        String sessionToken = "xxxxxx";

        // 1 初始化用户身份信息(secretId, secretKey)
        COSCredentials cred = new BasicCOSCredentials(tmpSecretId, tmpSecretKey);
        // 2 设置 bucket 区域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
        ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
        // 3 生成cos客户端
        COSClient cosclient = new COSClient(cred, clientConfig);
        // bucket名需包含appid
        String bucketName = "mybucket-1251668577";

        String key = "aaa/bbb.txt";
        // 上传 object, 建议 20M 以下的文件使用该接口
        File localFile = new File("src/test/resources/test.txt");
        PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);

        // 设置 x-cos-security-token header 字段
        ObjectMetadata objectMetadata = new ObjectMetadata();
        objectMetadata.setSecurityToken(sessionToken);
        putObjectRequest.setMetadata(objectMetadata);

        try {
            PutObjectResult putObjectResult = cosclient.putObject(putObjectRequest);
            // putobjectResult会返回文件的etag
            String etag = putObjectResult.getETag();
        } catch (CosServiceException e) {
            e.printStackTrace();
        } catch (CosClientException e) {
            e.printStackTrace();
        }

        // 关闭客户端
        cosclient.shutdown();

    }
}
```

### STS 云 API 接口
#### 接口请求地址
```shell
https://sts.api.qcloud.com/v2/index.php
```
#### 接口请求方法
云 API 的参数支持 GET 参数和 POST 参数两种格式，以下介绍 GET 参数的格式。
#### 接口请求参数说明

>? 以下请求参数列表中，临时密钥接口特有的参数有：name、policy、durationSeconds 。其他字段则是云 API 的 [公共请求参数](https://cloud.tencent.com/document/api/213/6976)。

| 字段 |  描述  |是否必选 | 类型  |
| ------------ | ------------ | ------------ | ------------ |
| name | 联合身份用户昵称。<br>备注字段，可以填写用户 uin 作为身份备注。 | 是 | String |
| policy | 策略语法，是一个 json 字符串 url encode 结果，真正发送请求在 url 里会是如下文例子的两次 url encode 的字符串 | 是 | String |
| durationSeconds |  指定临时证书的有效期，单位：秒。<br>默认值为1800秒，最长有效期：2小时（7200 秒）。 | 否 | Int |
| Action | 云 API的 Action 参数。需要指定 GetFederationToken。 | 是 | String |
| Timestamp | 当前 UNIX 时间戳。 | 是 | Int |
| Nonce | 随机正整数。与 Timestamp 联合起来，用于防止重放攻击。 | 是 | Int |
| Region | 云 API 地域参数，可填写空字符串，默认就近地域。可填写的地域请参见 [公共请求参数](https://cloud.tencent.com/document/api/213/6976)。 | 是 | String |
| SecretId | 在云 API 密钥上申请的标识身份的 SecretId。一个 SecretId 对应唯一的 SecretKey，SecretKey 会用来生成请求签名 Signature。 | 是 | String |
| Signature | 请求签名。用来验证此次请求的合法性，需要用户根据实际的输入参数计算得出。<br>计算方法可参考 [签名方法](https://cloud.tencent.com/document/api/213/6984#.E7.94.9F.E6.88.90.E7.AD.BE.E5.90.8D.E4.B8.B2 "签名方法") 章节。|是 | String |

#### 返回结果说明

| 字段 | 类型  | 描述  |
| ------------ | ------------ | ------------ |
| expiredTime | Int | 临时密钥失效的时间戳。 |
| credentials | Object | 对象中包含 Token，tmpSecretId，tmpSecretKey 三元组。 |
| --tmpSecretId | String| tmpSecretId 计算签名时使用。 |
| --tmpSecretKey |String| tmpSecretKey 计算签名时使用。 |
| --sessionToken | String | sessionToken 请求鉴权时使用，COS 接口放在 Header 的 x-cos-security-token 字段里。 |

#### 访问请求示例

```shell
https://sts.api.qcloud.com/v2/index.php?
policy=%7B%0D%0A++%22version%22%3A+%222.0%22%2C%0D%0A++%22statement%22%3A+%5B%0D%0A++++%7B%0D%0A++++++%22action%22%3A+%5B%0D%0A++++++++%22name%2Fcos%3AHead*%22%2C%0D%0A++++++++%22name%2Fcos%3AGet*%22%2C%0D%0A++++++++%22name%2Fcos%3AList*%22%2C%0D%0A++++++++%22name%2Fcos%3AOptionsObject%22%0D%0A++++++%5D%2C%0D%0A++++++%22effect%22%3A+%22allow%22%2C%0D%0A++++++%22resource%22%3A+%5B%0D%0A++++++++%22*%22%0D%0A++++++%5D%0D%0A++++%7D%0D%0A++%5D%0D%0A%7D&name=brady&Action=GetFederationToken&SecretId=AKIDPiqmW3qcgXVSKN8jngPzRhvxzYyDL5qP&Nonce=665530507&Timestamp=1545889218&RequestClient=net-sdk-v5&durationSeconds=7200&Signature=S5LPn2GNbi1mLR3EnAcVAW3iYe8%3D
```

#### 成功返回内容示例

```shell
{
  "code": 0,
  "message": "",
  "codeDesc": "Success",
  "data": {
    "credentials": {
      "sessionToken":"xxxxxx",
      "tmpSecretId":"AKIDxxxxx",
      "tmpSecretKey":"xxxxx"
    },
    "expiredTime":1545896418
  }
}
```

## 错误排查

返回结果中的错误码表示了错误的主要原因。

- code 为公共错误码，其适用于所有模块的 API 接口。code 为0，表示调用成功，否则表示调用失败。若调用失败，用户可以根据公共错误码列表确定错误原因并采取相应措施。

- codeDesc 为模块错误代码，表示与模块相关的错误。若调用失败，用户可以根据模块错误码列表确定错误原因并采取相应措施。

具体的错误说明请参考 [错误码](https://cloud.tencent.com/document/product/598/13884)。
