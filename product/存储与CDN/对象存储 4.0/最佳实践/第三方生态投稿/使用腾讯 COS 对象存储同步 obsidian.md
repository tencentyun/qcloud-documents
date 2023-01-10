## 简介
Obsidian 是一款笔记和知识管理应用程序，由创建 Dynalist 的人设计，Dynalist 是一种流行的在线大纲，也是我最喜欢的工具之一。 他们认为它是“笔记的 IDE”。 它可以让您将一组纯文本文件变成一个丰富的链接思想网络。

Obsidian 的 [数据存储](https://cloud.tencent.com/product/cdcs?from=10680) 在 Markdown 文件的本地文件夹中。 该应用程序强大的链接和反向链接功能将这些单独的文件变成一个知识库，作为您的第二大脑运行。 我最初对应用程序不知所措，直到我发现可以通过插件添加的广泛功能，您真的可以让它成为您自己的。

## 准备工作
下载并安装 [obsidian](https://obsidian.md/)。
创建一个腾讯 COS 存储桶，请详见 [COS 存储桶创建部分](https://cloud.tencent.com/developer/article/write/2069105?from=10680#cos)。

## COS 存储桶创建
1. 登录腾讯云官网，打开 [COS 控制台](https://console.cloud.tencent.com/cos/bucket)。
2. 切换到**存储桶列表**选项卡,单击**创建存储桶**并填写信息。
![](https://qcloudimg.tencent-cloud.cn/raw/18a93af712dc8a649e2bce80b6241f24.png)
![](https://qcloudimg.tencent-cloud.cn/raw/a0400eec797c94d53efc14302d74b937.png)
![](https://qcloudimg.tencent-cloud.cn/raw/aa9a8998536a248a90e59c878606ef16.png)
 为了您的 [数据安全](https://cloud.tencent.com/solution/data_protection?from=10680) 及防止被恶意盗刷而产生高额账单，建议选择**私有读写**访问权限。
3. 存储桶创建完成。
4. Obsidian 插件安装与配置：
 1. 打开 Obsidian 设置。
![](https://qcloudimg.tencent-cloud.cn/raw/7f21749ad531c5d8c5444002b3c40bbf.png)
 2. 找到**第三方插件**选项卡，单击**关闭安全模式**。
 ![](https://qcloudimg.tencent-cloud.cn/raw/9e5f0422116a871bcf52ca4017d74a39.png)
 3. 找到**社区插件市场**，单击**浏览**，搜索、安装并启用 remotely save。
 ![](https://qcloudimg.tencent-cloud.cn/raw/deed7f8f6343fb694c34be4485553063.png)
 4. 配置，单击您刚才创建的 COS 存储桶，切换到概览页面，找到以下信息。 
![](https://qcloudimg.tencent-cloud.cn/raw/d60876034bdf170c03e5d16d1df14841.png) 
5. 接着，创建 [腾讯云密钥](https://console.cloud.tencent.com/cos/bucket)。

得到的 SecretId 即 Access Key ID，SecretKey 即 Secret Access Key， 其他配置根据自己需要设置即可。
****
