EIP 是私有网络内无公网访问能力的云资源访问公网的一种常用方式。本章节介绍云服务器绑定 EIP 访问公网的操作指导，其它云资源操作类似。

## 操作场景
如果您 VPC 中的云服务器资源没有公网 IP，但是需要访问公网进行业务交互，您可以为其绑定 EIP，实现与公网的通信。
![](https://main.qcloudimg.com/raw/e4a8b87e8190044f0993ecef09c96911.png)

## 前提条件
+ 无公网IP的云服务器。
+ 与云服务器同地域的弹性公网IP。

## 操作步骤
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)，并选择地域。
2. 在待绑定实例的EIP右侧操作栏下，选择【更多】>【绑定】。
   ![](https://main.qcloudimg.com/raw/8773d86148c76b7e6c83c89fb687407a.png)
3. 在弹出的“绑定资源”窗口中，单击【CVM实例】，并选择待绑定的 CVM 实例，然后单击【确定】。
   ![](https://main.qcloudimg.com/raw/a900c27076f3b81515c0ce5f62f67b57.png)
   绑定 EIP 的 CVM 如图所示。
   ![](https://main.qcloudimg.com/raw/6e6664b6a2fb8faa72347e311422849f.png)

## 结果验证
1. 登录云服务器。
2. 测试公网连通性，例如执行`ping www.qq.com`，可看到有数据返回，表示该 CVM 可以访问公网。
   ![](https://main.qcloudimg.com/raw/40c8b66f305baac0a63858394ed88766.png)
