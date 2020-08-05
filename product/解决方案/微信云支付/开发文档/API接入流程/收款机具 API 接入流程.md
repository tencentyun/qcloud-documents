## 1. 修订记录

| 版本号 | 变更内容 | 变更日期   | 
| ------ | -------- | ---------- |
| 1.0    | 创建文档 | 2019-10-06 | 

## 2. 概述
机具通过小程序绑定指定商户与门店后，便可收款。机具的绑定和收款功能的后台能力由云支付提供。本文档主要说明了机具厂商如何通过云支付提供的 API，完成云支付后台的接入。

## 3. 机具要求
显示器能清晰展示 URL 为200字节大小的二维码。

## 4. 关键名词说明
### 4.1 sn 前缀
为了确保每个厂商机具的 sn 在云支付系统中不冲突，云支付会给每个厂商分配不同的 sn 前缀。

假设厂商按自有规则生成的原始 sn 为 91RA00001，云支付给厂商分配的 sn 前缀为 BF_M100_BF，其中 BF 为厂商简码，M100为产品型号简码，则需要存在两套新的 sn。
- 第一套为 BF91RA00001，即在原始 sn 前增加 BF。
- 第二套（完整 sn）为 BF_M100_BF91RA00001，即在原始 sn 前增加 BF_M100_BF。

调用云支付后台所有接口都使用第二套 sn。其它情况，如机具外壳上贴的 sn 都使用第一套 sn。

### 4.2 初始密钥
厂商需要给每台机具生成一个初始密钥，密钥是由数字（0-9）和大写字母（A-Z）组成的32字节随机字符串，而且必须是一机一密，不能相同。

