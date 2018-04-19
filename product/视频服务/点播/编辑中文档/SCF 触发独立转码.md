 
本方案介绍了如何在不搭建后台服务的情况下，对上传到 COS 中的视频文件自动进行转码。

## 方案概览

该方案涉及腾讯云[对象存储](https://cloud.tencent.com/product/cos)，[无服务器云函数](https://cloud.tencent.com/product/scf)和[点播系统独立转码](https://cloud.tencent.com/document/product/266/2833)三个服务，大致流程如下图所示：

![SCF 调用独立转码框架图](https://main.qcloudimg.com/raw/24b3d2b6ce152671251b60d4f828dcac.png)

## 配置过程

### 准备对象存储存储桶
1. 创建输入 COS Bucket：登录 [COS 控制台](https://console.cloud.tencent.com/cos5/bucket)，点击【存储桶列表】页面下的【创建Bucket】按钮，设置 Bucket 名称为 **inputbucket**，选择地域（以【北京】为例），设置访问权限为默认值【公有读私有写】，点击【保存】按钮。
2. 在 inputbucket 中新建视频上传目录 **video**。
3. 创建输出 COS Bucket：按照相同的方式在创建输出 **outputbucket**，并在该 Bucket 下新建视频写入目录 **video**。
5. Bucket 授权：进入【存储桶列表】，点击刚创建的 **outputbucket**，进入【权限管理】，在用户权限下点击【添加用户】，帐号 ID 填写 **2819697038**，【权限】勾选【数据读取】和【数据写入】，点击【保存】。

![COS Bucket 权限设置](https://main.qcloudimg.com/raw/ae4be63c286b1b8ffc6d2218284fdd25.png)

### 创建部署程序包
下载点播提供的无服务器云代码模版，解压文件夹，修改配置文件参数 config.json，将 SecretId 和 SecretKey 修改为您的实际参数，并将代码打包成 `RequestVideoTranscodeDemo.zip`。

``` 
{
    "SecretId":"your secretId",
    "SecretKey":"your secretKey",
    "outpuBucket":"outputbucket",
    "outputPath":"/video/",
    "mediaProcess":{
        "transcode":{
            "definition":[72782]
        }
    }
}
``` 

### 创建无服务器云函数
1. 登录[【无服务器云函数控制台】](https://console.cloud.tencent.com/scf)，在【北京】地域下点击【新建】按钮；
2. 进入【函数配置】选项，函数名称填写 **RequestVideoTranscodeDemo**，运行环境选择 Nodejs 6.10，超时时间设置为 10s，其余保持默认值，点击【下一步】；
3. 进入【函数代码】选项，选择【本地上传zip包】。执行方法填写 **index.main_handler**，选择上述步骤创建部署程序包中创建的 **RequestVideoTranscodeDemo.zip**，点击【下一步】；
4. 进入【触发方式】部分，点击【添加触发器】，触发方式选择 【COS触发】，COS Bucket选择 **inputbucket**，【事件类型】选择**文件上传**，点击【保存】后完成触发器创建，点击【完成】。

## 测试
1. 完成上述三个步骤后，进入 COS 控制台的【存储桶列表】，选择 **inputbucket**，点击【上传文件】，上传一个视频文件。
2. 登录[【无服务器云函数控制台】](https://console.cloud.tencent.com/scf)【函数服务】，进入 **RequestVideoTranscodeDemo** 函数，点击【日志】可以查看到请求参数和请求返回结果。
3. 转码完成后可在 **outputbucket** 观察到有转码文件生成。

![](https://main.qcloudimg.com/raw/2edf0c22ae509d397c8293a0821e486b.png)


***注意：***

1. **inputbucket**、**outputbucket** 和无服务器云函数必须在同一地域。
2. 目前支持该方案的地域包括**北京、上海和广州**，其它地域将逐步支持。
3. 视频文件不要直接存放在 Bucket 的根目录下（不论是原文件还是转码文件），否则会产生错误。至少需要有一级目录。
5. 控制台创建 Bucket 后，需要 1~2 分钟才会出现在 SCF 的配置选项中。
``` 





