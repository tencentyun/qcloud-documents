## 操作场景

本文通过一个demo进行 PHP 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心]()。
- 下载github的polaris-php源码
  - [php-7.x](https://github.com/polarismesh/polaris-php/tree/php-7.x)
  - [php-5.x](https://github.com/polarismesh/polaris-php/tree/php-5.x)
- 下载github的demo源码到本地并解压
  - [php-7.x](https://github.com/polarismesh/polaris-php/tree/php-7.x/examples/quickstart)
  - [php-5.x](https://github.com/polarismesh/polaris-php/tree/php-5.x/examples/quickstart)
- 【php环境安装】CVM需要安装了php-5.x或php-7.x的环境
- 根据您自身的业务，已准备好业务部署的资源，虚拟机部署和容器化部署选择其中一种方式即可。
  - 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。

2. 在**治理中心**下的 **polarismesh** 页面，点击页面上方下拉列表，选择目标地域：![region_icon](https://qcloudimg.tencent-cloud.cn/raw/b5153fa452844ee19e24436e11b2376e.png)

3. 单击目标引擎的“ID”，进入基本信息页面。

4. 查看访问地址，PHP应用访问使用gRPC端口（8091）：
    ![access](https://qcloudimg.tencent-cloud.cn/raw/561460943b0404c44c29d2c0dd09c56f.png)
    
5. 修改demo中的注册中心地址
- 在下载到本地的[demo源码](https://github.com/polarismesh/polaris-php/tree/php-7.x)目录下，分别找到“quickstart/consumer/polaris.yaml”以及“quickstart/provider/polaris.yaml”文件
- 添加微服务引擎服务治理中心地址到项目配置文件中（这里已“quickstart/consumer/polaris.yaml”为例）。
  
   ```yaml
   global:
     serverConnector:
     	# 治理中心地址，当前php sdk支持的gRPC协议，因此要使用8091端口
       addresses:
         - 192.168.100.9:8091
   ```
6. 上传demo源码以及polaris-php插件到CVM环境中。

- 安装php环境以及php插件编译开发以来

   ```shell
   ## 下载php-5.x版本
   yum -y install --enablerepo=remi --enablerepo=remi-php56 php
   yum -y install --enablerepo=remi --enablerepo=remi-php56 php-devel
   
   ## 下载php-7.x版本
   yum -y install --enablerepo=remi --enablerepo=remi-php74 php
   yum -y install --enablerepo=remi --enablerepo=remi-php74 php-devel
   ```

- 编译polaris-php插件，[构建文档]([polaris-php/HowToBuild_ZH.md at php-5.x · polarismesh/polaris-php (github.com)](https://github.com/polarismesh/polaris-php/blob/php-5.x/doc/HowToBuild_ZH.md))

- 确认插件安装完成

   ```shell
   [root@VM-50-33-centos ~]# php -m | grep polaris
   polaris
   ```

- 分别将`consumer`以及`provider`的demo源码上传到不同的CVM实例中，这里假定上传的路径均为/data/polaris/php_examples

7. 部署provider和consumer微服务应用，当前仅提供quickstart的虚拟机部署方式。

   （1）【虚拟机部署】部署provider和consumer微服务应用。

      - 上传demo源码至 CVM 实例。

      - 执行启动命令进行启动：

      ```
   cd /data/polaris/php_examples/{provider | consumer}

   export PHP_PROVIDER_IP={内网 or 外网IP}

   php [php文件名称]
      ```

8. 确认部署结果
- 进入前面提到的微服务治理中心实例页面。
- 选择“服务管理 > 服务列表”，查看微服务EchoServerPHP的实例数量：
- 若实例数量值不为0，则表示已经成功接入微服务引擎。
- 若实例数量为0，或者找不到`EchoServerPHP`服务名，则表示微服务应用接入微服务引擎失败。

   ![](https://qcloudimg.tencent-cloud.cn/raw/a74a63d171ff0f47b273b9a13b94ce6e.png)

   

