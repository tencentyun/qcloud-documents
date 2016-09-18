为了提升用户在云服务器上的软件安装效率，减少下载和安装软件的成本，腾讯云提供了YaST下载源。操作系统为SUSE10的云服务器用户可通过YaST快速安装软件。

## 1. 安装步骤
登录操作系统为SUSE的云服务器后，默认已获取root权限，在此权限下，通过以下命令列出软件源：

```
service-list 
```
或

```
sl
```
返回示例：
![](//mccdn.qcloud.com/img56a624f424c9b.png)

如果源中有上图中显示的2个软件源，则可以直接执行步骤3，正常进行软件下载和安装；

如果没有，请根据步骤2的说明添加软件源；

>注：为避免安装时出现“Please insert media [Failed to mount iso:///?iso=/data/SLES-10-SP1-DVD]#1. Retry [y/n]:”错误，如果源里面有"SUSE-Linux-Enterprise-Server"这个ISO光盘源时请使用“sd SUSE-Linux-Enterprise-Server”进行删除。

## 2. 添加软件源
如果上一步骤中没有列出软件源，则需要在root权限下，通过以下命令手动添加软件源：

```
service-add
```
或
```
sa
```
示例如下：

```
sa -t YaST http://mirrors.tencentyun.com/suse suse 
sa -t YaST http://mirrors.tencentyun.com/suse/update update
```

## 3. 搜索软件包
通过以下命令搜索软件包：

```
search
```
或

```
se
```
示例如下：

```
se nginx
```
结果：
![](//mccdn.qcloud.com/img56af4b0fab73a.png)

## 4. 安装软件包
根据搜索到的软件包的名字安装软件。如果要安装多个软件，中间用空格隔开。

>注：安装软件的时候，如果需要依赖包，会自动下载安装，用户无需自己安装依赖包。

通过以下命令安装软件包：

```
install
```
或
```
in
```
示例如下：

```
in nginx
```

结果如下：

![](//mccdn.qcloud.com/img56af4be96d4b4.png)

请按照相同的方式安装php和php-fpm等软件：

```
in MySQL-server-community php5-mysql php5 php5-fpm
```

## 5. 查看安装的软件信息
软件安装完成后，可通过以下命令查看软件包具体的安装目录：

```
rpm -ql 
```

可通过以下命令查看软件包的版本信息：

```
rpm -q
```

示例：

```
rpm -ql nginx
rpm -q nginx
```
结果如下（实际的版本可能和此版本不一致，请以实际查询到的版本为准）：
![](//mccdn.qcloud.com/img56af4cc4d0c52.png)
![](//mccdn.qcloud.com/img56af4ccb0d033.png)