调用云支付后台绑定相关接口需要使用这个密钥，详见 [机具绑定相关流程说明](#7.-.E6.9C.BA.E5.85.B7.E7.BB.91.E5.AE.9A.E7.9B.B8.E5.85.B3.E6.B5.81.E7.A8.8B.E8.AF.B4.E6.98.8E)。

此密钥要求高度保密，建议写入机具的安全区，至少要加密后再烧录到磁盘。由于初始密钥由厂商生成，厂商需要尽力保证密钥不外泄。

### 4.3 交易密钥
机具绑定成功后，会从云支付后台接口中获取到一个交易密钥。调用云支付后台支付相关接口需要使用这个密钥，详见 [机具收款相关流程说明](#8.-.E6.9C.BA.E5.85.B7.E6.94.B6.E6.AC.BE.E7.9B.B8.E5.85.B3.E6.B5.81.E7.A8.8B.E8.AF.B4.E6.98.8E)。

此密钥要求高度保密，获取到交易密钥后，必须先加密再写入磁盘，以防攻击者获取到这个交易密钥。

## 5. 接入准备工作
### 5.1 申请初始资源
厂商在正式进入开发阶段时，需要向云支付以邮箱（邮箱地址请咨询负责与厂商对接的人员）的方式申请获取以下内容。

| 名称                       | 说明                                                         |
| -------------------------- | ------------------------------------------------------------ |
| sn 前缀                     | 参见 [4.1 sn 前缀](#4.1-sn-.E5.89.8D.E7.BC.80)。                                                |
| app_cpay_version           | 由云支付统一规划的机具程序版本号，绑定和数据上报时会用到。      |
| sub_terminal_type          | 由云支付统一规划的设备类型码，支付的时候会用到。                |
| 加密用的公钥文件 public.key | 由云支付统一发放的公钥文件，用于 sn 和初始密钥录入，[6.2 录入操作说明](#6.2-.E5.BD.95.E5.85.A5.E6.93.8D.E4.BD.9C.E8.AF.B4.E6.98.8E) 会用到。 |
| 接收加密文件的邮箱地址     | 云支付接收 sn 和初始密钥信息的邮箱地址。                     |

### 5.2 申请测试账号	
默认情况下，厂商直接参考接口说明，在正式环境上调试接口即可。如遇后台接口还未正式发布等特殊情况，需要在测试环境调试接口，则联系负责与厂商对接的人员。
1. **sn 和初始密钥。**sn 和初始密钥是绑定等流程中必须要的内容。如果在正式环境上调试，则需按第6章所述方法录入 sn 和初始密钥。
2. **测试商户。**如果是正式环境测试，则调试人员需要有微信商业版的商户，通过“收款设备”小程序来完成绑定。

## 6. 机具出厂准备工作
### 6.1 背景说明
每台机具的 sn 和初始密钥录入到云支付后台后才能绑定成功，然后才能用于收款，初始密钥说明详见 [4.2 初始密钥](#4.2-.E5.88.9D.E5.A7.8B.E5.AF.86.E9.92.A5)。

每批机具在出厂前，厂商需要把所有 sn 和初始密钥写入到一个文件中，并使用指定方法加密。通过厂商官方邮箱把加密文件发送给云支付指定邮箱，云支付收到邮件后会执行录入操作。录入完成后，云支付会回复邮件提示录入完成，厂商收到录入成功的邮件回复后，这批机具才能正式出厂。

厂商如果想调试绑定相关接口，需要先通这个方式把调试用到的 sn 和初始密钥录入云支付后台。

### 6.2 录入操作说明
1. **确认 openssl 版本**
要求版本为 OpenSSL 1.1.0g  2 Nov 2017 及以上，可以通过 openssl version 命令查看版本号。
2. **生成 sn 和初始密钥文件**
文件只包含两列，第一列为 sn（带完整前缀），第二列为初始密钥，中间以空格分隔，每行结尾不要有多余的空格或其它无关字符，中间不要有空行，最后一行不能为空行。生成的文件名为`sn_init_key.txt`，文件内容示例如下：
```
BF_M100_BF91RA00001 696FF05FA7CE76664211A47CD788CC30
BF_M100_BF91RA00002 654502BB0F57EC8737B4CF12117575B8
```
3. **生成密码文件**
随机生成一个32字节的密码字符串，并把这个密码字符串写入到一个名为`encrypt_key.txt`的文件。**此文件只有一行，不能有多余的空格或空行。每次都要随机生成，不能使用相同的密码字符串。**
4. **加密 sn 和初始密钥文件**
使用第3步生成的`encrypt_key.txt`文件来加密第2步生成的`sn_init_key.txt`文件。执行命令：
```
openssl aes-128-cbc -salt -in sn_init_key.txt -out sn_init_key.txt.encrypted
```
这里会要求输入两次密码，密码内容即为第3步生成文件中的内容，直接从文件中复制过来就行，两次密码输入必须相同。执行成功后会生成一个 sn 和初始化密钥的加密文件`sn_init_key.txt.encrypted`，即`sn_init_key.txt`加密后的文件。
5. **加密密码文件**
使用 [5.1 申请初始资源](#5.1-.E7.94.B3.E8.AF.B7.E5.88.9D.E5.A7.8B.E8.B5.84.E6.BA.90) 所述云支付提供的公钥文件`public.key`加密第三步生成的密码文件`encrypt_key.txt`。执行命令：
```
openssl rsautl -encrypt -inkey public.key -pubin -in encrypt_key.txt -out encrypt_key.txt.encrypted
```
执行成功后会生成一个密码文件的加密文件`encrypt_key.txt.encrypted`。
6. **邮件发送加密文件**
将加密文件发送到 [5.1 申请初始资源](#5.1-.E7.94.B3.E8.AF.B7.E5.88.9D.E5.A7.8B.E8.B5.84.E6.BA.90) 所述的接收加密文件的邮箱地址，需要发送的文件有`sn_init_key.txt.encrypted`和`encrypt_key.txt.encrypted`。如果要将文件打包进行发送，则必须使用 zip 来压缩。邮件发送时，抄送人需添加厂商相关管理人员。
7. **其它说明**
以上所有文件都以 UTF-8 无 BOM 编码，发送前请先确认不能有可见/不可见的特殊字符。邮件发送完成后，销毁`encrypt_key.txt`和`sn_init_key.txt`（无用时销毁）文件，同时需保管好`public.key`文件，这些文件禁止外泄。

## 7. 机具绑定相关流程说明
### 7.1 背景说明
商户拿到机具后，需要先操作绑定才能进行收款。机具绑定主要是为了获取支付接口必须的部分参数内容，并在云支付后台建立逻辑绑定关系，从而成功发起收款。

### 7.2 机具开机或重启
以下为机具开机或重启成功后需要增加的逻辑处理过程：
![](https://main.qcloudimg.com/raw/3b704d53f26a7cd80185dc4afd407b77.png)
开机或重启完成后，调用云支付后台 ping 接口获取系统时间，并用获取到的时间修正系统时间。
- 如果机具系统内的绑定信息为空（没有绑定或恢复了出厂设置），则提示用户去绑定。
- 如果机具系统内的绑定信息不为空，则通过云支付后`check_bill_device_bind_info`接口来校验绑定信息是否可用，如果接口返回失败，则展示接口返回的错误信息。`check_bill_device_bind_info`接口主要完成以下内容，这三件事如果检查通过，则可确保机具能正常收款。
 - 检查机具 sn 对应设备在云支付后台是否是“已绑定”状态；
 - 检查机具的在云支付后台的逻辑绑定关系是否正确；
 - 检查机具支付密钥是否和云支付后台保存的支付密钥一致。
- 显示屏展示对应提示后，用户可通过按键或其它方式关闭提示信息进行其它操作。

流程中涉及到的接口，详见 [接口说明](#9.-.E6.8E.A5.E5.8F.A3.E8.AF.B4.E6.98.8E)。

### 7.3 绑定
1. **时序图**
![](https://main.qcloudimg.com/raw/c3b003cb690e5e105a4d426aa6ae2b22.png)
机具增加“生成绑定二维码”的功能项，用户进入这个功能项后，执行时序图中的逻辑。
2. **获取绑定二维码信息**
机具首先从云支付后台同步一次系统时间。然后通过`generate_bill_device_bind_qr_code`获取绑定二维码相关信息。`generate_bill_device_bind_qr_code`接口成功应答后，可以取到5个绑定逻辑相关字段：activator、token、ttl、mini_program_url、interval，接口详细说明详见 [接口说明](#9.-.E6.8E.A5.E5.8F.A3.E8.AF.B4.E6.98.8E)。
3. **生成二维码**
二维码内容组成：`mini_program_url?ac=activator&rs=nonce_str&sign=sha256sum&sn=sn`
 - mini_program_url 和 activator 来源于`generate_bill_device_bind_qr_code`接口应答。
 - nonce_str 由机具生成的8字节随机字符串。
 - sign 由机具使用初始密钥和多个字段拼接字符串（拼接格式：ac=activator&rs=nonce_str&sn=sn）计算的 sha256 值，即：hmac_sha256（ac=activator&rs=nonce_str&sn=sn，机具初始密钥）。

 举例说明，假设：
 - mini_program_url 值为：`https://payapp.weixin.qq.com/smartqr/entry/home`。
 - activator 值为：`p9fa01zex4mi`。
 - 机具完整 sn 值为：`LANDI_QM600_LA190000000`。
 - 机具初始密钥值为：`C852274D372982D5530B692FD77124D3`。

 则二维码生成流程为：
 - 机具生成的8字节随机字符串（nonce_str）：`c44f32e0`。
 2. 机具拼接字符串 ac=p9fa01zex4mi&rs=c44f32e0&sn=LANDI_QM600_LA190000000。
 3. 机具计算 sha256：hmac-sha256(“ac=p9fa01zex4mi&rs=c44f32e0&sn=LANDI_QM600_LA190000000”, “C852274D372982D5530B692FD77124D3”) ，获得 HMAC-SHA256 结果：`E0CA8FDA56464BDF702FCA1AE9692EB99483E065879247763B3A46B576EBF5AC`。
 4. 拼接二维码 URL：`https://payapp.weixin.qq.com/smartqr/entry/home?ac=p9fa01zex4mi&rs=c44f32e0&sn=LANDI_QM600_LA190000000&sign=E0CA8FDA56464BDF702FCA1AE9692EB99483E065879247763B3A46B576EBF5AC`，机具显示器把拼接二维码 URL 展示成二维码。
4. **轮询绑定结果**
机具展示出绑定二维码后，立即开始定时轮询云支付后台绑定结果。
 - 轮询接口：`get_bill_device_bind_info`，详见 [接口说明](#9.-.E6.8E.A5.E5.8F.A3.E8.AF.B4.E6.98.8E)。
 - 轮询时间间隔：由`generate_bill_device_bind_qr_code`接口返回的 interval 指定，单位为秒。假设 interval 为1，则机具每次调用`get_bill_device_bind_info`接口完成后等待1秒再继续调用。
 - 轮询结束条件有两个：
    - `get_bill_device_bind_info`接口返回了绑定信息，即应答中 activated 为 true；
    2. 轮询超过了二维码有效期，有效期长度由`generate_bill_device_bind_qr_code`接口应答中的 ttl 指定，单位为秒，假如 ttl 为180，表示整个轮询过程超过180秒就必须结束，并停止展示二维码。
5. **处理绑定信息**
获取到绑定信息后（即 activated 为 true），把应答中的 e_authen_key 内容先做 base64 解码，再执行解密（解密说明详见 [10.1 AES-128-CBC 解密说明](#10.1-aes-128-cbc-.E8.A7.A3.E5.AF.86.E8.AF.B4.E6.98.8E)），解密密钥为机具初始密钥。解密成功后，把解密后的内容和其它绑定信息使用机具自有加密方式加密一次，最后写入磁盘。

## 8. 机具收款相关流程说明
### 8.1 支付
![](https://main.qcloudimg.com/raw/ad059b755101589a7d3b9920879bd45c.png)
刷卡支付接口：`https://pay.qcloud.com/cpay/brief_micro_pay`，详见 [9.6 刷卡支付](#9.6-.E5.88.B7.E5.8D.A1.E6.94.AF.E4.BB.98)。
查询订单接口：`https://pay.qcloud.com/cpay/brief_query_order`，详见 [9.7 查询支付单](#9.7-.E6.9F.A5.E8.AF.A2.E6.94.AF.E4.BB.98.E5.8D.95)。
- 支付方式：微信支付、支付宝支付（配置方法详见 [支付宝子商户配置](https://cloud.tencent.com/document/product/569/35716)）、会员卡支付，云支付后台通过顾客付款码区分顾客的支付方式。
- 支付未知：网络请求超时和业务上的结果未知，详见 [9.11 其它消息体说明](#9.11-.E5.85.B6.E5.AE.83.E6.B6.88.E6.81.AF.E4.BD.93.E8.AF.B4.E6.98.8E) 中 Status 的说明。
- 接口返回 status 为0，只表示业务请求成功。订单的支付结果需通过订单的状态（即应答中的 cts 字段）来判断。
- 每次接口调用成功后等待2秒再查单，如果2分钟内查询不到结果，请到手机端管理系统查看交易明细确认支付结果。
- 支付流程完成后需要上报支付相关信息，详见 [9.10 支付信息上报](#9.10-.E6.94.AF.E4.BB.98.E4.BF.A1.E6.81.AF.E4.B8.8A.E6.8A.A5)。

### 8.2 退款
![](https://main.qcloudimg.com/raw/aa39c34df6f88665fb83f00a3517242e.png)
退款接口：`https://pay.qcloud.com/cpay/refund`，详见 [9.8 退款](#9.8-.E9.80.80.E6.AC.BE)。
查询退款订单接口：`https://pay.qcloud.com/cpay/query_refund_order`，详见 [9.9 查询退款单](#9.9-.E6.9F.A5.E8.AF.A2.E9.80.80.E6.AC.BE.E5.8D.95)。
- 申请退款成功，并不代表退款成功。
- 退款是一个异步过程，申请退款成功后，只是代表第三方支付平台受理这笔退款，是否到账需要看这笔钱退到哪里。
 - 如果是退款至微信零钱账户或支付宝账户，会很快到账。
 - 如果是退款至顾客的银行卡，到账时间与银行处理进度相关，可能要花几个小时。
- 申请退款成功后，需告知顾客，申请退款已经成功，请关注后续到账情况。顾客可关注微信或支付宝消息通知，收到已经发起退款或退款到账的消息。
- 如果想在设备上看这笔退款是否到账，可以调用退款查询接口，通过退款单的状态来查看是否退款成功。适配者可以自己选择是否适配退款查询接口。

### 8.3 机具支付使用 HTTPS 长连接
1. **背景**
机具与云支付后台使用 HTTPS 方式交互，如果机具收款时每次都新建连接请求云支付后台，则完成 TCP 握手和 TLS 握手需要很多次网络报文交互，会增加支付相关接口调用的整体耗时，影响收款体验。因此机具需要与云支付后台保持一个 HTTPS 长连接，使用长连接完成支付相关接口调用。
2. **创建连接**
 - 如果机具已绑定，机具启动完成后立即尝试创建与云支付后台的 HTTPS 连接，并保持这个连接，供后续支付使用。如果创建连接过程超时，则跳过此步骤，让机具完成启动。
 - 如果机具未绑定，待机具绑定成功后，立即尝试创建与云支付后台的 HTTPS 连接，并保持这个连接，供后续支付使用。
3. **保持连接**
每个 HTTPS 请求头设置`connection: keep-alive`。每隔2分钟，进行一次真实的 HTTPS 交互，发送请求：`GET / HTTP/1.1\r\nHost: pay.qcloud.com\r\nConnection: keep-alive\r\n\r\n`，接收完服务器应答后丢掉不处理。
4. **预热连接**
商家输入完金额并按下确定键之后，每隔0.5秒通过长连接以 GET 方式向后台发送'\r\n' 2个字符，扫码后停止发送，走正常支付流程。GET 请求不会触发后台返回应答。伪代码详细说明如下：
```
function uplink_warm_up() {
      while true {
         if qrcode_is_ready {
            return
         }
         t = now_time()
 
         https_send('\r\n', 2)
         wait_ack() // 不同机具可能做法不同
         while now_time() - t < 500ms {
            sleep(50ms)
         }
      }
}
```

## 9. 接口说明
### 9.1 接口规范

| 摘要     | 详细说明                                                     |
| -------- | ------------------------------------------------------------ |
| 传输方式 | HTTPS                                       |
| 提交方式 | POST                                                         |
| 字符编码 | UTF-8                                                     |
| 内容格式 | content_type：application/json                             |
| 证书校验 | 严格校验服务端证书。                                           |
| 应答校验 | 如果应答设置了 authen_info（或 a）则严格校验 authen_code（或 a）的值。 |

 
### 9.2 获取云支付后台系统时间
#### 接口地址
`https://pay.qcloud.com/cpay/ping`

#### 请求参数
POST 空字符串即可，后台不校验 POST 内容。

#### 应答参数

| 参数名      | 必填 | 类型   | 长度(Byte) | 说明                                           |
| ----------- | ---- | ------ | ---------- | ---------------------------------------------- |
| timestamp   | 是   | Int    | 8          | 后台系统的 UNIX 时间戳，单位为秒，如1568810504。 |
| status      | 是   | Int    | 4          | 错误码。                                         |
| description | 是   | String | 最长128    | status 对应的错误信息。                           |

#### 示例说明
```
curl -H "Content-Type:application/json" -X POST -data '' <https://pay.qcloud.com/cpay/ping>

{"description":"ok","status":0,"timestamp":1568810077}
```

### 9.3 检查机具绑定信息
#### 接口地址
`https://pay.qcloud.com/cpay/check_bill_device_bind_info`

#### 请求参数

| 参数名          | 必填 | 类型       | 长度 | 说明                                                         |
| --------------- | ---- | ---------- | ---- | ------------------------------------------------------------ |
| request_content | 是   | String     |   -   | 请求内容，该 string 可以转为 json 结构，json 格式见本节 RequestContent。 |
| authen_info     | 是   | AuthenInfo |   -   | 认证信息，详见“初始密钥认证信息”。                             |

**RequestContent 结构**

| 参数名       | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ------------ | ---- | ------ | ---------- | ------------------------------------------------------------ |
| sn_code           | 是   | String |      -      | 机具自身的 sn，注意要是完整的 sn，如`LANDI_QM800_LA19**********`，`POPSECU_SL51_BP51********`。 |
| out_shop_id  | 是   | String |     -       | 云支付系统内的全局门店 ID，机具绑定成功后即可获得这个 ID。       |
| device_id    | 是   | String |       -     | 云支付系统内的逻辑设备 ID，机具绑定成功后即可获得这个 ID。       |
| nonce_str    | 是   | String | 8          | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。                         |
| hash_content | 是   | String | 64         | authen_key（支付密钥）和随机字符串一起计算的 HAMC-SHA256 的值，authen_key 是在机具绑定成功后解密 e_authen_key 字段获得。 |
| timestamp    | 是   | Int    | 8          | 机具系统当前时间，UNIX 时间戳，单位为秒，如1568810504。      |

#### 应答参数

| 参数名           | 必填 | 类型            | 长度(Byte) | 说明                                 |
| ---------------- | ---- | --------------- | ---------- | ------------------------------------ |
| response_content | 是   | ResponseContent |      -      | 应答内容，详见本节 ResponseContent。     |
| authen_info      | 否   | AuthenInfo      |     -       | 认证信息，详见“初始密钥认证信息”。 |

**ResponseContent 结构**

| 参数名          | 必填 | 类型   | 长度(Byte) | 说明                                |
| --------------- | ---- | ------ | ---------- | ----------------------------------- |
| status          | 是   | Int    | 4          | 错误码。                              |
| description     | 是   | String | 最长128    | 错误信息。                            |
| log_id          | 是   | Int    | 4          | 消息 ID。                              |
| internal_status | 是   | Int    | 4          | 具体说明见 internal_status 错误码表。 |

#### 示例说明
**请求生成示例代码：**
```
std::string nonce_str = "ea90ceba"	// 生成8字节随机字符串
std::string authen_key_hash = hmac_sha256(authen_key, nonce_str); // 计算 authen_key 的 hash 值

Json::Value request_content;
request_content["sn_code"] = "aaa";
request_content["out_shop_id"] = "ddd";
request_content["device_id"] = "fff";
request_content["nonce_str"] = nonce_str;
request_content["hash_content"] = authen_key_hash;
request_content["timestamp"] = 1568859333;	//当前系统时间

Json::FastWriter w;
std::string request_content_str = w.write(request_content);
std::string authen_code = hmac_sha256(init_key, request_content_str); // 使用机具初始密钥计算签名

Json::Value authen;
authen["authen_code"] = authen_code
authen["authen_type"] = 1; //hmac_sha256 为 1

Json::Value authen_info;
authen_info["a"] = authen; //认证码

Json::Value request; //构造最终发给服务器的请求
request["request_content"] = request_content_str;
request["authen_info"] = authen_info;

std::string request_str = w.write(request);
```
request_str 即为 post 内容。

**请求内容示例：**
```
{
	"authen_info":{
		"a":{
			"authen_code":"091745D976208923097F66771324CA7C6EC32A55ABECAD6C3D42826AA363CA86",
			"authen_type":1
		}
	},
	"request_content":"{
		"device_id":"fff",
		"hash_content":"2F09EFCB064D4F9A4A0BABD5260842D8AC4D0611F4B941A03A77E5E55B5168D7",
		"nonce_str":"ea90ceba",
		"out_shop_id":"ddd",
		"sn_code":"aaa",
		"timestamp":1568859333
	}"
}
```
**应答内容示例：**
```
{
	"response_content":"{
	"status":0,
	"description":"",
	"log_id":18654852,
	"internal_status":0,
	}",
	"authen_info":{
		"a":{
			"authen_type":1,
			"authen_code":"xxxx"
		}
	}
}
```

### 9.4. 获取绑定二维码相关信息
#### 接口地址
`https://pay.qcloud.com/cpay/generate_bill_device_bind_qr_code`

#### 请求参数

| 参数名          | 必填 | 类型       | 长度 | 说明                                                         |
| --------------- | ---- | ---------- | ---- | ------------------------------------------------------------ |
| request_content | 是   | String     |  - | 请求内容，该 string 可以转为 json 结构，json 格式见本节 RequestContent。 |
| authen_info     | 是   | AuthenInfo |   -   | 认证信息，详见“初始密钥认证信息”。                             |

**RequestContent 结构**

| 参数名           | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ---------------- | ---- | ------ | ---------- | ------------------------------------------------------------ |
| sn_code               | 是   | String |      -      | 机具自身的 sn，注意要是完整的 sn，如`LANDI_QM800_LA19**********`，`POPSECU_SL51_BP51********`。 |
| mcc              | 否   | String |      -      | 基站信息中的 mcc 字段，如果未获取到可以不填。                    |
| mnc              | 否   | String |      -      | 基站信息中的 mnc 字段，如果未获取到可以不填。                    |
| lac              | 否   | String |       -     | 基站信息中的 lac 字段，如果未获取到可以不填。                    |
| cellid           | 否   | String |     -       | 基站信息中的 cellid 字段，如果未获取到可以不填。                 |
| rss              | 否   | String |     -       | 基站信息中的 rss 字段，如果未获取到可以不填。                    |
| app_cpay_version | 是   | String |     -       | 由云支付指定的版本号，初始值为1.0.0，需要编译到机具代码中，每次机具升级程序需要向云支付申请一个 app_cpay_version。 |
| nonce_str        | 是   | String | 8          | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。                        |
| timestamp        | 是   | Int    | 8          | 机具系统当前时间，UNIX 时间戳，单位为秒，如1568810504。       |

#### 应答参数

| 参数名           | 必填 | 类型            | 长度(Byte) | 说明                             |
| ---------------- | ---- | --------------- | ---------- | -------------------------------- |
| response_content | 是   | ResponseContent |       -    | 应答内容，详见本节 ResponseContent。 |
| authen_info      | 否   | AuthenInfo      |       -     | 认证信息，详见“初始密钥认证信息”。 |

**ResponseContent 结构**

| 参数名                                     | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ------------------------------------------ | ---- | ------ | ---------- | ------------------------------------------------------------ |
| status                                     | 是   | Int    | 4          | 错误码。                                                       |
| description                                | 是   | String | 最长128    | 错误信息。                                                     |
| log_id                                     | 是   | Int    | 4          | 消息 ID。                                                       |
| internal_status                            | 是   | Int    | 4          | 具体说明见 internal_status 错误码表。                          |
| generate_bill_device_bind_qr_code_response | 否   | String |      -      | 只有 status 为0的时候才存在，具体见 GenerateBillDeviceBindQrCodeResponse 说明。 |

**GenerateBillDeviceBindQrCodeResponse**

| 参数名           | 必填 | 类型   | 长度(Byte) | 说明                                                   |
| ---------------- | ---- | ------ | ---------- | ------------------------------------------------------ |
| activator        | 是   | String | 12         | 二维码唯一标识，用于生成绑定二维码。                     |
| token            | 是   | String | 12         | 轮询绑定结果时要用到的票据。                             |
| ttl              | 是   | Int    | 4          | 二维码有效时间，单位为秒，如180，表示二维码3分钟内有效。 |
| mini_program_url | 是   | Int    | 4          | 收款设备小程序的 url，用于生成绑定二维码。                |
| interval         | 是   | Int    | 4          | 轮询绑定结果的时间间隔，单位为秒。                       |

#### 示例说明
**请求生成示例代码：**
```
Json::Value request_content;
request_content["sn_code"] = "aaa";
request_content["mcc"] = "bbb";
request_content["mnc"] = "ccc";
request_content["lac"] = "ddd";
request_content["cellid"] = "eee";
request_content["rss"] = "fff";
request_content["app_cpay_version"] = "1.0.0";
request_content["nonce_str"] = "ea90ceba";	// 8字节随机字符串
request_content["timestamp"] = 1568859333;	// 当前系统时间

Json::FastWriter w;
std::string request_content_str = w.write(request_content);
std::string authen_code = hmac_sha256(init_key, request_content_str); // 使用机具初始密钥计算签名

Json::Value authen;
authen["authen_code"] = authen_code;
authen["authen_type"] = 1; //hmac_sha256 为 1

Json::Value authen_info;
authen_info["a"] = authen; //认证码，签名是 s

Json::Value request; //构造最终发给服务器的请求
request["request_content"] = request_content_str;
request["authen_info"] = authen_info;

std::string request_str = w.write(request);
```
request_str 即为 post 内容。

**请求内容示例：**
```
{
	"authen_info":{
		"a":{
			"authen_code":"E84DCFDF546D0A0F91FFB90746F6FC7E9A8FCF62C4E682FE769BFB64486F72E5",
			"authen_type":1
		}
	},
	"request_content":"{
		"app_cpay_version":"1.0.0",
		"cellid":"eee",
		"lac":"ddd",
		"mcc":"bbb",
		"mnc":"ccc",
		"nonce_str":"ea90ceba",
		"rss":"fff",
		"sn_code":"aaa",
		"timestamp":1568859333
	}"
}
```
**应答内容示例：**
```
{
	"response_content":"{
		"status":0,
		"description":"",
		"log_id":18654852,
		"internal_status":0,
		"generate_bill_device_bind_qr_code":"{
			"activator":"p9fa01zex4mi",
			"token":"8azip8115bq",
			"ttl":180,
			"mini_program_url":"https://payapp.weixin.qq.com/smartqr/entry/home",
			"interval":1
		}"
	}",
	"authen_info":{
		"a":{
			"authen_type":1,
			"authen_code":"xxxx"
		}
	}
}
```

### 9.5 获取绑定信息
#### 接口地址
`https://pay.qcloud.com/cpay/get_bill_device_bind_info`

#### 请求参数

| 参数名          | 必填 | 类型       | 长度 | 说明                                                         |
| --------------- | ---- | ---------- | ---- | ------------------------------------------------------------ |
| request_content | 是   | String     |  -    | 请求内容，该 string 可以转为 json 结构，json 格式见本节 RequestContent。 |
| authen_info     | 是   | AuthenInfo |  -    | 认证信息，详见“初始密钥认证信息”。                             |

**RequestContent 结构**

| 参数名    | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| --------- | ---- | ------ | ---------- | ------------------------------------------------------------ |
| sn_code        | 是   | String |      -      | 机具自身的 sn，注意要是完整的 sn，如`LANDI_QM800_LA19**********`，`POPSECU_SL51_BP51********`。 |
| token     | 是   | String | 12         | generate_bill_device_bind_qr_code 接口应答中的 token。           |
| nonce_str | 是   | String | 8          | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。                         |
| timestamp | 是   | Int    | 8          | 机具系统当前时间，UNIX 时间戳，单位为秒，如1568810504。       |

#### 应答参数

| 参数名           | 必填 | 类型            | 长度(Byte) | 说明                             |
| ---------------- | ---- | --------------- | ---------- | -------------------------------- |
| response_content | 是   | ResponseContent |       -     | 应答内容，详见本节 ResponseContent。 |
| authen_info      | 否   | AuthenInfo      |      -      | 认证信息，详见“初始密钥认证信息”。 |

**ResponseContent 结构**

| 参数名                             | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ---------------------------------- | ---- | ------ | ---------- | ------------------------------------------------------------ |
| status                             | 是   | Int    | 4          | 错误码。                                                       |
| description                        | 是   | String | 最长128    | 错误信息。                                                     |
| log_id                             | 是   | Int    | 4          | 消息 ID。                                                       |
| internal_status                    | 是   | Int    | 4          | 具体说明见 internal_status 错误码表。                          |
| get_bill_device_bind_info_response | 否   | String |       -     | 只有 status 为0的时候才存在，具体见 GetBillDeviceBindInfoResponse 说明。 |

**GetBillDeviceBindInfoResponse**

| 参数名            | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ----------------- | ---- | ------ | ---------- | ------------------------------------------------------------ |
| activated         | 是   | Int    | 4          | 后台是否绑定完成，0-未完成，1-已完成。                         |
| out_mch_id        | 否   | String | 最长64     | 云支付内部的服务商 ID，只当 activated 为1时才有。              |
| out_sub_mch_id    | 否   | String | 最长64     | 云支付内部的子商户 ID，只当 activated 为1时才有。              |
| cloud_cashier_id  | 否   | String | 最长64     | 云支付规定的定单前缀，只当 activated 为1时才有。               |
| authen_type       | 否   | Int    | 4          | 子商户与云支付之间的签名算法类型，只当 activated 为1时才有。   |
| e_authen_key      | 否   | String | 最长256    | Aes128CBC 加密并 base64 编码之后的支付密钥，机具先 base64 解码后，再使用初始化密钥来解密这个字段，以获得支付密钥（authen_key）。支付用这个密钥来计算签名。只当 activated 为1时才有。 |
| out_shop_id       | 否   | String | 最长64     | 云支付系统全局唯一门店 ID，只当 activated 为1时才有。          |
| shop_name         | 否   | String | 最长128    | 门店名称，只当 activated 为1时才有。                           |
| device_id         | 否   | String | 最长64     | 设备 ID，只当 activated 为1时才有。                            |
| device_name       | 否   | String | 最长256    | 设备名称，只当 activated 为1时才有。                           |
| staff_id          | 否   | String | 最长64     | 店员 ID，保留字段，暂未使用。                                     |
| staff_name        | 否   | String | 最长256    | 店员名称，保留字段，暂未使用。                                   |
| device_shift_type | 否   | Int    | 4          | 设备类型，只当 activated 为1时才有。                           |
| nonce_str         | 是   | String | 32         | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。                         |

#### 示例说明

**请求生成示例代码：**

```
Json::Value request_content;
request_content["sn_code"] = "aaa";
request_content["token"] = "8azip8115bq";
request_content["nonce_str"] = "ea90ceba";	// 8字节随机字符串
request_content["timestamp"] = 1568859333;	// 当前系统时间

Json::FastWriter w;
std::string request_content_str = w.write(request_content);
std::string authen_code = hmac_sha256(init_key, request_content_str); // 使用机具初始密钥计算签名

Json::Value authen;
authen["authen_code"] = authen_code
authen["authen_type"] = 1; //hmac_sha256 为 1

Json::Value authen_info;
authen_info["a"] = authen; //认证码，签名是 s

Json::Value request; //构造最终发给服务器的请求
request["request_content"] = request_content_str;
request["authen_info"] = authen_info;

std::string request_str = w.write(request);
```
request_str 即为 post 内容。

**请求内容示例：**

```
{
	"authen_info":"{
		"a":{
			"authen_code":"09E33D5E1D208569EE634C733F0B1FD933DD690B25F5BF72B386257B7A2113B0",
			"authen_type":1
		}
	},"
	request_content":"{
		"nonce_str":"ea90ceba",
		"sn_code":"aaa",
		"timestamp":1568859333,
		"token":"8azip8115bq"
	}"
}
```
**应答内容示例：**

```
{
	"response_content":"{
		"status":0,
		"description":"",
		"log_id":18654852,
		"internal_status":0,
		"bill_device_bind_sn" : "{
			"activated":1,
			"out_mch_id":"aaa",
			"out_sub_mch_id":"bbb",
			"cloud_cashier_id":"ccc",
			"authen_type":1,
			"authen_key":"ddd",
			"out_shop_id":"eee",
			"shop_name":"fff",
			"device_id":"ggg",
			"device_name":"hhh",
			"device_shift_type":1,
			"nonce_str":"416492026bc84091bcaf7e74ea90ceba"
		}"
	}",
	"authen_info":{
		"a":{
			"authen_type":1,
			"authen_code":"xxxx"
		}
	}
}
```

### 9.6 刷卡支付

#### 接口地址

`https://pay.qcloud.com/cpay/brief_micro_pay`

#### 请求参数

| 参数名 | 必填 | 类型           | 长度 | 说明                                                 |
| ------ | ---- | -------------- | ---- | ---------------------------------------------------- |
| r      | 是   | RequestContent |  -    | 请求内容，详见本节 RequestContent。                     |
| a      | 是   | string         |    -  | 使用支付密钥计算的认证码，目前只支持 sha256 计算认证码。 |

**RequestContent 结构**

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ------ | ---- | ------ | ---------- | ------------------------------------------------------------ |
| sc     | 是   | String |     -       | 机具的 sn，注意要是完整的 sn，如：`LANDI_QM800_LA19**********`，`POPSECU_SL51_BP51********`。 |
| osi    | 是   | String |       -     | 云支付分配的门店全局 ID，由绑定成功时获取。                      |
| ns     | 是   | String | 32         | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。                     |
| otn    | 是   | String |     -       | 由调用方生成的订单号，前缀必须是绑定成功时获取的云支付订单前缀。 |
| ac     | 是   | String |    -        | author_code，刷卡支付时顾客的付款码。云支付后台通过这个字段来区分是微信支付，或支付宝支付还是会员卡支付。 |
| tf     | 是   | Int    | 8          | 即 total_fee，订单总金额，单位分。                              |
| bd     | 是   | String |    -        | 即 body，商品或订单简要描述。                                   |
| di     | 是   | String |     -       | 即 device_id，设备编号，由绑定成功时获取。                       |
| stt    | 是   | Int    |      -    | 即 sub_terminal_type，子终端类型，代表一个机具品牌，由云支付分配，详见 [5.1 申请初始资源](#5.1-.E7.94.B3.E8.AF.B7.E5.88.9D.E5.A7.8B.E8.B5.84.E6.BA.90)。 |

#### 应答参数

| 参数名 | 必填 | 类型            | 长度(Byte) | 说明                               |
| ------ | ---- | --------------- | ---------- | ---------------------------------- |
| rc     | 是   | ResponseContent |     -       | 请求内容，详见本节 ResponseContent。  |
| a      | 是   | String          | 32         | 认证码，目前只支持 sha256 计算认证码。 |

**ResponseContent 结构**

| 参数名          | 必填 | 类型                  | 长度(Byte) | 说明                                |
| --------------- | ---- | --------------------- | ---------- | ----------------------------------- |
| s               | 是   | Int                   | 4          | 错误码。                              |
| d               | 是   | String                | 最长128    | 即 description，错误信息。              |
| li              | 否   | Int                   | 4          | 即 log_id，消息 ID。                     |
| is              | 是   | Int                   | 4          | 具体说明见 internal_status 错误码表。 |
| brief_micro_pay | 否   | BriefMicroPayResponse |     -       | 详见本节 BriefMicroPayResponse。       |

**BriefMicroPayResponse**

| 参数名 | 必填 | 类型                       | 长度(Byte) | 说明                           |
| ------ | ---- | -------------------------- | ---------- | ------------------------------ |
| wx     | 否   | BriefWxpayOrderContentExt  |        -    | 详见 BriefWxpayOrderContentExt。  |
| ali    | 否   | BriefAlipayOrderContentExt |       -     | 详见 BriefAlipayOrderContentExt。 |
| cd     | 否   | BriefCardOrderContentExt   |      -      | 详见 BriefCardOrderContentExt。   |
| ns     | 是   | String                     | 8          | 8字节随机字符串。                |

#### 示例说明
**请求生成示例代码：**
```
Json::Value request_content;
request_content["ns"] = generate_random_nonce_str();
request_content["osi"] = out_shop_id;
request_content["otn"] = out_trade_no;
request_content["ac"] = author_code;
request_content["tf"] = total_fee;
request_content["bd"] = body;
request_content["di"] = device_id;
request_content["sc"] = sn_code;
request_content["stt"] = sub_terminal_type;
Json::FastWriter w;
const std::string &rc = w.write(request_content);
std::string authen_code = hmac_sha256(authen_key, rc); // 计算签名
Json::Value request;
request["r"] = rc;
request["a"] = authen_code;
return w.write(request);
```
**请求内容示例：**
```
{
	"r":"{
		"ns":"69050786d195198efe9070ae45857070",
		"osi":"sz01QgJZkxDB7RVeL6XY",
		"otn":"0100826651692015704554111",
		"ac":"135005875955002257",
		"tf":900,
		"bd":"支付简述",
		"di":"tdFQtGl2M9MOcgTn",
		"sc":"LANDI_QM800_LA198KBQ8W1666",
		"stt":2451
	}",
	"a":"A4BCE4DF5C59C1D1532FA38D5C0298E46F224D02D38EFA6A766A5368271413B1"
}
```
**应答内容示例：**
```
{
	"rc":"{
		"s":0,
		"d":"xxx",
		"li":2643575008,
		"is":0,
		"brief_micro_pay":{
			"wx":{
				"cts":2
			},
			"ns":"dJMSHgYs"
		}
	}",
	"a":"4E80102BC41267241DE4B55AC40A5B2952C2F739E384767DDD065B8E1189846A"
}
```

### 9.7 查询支付单
#### 接口地址
`https://pay.qcloud.com/cpay/brief_query_order`

#### 请求参数

| 参数名 | 必填 | 类型           | 长度 | 说明                                                      |
| ------ | ---- | -------------- | ---- | --------------------------------------------------------- |
| r      | 是   | RequestContent |  -    | 请求内容，详见本节 RequestContent。                          |
| a      | 是   | string         |   -   | 使用支付密钥计算的认证码，目前只支持 hmac-sha256 计算认证码。 |

**RequestContent 结构**

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                                    |
| ------ | ---- | ------ | ---------- | --------------------------------------- |
| osi    | 是   | String |       -     | 云支付分配的门店全局 ID，由绑定成功时获取。 |
| ns     | 是   | String | 32         | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。   |
| otn    | 是   | String |        -    | 由调用方生成的支付订单号。                |

#### 应答参数

| 参数名 | 必填 | 类型            | 长度(Byte) | 说明                                                      |
| ------ | ---- | --------------- | ---------- | --------------------------------------------------------- |
| rc     | 是   | ResponseContent |    -        | 请求内容，详见本节 ResponseContent。                         |
| a      | 是   | String          | 32         | 使用支付密钥计算的认证码，目前只支持 hmac-sha256 计算认证码。 |

**ResponseContent 结构**

| 参数名            | 必填 | 类型                    | 长度(Byte) | 说明                                |
| ----------------- | ---- | ----------------------- | ---------- | ----------------------------------- |
| s                 | 是   | Int                     | 4          | 错误码。                              |
| d                 | 是   | String                  | 最长128    | 即 description，错误信息。              |
| li                | 否   | Int                     | 4          | 即 log_id，消息 ID。                     |
| is                | 是   | Int                     | 4          | 具体说明见 internal_status 错误码表。 |
| brief_query_order | 否   | BriefQueryOrderResponse |    -        | 详见本节 BriefQueryOrderResponse。     |

**BriefQueryOrderResponse**

| 参数名 | 必填 | 类型                       | 长度(Byte) | 说明                              |
| ------ | ---- | -------------------------- | ---------- | --------------------------------- |
| pp     | 是   | Int                        | 4          | 第三方支付平台，详细见 PayPlatform。 |
| otn    | 是   | String                     |    -        | 由支付调用户生成的订单号。          |
| tf     | 是   | Int                        | 8          | 订单总金额，单位为分。               |
| wx     | 否   | BriefWxpayOrderContentExt  |         -   | 详见 BriefWxpayOrderContentExt。     |
| ali    | 否   | BriefAlipayOrderContentExt |      -      | 详见 BriefAlipayOrderContentExt。    |
| cd     | 否   | BriefCardOrderContentExt   |      -      | 详见 BriefCardOrderContentExt。      |
| ns     | 是   | String                     | 8          | 8字节随机字符串。                   |

#### 示例说明
**请求生成示例代码：**
```
Json::Value request_content;
request_content["ns"] = generate_random_nonce_str();
request_content["osi"] = out_shop_id;
request_content["di"] = device_id;
request_content["sc"] = sn_code;
request_content["otn"] = out_trade_no;

Json::FastWriter w;
const std::string &rc = w.write(request_content);

std::string authen_code = hmac_sha256(authen_key, rc); // 计算签名

Json::Value request;
request["r"] = rc;
request["a"] = authen_code;
return w.write(request);
```
**请求内容示例：**
```
{
	"r":"{
		"ns":"92f7ba8154a4532d97cb6f2b181309e9",
		"otn":"013907131297815704553502",
		"osi":"sz015Xco0HsfMcFGkeB9"
	}",
	"a":"D9C1233C5D08288A00975F61DF328E7E76F426C3519284A1F43245703F7CFCFE"
}
```
**应答内容示例：**
```
{
	"rc":"{
		"s":0,
		"d":"u64CDu4F5Cu6210u529Fu3002",
		"li":2185455507,
		"is":0,
		"brief_query_order":{
			"otn":"013907131297815704553502",
			"tf":240000,
			"pp":2,
			"ali":{
				"cts":4
			},
			"ns":"sclBgLM9"
		}
	}",
	"a":"C8A4986C17BAB6F88623CBA0F89C375288F972C43181E193A22EC6BDA25CFDAA"
}
```

### 9.8 退款
#### 接口地址
`https://pay.qcloud.com/cpay/refund`

#### 说明文档链接
[申请退款](https://cloud.tencent.com/document/product/569/37673)

### 9.9 查询退款单
#### 接口地址
`https://pay.qcloud.com/cpay/query_refund_order`

#### 说明文档链接
[查询退款单](https://cloud.tencent.com/document/product/569/37675)

### 9.10 支付信息上报
#### 接口地址
`https://pay.qcloud.com/cpay/device_report`

#### 请求参数

| 参数名          | 必填 | 类型           | 长度 | 说明                                                         |
| --------------- | ---- | -------------- | ---- | ------------------------------------------------------------ |
| request_content | 是   | RequestContent |   -   | 请求内容，该 string 可以转为 json 结构，json 格式见本节 RequestContent。 |
| authen_info     | 是   | Authen_info    |    -  | 认证信息，详见“支付密钥认证信息”。                          |

**RequestContent 结构**

| 参数名                  | 必填 | 类型           | 长度(Byte) | 说明                                              |
| ----------------------- | ---- | -------------- | ---------- | ------------------------------------------------- |
| device_type             | 是   | Int            | 4          | 设备类型：1-移动收款机具。                         |
| company_code            | 是   | String         |  -          | 公司简码，4.1节中有说明。                            |
| model                   | 是   | String         |      -      | 型号简码，4.1节中有说明。                            |
| sn                      | 是   | String         |      -      | 完整 sn，4.1节中有说明。                              |
| begin_timestamp         | 是   | Int            | 8          | 统计开始时间，UNIX 时间戳，单位为秒，如1568810504。 |
| end_timestamp           | 是   | Int            | 8          | 统计结束时间，UNIX 时间戳，单位为秒，如1568810504。 |
| sim_number              | 否   | String         |     -       | Sim 卡号，即 ICCID 号。                                |
| cpu_usage               | 否   | Int            | 4          | 当前 CPU 使用率0-100。                                |
| mem_max                 | 否   | Int            | 4          | 最大内存 KB。                                        |
| mem_in_use              | 否   | Int            | 4          | 当前已用内存 KB。                                    |
| disk_max                | 否   | Int            | 4          | 最大硬盘 KB。                                        |
| disk_in_use             | 否   | Int            | 4          | 当前已用硬盘 KB。                                    |
| network_type            | 是   | String         |   -         | 支付所使用的网络类型：wifi、2g、3g、4g 等。          |
| upload_net_flow         | 否   | Int            | 4          | 累计上传流量。                                      |
| download_net_flow       | 否   | Int            | 4          | 累计下载流量。                                      |
| mcc                     | 否   | String         |     -       | 基站国家码，十进制数字字符串。                                    |
| mnc                     | 否   | String         |     -       | 基站网络码，十进制数字字符串。                                      |
| lac                     | 否   | String         |    -        | 基站小区号，十进制数字字符串。                                |
| cellid                  | 否   | String         |     -       | 基站 ID，十进制数字字符串。                                 |
| rss                     | 否   | String         |      -      | 基站信号强度，单位 dbm，十进制数字字符串。                      |
| longitude               | 否   | String         |    -        | 经度。                                              |
| latitude                | 否   | String         |      -      | 纬度。                                              |
| wx_pay_count            | 是   | Int            | 4          | 累计微信支付笔数，上报后清零计数。                  |
| wx_pay_success_count    | 是   | Int            | 4          | 累计微信支付成功笔数，上报后清零计数。              |
| ali_pay_count           | 是   |       Int            | 4   | 累计支付宝笔数，上报后清零计数。                    |
| ali_pay_success_count   | 是   |   Int            | 4      | 累计支付宝成功笔数，上报后清零计数。                |
| other_pay_count         | 是   |      Int            | 4     | 累计其他支付笔数，上报后清零计数。                  |
| other_pay_success_count | 是   |   Int            | 4       | 累计其他支付成功笔数，上报后清零计数。              |
| wx_pay_amount           | 是   | Int            | 8          | 累计微信支付金额，单位分，上报后清零计数。          |
| ali_pay_amount          | 是   | Int            | 8          | 累计支付宝金额，上报后清零计数。                    |
| other_pay_amount        | 是   | Int            | 8          | 累计其他支付金额，上报后清零计数。                  |
| out_mch_id              | 是   | String         |     -       | 云支付服务商号，绑定成功时获取。                     |
| out_sub_mch_id          | 是   | String         |  -          | 云支付子商户号，绑定成功时获取。                     |
| cloud_cashier_id        | 是   | String         |    -        | 云支付分配给商户订单前缀，绑定成功时获取。           |
| authen_type             | 是   | Int            | 4          | 签名类型1：HMAC-SHA256，绑定成功获取。               |
| out_shop_id             | 是   | String         |     -       | 云支付门店全局 ID，绑定成功时获取。                   |
| device_id               | 是   | String         |    -        | 云支付设备 ID，绑定成功时获取。                       |
| staff_id                | 否   | String         |      -      | 云支付店员 ID，绑定成功时获取，有可能没有。            |
| app_cpay_version        | 是   | String         |      -      | 云支付统一分配的版本号。                            |
| api_calling_infos       | 否   | ApICallingInfo |     -       | 接口调用数据，见 ApiCallingInfo。                    |

**ApiCallingInfo 结构**

| 参数名           | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ---------------- | ---- | ------ | ---------- | ------------------------------------------------------------ |
| out_trade_no     | 是   | String |     -       | 支付时的订单号。                                               |
| code             | 是   | Int    | 4          | 如果能正常获取 HTTP 的状态码（如200、404、405）则用状态码填充，其它情况：连接失败填（-2），接口获取应答超时填（-3），未知问题填（-4）。 |
| status           | 是   | Int    | 4          | brief_micro_pay 应答的一级错误码，应答中 s 字段。                  |
| internal_status  | 是   | Int    | 4          | brief_micro_pay 应答的二级错误码，应答中 is 字段。                 |
| delay_ms         | 是   | Int    | 4          | 从扫用户收款码开始到获取到 brief_micro_pay 接口应答中间的耗时，单位为毫秒。 |
| description      | 是   | String |       -     | brief_micro_pay 应答中的 d 字段内容。                             |
| pay_platform     | 是   | Int    | 4          | 支付方式，见 PayPlatform 说明。                                   |
| order_status     | 否   | Int    | 4          | 支付完成最后一次云支付接口（可能是 brief_micro_pay 或 brief_query_order）返回的订单状态，即 cts 字段内容。 |
| trade_state_desc | 否   | String |    -        | 支付完成最后一次云支付接口（可能是 brief_micro_pay 或 brief_query_order）返回的订单状态描述，即 tsd 字段内容。 |

#### 应答参数

| 参数名           | 必填 | 类型            | 长度(Byte) | 说明                             |
| ---------------- | ---- | --------------- | ---------- | -------------------------------- |
| response_content | 是   | ResponseContent |     -       | 应答内容，详见本节 ResponseContent。 |
| authen_info      | 否   | AuthenInfo      |          -  | 认证信息，详见“支付密钥认证信息”。 |

**ResponseContent 结构**

| 参数名          | 必填 | 类型   | 长度(Byte) | 说明                                |
| --------------- | ---- | ------ | ---------- | ----------------------------------- |
| status          | 是   | Int    | 4          | 错误码。                              |
| description     | 是   | String | 最长128    | 错误信息。                            |
| log_id          | 是   | Int    | 4          | 消息 ID。                              |
| internal_status | 是   | Int    | 4          | 具体说明见 internal_status 错误码表。 |

#### 示例说明

**请求生成示例代码：**
```
Json::Value request_content;
request_content["device_type"] = 1;
request_content["company_code"] = "aa";
request_content["model"] = "bb";
request_content["sn"] = "cc";
request_content["sim_number"] = "dd";
request_content["cpu_usage"] = 33;
request_content["mem_max"] = 100000;
request_content["mem_in_use"] = 2000;
request_content["disk_max"] = 200000;
request_content["disk_in_use"] = 39999;
request_content["network_type"] = "ccc";
request_content["upload_net_flow"] = 33333;
request_content["download_net_flow"] = 4444444;
request_content["mcc"] = "fff";
request_content["mnc"] = "ggg";
request_content["lac"] = "aaa";
request_content["cellid"] = "bbb";
request_content["rss"] = "ccc";
request_content["longitude"] = "ddd";
request_content["latitude"] = "eee";
request_content["begin_timestamp"] = 1553268531;
request_content["end_timestamp"] = 1553268531;
request_content["wx_pay_count"] = 11;
request_content["wx_pay_success_count"] = 11;
request_content["ali_pay_count"] = 12;
request_content["ali_pay_success_count"] = 12;
request_content["other_pay_count"] = 13;
request_content["other_pay_success_count"] = 13;
request_content["wx_pay_amount"] = 22;
request_content["ali_pay_amount"] = 23;
request_content["other_pay_amount"] = 24;
request_content["out_mch_id"] = "gggg";
request_content["out_sub_mch_id"] = "a1";
request_content["cloud_cashier_id"] = "b1";
request_content["authen_type"] = 1;
request_content["out_shop_id"] = "d1";
request_content["device_id"] = "e1";
request_content["staff_id"] = "f1";
request_content["device_shift_type"] = "g1";
request_content["nonce_str"] = "416492026bc84091bcaf7e74ea90ceba";

Json::Value info_0;
info_0["out_trade_no"] = "EEEEEEEEEEEEEE";
info_0["code"] = 200;
info_0["status"] = 2;
info_0["internal_status"] = 2;
info_0["delay_ms"] = 200;
info_0["description"] = "操作成功";
info_0["pay_platform"] = 1;
info_0["order_status"] = 3;
info_0["trade_state_desc"] = "支付成功";

request_content["api_calling_infos"].append(info_0);

Json::Value info_1;
info_1["out_trade_no"] = "FFFFFFFF";
info_1["code"] = 200;
info_1["status"] = 22;
info_1["internal_status"] = 22;
info_1["delay_ms"] = 300;
info_1["description"] = "xxxx";
info_1["pay_platform"] = 1;
info_1["order_status"] = 3;
info_1["trade_state_desc"] = "xxx";

request_content["api_calling_infos"].append(info_1);

Json::FastWriter w;
std::string request_content_str = w.write(request_content);
std::string authen_code = hmac_sha256(authen_key, request_content_str); // 计算签名

Json::Value authen;
authen["authen_code"] = authen_code;
authen["authen_type"] = 1; //统一使用 hmac_sha256，填1

Json::Value authen_info;
authen_info["a"] = authen;  //key 填"a"就行，表示认证码

Json::Value request;
request["request_content"] = request_content_str;
request["authen_info"]  = authen_info;
std::string request_str = w.write(request);
```
request_str 即为 post 内容。

**请求内容示例：**
```
{
	"request_content":"{
		"nonce_str":"4db12671e9510667d9c8d65bdf50a27b",
		"company_code":"LANDI",
		"model":"LANDI_QM600",
		"sn":"LANDI_QM600_LA197LB331212",
		"begin_timestamp":1570458756,
		"end_timestamp":1570462751,
		"network_type":"wifi",
		"mcc":"460",
		"mnc":"00",
		"lac":"2733",
		"cellid":"3437",
		"rss":"-79",
		"sim_number":"89860412101871062566",
		"wx_pay_count":1,
		"wx_pay_success_count":1,
		"ali_pay_count":0,
		"ali_pay_sucess_count":0,
		"ali_pay_amount":0,
		"other_pay_count":0,		
		"other_pay_success_count":0,
		"other_pay_amount":0,
		"out_mch_id":"sz01M43ouf007JL1sn33",
		"out_sub_mch_id":"sz01NI6PoQVvYEmOcoRp",
		"cloud_cashier_id":"010110893",
		"authen_type":1,
		"out_shop_id":"sz01aZk73lnFVxX6XSWp",
		"device_id":"kUwbvm1cpdGn4Kxm",
		"device_type":1,
		"device_shift_type":1,
		"app_cpay_version":"1.0.0",
		"api_calling_infos":[
			{
				"out_trade_no":"0101108936210615704627481",
				"code":200,
				"status":0,
				"internal_status":0,
				"delay_ms":2060
			}
		]
	}",
	"authen_info":{
		"a":{
			"authen_type":1,
			"authen_code":"C80A72B0A7858D2D84E26093F562516C64DB1D319534A7D1B9ACF17556226019"
		}
	}
}
```
**应答内容示例：**
```
{
	"response_content":"{
		"status":0,
		"description":"xxxx",
		"log_id":973138369,
		"internal_status":0,
		"device_info_report":{
			"nonce_str":"4dOOZyhxzTRexn5OBDqA8vhve3FqnCHL"
		}
	}",
	"authen_info":{
		"a":{
			"authen_type":1,
			"authen_code":"5E417C5D6FE523982C3507A22D762F3215255F752C3CD4DC37C7792D964418C3"
		}
	}
}
```

### 9.11 查询订单明细
####  接口地址
`https://pay.qcloud.com/cpay/brief_query_order_list`

#### 请求参数

| 参数名 | 必填 | 类型           | 长度 | 说明                                                      |
| ------ | ---- | -------------- | ---- | --------------------------------------------------------- |
| r      | 是   | RequestContent |  -    | 请求内容，详见本节 RequestContent。                          |
| a      | 是   | string         |  -    | 使用支付密钥计算的认证码，目前只支持 hmac-sha256 计算认证码。 |

**RequestContent 结构**

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ------ | ---- | ------ | ---------- | ------------------------------------------------------------ |
| spps   | 否   | Int [] | 单个元素4  | sub_pay_platforms：子支付平台列表，100：普通微信支付，200：普通支付宝，300：会员卡，机具填写这三个值即可。 |
| osmi   | 是   | String | -          | out_sub_mch_id：云支付分配的商户 ID，绑定成功后可获取此 ID。     |
| osi    | 是   | String | -          | out_shop_id：云支付分配的门店 ID，绑定成功后可获取此 ID。       |
| di     | 是   | String | -          | device_id：云支付分配的设备ID，绑定后可获取此 ID。              |
| ot     | 是   | Int    | 4          | order_type：单据类型，1：支付订单，2：退款单，3：全部单据。    |
| st     | 是   | Int    | 8          | start_time：查询开始时间。                                     |
| et     | 是   | Int    | 8          | end_time：查询结束时间。                                       |
| pn     | 是   | Int    | 4          | page_num：页码，必需大于0。                                    |
| ps     | 是   | Int    | 4          | page_size：单页条数，必需大于0。                               |
| tt     | 否   | Int    | 4          | 交易类型，1：刷卡支付，2：扫码支付，3：公众号支付，4：App 支付，5：声波支付， 6：H5 支付，8：一码付支付，9：小程序支付。机具应填1。 |
| ns     | 是   | String | 32         | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。                         |

#### 应答参数

| 参数名 | 必填 | 类型            | 长度(Byte) | 说明                                                      |
| ------ | ---- | --------------- | ---------- | --------------------------------------------------------- |
| rc     | 是   | ResponseContent | -          | 请求内容，详见本节 ResponseContent。                         |
| a      | 是   | String          | 32         | 使用支付密钥计算的认证码，目前只支持 hmac-sha256 计算认证码。 |

**ResponseContent 结构**

| 参数名                 | 必填 | 类型                        | 长度(Byte) | 说明                                |
| ---------------------- | ---- | --------------------------- | ---------- | ----------------------------------- |
| s                      | 是   | Int                         | 4          | 错误码。                              |
| d                      | 是   | String                      | 最长128    | 即 description，错误信息。              |
| li                     | 否   | Int                         | 4          | 即 log_id，消息 ID。                     |
| is                     | 是   | Int                         | 4          | 具体说明见 internal_status 错误码表。 |
| brief_query_order_list | 否   | BriefQueryOrderListResponse | -      | 详见本节 BriefQueryOrderListResponse。 |

**BriefQueryOrderResponse**

| 参数名 | 必填 | 类型           | 长度(Byte) | 说明                                 |
| ------ | ---- | -------------- | ---------- | ------------------------------------ |
| tc     | 是   | Int            | 4          | total_count：订单总数。                |
| ods    | 否   | OrderDetail [] | -          | order_details：见 OrderDetail 说明。     |
| ns     | 是   | String         | 32         | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。 |

**OrderDetail**

| 参数名 | 必填 | 类型             | 长度(Byte) | 说明                                   |
| ------ | ---- | ---------------- | ---------- | -------------------------------------- |
| bo     | 否   | BriefOrder       | -          | 订单结构体，见本节 BriefOrder。          |
| bro    | 否   | BriefRefundOrder | -          | 退款单结构体，见本节 BriefRefundOrder。 |

order、refund_order 只包含一个。

**BriefOrder**

| 参数名  | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ------- | ---- | ------ | ---------- | ------------------------------------------------------------ |
| spp     | 否   | Int    | 4          | sub_pay_platform：子支付平台，100：普通微信支付，200：普通支付宝，300：会员卡。 |
| tt      | 否   | Int    | 4          | trade_type：交易类型，1：刷卡支付，2：扫码支付，3：公众号支付，4：App 支付，5：声波支付，6：H5 支付，8：一码付支付，9：小程序支付。 |
| otn     | 是   | String |      32      | out_trade_no：支付单号。                                       |
| tf      | 否   |    Int    |        8    | total_fee：订单总金额。                                        |
| ct      | 是   | Int    | 8          | create_time：订单创建时间。                                    |
| wx_cts  | 否   | Int    | 4          | wxpay_current_trade_state：见枚举值定义 WxpayOrderState。      |
| ali_cts | 否   | Int    | 4          | 支付宝订单状态，见枚举值定义 AlipayOrderState。                |
 |card_cts  | 否  |int   |4  |card_current_trade_state：会员卡订单状态，见枚举值定义 CardOrderState。 |

**BriefRefundOrder**

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ------ | ---- | ------ | ---------- | ------------------------------------------------------------ |
| spp    | 否   | Int    | 4          | sub_pay_platform：子支付平台，100：普通微信支付，200：普通支付宝，300：会员卡。 |
| tt     | 否   | Int    | 4          | trade_type：交易类型，1：刷卡支付，2：扫码支付，3：公众号支付，4：App 支付，5：声波支付，6：H5 支付，8：一码付支付，9：小程序支付。 |
| otn    | 是   | String | 32         | out_trade_no：支付单号。                                       |
| tf     | 是   | Int    | 8          | total_fee：订单总金额。                                        |
| orn    | 是   | String | 32         | out_refund_no：退款单号。                                      |
| rf     | 是   | Int    | 8          | refund_fee：本次退款总金额。                                   |
| ct     | 是   | Int    | 8          | create_time：退款单创建时间。                                  |
| wx_rs  | 否   | Int    | 4          | wxpay_refund_state：微信退款状态，见枚举值定义 WxpayRefundOrderState。 |
| ali_rs | 否   | Int    | 4          | alipay_refund_state：支付宝退款状态，见枚举值定义 AlipayRefundOrderState。 |
|card_rs | 否| int | 4 |card_refund_state：会员卡退款状态，见枚举值定义 CardRefundOrderState。|

#### 示例说明
**请求生成示例代码：**
```
Json::Value request_content;
request_content["spps"].append(100);
request_content["spps"].append(200);
request_content["osmi"] = "sz0138zjfiwezee";
request_content["osi"] = "sz01FzZfei91";
request_content["di"] = "FzZfei91iefaefz";
request_content["ot"] = 1;
request_content["st"] = 1571817655;
request_content["et"] = 1571817755;
request_content["pn"] = 1;
request_content["ps"] = 2;
request_content["tt"] = 1;
request_content["ns"] = generate_random_nonce_str();

Json::FastWriter w;
const std::string &rc = w.write(request_content);

std::string authen_code = hmac_sha256(authen_key, rc); // 支付密钥计算签名

Json::Value request;
request["r"] = rc;
request["a"] = authen_code;
return w.write(request);
```
**请求内容示例：**
```
{	
	"a":"6A664293966BECE1D72CA468F2B3CD8283113BE4CDF7BC0153C28F29C77054B8",
	"r":"{
		"spps":[100,200],
		"osmi":"sz0138zjfiwezee",
		"osi":"sz01FzZfei91",
		"di":"FzZfei91iefaefz",
		"ot":1,
		"st":1571817655,
		"et":1571817755,
		"pn":1,
		"ps":2,
		"tt":1,
		"ns":"faeofeifazfeijfi"
	}"
}
```
**应答内容示例：**
```
{
	"a":"C6E3976196205719D36909D706206132EFDCFC6B672E45FC05CFDE5933BB8F18",
	"rc":"{
		"tc":102,
		"ods":[
			{
				"bo":{
					"spp":100,
					"tt":1,
					"otn":"110138591298768",
					"spp":100,
					"tt":1,
					"otn":"110138591298768",
					"tf":200,
					"ct":1571817657,
					"wx_cts":2
				}
			},
			{
				"bro":{
					"spp":200,
					"tt":1,
					"otn":"110187443881321",
					"tf":300,
					"orn":"110187812300831",
					"rf":100,
					"ct":1571817660,
					"ali_rs":2
				}
			}
		],
		"ns":"faeofeifazfeijfi"
	}"
}
```

### 9.12 查询订单汇总
####  接口地址
`https://pay.qcloud.com/cpay/brief_query_order_list_overview`

#### 请求参数

| 参数名 | 必填 | 类型           | 长度 | 说明                                                      |
| ------ | ---- | -------------- | ---- | --------------------------------------------------------- |
| r      | 是   | RequestContent |    -  | 请求内容，详见本节 RequestContent。                          |
| a      | 是   | string         |   64   | 使用支付密钥计算的认证码，目前只支持 hmac-sha256 计算认证码。 |

**RequestContent 结构**

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                                                         |
| ------ | ---- | ------ | ---------- | ------------------------------------------------------------ |
| spps   | 否   | Int[] | 单个元素4  | sub_pay_platforms：子支付平台列表，100：普通微信支付，200：普通支付宝，300：会员卡，机具填写这三个值即可。 |
| osmi   | 是   | String | -          | out_sub_mch_id：云支付分配的商户 ID，绑定成功后可获取此 ID。     |
| osi    | 是   | String | -          | out_shop_id：云支付分配的门店 ID，绑定成功后可获取此 ID。       |
| di     | 是   | String | -          | device_id：云支付分配的设备 ID，绑定后可获取此 ID。              |
| ot     | 是   | Int    | 4          | order_type：单据类型，1：支付订单，2：退款单，3：全部单据。    |
| st     | 是   | Int    | 8          | start_time：查询开始时间。                                     |
| et     | 是   | Int    | 8          | end_time：查询结束时间。                                       |
| tt     | 否   | Int    | 4          | 交易类型，1：刷卡支付，2：扫码支付，3：公众号支付，4：App 支付，5：声波支付，6：H5 支付，8：一码付支付，9：小程序支付。机具应填1。 |
| ns     | 是   | String | 32         | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。                        |

#### 应答参数

| 参数名 | 必填 | 类型            | 长度(Byte) | 说明                                                      |
| ------ | ---- | --------------- | ---------- | --------------------------------------------------------- |
| rc     | 是   | ResponseContent | -          | 请求内容，详见本节 ResponseContent。                         |
| a      | 是   | String          | 32         | 使用支付密钥计算的认证码，目前只支持 hmac-sha256 计算认证码。 |

**ResponseContent 结构**

| 参数名                 | 必填 | 类型                        | 长度(Byte) | 说明                                |
| ---------------------- | ---- | --------------------------- | ---------- | ----------------------------------- |
| s                      | 是   | Int                         | 4          | 错误码。                              |
| d                      | 是   | String                      | 最长128    | 即 description，错误信息。              |
| li                     | 否   | Int                         | 4          | 即 log_id，消息 ID。                     |
| is                     | 是   | Int                         | 4          | 具体说明见 internal_status 错误码表。 |
| brief_query_order_list | 否   | BriefQueryOrderListResponse | -          | 详见本节 BriefQueryOrderListResponse。 |

**BriefQueryOrderResponse**

| 参数名 | 必填 | 类型                   | 长度(Byte) | 说明                                 |
| ------ | ---- | ---------------------- | ---------- | ------------------------------------ |
| ovs    | 否   | OrderStatClientInfo[] | -          | overviews，见 OrderStatClientInfo 说明。 |
| ns     | 是   | String                 | 32         | 随机字符串，ASCII 字符（0-9、a-z、A-Z）。 |

**OrderStatClientInfo**

| 参数名 | 必填 | 类型 | 长度(Byte) | 说明                                                         |
| ------ | ---- | ---- | ---------- | ------------------------------------------------------------ |
| spp    | 否   | Int  | 4          | sub_pay_platform：子支付平台，100：普通微信支付，200：普通支付宝，300：会员卡。 |
| tt     | 否   | Int  | 4          | trade_type：交易类型，1：刷卡支付，2：扫码支付，3：公众号支付，4：App 支付，5：声波支付，6：H5 支付，8：一码付支付，9：小程序支付。 |
| sc     | 是   | Int  | 8          | success_count：（交易量）不含撤单的，扣款成功交易笔数，有可能是负值。 |
| sa     | 是   | Int  | 8          | success_amount：不含撤单的，扣款成功交易金额，有可能是负值。   |
| sta    | 是   | Int  | 8          | settlement_amount：操作人扣款成功结算金额 - 操作人退款结算金额 - 操作人扣款成功撤单结算金额。 |
| da     | 是   | Int  | 8          | discount_amount：必返回 net_amount - settle_amount。           |
| psa    | 是   | Int  | 8          | pay_settle_amount，扣款成功结算金额。                          |
| rsa    | 是   | Int  | 8          | refund_settle_amount，扣款成功结算金额。                       |
| rcc    | 是   | Int  | 8          | refund_create_count，退款发起笔数。                            |
| rca    | 是   | Int  | 8          | refund_create_amount，退款发起总额。                           |
| pdg    | 是   | Int  | 8          | poundage，扣款成功手续费 - 撤单返还手续费 - 退款成功返还的手续费，有可能是负值。 |
| ia     | 是   | Int  | 8          | income_amount，入账金额。                                      |
| ora    | 是   | Int  | 8          | order_refunded_amount，订单已退金额。                          |

#### 示例说明
**请求生成示例代码：**
```
Json::Value request_content;
request_content["spps"].append(100);
request_content["spps"].append(200);
request_content["osmi"] = "sz0138zjfiwezee";
request_content["osi"] = "sz01FzZfei91";
request_content["di"] = "FzZfei91iefaefz";
request_content["ot"] = 1;
request_content["st"] = 1571817655;
request_content["et"] = 1571817755;
request_content["tt"] = 1;
request_content["ns"] = generate_random_nonce_str();

Json::FastWriter w;
const std::string &rc = w.write(request_content);

std::string authen_code = hmac_sha256(authen_key, rc); // 支付密钥计算签名

Json::Value request;
request["r"] = rc;
request["a"] = authen_code;
return w.write(request);
```
**请求内容示例：**
```
{
	"a":"156073D9F354BF8000E1EF82AC82EDB2836A9D6DF7CDFD33B05ED5DFE3407516",
	"r":"{
		"spps":[100,200],
		"osmi":"sz0138zjfiwezee",
		"osi":"sz01FzZfei91",
		"di":"FzZfei91iefaefz",
		"ot":1,
		"st":1571817655,
		"et":1571817755,
		"tt":1,
		"ns":"faeofeifazfeijfi"
	}"
}
```
**应答内容示例：**
```
{
	"a":"883E4B4406668C45EECCC331A8967A4A64F07BA79B4F24395A39192F28D0F231",
	"rc":"{
		"ovs":[
			{
				"spp":200,
				"tt":1,
				"sc":4,
				"sa":2400,
				"sta":2400,
				"da":0,
				"psa":2400,
				"rsa":2100,
				"rcc":1,
				"rca":300,
				"pdg":200,
				"ia":1900,
				"ora":300
			},
			{
				"spp":100,
				"tt":1,
				"sc":14,
				"sa":9100,
				"sta":9100,
				"da":100,
				"psa":9100,
				"rsa":8100,
				"rcc":1,
				"rca":300,
				"pdg":200,
				"ia":8000,
				"ora":500
			}
		],
		"ns":"ZMEEOPPfeaeiwf122"
	}"
}
```


### 9.13 其它消息体说明

#### WxpayOrderContentExt

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                                   |
| ------ | ---- | ------ | ---------- | -------------------------------------- |
| cts    | 是   | Int    | 4          | 订单当前状态，详见 WxpayOrderState。     |
| tsd    | 是   | String | 256        | 对当前查询订单状态描述和下一步操作指引。 |

#### AlipayOrderContentExt

| 参数名 | 必填 | 类型 | 长度(Byte) | 说明                                |
| ------ | ---- | ---- | ---------- | ----------------------------------- |
| cts    | 是   | Int  | 4          | 订单当前状态，详见 AlipayOrderState。 |

#### CardOrderContentExt

| 参数名 | 必填 | 类型 | 长度(Byte) | 说明                              |
| ------ | ---- | ---- | ---------- | --------------------------------- |
| cts    | 是   | Int  | 4          | 订单当前状态，详见 CardOrderState。 |

#### 初始密钥认证信息

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                   |
| ------ | ---- | ------ | ---------- | ---------------------- |
| a      | 是   | Authen |   -         | 认证信息，见本节 Authen。 |

**Authen 结构**

| 参数名      | 必填 | 类型   | 长度(Byte) | 说明                                             |
| ----------- | ---- | ------ | ---------- | ------------------------------------------------ |
| authen_type | 是   | Int    | 4          | 签名类型1：HMAC-SHA256。                           |
| authen_code | 是   | String | 32         | 使用机具初始密钥计算的认证码，初始密钥说明见4.2节。 |

#### 支付密钥认证信息

| 参数名 | 必填 | 类型   | 长度(Byte) | 说明                   |
| ------ | ---- | ------ | ---------- | ---------------------- |
| a      | 是   | Authen |     -       | 认证信息，见本节 Authen。 |

**Authen 结构**

| 参数名      | 必填 | 类型   | 长度(Byte) | 说明                                             |
| ----------- | ---- | ------ | ---------- | ------------------------------------------------ |
| authen_type | 是   | Int    | 4          | 签名类型1：HMAC-SHA256。                           |
| authen_code | 是   | String | 32         | 使用机具初始密钥计算的认证码，支付密钥说明见4.3节。 |

#### Status

| 枚举值 | 操作结果 | 返回内容是否带认证码 | 原请求是否能重试 | 用户操作建议                                                 |
| ------ | -------- | -------------------- | ---------------- | ------------------------------------------------------------ |
| 0      | 成功     | 是                   | 是               | -                                                            |
| 3      | 未知     | 否                   | 是               | 原请求重试。                                                   |
| 101    | 失败     | 否                   | 否               | 根据 description 内容，检查调用逻辑是否有问题，如认证码计算错误。 |
| 102    | 失败     | 是                   | 否               | 换新单号重试，并根据 description 字段内容，检查调用逻辑是否有问题，如单号重复。 |
| 103    | 失败     | 是                   | 是               | 隔3秒后原请求重试或查询结果。                                  |
| 104    | 失败     | 是                   | 否               | 根据 description 字段内容操作，如退款时顾客余额不足。            |

#### WxpayOrderState

| 枚举值 | 说明                                           |
| ------ | ---------------------------------------------- |
| 1      | 订单初始态。                                     |
| 2      | 刷卡支付，成功。                                 |
| 3      | 统一下单，支付成功。                             |
| 4      | 已转入退款。                                     |
| 5      | 刷卡支付，顾客停止支付。                         |
| 6      | 统一下单，待顾客支付。                           |
| 7      | 统一下单，订单已关闭。                           |
| 8      | 刷卡支付，已撤单。                               |
| 9      | 刷卡支付，用户支付中。                           |
| 10     | 刷卡支付，支付错误。                             |
| 11     | 作废状态，表示本地有，第三方支付平台没有的订单。 |

####  AlipayOrderState

| 枚举值 | 说明               |
| ------ | ------------------ |
| 1      | 订单初始态。         |
| 2      | 成功。               |
| 4      | 等待用户支付。       |
| 5      | 已关闭，或者已退款。  |
| 6      | 交易结束，不可退款。 |
| 7      | 订单不存在。         |

#### CardOrderState

| 枚举值 | 说明         |
| ------ | ------------ |
| 1      | 订单初始态。   |
| 2      | 成功。         |
| 3      | 等待用户支付。 |
| 4      | 已退款。       |
| 5      | 已关单。       |

#### PayPlatform

| 枚举值 | 说明     |
| ------ | -------- |
| 1      | 微信支付。 |
| 2      | 支付宝。   |
| 3      | 会员卡。   |


#### WxpayRefundOrderState 

| 枚举值 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| 1      | 退款单初始态。                                                 |
| 2      | 退款成功。                                                     |
| 3      | 退款失败。                                                     |
| 4      | 退款处理中。                                                   |
| 5      | 转入代发，退款到银行发现用户的卡作废或冻结了，导致原路退款银行卡失败，资金回流到子商户的现金帐号，需要子商户人工干预，通过线下或者财付通转账的方式进行退款。 |
| 6      | 作废状态，表示本地有，第三方支付平台没有的订单。               |

#### AlipayRefundOrderState 

| 枚举值 | 说明         |
| ------ | ------------ |
| 1      | 退款单初始态。 |
| 2      | 退款成功。     |
| 3      | 退款失败。     |
| 4      | 退款处理中。   |
| 5      | 订单不存在。   |

#### CardRefundOrderState
| 枚举值 | 说明         |
| ------ | ------------ |
1| 退款单初始态。
2| 退款成功。
3 |退款失败。

##  10 加解密相关说明
### 10.1 AES-128-CBC 解密说明
- 算法：AES-128
- 模式：CBC 
- 填充类型：PKCS5Padding
- 盐（salt）：要解密的内容前8字节为盐，剩余字节内容为原始明文内容的加密内容。

示例代码如下：
```
bool aes_128_cbc_decrpty(
            const std::string &session_key,
            const std::string &input,
            std::string *output)
{
    assert(output);
    output->clear();
    output->reserve(input.length() + 24); // Space for salt + padding.

    unsigned char salt[8];
    size_t total = input.size();
    const char *inptr = input.data();

    if (input.length() < sizeof(salt)) {
        return false;
    }

    memcpy(salt, inptr, sizeof(salt));
    inptr += sizeof(salt);
    total -= sizeof(salt);

    unsigned char iv[16];
    unsigned char key[16];
    int ret = EVP_BytesToKey(EVP_aes_128_cbc(), EVP_sha1(), salt,
                             (const unsigned char *)session_key.data(),
                             session_key.length(),
                             1, key, iv);

    if (ret != sizeof(key)) {
        return false;
    }

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    EVP_CIPHER_CTX_init(ctx);

    if (!EVP_CipherInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv, 0)) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    int outlen;
    unsigned char buffer[2560];
    for (size_t i = 0; i < total; i += 2048, inptr += 2048) {
        outlen = sizeof(buffer);
        unsigned char *in = (unsigned char *)inptr;
        int inlen = total - i < 2048 ? total - i : 2048;
        if (!EVP_CipherUpdate(ctx, buffer, &outlen, in, inlen)) {
            EVP_CIPHER_CTX_free(ctx);
            return false;
        }

        output->append(reinterpret_cast<const char *>(buffer), outlen);
    }

    outlen = sizeof(buffer);
    if (!EVP_CipherFinal_ex(ctx, buffer, &outlen)) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    output->append(reinterpret_cast<const char *>(buffer), outlen);
    EVP_CIPHER_CTX_free(ctx);
    return true;
}
```
