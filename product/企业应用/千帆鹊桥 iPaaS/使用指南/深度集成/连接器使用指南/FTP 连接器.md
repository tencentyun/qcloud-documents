

## 简介
- FTP（File Transfer Protocol，文件传输协议）是 TCP/IP 协议组中的协议之一。FTP 协议包括两个组成部分：FTP 服务器和 FTP 客户端。其中 FTP 服务器用来存储文件，用户可以使用 FTP 客户端通过 FTP 协议访问位于 FTP 服务器上的资源。在开发网站的时候，通常利用 FTP 协议把网页或程序传到 Web 服务器上。此外，由于 FTP 传输效率非常高，在网络上传输大的文件时，一般也采用该协议。
- 默认情况下，FTP 协议使用 TCP 端口中的20和21这两个端口，其中20用于传输数据，21用于传输控制信息（命令）。是否使用20作为传输数据的端口与 FTP 使用的传输模式有关，如果采用主动模式，则数据传输端口为20；如果采用被动模式，则最终使用的端口由服务器端和客户端协商决定。
- FTP 连接器是基于 FTP 协议实现文件传输的通道，因此应用程序才可与外部 FTP 服务器进行文件的交换。
- 针对 FTP 连接器提供对 FTP 服务器上的文件和文件夹的访问，主要特性包括：
 - 根据需要读写文件或完全列出目录内容的功能。
 - 支持常见的 FTP 操作，例如：创建目录和复制、移动、重命名和删除文件。
 - 支持锁定文件。
 - 支持文件匹配功能。

## 连接器配置

#### 通用配置

| 参数             | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ---------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 域名             | string   | FTP 服务器域名                                               | 是       |        |
| 端口号           | int      | FTP 服务器端口号                                             | 否       | 21     |
| 用户名           | string   | FTP 服务器的用户名，如果服务器需要身份验证，则为必需参数   | 否       |        |
| 密码             | string   | FTP 服务器的密码，如果服务器需要身份验证，则为必需参数     | 否       |        |
| 工作路径         | string   | 指定 FTP 服务器路径作为根目录。若未提供，则为 FTP 服务器默认值 | 否       |        |
| 传输模式         | enum     | 传输模式，目前支持 BINARY（默认值）和 ASCII               | 否       | BINARY |
| 远程 Host 连接验证 | bool     | 启用或禁用验证，判断进行数据连接的远程 host 与控制命令连接的 host 是否相同 | 否       | True   |

#### 高级配置

| 参数             | 数据类型 | 描述                                           | 是否必填 | 默认值     |
| ---------------- | -------- | ---------------------------------------------- | -------- | ---------- |
| 重连接频率（秒）  | int      | 重连接频率（单位s），范围：0～300            | 否       | 10(s)      |
| 控制编码         | enum     | 服务器通道控制编码，ISO-8859-1（默认）和 UTF-8 | 否       | ISO-8859-1 |
| 连接超时时间（秒） | int      | 连接超时等待时间（单位s），范围：0～300      | 否       | 60(s)      |
| 响应超时时间（秒） | int      | 请求响应超时等待时间（单位s），范围：0～300  | 否       | 60(s)      |

