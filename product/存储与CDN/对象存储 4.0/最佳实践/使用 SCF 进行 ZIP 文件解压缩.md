## 操作场景

在本实践中，我们用到了 [无服务器云函数 SCF](https://cloud.tencent.com/document/product/583) 和 [对象存储 COS](https://cloud.tencent.com/document/product/436)。假定用户上传到 COS 的 zip 文件需要进行解压缩，并以 zip 包名作为文件夹名，回传到 COS。用户可根据示例代码进行扩展，例如支持其他格式文件的解压缩操作。

> ?由于当前云函数每次运行时分配的临时存储空间为512MB，因此建议单个 zip 包的大小不大于300MB，解压出来的单个文件不大于200MB。

## 操作步骤

<span id="step01"></span>

### 创建存储桶

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 创建一个源存储桶，用于存放上传的 zip 文件，命名为 zip-upload，并选择**北京**地域，访问权限选择**私有读写**。
3. 创建一个目标存储桶，用于存放解压后的文件，命名为 unzip，并选择**北京**地域，访问权限选择**私有读写**。

>?了解创建存储桶和为存储桶设置访问权限，详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 和 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。 

<span id="step02"></span>

### 创建云函数 SCF

1. 登录 [无服务器云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，进入【函数服务】页面。
2. 选择**北京**地域，单击【新建】，进入新建函数页面。
3. 在**新建函数**页面配置以下信息，配置完成后，然后单击【下一步】。
	- **创建方式**：选择 “模板函数”。
	- **函数名称**：命名为 “unzip_to_cos”。
	- **模板搜索**：选择搜索“语言” 为 “Python2.7” 的 “zip 包解压” 模板，此时将鼠标移至模板函数上，可单击【查看详情】查看模板函数详情，函数代码支持下载操作。
![](https://main.qcloudimg.com/raw/1cee42e5814793159daecd8387fb37ee.jpg)
4. 进入函数配置页面，保持默认配置即可，单击【完成】，完成函数的创建。
5. 单击【函数代码】，此时需要在函数代码编辑器中，按照注释修改参数。
修改配置变量： appid、secret_id、secret_key、region、bucket_upload（此处应为 unzip bucket）和 password（选配，压缩包的密码），配置完成，单击【保存】。
6. 单击【函数配置】，修改函数的超时时间为100秒，在实际运行过程中，如果有遇到函数执行超时，可以根据实际情况加大超时时间。

<span id="step03"></span>

### 配置 COS 触发器
1. 完成上述步骤创建云函数 SCF 之后。
2. 选择【触发方式】>【添加触发方式】，为云函数添加 COS 触发器，配置如下信息。
 - **触发方式**：选择 “COS 触发”。
 - **COS Bucket**：选择“zip-upload”。
 - **事件类型**：选择“全部创建”，其它保持默认参数。
3. 单击【保存】。

<span id="step04"></span>

### 测试函数功能

1. 下载 zip 格式的 [测试样例](https://main.qcloudimg.com/raw/6e0d4837eefd0ce77dac8a3973acdf39.zip)。
2. 进入 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，选择创建好的存储桶：zip-upload，单击【上传文件】。
3. 在弹出的“上传文件”窗口中，选择第1步下载的测试样例，单击【上传】。
4. 进入另外一个存储桶：unzip，可查看到解压后的文件。
5. 进入 [无服务器云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，查看执行结果。选择【函数服务】>【“函数”】>【运行日志】，即可看到打印出的日志信息。

