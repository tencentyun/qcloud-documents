## 操作场景

在本实践中，我们用到了 [云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583) 和 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/document/product/436)。假定用户上传到 COS 的 zip 文件需要进行解压缩，并以 zip 包名作为文件夹名，回传到 COS。用户可根据示例代码进行扩展，例如支持其他格式文件的解压缩操作。

>? 由于当前云函数每次运行时分配的临时存储空间为512MB，因此建议单个 zip 包的大小不大于300MB，解压出来的单个文件不大于200MB。
>

## 操作步骤

<span id="step01"></span>
### 创建存储桶

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 创建一个源存储桶，用于存放上传的 zip 文件，命名为 zip-upload，并选择**北京**地域，访问权限选择**私有读写**。
![](https://qcloudimg.tencent-cloud.cn/raw/5941b79650510cb4d25d870292a4ad58.png)
3. 创建一个目标存储桶，用于存放解压后的文件，命名为 unzip，并选择**北京**地域，访问权限选择**私有读写**。
![](https://qcloudimg.tencent-cloud.cn/raw/d46d624c36e39cb8edaf4382bc6dba89.png)
>? 了解创建存储桶和为存储桶设置访问权限，详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 和 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。 
>

<span id="step02"></span>
### 创建云函数

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，进入**函数服务**页面。
2. 选择**北京**地域，单击**新建**，进入新建函数页面。
3. 选择**模板创建**，搜索**ZIP包解压**并选择该模板，单击**下一步**。
**ZIP 包解压**模板目前仅支持 zip 格式，如需处理 rar 或 7z 等其他格式，需自行扩展代码。您可单击**查看详情**查看模板函数详情，模板函数代码支持下载操作。
4. 配置如下主要信息：
 - **函数名称**：命名为“unzip_to_cos”。
![](https://qcloudimg.tencent-cloud.cn/raw/3f3307ac2f0d96ff874a1a380b379fd2.png)
 - **函数代码**：按照注释修改如下参数。
![](https://qcloudimg.tencent-cloud.cn/raw/5a6549ec9e0602941d1f2a94d242765b.png)
    - appid：可在 [账号信息](https://console.cloud.tencent.com/developer) 中获取。
    - secret_id、secret_key：可在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取。
    - region：目标存储桶的所属地域，此处为 ap-beijing。
    - bucket_upload：此处应填 unzip-125xxxxxxx。
    - password：压缩包的解压密码，若不设解压密钥则留空。
 - **高级配置**：修改函数的超时时间为100秒。在实际运行过程中，如果有遇到函数执行超时，可以根据实际情况加大超时时间。
![](https://qcloudimg.tencent-cloud.cn/raw/2e615c88c3302ee306b9aa3e6bca1344.png)
 - **触发器配置**：
![](https://qcloudimg.tencent-cloud.cn/raw/8fb7060dd7937b5bb504a7468f4e6a9e.png)
    - **触发方式**：选择“COS 触发”。
    - **COS Bucket**：选择“zip-upload”。
    - **事件类型**：选择“全部创建”，其他保持默认参数。
5. 单击**完成**。

<span id="step03"></span>
### 测试函数功能

1. 下载 **zip 格式**的 [测试样例](https://main.qcloudimg.com/raw/6e0d4837eefd0ce77dac8a3973acdf39.zip)。
2. 进入 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，选择创建好的存储桶：zip-upload，单击**上传文件**。
3. 在弹出的“上传文件”窗口中，选择第1步下载的测试样例，单击**上传**。
4. 进入另外一个存储桶：unzip，可查看到解压后的文件。
![](https://main.qcloudimg.com/raw/c2b930bceda5ee4910da50545f78b911.png)
5. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，进入**函数服务**页面。
6. 找到刚创建的函数，单击其函数名称，进入该函数管理页面。
7. 选择**日志查询**，即可看到打印出的日志信息。