**连接器配置界面如下：**
![](https://main.qcloudimg.com/raw/7b352f574862cebf9bc5c03c1092537a/FTP1.png)

## 操作配置
<dx-tabs>
::: 读取文件
#### 输入参数

| 参数                 | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 文件路径             | string   | 读取文件路径                                                   | 是       |        |
| 文件锁               | bool     | 是否开启文件锁                                               | 否       | false  |
| 文件锁等待时间（秒）   | int      | 文件锁等待时间（秒），范围：0～60                         | 否       | 30(s)  |
| 文件校验时间间隔（秒） | int      | 文件大小校验等待时间（秒），范围：0～60，以判断文件是否可读。在等待时间前后执行两次 sizecheck 文件大小检测，如果两次检测都返回相同的值，即 sizecheck 期间文件没有其他修改操作则可以读取该文件 | 否       | 0(s)   |

![](https://main.qcloudimg.com/raw/6dcad4f7c7650b9827c405a0b75b6b9c/FTP2.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 Entity 类型；执行失败后，payload 为空     |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

- FTP 读取文件操作会返回文件内容，根据文件名后缀设置消息的 mimeType 和 encoding 并放到消息 payload 中，后续可通过 dataway 表达式直接访问。
![](https://main.qcloudimg.com/raw/f4f8613b3c2339e28b262fa113da2947/FTP-Read3.png)
- FTP 读取文件操作若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/1da6e32cc74c659e598facaacedc0b35/FTP-Read5.png)

#### 案例

1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 读取文件操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/52aa50adfd6a87da7848d7ad54624fed/FTP-Read1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 FTP 服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图:
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件路径设为“/data/ftptest.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/b2bfb5fb816c63fd347ade2fc858feab/FTP-Read.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制HTTP Listener监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 返回 payload 响应结果如下，即为“/data/ftptest.txt”文件内容。
![](https://main.qcloudimg.com/raw/34e9cb6ad9b14ada283d9038d3af7291/FTP-Read2.png)
![](https://main.qcloudimg.com/raw/f4f8613b3c2339e28b262fa113da2947/FTP-Read3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/d4dcdb5b32cc72e302e65063477d3444/FTP-Read4.png)
![](https://main.qcloudimg.com/raw/1da6e32cc74c659e598facaacedc0b35/FTP-Read5.png)

:::
::: 写文件
#### 输入参数

| 参数               | 数据类型                             | 描述                                                         | 是否必填 | 默认值     |
| ------------------ | ------------------------------------ | ------------------------------------------------------------ | -------- | ---------- |
| 文件路径           | string                               | 待写入文件路径（当检测为目录时抛错）支持表达式输入           | 是       |            |
| 文件内容           | string                               | 待写入文件的内容，默认为当前消息 payload 支持表达式输入        | 否       | #[payload] |
| 创建父级目录       | bool                                 | 是否尝试创建任何不存在的父目录                               | 否       | true       |
| 文件锁             | bool                                 | 是否锁定文件                                               | 否       | false      |
| 文件锁等待时间（秒）| int                                  | 文件锁等待时间（秒）（范围：0～60）                            | 否       | 30(s)      |
| 文件写模式         | enum: OVERWRITE、 APPEND、CREATE_NEW | 文件写模式：<br><li>OVERWRITE：覆盖写<br><li>APPEND：追加写<br><li>CREATE_NEW：当文件不存在时新建，否则抛错 | 否       | OVERWRITE  |

![](https://main.qcloudimg.com/raw/472c2444549a3f905da83ecf4895e419/FTP3.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

FTP 写文件操作，若执行成功则 payload 为空；若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

#### 案例
1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 写文件操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/8dc123452622cd771476cf226f5aede0/FTP-Write1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 FTP 服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图:
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件路径设为“/data/ftptest.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/39affa873000ccd7081966d25f9360de/FTP-Write.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 写文件操作若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/2cc48d6536616e2be873ad5fb61f7dab/FTP-Write2.png)
![](https://main.qcloudimg.com/raw/d8cfed4cc4086802dfb2469e341a39fe/FTP-Write3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/7cdb0ff46805fce4551479ac432c1c49/FTP-Write4.png)
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

:::
::: 删除文件
#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 文件删除路径 | string   | 待删除的文件或路径：<br><li>当文件或路径不存在时抛错<br><li>支持删除单个文件以及目录（包括目录下所有文件）<br><li>如果文件未被锁定，则删除路径指向的文件，支持表达式输入 | 是       |        |

![](https://main.qcloudimg.com/raw/e0caa699dc2613e820c3a4f67be93acb/FTP4.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

FTP 删除文件操作，若执行成功则 payload 为空；若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

#### 案例
1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 删除文件操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/b70e4865d9f9074355ad762b41af6c42/FTP-Delete1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的FTP服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图:
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数，文件删除路径设为“/data/ftptest.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/8456cab743e98664be47850a24639b29/FTP-Delete.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 删除文件操作，若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/2cc48d6536616e2be873ad5fb61f7dab/FTP-Write2.png)
![](https://main.qcloudimg.com/raw/d8cfed4cc4086802dfb2469e341a39fe/FTP-Write3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/7cdb0ff46805fce4551479ac432c1c49/FTP-Write4.png)
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

:::
::: 复制文件
#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 源文件路径   | string   | 要复制文件的源路径支持复制单个文件和目录（包括目录下所有文件），支持表达式输入 | 是       |        |
| 目标文件路径 | string   | 文件要复制到的目标路径支持表达式输入                         | 是       |        |
| 创建父级目录 | bool     | 是否创建不存在的父级目录                                     | 否       | true   |
| 覆盖文件     | bool     | 是否覆盖文件。当目标路径已存在同名源文件路径时，若 Overwrite 为 false，则抛错；若 Overwrite 为 true，则覆盖写 | 否       | false  |
| 重命名       | string   | 复制文件的新名称。如果未提供，则保留原始文件名；当目标路径已存在同名源文件路径时，可设置 RenameTo 参数命名新名称解决复制文件同名冲突支持表达式输入 | 否       |        |

![](https://main.qcloudimg.com/raw/8f4ee381355c08bcab38f7ad2d4700ab/FTP5.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

FTP 复制文件操作，若执行成功则 payload 为空；若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

#### 案例
1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 复制文件操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/6ca5fd405bf6abff2c42f29a5a77995a/FTP-Copy1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 FTP 服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。源文件路径设为“/data/ftptest.txt”，目标文件路径设为“/data/copydir”，重命名设为“ftptestcopy.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/c0565f8a0dbf7df7c4bb66fb694c2728/FTP-Copy.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 复制文件操作，若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/2cc48d6536616e2be873ad5fb61f7dab/FTP-Write2.png)
![](https://main.qcloudimg.com/raw/d8cfed4cc4086802dfb2469e341a39fe/FTP-Write3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/7cdb0ff46805fce4551479ac432c1c49/FTP-Write4.png)
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)
:::
::: 重命名文件
#### 输入参数 

| 参数       | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ---------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 文件路径   | string   | 待重命名的文件路径：<br><li>当路径或文件不存在时报错<br><li>同时支持目录和文件重命名，支持表达式输入 | 是       |        |
| 重命名名称 | string   | 文件或路径的新名称支持表达式输入                             | 是       |        |
| 覆盖文件   | bool     | 是否覆盖文件：<br><li>当 Overwrite 为 false 时，若重命名文件路径已存在则抛错<br><li>当 Overwrite 为 true 时，则直接覆盖写 | 否       | false  |

![](https://main.qcloudimg.com/raw/1cfdd0dfab059940d1d133b54db5ad25/FTP6.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

FTP 重命名文件操作，若执行成功则 payload 为空；若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

#### 案例
1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 重命名文件操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/4c127aa2959b625d3be84239acfc4623/FTP-Rename1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 FTP 服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件路径设为“/data/ftptest.txt”，重命名名称设为“ftptestrename.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/5f473fca18d70258bf3c145a05608aba/FTP-Rename.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 重命名文件操作，若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/2cc48d6536616e2be873ad5fb61f7dab/FTP-Write2.png)
![](https://main.qcloudimg.com/raw/d8cfed4cc4086802dfb2469e341a39fe/FTP-Write3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/7cdb0ff46805fce4551479ac432c1c49/FTP-Write4.png)
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)
:::
::: 移动文件
#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 源文件路径   | string   | 要转移的文件或目录路径支持移动单个文件和目录（包括目录下所有文件），支持表达式输入 | 是       |        |
| 目标文件路径 | string   | 文件要移动到的目标路径支持表达式输入                         | 是       |        |
| 创建父级目录 | bool     | 是否创建不存在的父级目录                                 | 否       | true   |
| 覆盖文件     | bool     | 是否覆盖文件。当目标路径已存在同名源文件路径时，若 Overwrite 为 false，则抛错；若 Overwrite 为 true，则覆盖写 | 否       | false  |
| 重命名       | string   | 移动文件的新名称。如果未提供，则保留原始文件名；当目标路径已存在同名源文件路径时，可设置 RenameTo 参数命名新名称解决移动文件同名冲突支持表达式输入 | 否       |        |

![](https://main.qcloudimg.com/raw/0ce16f230d94ac5d0df0367da02f8547/FTP7.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

FTP 移动文件操作，若执行成功则 payload 为空；若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

#### 案例
1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 移动文件操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/947b3b5e92bb46ebb63e704b6c37bde1/FTP-Move1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 FTP 服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。源文件路径设为“/data/ftptest.txt”，目标文件路径设为“/data/movedir”，重命名设为“ftptestmove.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/78e9e6ae191b32732bf9c9d59be7fd07/FTP-Move.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 移动文件操作，若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/2cc48d6536616e2be873ad5fb61f7dab/FTP-Write2.png)
![](https://main.qcloudimg.com/raw/d8cfed4cc4086802dfb2469e341a39fe/FTP-Write3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/7cdb0ff46805fce4551479ac432c1c49/FTP-Write4.png)
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)
:::
::: 目录遍历
#### 输入参数

| 参数                 | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 遍历目录路径         | string   | 要列出的目录的路径支持表达式输入                             | 是       |        |
| 子目录递归轮询       | bool     | 是否递归包含子目录的文件和目录                               | 否       | false  |
| 起始时间             | string   | 在此日期之前创建的文件将被过滤，2020-11-14T08:30:00+00:00支持表达式输入 | 否       |        |
| 截止时间             | string   | 在此日期之后创建的文件将被过滤，2020-11-15T17:30:00+00:00支持表达式输入 | 否       |        |
| 文件名正则匹配       | String   | 使用正则表达式过滤文件或目录名称 [a-z]* 支持表达式输入         | 否       |        |
| 文件路径匹配         | String   | 目录路径过滤匹配模式，只保留指定文件或目录 /mydir/ftptest.txt 支持表达式输入 | 否       |        |
| 目录                 | bool     | 是否过滤目录默认为 true，表示遍历结果中包含目录类型           | 否       | true   |
| 文件                 | bool     | 是否过滤文件默认为 true，表示遍历结果中包含文件类型           | 否       | true   |
| 符号链接             | bool     | 是否过滤符号链接默认为 true，表示遍历结果中包含符号链接类型   | 否       | true   |
| 最小比特值           | int      | 文件 Size 过滤最小值                                           | 否       |        |
| 最大比特值           | int      | 文件 Size 过滤最大值                                           | 否       |        |
| 文件校验时间间隔（秒） | int      | 文件大小校验等待时间（秒），范围：0～60，以判断文件是否可读。在等待时间前后执行两次 sizecheck 文件大小检测，如果两次检测都返回相同的值，即 sizecheck 期间文件没有其他修改操作则可以读取该文件。 | 否       | 0(s)   |
| 时间戳使能           | bool     | 判断是否支持根据文件的修改或创建时间戳来判断触发流，缓存持久化记录上次轮询截止时间戳作为下次轮询起始判断时间。 | 否       | false  |
|时间戳状态标识           | String     |当时间戳使能为 true 时，需设置非空值作为当前流 FTP 组件时间戳状态缓存持久化的唯一识别标志。 | 否       |   |

![](https://main.qcloudimg.com/raw/e6d3d808996b1843d68d3004a65b30d3.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

- FTP 目录遍历操作会在消息 payload 中返回每个文件的属性信息：

| 参数     | 数据类型 | 描述                           |
| -------- | -------- | ------------------------------ |
| Name     | string   | 文件名称                       |
| Type     | string   | 文件类型： File Folder SymLink |
| Target   | string   | SymLink 对应路径                |
| Size     | int      | 文件大小                       |
| Time     | string   | 文件最后修改时间               |
| PathName | string   | 文件绝对路径                   |

![](https://main.qcloudimg.com/raw/7f5c58e178e995550dd8d09ccf4316da/FTP-List3.png)
- FTP 目录遍历操作，若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/e59c6d2bde1b374e0a161043a3a78181/FTP-List5.png)

#### 案例
1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 目录遍历操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/1adda87a32db99d8b9e8cf0e151067f6/FTP-List1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 FTP 服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。遍历目录路径设为“/data”，其他参数输入见下图：
![](https://main.qcloudimg.com/raw/ac786be8f13da5bfe7100ecded2d875b/FTP-List.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制HTTP Listener监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 返回 payload 响应结果如下，即为“/data”目录下遍历文件的属性列表。
![](https://main.qcloudimg.com/raw/06f07c09ab654e4ebf3f166ee1fee8fa/FTP-List2.png)
![](https://main.qcloudimg.com/raw/7f5c58e178e995550dd8d09ccf4316da/FTP-List3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/e2bdabb230c1a8a37b335daf4e043827/FTP-List4.png)
![](https://main.qcloudimg.com/raw/e59c6d2bde1b374e0a161043a3a78181/FTP-List5.png)
:::
::: 目录创建
#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 目录创建路径 | string   | 新创建目录的名称默认支持创建多级目录，当路径已存在时返错支持表达式输入 | 是       |        |

![](https://main.qcloudimg.com/raw/9e1c84c6f01ede55fa2a14fb1000954b/FTP9.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

FTP 目录创建操作，若执行成功则 payload 为空；若执行失败时输出消息 error 中会设置详细返错信息。错误输出为dict类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

#### 案例
1. 在连接器列表中选择 FTP 连接器，然后选择 FTP 目录创建操作。
![](https://main.qcloudimg.com/raw/3f47875db6fdad9083d2de814b7516e7/FTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/3c584305d19ff444e798251b1f4201be/FTP-CreateDir1.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 FTP 服务器对应参数，工作路径设置为 FTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/0152ba7ce05144355c18a37b91ce0341/FTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数，文件路径设为“/data/a/b/c”，参数输入见下图：
![](https://main.qcloudimg.com/raw/1f5ffa89b2fe0de589efca326665e2d4/FTP-CreateDir.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/9fdfb937c0768c045f49bf4df21d75ed/FTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/7558ed97027d252256f804b0670f115c/FTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - FTP 目录创建操作，若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/2cc48d6536616e2be873ad5fb61f7dab/FTP-Write2.png)
![](https://main.qcloudimg.com/raw/d8cfed4cc4086802dfb2469e341a39fe/FTP-Write3.png)
 - 当操作执行失败时，FTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/7cdb0ff46805fce4551479ac432c1c49/FTP-Write4.png)
![](https://main.qcloudimg.com/raw/3858ec4979ae74cca24d28f391d3cf0a/FTP-Write5.png)

:::
</dx-tabs>


