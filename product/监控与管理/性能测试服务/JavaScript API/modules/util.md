
## Variables（变量）

[](id:default)
### Const default

default: { base64Decoding: *any*; base64Encoding: *any*; cloudAPISignatureV3: *any*; md5Sum: *any*; sloginEncrypt: *any*; toArrayBuffer: *any*; uuid: *any* }


#### Type declaration

- ##### base64Decoding:function

  - base64Decoding(input: *string*, encoding?: *"std"* | *"rawstd"* | *"url"* | *"rawurl"*, mode?: *"b"*): *string* | *ArrayBuffer*
 
  base64 解码。
   - StdEncoding 是标准的 base64 编码，如 RFC 4648 中所定义。
   - RawStdEncoding 是标准的原始、未填充的 base64 编码，如 RFC 4648 第 3.2 节中所定义。 这与 StdEncoding 相同，但省略了填充字符。
   - URLEncoding 是 RFC 4648 中定义的备用 base64 编码。它通常用于 URL 和文件名。
   - RawURLEncoding 是 RFC 4648 中定义的未填充的替代 base64 编码。它通常用于 URL 和文件名。 这与 URLEncoding 相同，但省略了填充字符。

  ```js
   import util from 'pts/util';
    
   export default function () {
    console.log(util.base64Decoding('SGVsbG8sIHdvcmxk')); // Hello, world
    }
    ```

  #### Parameters

  - ##### input: *string*
输入
    - ##### Optional encoding: *"std"* | *"rawstd"* | *"url"* | *"rawurl"*

      可选，默认 std。可选 std、rawstd、url、rawurl

    - ##### Optional mode: *"b"*
      可选，为 b 返回 ArrayBuffer 类型

#### Returns *string* | *ArrayBuffer*
解码结果

- ##### base64Encoding:function

  - base64Encoding(input: *string* | *ArrayBuffer*, encoding?: *"std"* | *"rawstd"* | *"url"* | *"rawurl"*): *string
  
   base64 编码。
   - StdEncoding 是标准的 base64 编码，如 RFC 4648 中所定义。
   - RawStdEncoding 是标准的原始、未填充的 base64 编码，如 RFC 4648 第 3.2 节中所定义。 这与 StdEncoding 相同，但省略了填充字符。
   - URLEncoding 是 RFC 4648 中定义的备用 base64 编码。它通常用于 URL 和文件名。
   - RawURLEncoding 是 RFC 4648 中定义的未填充的替代 base64 编码。它通常用于 URL 和文件名。 这与 URLEncoding 相同，但省略了填充字符。

   ```js
    import util from 'pts/util';
    
    export default function () {
        console.log(util.base64Encoding('Hello, world')); // SGVsbG8sIHdvcmxk
    }
    ```

  #### Parameters
 - ##### input: *string* | *ArrayBuffer*
      输入
    - ##### Optional encoding: *"std"* | *"rawstd"* | *"url"* | *"rawurl"*

      可选，默认 std。可选 std、rawstd、url、rawurl

#### Returns *string*
编码结果

- ##### cloudAPISignatureV3:function

  - cloudAPISignatureV3(param: *CloudAPISignatureV3Param*): *string*
    腾讯云 api 签名方法 v3。

    ```js
    import util from 'pts/util';
    import http from 'pts/http';
    
    export default function () {
        let timestamp = parseInt(new Date().getTime() / 1000);
        let body = {
            'EnvironmentId': 'wtp',
            'TopicName': 'access_server',
            'ClusterId': 'pulsar-vgb3w9ezndvx',
        }
        let headers = {
            'Content-Type': 'application/json',
            'Host': 'tdmq.tencentcloudapi.com',
            'X-TC-Action': 'DescribeSubscriptions',
            'X-TC-Version': '2020-02-17',
            'X-TC-Timestamp': timestamp.toString(),
            'X-TC-Region': 'ap-guangzhou',
        }
        headers['Authorization'] = util.cloudAPISignatureV3({
            secretID: 'xxx',
            secretKey: 'xxx',
            service: 'tdmq',
            method: 'POST',
            timestamp: timestamp,
            headers: headers,
            body: body,
        })
        let resp = http.post('https://tdmq.tencentcloudapi.com', body, {
            headers: headers,
        });
        console.log(resp.body);
    }
    ```

   #### Parameters

    - ##### param: *CloudAPISignatureV3Param*

      签名参数

    #### Returns *string*

    签名结果

- ##### md5Sum:function

  - md5Sum(data: *string* | *ArrayBuffer*): *string*

    md5 加密。

    ```js
    import util from 'pts/util';
    
    export default function () {
        console.log(util.md5Sum("12345")); // 827ccb0eea8a706c4c34a16891f84e7b
    }
    ```

    #### Parameters

    - ##### data: *string* | *ArrayBuffer*

      需要加密的数据

    #### Returns *string*

- ##### sloginEncrypt:function

  - sloginEncrypt(salt: *number*, pwd: *string*, vcode: *string*): *string*

    qq slogin 加密。

    ```js
    import util from 'pts/util';
    
    export default function () {
        console.log(util.sloginEncrypt(123456, "abcdef", "14")); 
        // lXYi46n51i4I2E6rFgaR75Lnp9kt4S4ZTq9ZTCxPv-Ce0jWsjCss2uCl9Hed163KGkCLUxFivS9BTGRyR7YuWrDa9*tGcqal6q3BW2jxPR2M3Si3Q2prGGIM5sIgwaaBeQWo1w-67Hgd-Qt*N4fszGRSS55VDl-b4THwmOAp6eKA*sG80HEzbLRUWmNnfmg8wdmtyxiZisYtyWI2HJozH1EKuN2u9byOvFnMdzCMlL7kPIZACk3zt84DM5byfCVpBII5N1EM6IMZ*u7A2WOd2c2RerWbVwAyu1raYoZwTODeOx18xw2uTnGi8aLJTz4PIG*3svujqwMayIgtzhq1IQ__
    }
    ```

  #### Parameters

    - ##### salt: *number*

      QQ号码字符串

    - ##### pwd: *string*

      用户的明文密码

    - ##### vcode: *string*

      appid，即aid字段的值

    #### Returns *string*

    加密后的密码

- ##### toArrayBuffer:function

  - toArrayBuffer(data: *string* | *ArrayBuffer*): *ArrayBuffer*


    尝试从兼容类型返回字节数组。
  ```js
    import util from 'pts/util';
    
    export default function () {
        console.log(util.toArrayBuffer("12345")); // [object ArrayBuffer]
    }
  ```

   #### Parameters

   - ##### data: *string* | *ArrayBuffer*

      数据

    #### Returns *ArrayBuffer*

- ##### uuid:function

  - uuid(): *string*

 uuid v4。

    ```js
    import util from 'pts/util';
    
    export default function () {
        console.log(util.uuid()) // 5fbf1e59-cabf-469b-9d9f-6622e97de1ec
    }
    ```

  #### Returns *string*

    uuid 字符串
