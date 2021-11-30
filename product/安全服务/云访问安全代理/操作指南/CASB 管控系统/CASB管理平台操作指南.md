本文档将以一个 Java 工程为例为您介绍如何进行敏感信息加密，并指导您如何使用 CASB 管理平台的主要功能。
## 背景信息

CASB 管理系统以免改造的方式，实现云环境下应用中结构化数据（包括实时数据和历史数据）的存储加密，提供多种加解密策略，为公有云提供方便快捷易于部署的数据安全解决方案。

### 拓扑结构
![](https://main.qcloudimg.com/raw/e43e546f840341ce43fca97a095bed51.png)

### 系统组成

CASB 管理系统由 CASB Plugin、CASB Client、CASB 管理平台组成。

- CASB Plugin：数据安全插件，提供数据加密使用的密码算法，用于实时数据加解密。
- CASB Client：客户端管理工具，是数据安全工具套件。由 Extractor 和 Processor 组成，Extractor 用于提取数据库表结构，Processor 用于数据库数据的全量加密和解密。
- CASB 管理平台：提供可视化的管理控制台，提供鉴权、权限管理、数据源管理、加解密策略管理等功能。


## 前提条件
需已通过 CASB [内测申请](https://cloud.tencent.com/apply/p/2vnlem5njlz)，并已 [购买 CASB 实例](https://cloud.tencent.com/document/product/1303/48148)。
<span id="done"></span>

<span id="test"></span>
## 准备测试环境
### 步骤1：提供测试 Demo 应用

[下载 Demo 应用](https://casb-1300274530.cos.ap-guangzhou.myqcloud.com/demo.zip)，将获取的 Demo 应用传到服务器上，并解压到任意目录。

### 步骤2：创建 Demo 应用的数据库和数据
在 mysql5.7 数据库下执行如下操作：

```mysql
-- ----------------------------
-- 创建数据库
-- ----------------------------
CREATE DATABASE casb_test DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ----------------------------
-- 创建部门表
-- ----------------------------
CREATE TABLE `department`  (
  `id` 		int(11) NOT NULL AUTO_INCREMENT COMMENT '部门id',
  `name` 	varchar(255) NOT NULL COMMENT '部门名称',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB COMMENT = '部门表';

-- ----------------------------
-- 创建用户表
-- ----------------------------
CREATE TABLE `user`  (
  `user_id`             varchar(31) NOT NULL COMMENT '用户id',
  `user_name`           varchar(20) NOT NULL COMMENT '用户姓名',
  `user_sex`            int(1) NOT NULL DEFAULT 1 COMMENT '用户性别，1男2女',
  `user_age`            int(4) NULL DEFAULT NULL COMMENT '用户年龄',
  `user_birthday`       datetime(0) NULL DEFAULT NULL COMMENT '用户生日',
  `user_department`     int(11) NULL DEFAULT NULL COMMENT '部门id',
  `created_time`        datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `created_by`          varchar(31) NULL DEFAULT NULL COMMENT '创建人id',
  `update_time`         datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  `update_by`           varchar(31) NULL DEFAULT NULL COMMENT '更新人id',
  `version`             int(11) UNSIGNED ZEROFILL NOT NULL DEFAULT 00000000000 COMMENT '乐观锁',
  `deleted`             int(1) UNSIGNED ZEROFILL NOT NULL DEFAULT 0 COMMENT '逻辑删除，1已删除0未删除',
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB COMMENT = '用户表';

-- ----------------------------
-- 向部门表中写入测试数据
-- ----------------------------
INSERT INTO `department` VALUES (1, '技术部');
INSERT INTO `department` VALUES (2, '业务部');
INSERT INTO `department` VALUES (3, '财务部');
INSERT INTO `department` VALUES (4, '人事部');
INSERT INTO `department` VALUES (5, '行政部');

-- ---------------------------- 
-- 向要用户表中写入
-- ---------------------------- 
INSERT INTO `user` VALUES ('1288078496635195392', 'test123', 1, 22, '2020-07-21 00:00:00', 2, '2020-07-28 12:31:08', NULL, '2020-07-28 12:31:08', NULL, 00000000000, 0);
INSERT INTO `user` VALUES ('1288078561810485248', '1234test', 2, 25, '2020-07-25 00:00:00', 1, '2020-07-28 12:31:08', NULL, '2020-07-28 12:31:08', NULL, 00000000000, 0);
```

### 步骤3：加密字段扩容

数据加密后，密文数据膨胀，在实施数据加密前需要着重考虑。加密数据中需要保存原始的数据、校验信息以及一些额外的信息，加密后密文数据长度的计算公式为： length = ceil((len * 3 + 34) / 3) * 4 + 3。
其中：
- len 为明文数据长度。
>?数据是中文的时，len乘以3，数据是英文时，len 不变。
- ceil() 为向上取整
- length 为计算得到的密文长度

>?在本次示例中，用户表中的`user_name`作为敏感信息进行加密。根据计算公式，我们需要将`user_name`的字段长度由原来的20个字符长度增加到129个字符长度。

## 数据库加密
### 步骤1：登录 CASB 管理平台

1. 打开浏览器，输入`https://IP`（其中 IP 为 CASB 管理平台地址），进入登录页面。
2. 输入账户名 admin 以及在 [CASB 控制台](https://console.cloud.tencent.com/casb) 设置的密码，单击【登录】，即可登录 CASB 管理平台。
![](https://main.qcloudimg.com/raw/a78170e0637145171de2b3853c740f45.png)

### 步骤2：下载安装客户端工具

1. 在 CASB 管理平台的右上角，单击【下载客户端工具】，下载客户端工具。
![](https://main.qcloudimg.com/raw/282a1b92f3cc172c06fefda266805d92.png)
2. 将下载后客户端工具 zip 包，上传到数据库 Linux 服务器或可以连接到数据库的 Liunx 服务器上的任意目录下，以 root 用户执行以下安装命令：
```shell
# 切换root用户
~$ su root
# 解压压缩包，视包名有所不同
~$ unzip AOEClient-V1.1.13-1598319153736.zip
# 进入解压后AOE目录，视具体目录名有所不同
~$ cd AOEClient-V1.1.13-1598319153736_300
# 给安装脚本加上执行权限
~$ chmod u+x aoe-client.sh
# 执行安装,后面的参数 /opt/client 是安装位置，安装目录可以根据自己的需要填写
$ sh aoe-client.sh  /opt/client/
# 加载环境变量
$ source /etc/profile
```

### 步骤3：提取数据库表结构并新增数据源
1. 进入客户端安装目录下，执行如下命令提取数据库表结构：
```shell
# 进入客户端安装目录下，安装目录以实际安装的目录为准
$ cd  /opt/client/extractor
# 如下jar包名称根据实际安装后的jar包名称为准，数据库名称，ip，用户名，密码以实际为准
# 验证数据库连接
[root@localhost extractor]# java -jar extractor-1.1.6.jar --op=verify --db-type=mysql --host=192.168.10.130 
--port=3306 --user=root --password=hellocasb --database=ceshi
# 如下是提取过程中打印的日志，可做参考
--op=verify
--db-type=mysql
--host=192.168.10.130 
--port=3306
--user=root
--password=hellocasb
--database=ceshi
user.dir=/opt/casb_client/extractor
cg-casb.properties loaded from /opt/casb_client/extractor/cg-casb.properties
Tue Sep 15 16:18:00 CST 2020 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
[2020-09-15 16:18:01] success
# 提取表结构
[root@localhost extractor]# java -jar extractor-1.1.6-release.jar --op=extract --db-type=mysql --host=192.168.10.130 --port=3306 --user=root --password=hellocasb 
# 如下是提取过程中打印的日志，可做参考
--op=extract
--db-type=mysql
--host=192.168.10.130
--port=3306
--user=root
--password=hellocasb
--database=ceshi
user.dir=/opt/client/extractor
cg-casb.properties loaded from /opt/client/extractor/cg-casb.properties
[2020-08-25 09:49:40] [start] mysql 192.168.10.130:3306 database:ceshi user:root
[2020-08-25 09:49:40] [extract] ceshi.RESULT columnNum:6 8/15
[2020-08-25 09:49:40] [extract] ceshi.Test001 columnNum:3 10/15
[2020-08-25 09:49:40] [extract] ceshi.test0527 columnNum:1 11/15
[2020-08-25 09:49:40] [extract] ceshi.testUser columnNum:2 12/15
[2020-08-25 09:49:40] [extract] ceshi.user columnNum:4 13/15
[2020-08-25 09:49:40] save table structre to: /opt/casb/logs/1294099137360302082/db/584775-MYSQL-ceshi-15-202007202101.json
[2020-08-25 09:49:40] Sending table structure to https://#{ip}:443/sem/v1/aoe/upload-collect
[2020-08-25 09:49:40] 当前占位符#{ip}所指ip为:10.1.1.141
[2020-08-25 09:49:40] 当前占位符#{ip}所指ip为:10.1.1.141
[2020-08-25 09:49:40] [completed] mysql 192.168.10.130:3306 database:ceshi user:root
```
2. 命令执行完毕后，客户端工具会自动把表结构文件上传到管理平台，可以在“策略管理”的“新增数据源”页面查看，并单击【下一步：选择应用】。
![](https://main.qcloudimg.com/raw/571aae60e28c8ec288b73acbbb5c6073.png)
3. 在“选择应用”页面，单击【新增应用】。
4. 在“新增应用”弹窗中，输入应用信息，单击【确定】。
![](https://main.qcloudimg.com/raw/26c09f5ca9172e324bb2dcdb0834dfcb.png)
5. 选择需要关联的应用，建立采集到的表结构与应用之间的关系，确认应用后，单击【下一步：选择工作模式】。
>?被加密系统可能含有多个应用，为防止混淆，区分不同的应用，通过关联操作把表结构和应用做关联，可在后续设置策略时作为参考。
>
![](https://main.qcloudimg.com/raw/24c6f508b0eda2040e7a3e38c8de2c94.png)
6. 选择工作模式，应用工作模式优先全局工作模式，单击【下一步：选择密钥】。
![](https://main.qcloudimg.com/raw/799b1e2174ce2c1041f64124b569f79e.png)
7. 创建并选择密钥，密钥有两种类型可以选择：系统默认的密钥和用户自定义的密钥，选择完成，单击【确认创建】。
![](https://main.qcloudimg.com/raw/1adf9e1bf8893ba9aede966a634276d6.png)
8. 在二次确认页面，单击【确认】，数据源即可创建成功。

### 步骤4：设置加解密策略
1. 在 CASB 管理平台的“策略管理”页面，找到需要加密的应用，在右侧“操作”栏，单击【设置策略】。
![](https://main.qcloudimg.com/raw/0e54ac26298cf83ad7c5a3ecdae2c24c.png)
2. 在该数据源下找到需要加密的表，在右侧“操作”栏，单击【设置策略】，进入表字段页面。
![](https://main.qcloudimg.com/raw/03ff86eda8e06e4b2b87a11745da3fa0.png)
3. 在表字段页面，选中需要加密的字段，在右侧“操作”栏，单击【设置策略】，弹出加密算法窗口。
![](https://main.qcloudimg.com/raw/70a5dc0dd6ddbd058c0d7e378293c0e7.png)
4. 选择“加密算法”，单击【确定】。
![](https://main.qcloudimg.com/raw/ea3b8b569ef648c60ada01c57e7ca3a0.png)
5. （可选）如需还对其他表或字段设置策略，重复上述操作即可。

### 步骤5：安装插件

1. **创建插件**
 1. 在 CASB 管理平台的左侧导航中，单击【应用插件管理】。
 2. 在“应用插件管理”页面，找到需要安装插件的应用，在右侧操作栏，单击【插件详情】，进入制作插件页面。
![](https://main.qcloudimg.com/raw/00b9fec2586f3cf288b73fa496b9a811.png)
 3. 在“制作插件”页面，单击【新增插件】。
 4. 在“新增插件弹窗”中，输入“插件名称”、选择“插件版本”、设置“是否开启插件断连告警”、输入“服务器 IP”，即 CASB 管理平台的服务器 IP 地址、输入“端口”即管理平台端口，输入完成后，单击【确定】，插件制作成功。
![](https://main.qcloudimg.com/raw/58f254ae8a792baf8d6508d5e49ac3b8.png)
2. **下载安装插件**
 1. 插件创建完成后，在插件列表中，找到目标插件，并在右侧操作栏，单击【下载】。
![](https://main.qcloudimg.com/raw/a9bb21600ebf9fe8e9079cbc952de82a.png)
 2. 将下载后的插件，拷贝到应用服务器上，以`root`用户运行`aoe-plugin.sh`安装插件
```
# 切换root用户
~$ su root
# 解压压缩包，视具体包名不同
~$ unzip plugin_ceshi.zip
# 进入解压后AOE目录，视具体目录名不同
~$ cd AOEPlugin-V1.1.10_1596696550082_149 
# 执行安装,后面的参数/opt/casb/plugin是安装位置，安装目录可以根据自己的需要填写
$ sh aoe-client.sh  /opt/casb/plugin
# 加载环境变量
$ source /etc/profile
```


### 步骤6：Demo 应用数据实时加解密

1. 确认 Demo 应用的数据库及表已经创建。
Demo 应用的数据源需要按照 [准备测试环境](#test) 创建，连接到数据库，并确认数据库已创建成功。
2. 修改配置并启动测试 Demo 应用。
将 Demo 应用上传到服务器，解压后修改 application.yml 文件，修改如下配置：
	- 将URL由`jdbc:mysql:// `改为`jdbc:aoe:mysql://`。
	- 将`driver-class-name`的值 改为：`com.tencent.cloud.aoe.plugin.engine.AOEDriver`。
	- 可根据实际情况修改端口 port:8095。
	>!后续使用浏览器访问时需要使用修改后的端口。
	>
```
server:
			# port端口可以根据情况作修改
			port: 8095
spring:
		datasource:
				# 将URL由jdbc:mysql:// 改为 jdbc:aoe:mysql://
				url: jdbc:aoe:mysql://10.1.1.211:3306/ceshi?serverTimezone=GMT%2B8&useUnicode=true&characterEncoding=utf8
				# 将driver-class-name 改为：com.tencent.cloud.aoe.plugin.engine.AOEDriver
				driver-class-name: com.tencent.cloud.aoe.plugin.engine.AOEDriver
				username: root
				password: hellocasb
				hikari:
					max-lifetime: 120000
mybatis:
			mapper-locations: classpath:mapper/*Mapper.xml
			type-aliases-package: com.cloudfly.springboot.crud.pojo
pagehelper:
			helper-dialect: mysql
			reasonable: true
			support-methods-arguments: true
			params: count=countsql
```
3. 启动测试 Demo 应用，观察日志，确认没有报错。
```shell
$ java -Dloader.path=./lib,$CASB_AOE_PLUGIN_PATH -jar springboot_crud.jar
注：这个参数$CASB_AOE_PLUGIN_PATH 这是plugin的安装路径，见文中步骤5中内容
```
4. 在防火墙中开放 Demo 应用的端口。
```
# root用户下执行命令 
$ firewall-cmd --zone=public --add-port=8095/tcp --permanent   
（注：--permanent永久生效，没有此参数重启后失效）
```
5. 打开 Demo 应用页面，浏览器访问 `http://ip:8095/index.html`。
>!IP 为部署 Demo 应用的服务器 IP，端口为 application.yaml 文件中设置的端口。
>
	- **添加新用户**
	在用户管理页面，填写相关信息，单击【立即创建】，即可成功添加新用户。
![](https://main.qcloudimg.com/raw/c2d697b7847acb2026701182bb1392ec.png)
	- **查看密文数据**
使用 DBeaver 或 Navicat 工具直接连接数据库查看数据如下，其中 user_name 数据已被加密。
![](https://main.qcloudimg.com/raw/b92ad705213e084198fe31cafe4d24c6.png)

### 步骤7：全量加解密

1. 创建全量加解密任务
	1. 在 CASB 管理平台的左侧导航中，单击【全量加解密】，进入“全量加解密”页面。
	2. 在“全量加解密”页面，单击【新增任务】。
![](https://main.qcloudimg.com/raw/e4a53322d263a6cc2c377c77d74760d2.png)
	3. 选择“全量加解密任务类型”，并单击【下一步：选择数据源】。
![](https://main.qcloudimg.com/raw/2d27cc3d8463bf3dda6bc9e8e151975f.png)
	4. 选中需要全量加解密的数据源，并单击【下一步：选择字段】。
![](https://main.qcloudimg.com/raw/006e2d6dc9fd971abafcea6d81acc0cf.png)
	5. 选中需要全量加解密的字段，并单击【确认创建全量加解密任务】。
![](https://main.qcloudimg.com/raw/8145126e80de2ea79fe8a73863a95ffd.png)
	6. 成功创建全量加解密任务后，在“全量加解密”页面将会展示任务 ID。
2. 执行全量加解密
	1. 登录到安装客户端工具的服务器上，执行以下命令：
```
# 进入客户端安装目录
~$ cd /opt/casb/processor
# 如下jar包名称根据实际安装后的jar包名称为准，数据库名称，ip，用户名，密码以实际为准，taskId号为管理平台创建的全量加解密任务id
# Processor验证数据库连接
~$ java -jar processor-1.1.12-release.jar --op=verify --db-type=mysql --host=10.1.1.222 --port=3306 --user=root --password=hellocasb --database=ceshi
# Processor进行全量加解密
~$ java -jar processor-1.1.12-release.jar --op=batchUpdate --password=hellocasb --taskId=1294661156949987330 --threads=4 --db-type=mysql
```
	2. 命令执行完成后，查看数据库中 user_name 数据已被加密。

## 其他
### 用户权限管理
1. 打开浏览器，输入`https://IP`（其中 IP 为 CASB 管理平台地址），进入登录页面。
2. 输入账户名及密码，单击【登录】，即可登录 CASB 管理平台。
<span id="role"></span>
	- **角色的新增、修改、删除**
		1. 在 CASB 管理平台的左侧导航中，单击【用户权限管理】。
		2. 在“用户权限管理”页面，选择【角色管理】>【新增角色】。
		3. 在弹出的“角色编辑”对话框中，选择角色，填写“角色名称”，单击【确定】即可新增角色。
		4. （可选）在角色管理页面，找到目标角色，在右侧操作栏，单击【修改】或【删除】，可对角色进行编辑或删除。
![](https://main.qcloudimg.com/raw/fd99bc18933eafa95bc82753ab2e9e1c.png)
	- **进行用户的新增、修改、删除**
		1. 在 CASB 管理平台的左侧导航中，单击【用户权限管理】。
		2. 在“用户权限管理”页面，选择【用户管理】>【新增用户】。
		3. 在弹出的“新增用户”对话框中，输入用户名、真实姓名、密码、邮箱、手机号及角色（选择在 [角色管理](#role) 中，所创建的角色）等信息，单击【确定】，即可新增用户。
	![](https://main.qcloudimg.com/raw/1d7cfb4761e0536c6b77345f7a8d4834.png)
		4. （可选）在用户管理页面，找到目标用户，在右侧操作栏，单击【修改】或【删除】，可对角色进行编辑或删除。

### 系统日志管理
1. 打开浏览器，输入`https://IP`（其中 IP 为 CASB 管理平台地址），进入登录页面。
2. 输入账户名及密码，单击【登录】，即可登录 CASB 管理平台。
3. 在 CASB 管理平台的左侧导航中，单击【系统日志】。
4. 在“操作日志”页面，可以根据用户、操作、日期进行筛选查看。
![](https://main.qcloudimg.com/raw/b04406bf9e69872f12610a7f7ef684c9.png)
