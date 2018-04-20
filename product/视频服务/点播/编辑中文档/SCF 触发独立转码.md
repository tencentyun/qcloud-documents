 
本方案介绍了如何在不搭建后台服务的情况下，对上传到 COS 中的视频文件自动进行转码。

## 方案概览

该方案涉及腾讯云[对象存储](https://cloud.tencent.com/product/cos)（以下简称为 COS），[无服务器云函数](https://cloud.tencent.com/product/scf)（以下简称为 SCF）和[点播系统独立转码](https://cloud.tencent.com/document/product/266/2833)三个服务。方案的大致流程如下图所示（在完成相关配置的情况下）：

![SCF 调用独立转码框架图](https://main.qcloudimg.com/raw/7ddb98640a9f0c1de45cffba447792a4.jpg)

1. 开发者将视频文件上传到 COS 的输入 Bucket；
2. COS 自动通知 SCF 有新文件上传；
3. SCF 自动向点播转码服务发起转码请求；
4. 转码服务从 COS 的输入 Bucket 中读取新上传的文件；
5. 转码服务执行转码，并把生成的文件写入到 COS 输出 Bucket。

整个过程中开发者仅需要执行上传操作，其余均由腾讯云自动完成。

## 配置过程

为了使用上述功能，开发者需要对 COS 和 SCF 进行配置。配置操作仅需执行一次，除非对该服务的需求有变更（比如修改输入/输出 Bucket、修改输出路径、修改转码规格等）。

### 准备 COS Bucket

1. 创建输入 COS Bucket：登录 [COS 控制台](https://console.cloud.tencent.com/cos5/bucket)，点击【存储桶列表】页面下的【创建Bucket】按钮，设置 Bucket 名称为 **inputbucket**，选择地域（以【北京】为例），设置访问权限为默认值【公有读私有写】，点击【保存】按钮。
2. 在 inputbucket 中新建视频上传目录 **video**。
3. 创建输出 COS Bucket：按照相同的方式在创建输出 **outputbucket**，并在该 Bucket 下新建视频写入目录 **video**。
5. Bucket 授权：因为转码服务需要访问输出 Bucket，因此需要得到开发者的授权。进入【存储桶列表】，点击刚创建的 **outputbucket**，进入【权限管理】，在用户权限下点击【添加用户】，帐号 ID 填写 **2819697038**，【权限】勾选【数据读取】和【数据写入】，点击【保存】。

![COS Bucket 权限设置](https://main.qcloudimg.com/raw/ae4be63c286b1b8ffc6d2218284fdd25.png)

### 准备 SCF 程序包

SCF 向转码服务发起请求是通过部署一段代码实现的，为了方便开发者，腾讯云点播提供了代码模版。开发者通过修改几个参数，即可以控制输出 Bucket、输出文件路径、转码规格。

1. 创建 SecretId 和 SecretKey：SCF 代码请求转码服务时，需要使用到开发者的 SecketId 和 SecretKey，用于鉴权。获取 SecketId 和 SecretKey 的方法请参考[申请安全凭证](https://cloud.tencent.com/document/api/213/6984#1.-.E7.94.B3.E8.AF.B7.E5.AE.89.E5.85.A8.E5.87.AD.E8.AF.81)
2. 下载 SCF [代码模版](https://main.qcloudimg.com/raw/63c82dcc941a538dee90ec8b6535b9cc.zip)，解压，修改配置文件 `config.json`，按实际情况修改其中的配置参数（含义见下表）。
3. 将修改后的代码重新打包成 zip 文件，命名为 RequestVideoTranscodeDemo.zip

| 配置参数 | 含义 | 用法 |
|---|
| `SecretId` | SCF 代码请求转码服务时的身份凭证 | 按实际内容填写 |
| `SecretKey` | 与 SecretId 配对使用| 按实际内容填写 |
| `outpuBucket` | 转码生成的视频文件的存放 Bucket | 填写 Bucket 名称，注意：<br />不可以为输入 Bucket；<br />要与输入 Bucket 同地域;<br />要完成访问授权 |
| `outputPath` | 转码生成的视频文件的存放路径 | 如果不填写，输出路径和输入文件的路径保持一致；<br />如果填写，所有输出文件都存在该路径下，输入文件的路径将被忽略；<br />不能够直接使用根目录 `"/"` |
| `definition` | 转码规格 | 填写点播转码[参数模版](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF) ID |

``` 
{
    "SecretId":"your secretId",
    "SecretKey":"your secretKey",
    "outpuBucket":"outputbucket",
    "outputPath":"",
    "mediaProcess":{
        "transcode":{
            "definition":[30]
        }
    }
}
``` 

### 创建 SCF
1. 登录[【无服务器云函数控制台】](https://console.cloud.tencent.com/scf)，在【北京】地域下点击【新建】按钮；
2. 进入【函数配置】选项，函数名称填写 **RequestVideoTranscodeDemo**，运行环境选择 Nodejs 6.10，超时时间设置为 10s，其余保持默认值，点击【下一步】；
3. 进入【函数代码】选项，选择【本地上传zip包】。执行方法填写 **index.main_handler**，选择上述步骤创建部署程序包中创建的 **RequestVideoTranscodeDemo.zip**，点击【下一步】；
4. 进入【触发方式】部分，点击【添加触发器】，触发方式选择 【COS触发】，COS Bucket选择 **inputbucket**，【事件类型】选择**文件上传**，点击【保存】后完成触发器创建，点击【完成】。

## 测试
1. 进入 COS 控制台的【存储桶列表】，选择 **inputbucket**，点击【上传文件】，上传一个视频文件。
2. 登录[【无服务器云函数控制台】](https://console.cloud.tencent.com/scf)【函数服务】，进入 **RequestVideoTranscodeDemo** 函数，点击【日志】可以查看到请求参数和请求返回结果。
3. 转码完成后可在 **outputbucket** 观察到有转码文件生成。

![](https://main.qcloudimg.com/raw/2edf0c22ae509d397c8293a0821e486b.png)


***注意：***

1. **inputbucket**、**outputbucket** 和 SCF 必须在同一地域。
2. 目前支持该方案的地域包括**北京、上海和广州**，其它地域将逐步支持。
3. 视频文件不要直接存放在 Bucket 的根目录下（不论是原文件还是转码文件），否则会产生错误。至少需要有一级目录。
5. 控制台创建 Bucket 后，需要 1~2 分钟才会出现在 SCF 的配置选项中。
``` 





