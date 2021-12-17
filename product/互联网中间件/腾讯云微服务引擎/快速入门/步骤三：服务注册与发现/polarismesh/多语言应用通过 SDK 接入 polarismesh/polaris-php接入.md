# Polaris-PHP服务应用接入

本文通过一个demo进行 PHP 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心]()。
- 下载github的polaris-php源码
  - [php-7.x](https://github.com/polarismesh/polaris-php/tree/php-7.x)
  - [php-5.x](https://github.com/polarismesh/polaris-php/tree/php-5.x)
- 下载github的demo源码到本地并解压
  - [php-7.x](https://github.com/polarismesh/polaris-php/tree/php-7.x/examples/quickstart)
  - [php-5.x](https://github.com/polarismesh/polaris-php/tree/php-5.x/examples/quickstart)
- 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)
- 【php环境安装】CVM需要安装了php-5.x或php-7.x的环境

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。

2. 在**治理中心**下的 **polarismesh** 页面，点击页面上方下拉列表，选择目标地域：![region_icon](https://qcloudimg.tencent-cloud.cn/raw/b5153fa452844ee19e24436e11b2376e.png)

3. 单击目标引擎的“ID”，进入基本信息页面。

4. 查看访问地址，PHP应用访问使用gRPC端口（8091）：
    ![access](https://qcloudimg.tencent-cloud.cn/raw/561460943b0404c44c29d2c0dd09c56f.png)
    
5. 修改demo中的注册中心地址
- 在下载到本地的demo源码目录下，分别找到`quickstart/consumer/polaris.yaml`以及`quickstart/provider/polaris.yaml`文件
- 添加polarismesh治理中心的地址到项目的配置文件中（这里已`quickstart/consumer/polaris.yaml`为例）。
  
   ```yaml
   global:
     serverConnector:
     	# 治理中心地址，当前php sdk支持的gRPC协议，因此要使用8091端口
       addresses:
         - 192.168.100.9:8091
   ```
6. 上传demo源码以及`polaris-php`插件到CVM环境中。

- 安装`php`环境以及`php`插件编译开发以来

   ```shell
   ## 下载php-5.x版本
   yum -y install --enablerepo=remi --enablerepo=remi-php56 php
   yum -y install --enablerepo=remi --enablerepo=remi-php56 php-devel
   
   ## 下载php-7.x版本
   yum -y install --enablerepo=remi --enablerepo=remi-php74 php
   yum -y install --enablerepo=remi --enablerepo=remi-php74 php-devel
   ```

- 编译`polaris-php`插件，[构建文档]([polaris-php/HowToBuild_ZH.md at php-5.x · polarismesh/polaris-php (github.com)](https://github.com/polarismesh/polaris-php/blob/php-5.x/doc/HowToBuild_ZH.md))

- 确认插件安装完成

   ```shell
   [root@VM-50-33-centos ~]# php -m | grep polaris
   polaris
   ```

- 分别将`consumer`以及`provider`的demo源码上传到不同的CVM实例中，这里假定上传的路径均为`/data/polaris/php_examples`

7. 【虚拟机部署】部署provider和consumer微服务。

- 运行`provider`

   ```shell
   # 进入provider目录
   cd /data/polaris/php_examples/provider
   # 设置Provider的IP信息
   export PHP_PROVIDER_IP={内网 or 外网IP}
   # 运行 provider
   php provider.php
   ```

- 运行`consumer`

   ```shell
   # 进入consumer目录
   cd /data/polaris/php_examples/consumer
   # 运行 consumer
   php consumer.php
   
   # 确认是否收到输出
   [root@VM-50-33-centos ~/Github/polaris-php/examples/quickstart/consumer]# php consumer.php 
   Attempting to connect to '10.0.50.33' on port '9996'...Connect success. 
   Client send success 
   Reading response:
   hello. I`m provider
   ```

8. 确认部署结果
- 进入微服务引擎控制台，选择前提条件中创建的polarismesh治理中心实例
- 选择`服务管理` > `服务列表`，查看服务`EchoServerPHP`的实例数量
- 若实例数量值不为0，则表示已经成功接入微服务引擎
- 若实例数量为0，或者找不到`EchoServerPHP`服务名，则表示微服务应用接入微服务引擎失败。

   ![](https://qcloudimg.tencent-cloud.cn/raw/679fa9f05664606803c018182c52b697.png)

   

