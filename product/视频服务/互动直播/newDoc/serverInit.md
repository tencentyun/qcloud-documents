# 随心播 Server QuickStart

## 1. 代码部署

### 1.1 搭建PHP和数据库环境

#### 服务器环境要求 

* Linux OS
* PHP >= 5.4
* MySQL >= 5.5.3

### 1.2 修改配置

* [下载代码](https://github.com/zhaoyang21cn/SuiXinBoPHPServer/tree/StandaloneAuth)，部署到php目录中
* 在lib/db/DBConfig.php填写mysql的数据库url、用户名和密码
* 调整server/account/AccountLoginCmd.php为自己互动直播的SDKAPPID：

```php
	const SDKAPPID = '1400019352';
```

* 修改service/service/Server.php的这句代码为自己的日志路径

```php
	$handler = new FileLogHandler('/data/log/sxb/sxb_' . date('Y-m-d') . '.log');
```

* 修改deps/bin/tls_licence_tools具有可执行权限，用于生产userSig
* 修改deps/sig目录权限，使得其他用户有可读写执行权限（chmod 757 deps/sig），用于生成sig临时文件的目录，将用于生成和校验sig的公私钥放置于此目录。<br/>
如果用户自定义置于其他目录，则需要修改server/account/AccountLoginCmd.php为自定义路径，保证这些文件至少具有可读权限。

```php
	$private_key = DEPS_PATH . '/sig/private_key';
	$public_key = DEPS_PATH . '/sig/public_key';
```

* 如果您在使用直播码进行旁路推流，调整server/live/ReportLiveRoomInfoCmd.php代码的BIZID。

```php
	const BIZID = '123456';
```

* 如果想使用图片上传功能，需要开通腾讯云COS服务，并在deps/cos-php-sdk/Conf.php填写对应APPID、SecretKey和SecretID。

### 1.3 数据库建表建库

执行sxb_db.sql文件中的sql。

## 2. 代码目录结构

![](https://mc.qcloudimg.com/static/img/0413205b36b65645ef4a5ddd8135198c/2.png)

### 2.1 service 

服务层，也就是接口层，主要包括：账号管理，直播服务、AV房间服务、COS服务。每个服务（亦即模块）下是各个子接口。详细可参看协议文档。

#### 2.1.1 直播服务

- 开始直播：数据库Replace一条记录，注意一个用户同一时间最多只能有一场直播；
- 直播结束：从数据库中删除记录；
- 直播列表：从数据库分页获取直播列表；
- 直播心跳包：客户端10秒发一次心跳包更新数据。

#### 2.1.2 Cos服务

获取Cos签名。

#### 2.1.3 AvRoom服务

获取AV房间号。


### 2.2 model 

数据层。

### 2.3 client-data 

客户端数据对象层，主要用于接收和返回给客户端的数据对象。

### 2.4 lib 

包括数据库和日志等库。

### 2.5 deps 

依赖库和依赖程序和文件，主要是其他项目或者SDK，比如腾讯云COS SDK。

### 2.6 cron 
后台定时任务。清理90秒没有发心跳包的直播记录。可以crontab定时执行。

## 3. 再次强调
 
 * sig目录其他用户一定要有读写可执行权限
 * deps/bin/tls_licence_tools签名程序一定可执行权限
 * 调整为自己的SDKAPPID和私钥公钥路径

## 4. 交互图
![腾讯互动直播数据交互](https://mc.qcloudimg.com/static/img/4094feaf383cf1e3c5714bd3f9dbfc8e/hudongzhibo.png)

## 5. 已实现的功能

* 注册
* 登录
* 创建房间
* 上报创建房间结果
* 拉取直播房间列表
* 上报进入房间信息
* 拉取房间成员列表
* 心跳上报
* 申请上麦
* 申请上麦结果上报
* 录制视频完成上报
* 退出房间
* 拉取点播列表
* 拉取旁路直播地址列表
* 拉取指定房间的旁路直播地址
* 下线
