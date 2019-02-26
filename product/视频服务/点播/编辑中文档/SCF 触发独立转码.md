## 概述

腾讯云视频转码服务，提供了 [视频处理 API](/document/product/266/15571)，开发者可以通过调用 API 对存储在 COS 中的视频执行转码任务。
本方案介绍一种无须开发者主动调用 API，即可发起视频转码任务的方式。通过在 COS 上进行简单的配置，开发者上传文件到 COS 时将触发预设操作，自动发起视频处理的任务。

## 方案原理

方案主要涉及到腾讯云的以下三个服务：
1. [对象存储](https://cloud.tencent.com/product/cos)（即 COS）
2. [无服务器云函数](https://cloud.tencent.com/product/scf)（即 SCF）
3. 视频转码

![SCF 调用转码框架图](https://main.qcloudimg.com/raw/7ddb98640a9f0c1de45cffba447792a4.jpg)

如上面的流程图所示，方案的工作原理如下：
1. 开发者将视频文件上传到 COS 的输入 Bucket；
2. COS 自动通知 SCF 有新文件上传；
3. SCF 自动向转码服务发起视频处理请求；
4. 转码服务从 COS 的输入 Bucket 中读取新上传的文件并进行转码操作；
5. 转码服务将转码后生成的文件写入 COS 输出 Bucket。

整个过程中，开发者仅需要执行上传操作，其余步骤均由腾讯云自动完成。

## 配置过程

为了使用上述功能，开发者需要对 COS 和 SCF 进行配置。除非对转码服务的需求有变更（比如修改输入/输出 Bucket、修改输出路径、修改转码规格等），配置操作仅需执行一次。

### COS Bucket 配置

开发者需要使用自己的账号创建一个输入 Bucket 和一个输出 Bucket，并完成对 Bucket 的配置（参见 [Bucket 配置](/document/product/266/16923)）。


### SCF 配置

方案提供了一个 SCF 模板，开发者根据对视频文件的处理需要，完成对模板的配置。模板配置完成后，在 SCF 控制台中上传模板并创建触发器。

#### 1. 获取密钥 SecretId 和 SecretKey
通过 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)，获取 SecretId 和 SecretKey。如果尚未创建过密钥，请先 [申请密钥](/document/api/213/6984#1.-.E7.94.B3.E8.AF.B7.E5.AE.89.E5.85.A8.E5.87.AD.E8.AF.81)。

#### 2. 填写 SCF 模板
下载 [SCF 模板](https://main.qcloudimg.com/raw/8bb02ea0d7edac6733886dc67f96b6de.zip)，根据表格中的内容填写配置文件 **config.json**，配置文件中的各个参数含义如下：

| 参数名称  | 必填 | 类型 | 说明 |
|---|---|---|---|---|
| SecretId | 是 | String | API 密钥中的 SecretId |
| SecretKey | 是 | String | API 密钥中的 SecretKey |
| Para | Object | 是 | 参见 [执行任务参数](#para.EF.BC.88.E6.89.A7.E8.A1.8C.E4.BB.BB.E5.8A.A1.E5.8F.82.E6.95.B0.EF.BC.89) |

##### Para（执行任务参数）
| 参数名称 | 必填 | 类型 | 说明 |
|---|---|---|---|---|
| output | 是 | Object | 参见 [输出文件信息参数](/document/product/266/15571#output.EF.BC.88.E8.BE.93.E5.87.BA.E6.96.87.E4.BB.B6.E4.BF.A1.E6.81.AF.E5.8F.82.E6.95.B0.EF.BC.89) |
| mediaCheck | 否 | Object| 参见 [视频鉴黄参数](/document/product/266/15571#mediacheck.EF.BC.88.E8.A7.86.E9.A2.91.E9.89.B4.E9.BB.84.E5.8F.82.E6.95.B0.EF.BC.89) |
| mediaProcess| 否 | Object | 参见 [视频处理参数](/document/product/266/15571#mediaprocess.EF.BC.88.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E5.8F.82.E6.95.B0.EF.BC.89) |
| taskAttribute | 否 | Object | 参见 [任务属性配置参数](/document/product/266/15571#taskattribute.EF.BC.88.E4.BB.BB.E5.8A.A1.E5.B1.9E.E6.80.A7.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0.EF.BC.89) |

##### 示例
对输入文件进行做转码操作，转码的模板 ID 有 **210**，**220** 和 **230**。
转码后输出到名为 **myoutputbucket** 的 Bucket 的 **/output/test/** 目录下。

```json
{
    "SecretId":"AKIDgJoxxxxxxxxxxxxxxxxxxxxxxsW78G9r",
    "SecretKey":"f8OTP9xxxxxxxxxxxxxxxxxxCh186sUy",
    "Para": {
        "output": {
            "bucket": "myoutputbucket",
            "dir": "/output/test/"
        },
        "mediaProcess":{
            "transcode":{
                "definition":[210，220，230]
            }
        }
    }
}
``` 

配置 **config.json** 之后，将修改后的模板打包成 zip 文件，命名为 **RequestVideoTranscode.zip**。

#### 3. 创建 SCF 触发器
1. 登录 [无服务器云函数控制台](https://console.cloud.tencent.com/scf)，选择与输入文件 Bucket 相同的地域（如输入文件 Bucket 属于广州，则此处选择 **广州**），单击【新建】按钮；
2. 进入【函数配置】选项，函数名称填写 **RequestVideoTranscode**，【运行环境】选择 **Nodejs 6.10**，【超时时间】设置为 **10s**，其余保持默认值，单击【下一步】；
3. 进入【函数代码】选项，选择【本地上传 zip 包】。执行方法填写  **index.main_handler**，选择上一步创建的 **RequestVideoTranscode.zip**，单击【下一步】；
4. 进入【触发方式】部分，单击【添加触发器】，触发方式选择【COS触发】，【COS Bucket】选择输入文件 Bucket 的名字（例如为 **myinputbucket**），【事件类型】选择【文件上传】，单击【保存】后完成触发器创建，最后单击【完成】。

## 验证方式
这一节，将介绍如何验证 COS 上传是否正常触发视频处理，并获取转码后的视频文件。
1. 按照 [配置过程](/document/product/266/16923) 的介绍，完成对 COS Bucket 和 SCF 的配置，并假设：
输入 Bucket 名为 **myinputbucket**；
输出 Bucket 名为 **myoutputbucket**；
目标转码模板 ID 为 **30**，**40** 和 **50**；
2. 进入 COS 控制台的【存储桶列表】，选择 **myinputbucket**，单击【上传文件】，向输入文件 Bucket 上传一个视频文件；
2. 登录 [无服务器云函数控制台](https://console.cloud.tencent.com/scf) 的【函数服务】，进入 **RequestVideoTranscode** 函数，单击【日志】可以查看到请求参数和请求返回结果；
3. 转码完成后可在 COS 的 **myoutputbucket**，观察到有转码文件生成。

![](https://main.qcloudimg.com/raw/2edf0c22ae509d397c8293a0821e486b.png)


***注意：***

1. 输入文件 Bucket，输出文件 Bucket 和 SCF 必须在同一地域。
2. 目前支持该方案的地域包括 **北京**、**上海** 和 **广州**，其它地域将逐步支持。
3. 视频文件不要直接存放在 Bucket 的根目录下（不论是原文件还是转码文件），否则会产生错误（至少需要有一级目录）。
4. 控制台创建 Bucket 后，需要 1~2 分钟才会出现在 SCF 的配置选项中。
