## 操作场景

本文通过一个 demo 进行 PHP 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建 PolarisMesh服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 下载 Github 的 polaris-php 源码：
  - [php-7.x](https://github.com/polarismesh/polaris-php/tree/php-7.x)
  - [php-5.x](https://github.com/polarismesh/polaris-php/tree/php-5.x)
- 下载 Github 的 demo 源码到本地并解压：
  - [php-7.x](https://github.com/polarismesh/polaris-php/tree/php-7.x/examples/quickstart)
  - [php-5.x](https://github.com/polarismesh/polaris-php/tree/php-5.x/examples/quickstart)
- 根据您自身的业务，已准备好业务部署的资源，当前 php 的 quickstart 仅提供虚拟机部署方式。
  - **虚拟机部署**已创建 CVM 虚拟机，请参见 [创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)。CVM 需要安装了 php-5.x 或 php-7.x 的环境。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，PHP 应用访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
5. 修改 demo 中的注册中心地址
 1. 在下载到本地的 [demo 源码](https://github.com/polarismesh/polaris-php/tree/php-7.x) 目录下，分别找到`quickstart/consumer/polaris.yaml`以及`quickstart/provider/polaris.yaml`文件
 - 添加微服务引擎服务治理中心地址到项目配置文件中（这里已`quickstart/consumer/polaris.yaml`为例）。
<dx-codeblock>
:::  yaml
   global:
     serverConnector:
       addresses:
         - 10.0.4.6:8091
:::
</dx-codeblock>
6. 上传 demo 源码以及 polaris-php 插件到 CVM 环境中。
   1. 安装 php 环境以及 php 插件编译开发以来。
<dx-codeblock>
:::  shell
   ## 下载php-5.x版本
   yum -y install --enablerepo=remi --enablerepo=remi-php56 php
   yum -y install --enablerepo=remi --enablerepo=remi-php56 php-devel
   
   ## 下载php-7.x版本
   yum -y install --enablerepo=remi --enablerepo=remi-php74 php
   yum -y install --enablerepo=remi --enablerepo=remi-php74 php-devel
:::
</dx-codeblock>
  - 编译 polaris-php 插件，[构建文档]([polaris-php/HowToBuild_ZH.md at php-5.x · polarismesh/polaris-php (github.com)](https://github.com/polarismesh/polaris-php/blob/php-5.x/doc/HowToBuild_ZH.md))
 - 确认插件安装完成
<dx-codeblock>
:::  shell
   [root@VM-50-33-centos ~]# php -m | grep polaris
   polaris
:::
</dx-codeblock>
 - 分别将`consumer`以及`provider`的 demo 源码上传到不同的 CVM 实例中，这里假定上传的路径均为 /data/polaris/php_examples。
7. 部署 provider 和 consumer 微服务应用，当前仅提供 quickstart 的虚拟机部署方式。
  - **虚拟机部署**部署 provider 和 consumer 微服务应用。
      - 上传 demo 源码至 CVM 实例。
      - 执行启动命令进行启动：
<dx-codeblock>
:::  php
   cd /data/polaris/php_examples/{provider | consumer}

   export PHP_PROVIDER_IP={内网 or 外网IP}

   php [php文件名称]
:::
</dx-codeblock>
8. 确认部署结果
 1. 进入前面提到的微服务治理中心实例页面。
 - 选择**服务管理** > **服务列表**，查看微服务 EchoServerPHP 的实例数量：
    - 若实例数量值不为0，则表示已经成功接入微服务引擎。
    - 若实例数量为0，或者找不到`EchoServerPHP`服务名，则表示微服务应用接入微服务引擎失败。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a74a63d171ff0f47b273b9a13b94ce6e.png)

   

