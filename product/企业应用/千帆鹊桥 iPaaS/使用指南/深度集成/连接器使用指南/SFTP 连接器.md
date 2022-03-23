

## 简介
- SSH 文件传输协议（SSH File Transfer Protocol，也称 Secret File Transfer Protocol 即安全文件传送协议）是一 [数据流](https://baike.baidu.com/item/数据流) 连接，提供文件访问、传输和管理功能的 [网络传输协议](https://baike.baidu.com/item/网络传输协议)。
- SSH（Secure Shell）：安全外壳协议 ，由 IETF 的网络小组（Network Working Group）所制定；SSH 为建立在应用层基础上的安全协议。SSH 是目前较可靠，专为远程登录会话和其他网络服务提供安全性的协议。利用 SSH 协议可以有效防止远程管理过程中的信息泄露问题。
- SFTP 与 FTP 有着几乎一样的语法和功能。SFTP 为 SSH 的其中一部分，是一种传输档案至 Blogger 伺服器的安全方式。其实在 SSH 软件包中，已经包含一个叫作 SFTP 的安全文件信息传输子系统，SFTP 本身没有单独的守护进程，它必须使用 sshd 守护进程（端口号默认是22）来完成相应的连接和答复操作，所以从某种意义上来说，SFTP 并不像一个服务器程序，而更像是一个客户端程序。
- SFTP 与 FTP 的主要区别：
 - 链接方式：FTP 使用 TCP 端口21上的控制连接建立连接，而 SFTP 是在客户端和服务器之间通过 SSH 协议（TCP 端口22）建立的安全连接来传输文件。
 - 安全性：SFTP 使用加密传输认证信息和传输的数据，所以使用 SFTP 相对于 FTP 是非常安全。
 - 效率：SFTP 传输方式使用加密解密技术，所以传输效率比普通的 FTP 要低得多。
 - SFTP（SFTP Connector）提供对 SFTP 服务器上的文件和文件夹的访问。SFTP 连接器操作通过 SFTP（安全文件传输协议）协议管理文件传输。连接器的主要特点包括：
   - 根据需要读取文件或列出目录内容。
   - 支持常见的 SFTP 操作，如创建目录、复制、移动、重命名、删除文件。
   - 支持锁定文件。
   - 文件匹配功能。

## 连接器配置

### 通用配置

| 参数                    | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ----------------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 域名                    | string   | SFTP 服务器域名                                              | 是       |        |
| 端口号                  | int      | SFTP 服务器端口号                                            | 否       | 22     |
| 用户名                  | string   | SFTP 服务器的用户名。如果服务器需要身份验证，则为必需参数  | 否       |        |
| 密码                    | string   | SFTP 服务器的密码。如果服务器需要身份验证，则为必需参数    | 否       |        |
| 工作路径                | string   | 指定为此连接器所使用的每个相对路径的根目录。如果未提供，则默认为远程服务器默认值 | 否       | /      |
| SSH 公钥认证             | bool     | 是否开启 SSH 公钥认证                                          | 否       | false  |
| 私钥认证文件            | string   | 私钥认证文件                                                 | 否       |        |
| 认证文件密码            | string   | 私钥认证文件密码。如果没有提供标识文件 Identity File，参数将被忽略 | 否       |        |
| KNOWN_HOSTS 密钥验证     | bool     | 是否开启 knownHosts 密钥验证                                   | 否       | false  |
| KNOWN_HOSTS 密钥验证文件 | string   | 如果已提供，客户机将根据引用文件中的 knownHosts 密钥验证服务器的密钥。如果服务器密钥与文件中的密钥不匹配，连接将被中止 | 否       |        |

### 高级配置

| 参数             | 数据类型 | 描述                                          | 是否必填 | 默认值 |
| ---------------- | -------- | --------------------------------------------- | -------- | ------ |
| 代理域名         | string   | 代理服务器域名                                | 否       |        |
| 代理端口号       | int      | 代理服务器端口号                              | 否       |        |
| 代理用户名       | string   | 代理服务器用户名                              | 否       |        |
| 代理密码         | string   | 代理服务器密码                                | 否       |        |
| 代理协议         | enum     | 代理服务器协议：HTTP、SOCKS4、SOCKS5          | 否       |        |
| 重连接频率（秒） | int      | 重连接频率（单位s）（范围：0～300）           | 否       | 10（s）  |
| 连接超时时间（秒） | int      | 连接超时等待时间（单位s）（范围：0～300）     | 否       | 60（s） |
| 响应超时时间（秒） | int      | 请求响应超时等待时间（单位s）（范围：0～300） | 否       | 60（s） |

**连接器配置界面如下：**
![](https://main.qcloudimg.com/raw/e8d7b67f9c5ae66612741909ed23aafb/SFTP1.png)

## 操作配置
<dx-tabs>
::: 读取文件
#### 输入参数

| 参数                 | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 文件路径             | string   | 读文件路径                                                   | 是       |        |
| 文件锁               | bool     | 是否开启文件锁                                               | 否       | false  |
| l文件锁等待时间（秒）  | int      | 文件锁等待时间（秒）（范围：0～60）                            | 否       | 30（s） |
| 文件校验时间间隔（秒） | int      | 文件大小校验等待时间（秒） ，以判断文件是否可读。在等待时间前后执行两次 sizecheck 文件大小检测。如果两次检测都返回相同的值，即 sizecheck 期间文件没有其他修改操作则可以读取该文件（范围：0～60） | 否       | 0（s）  |

![](https://main.qcloudimg.com/raw/c48a4a97347ef161633cc8d968ddbdde/SFTP2.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 Entity 类型；执行失败后，payload 为空     |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

- SFTP 读取文件操作会返回文件内容，根据文件名后缀设置消息的 mimeType 和 encoding 并放到消息 payload 中，后续可通过 dataway 表达式直接访问。
![](https://main.qcloudimg.com/raw/07f7f9a1c1dc738b9f52df0e3d9b57f3/SFTP-Read3.png)
- SFTP 读取文件操作若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/bbb008520ecbdcb1610ad9326da6ca8a/SFTP-Read5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 读取文件操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 SFTP 服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图:
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件路径设为“/data/sftptest.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/d6415e40409100a733fa06a103f2fdc3/SFTP-Read.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 返回 payload 响应结果如下，即为“/data/sftptest.txt”文件内容。
![](https://main.qcloudimg.com/raw/d6c4cd4dab7a301932e086e5be3b3ac9/SFTP-Read2.png)
![](https://main.qcloudimg.com/raw/07f7f9a1c1dc738b9f52df0e3d9b57f3/SFTP-Read3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/3ddeb37817fd3242d3fbc36f07f6fd9a/SFTP-Read4.png)
![](https://main.qcloudimg.com/raw/bbb008520ecbdcb1610ad9326da6ca8a/SFTP-Read5.png)
:::
::: 写文件
#### 输入参数

| 参数               | 数据类型                             | 描述                                                         | 是否必填 | 默认值     |
| ------------------ | ------------------------------------ | ------------------------------------------------------------ | -------- | ---------- |
| 文件路径           | string                               | 待写入文件路径（当检测为目录时抛错）支持表达式输入           | 是       |            |
| 文件内容           | string                               | 待写入文件的内容。默认为当前消息 payload 支持表达式输入        | 否       | #[payload] |
| 创建父级目录       | bool                                 | 是否尝试创建任何不存在的父目录                               | 否       | true       |
| 文件锁             | bool                                 | 是否锁定文件                                               | 否       | false      |
| 文件锁等待时间（秒） | int                                  | 文件锁等待时间（秒）（范围：0～60）                            | 否       | 30（s）   |
| 文件写模式         | enum: OVERWRITE 、APPEND、CREATE_NEW | 文件写模式<br><li>OVERWRITE：覆盖写<br><li>APPEND：追加写<br><li>CREATE_NEW：当文件不存在时新建，否则抛错 | 否       | OVERWRITE  |

![](https://main.qcloudimg.com/raw/95db62b65d96f5efdb9e20c446c27543/SFTP3.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

SFTP 写文件操作，若执行成功则 payload 为空；若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 写文件操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 SFTP 服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件路径设为“/data/sftptest.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/4c65bb755931088bbf9f26a27900dc91/SFTP-Write.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 写文件操作若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/3f15b4ebdcbe8f665661d9b8bd3f72d5/SFTP-Write2.png)
![](https://main.qcloudimg.com/raw/9bd8187d78e47eed6ccf68f3063833e9/SFTP-Write3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/afb5f2696505ae4e55674b6e1651df9a/SFTP-Write4.png)
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)
:::
::: 删除文件
#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 文件删除路径 | string   | 待删除的文件或路径：<br><li>当文件或路径不存在时抛错<br><li>支持删除单个文件以及目录（包括目录下所有文件）<br><li>如果文件没有被锁定，则删除路径指向的文件，支持表达式输入 | 是       |        |

![](https://main.qcloudimg.com/raw/d8022c887d81acbe12536912001a6a59/SFTP4.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

SFTP 删除文件操作若执行成功 payload 为空，若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 删除文件操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 SFTP 服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件删除路径设为“/data/sftptest.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/2c150e0dd64aeb1fd9fed83b237632da/SFTP-Delete.png)
4. 操作配置参数设置完成后保存返回即可，单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 删除文件操作若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/3f15b4ebdcbe8f665661d9b8bd3f72d5/SFTP-Write2.png)
![](https://main.qcloudimg.com/raw/9bd8187d78e47eed6ccf68f3063833e9/SFTP-Write3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/afb5f2696505ae4e55674b6e1651df9a/SFTP-Write4.png)
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)
:::
::: 复制文件
#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 源文件路径   | string   | 要复制文件的源路径支持复制单个文件和目录（包括目录下所有文件）支持表达式输入 | 是       |        |
| 目标文件路径 | string   | 文件要复制到的目标路径支持表达式输入                         | 是       |        |
| 创建父级目录 | bool     | 是否创建不存在的父级目录                                     | 否       | true   |
| 覆盖文件     | bool     | 是否覆盖文件，当目标路径已存在同名源文件路径时，若 Overwrite 为 false 则抛错，若 Overwrite 为 true 则覆盖写 | 否       | false  |
| 重命名       | string   | 复制文件的新名称，如果未提供，则保留原始文件名。当目标路径已存在同名源文件路径时，可设置 RenameTo 参数命名新名称解决复制文件同名冲突支持表达式输入 | 否       |        |

![](https://main.qcloudimg.com/raw/d5d17c2517f6c2d44d3a480b3cbc71e6/SFTP5.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

SFTP 复制文件操作若执行成功 payload 为空，若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 复制文件操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 SFTP 服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。源文件路径设为“/data/sftptest.txt”，目标文件路径设为“/data/copydir”，重命名设为“sftptestcopy.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/b882d2c30bdd7025c3540899adbe1348/SFTP-Copy.png)
4. 操作配置参数设置完成后保存返回即可，单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 复制文件操作若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/3f15b4ebdcbe8f665661d9b8bd3f72d5/SFTP-Write2.png)
![](https://main.qcloudimg.com/raw/9bd8187d78e47eed6ccf68f3063833e9/SFTP-Write3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/afb5f2696505ae4e55674b6e1651df9a/SFTP-Write4.png)
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)

:::
::: 重命名文件
#### 输入参数 

| 参数       | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ---------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 文件路径   | string   | 待重命名的文件路径：<br><li>当路径或文件不存在时报错<br><li>同时支持目录和文件重命名,支持表达式输入 | 是       |        |
| 重命名名称 | string   | 文件或路径的新名称,支持表达式输入                             | 是       |        |
| 覆盖文件   | bool     | 是否覆盖文件：<br><li>当 Overwrite 为 false 时，若重命名文件路径已存在则抛错<br><li>当 Overwrite 为 true 时则直接覆盖写 | 否       | false  |

![](https://main.qcloudimg.com/raw/3f8e1c064c19b44e6725bb8a01c0eb62/SFTP6.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

SFTP 重命名文件操作若执行成功则 payload 为空，若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 重命名文件操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 SFTP 服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件路径设为“/data/sftptest.txt”，重命名名称设为“sftptestrename.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/3e0a65300163cb8d8b801c08b15009df/SFTP-Rename.png)
4. 操作配置参数设置完成后保存返回即可，单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 重命名文件操作若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/3f15b4ebdcbe8f665661d9b8bd3f72d5/SFTP-Write2.png)
![](https://main.qcloudimg.com/raw/9bd8187d78e47eed6ccf68f3063833e9/SFTP-Write3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/afb5f2696505ae4e55674b6e1651df9a/SFTP-Write4.png)
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)
:::
::: 移动文件
#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 源文件路径   | string   | 要转移的文件或目录路径支持移动单个文件和目录（包括目录下所有文件）支持表达式输入 | 是       |        |
| 目标文件路径 | string   | 文件要移动到的目标路径支持表达式输入                         | 是       |        |
| 创建父级目录 | bool     | 是否创建不存在的父级目录。                                   | 否       | true   |
| 覆盖文件     | bool     | 是否覆盖文件，当目标路径已存在同名源文件路径时，若 Overwrite 为 false 则抛错，若 Overwrite 为 true 则覆盖写 | 否       | false  |
| 重命名       | string   | 移动文件的新名称，如果未提供，则保留原始文件名。当目标路径已存在同名源文件路径时，可设置 RenameTo 参数命名新名称解决移动文件同名冲突，支持表达式输入 | 否       |        |

![](https://main.qcloudimg.com/raw/a9bd8335c7e7d921242e50609757b2f2/SFTP7.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

SFTP 移动文件操作若执行成功 payload 为空，若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 移动文件操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 SFTP 服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。源文件路径设为“/data/sftptest.txt”，目标文件路径设为“/data/movedir”，重命名设为“sftptestmove.txt”，参数输入见下图：
![](https://main.qcloudimg.com/raw/0992064a7fa9312fa458f5765069050f/SFTP-Move.png)
4. 操作配置参数设置完成后保存返回即可，单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 移动文件操作若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/3f15b4ebdcbe8f665661d9b8bd3f72d5/SFTP-Write2.png)
![](https://main.qcloudimg.com/raw/9bd8187d78e47eed6ccf68f3063833e9/SFTP-Write3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/afb5f2696505ae4e55674b6e1651df9a/SFTP-Write4.png)
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)
:::
::: 目录遍历
#### 输入参数

| 参数                 | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 遍历目录路径         | string   | 要列出的目录的路径支持表达式输入                             | 是       |        |
| 子目录递归轮询       | bool     | 是否递归包含子目录的文件和目录                               | 否       | false  |
| 起始时间             | string   | 在此日期之前创建的文件将被过滤。2020-11-14T08:30:00+00:00支持表达式输入 | 否       |        |
| 截止时间             | string   | 在此日期之后创建的文件将被过滤。 2020-11-15T17:30:00+00:00支持表达式输入 | 否       |        |
| 文件名正则匹配       | String   | 使用正则表达式过滤文件或目录名称 [a-z]* 支持表达式输入         | 否       |        |
| 文件路径匹配         | String   | 目录路径过滤匹配模式，只保留指定文件或目录 /mydir/ftptest.txt，支持表达式输入 | 否       |        |
| 目录                 | bool     | 是否过滤目录默认为 true，表示遍历结果中包含目录类型           | 否       | true   |
| 文件                 | bool     | 是否过滤文件默认为 true，表示遍历结果中包含文件类型           | 否       | true   |
| 符号链接             | bool     | 是否过滤符号链接默认为 true，表示遍历结果中包含符号链接类型   | 否       | true   |
| 最小比特值           | int      | 文件 Size 过滤最小值                                           | 否       |        |
| 最大比特值           | int      | 文件 Size 过滤最大值                                           | 否       |        |
| 文件校验时间间隔(秒) | int      | 文件大小校验等待时间（秒），以判断文件是否可读。在等待时间前后执行两次 sizecheck 文件大小检测。如果两次检测都返回相同的值，即 sizecheck 期间文件没有其他修改操作则可以读取该文件。（范围：0～60） | 否       | 0（s）  |
| 时间戳使能           | bool     | 判断是否支持根据文件的修改或创建时间戳来判断触发流，缓存持久化记录上次轮询截止时间戳作为下次轮询起始判断时间。 | 否       | false  |
| 时间戳状态标识          | String    | 当时间戳使能为 true 时，需设置非空值作为当前流 SFTP 组件时间戳状态缓存持久化的唯一识别标志。 | 否       |  |

![](https://main.qcloudimg.com/raw/0e9e92d814da2bc7d377445abf171a24.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

**SFTP 目录遍历操作会在消息 payload 中返回每个文件的属性信息：**

| 参数     | 数据类型 | 描述                           |
| -------- | -------- | ------------------------------ |
| Name     | string   | 文件名称                       |
| Type     | string   | 文件类型： File Folder SymLink |
| Target   | string   | SymLink 对应路径                |
| Size     | int      | 文件大小                       |
| Time     | string   | 文件最后修改时间               |
| PathName | string   | 文件绝对路径                   |

![](https://main.qcloudimg.com/raw/eb3ba0b1c5c54f8ee56192fb83b65c74/SFTP-List3.png)
SFTP 目录遍历操作若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/88f3c34b0622565ed709fdac93c3bafd/SFTP-List5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 目录遍历操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的 SFTP 服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。遍历目录路径设为“/data”，其他参数输入见下图：
![](https://main.qcloudimg.com/raw/d67552c581e4030c1489d830c859ae35/SFTP-List.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 返回 payload 响应结果如下，即为“/data”目录下遍历文件的属性列表。
![](https://main.qcloudimg.com/raw/584cd6dc401f32918069cef2812c413d/SFTP-List2.png)
![](https://main.qcloudimg.com/raw/eb3ba0b1c5c54f8ee56192fb83b65c74/SFTP-List3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/df89b4cc0e10c9cbfd3fd50bd8f81378/SFTP-List4.png)
![](https://main.qcloudimg.com/raw/88f3c34b0622565ed709fdac93c3bafd/SFTP-List5.png)

:::
::: 目录创建

#### 输入参数

| 参数         | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 目录创建路径 | string   | 新创建目录的名称默认支持创建多级目录，当路径已存在时返错支持表达式输入 | 是       |        |

![](https://main.qcloudimg.com/raw/d07f18146ab670ec6d40b545805d795b/SFTP9.png)

#### 输出

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功或失败，payload 均为空                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

SFTP 目录创建操作若执行成功 payload 为空，若执行失败时输出消息 error 中会设置详细返错信息。错误输出为 dict 类型，包含“Code”和“Description”元素，“Code”表示错误类型，“Description”表示错误具体信息，例如：
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)

#### 案例
1. 在连接器列表中选择 SFTP 连接器，然后选择 SFTP 目录创建操作。
![](https://main.qcloudimg.com/raw/46e1bcd295b69f35bb72ce8018994f28/SFTP%E7%BB%84%E4%BB%B6%E9%80%89%E6%8B%A9.png)
![](https://main.qcloudimg.com/raw/bc86011ea5e668863ab8d2e513fab075/SFTP%E9%80%89%E6%8B%A9%E6%93%8D%E4%BD%9C.png)
2. 输入连接器配置参数，其中域名、端口、用户名和密码设置为待连接的SFTP服务器对应参数，工作路径设置为 SFTP 服务器下文件处理的相对路径，默认为根路径“/”，其他参数保持默认值即可。参数填写完后可单击下方**测试连接**校验连接配置参数有效性。具体如下图：
![](https://main.qcloudimg.com/raw/1637256729a45ea904246dc08ab56c45/SFTP%E8%BF%9E%E6%8E%A5%E5%99%A8%E9%85%8D%E7%BD%AE.png)
3. 确认连接器配置参数填写无误后单击**保存**，然后设置操作配置参数。文件路径设为“/data/a/b/c”，参数输入见下图：
![](https://main.qcloudimg.com/raw/2770b6100b4083edd4df7a9c7634ed8b/SFTP-CreateDir.png)
4. 操作配置参数设置完成后保存返回即可，然后单击右上角**发布**，选择发布地域后单击**确定**。
![](https://main.qcloudimg.com/raw/e4eb65a1fae7ea6666fc18e86ce401ba/SFTP%E5%8F%91%E5%B8%83%E6%B5%81.png)
5. 待集成流发布成功后复制 HTTP Listener 监听路径后访问该域名即可触发流。
![](https://main.qcloudimg.com/raw/254ef6641c1fdf46fc136f4b153f546a/SFTP%E7%9B%91%E5%90%AC%E5%9F%9F%E5%90%8D.png)
 - SFTP 目录创建操作若执行成功则返回 payload 响应结果为空。
![](https://main.qcloudimg.com/raw/3f15b4ebdcbe8f665661d9b8bd3f72d5/SFTP-Write2.png)
![](https://main.qcloudimg.com/raw/9bd8187d78e47eed6ccf68f3063833e9/SFTP-Write3.png)
 - 当操作执行失败时，SFTP 输出消息 error 中会设置详细返错信息。
![](https://main.qcloudimg.com/raw/afb5f2696505ae4e55674b6e1651df9a/SFTP-Write4.png)
![](https://main.qcloudimg.com/raw/bbe154fd5f28416dcde484b0ff33ae02/SFTP-Write5.png)
:::
</dx-tabs>





