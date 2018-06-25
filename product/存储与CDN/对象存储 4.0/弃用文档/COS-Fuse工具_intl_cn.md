
## 功能说明

COSFS 是基于 libfuse 实现的一个用户态的文件系统，通过 COSFS 可以将远程的腾讯云 COS 挂载在用户机器上，像访问本地磁盘一样访问腾讯云 COS，用户或者程序操作本地文件系统相当于直接操作腾讯云 COS。目前仅支持文件读取。**只适用于COS 4.0**

## 使用环境

### 系统环境

Linux


### 依赖动态库

dl z ssl crypto stdc++ pthread


### 静态库(程序包已携带)

cossdk fuse curl jsoncpp


## 使用方法

### 获取程序包

当前版本： COSFS-v4.2.0 [点击下载](https://github.com/tencentyun/cosfs-v4.2.0) 


### 编译

```
cmake .
make
```


### 配置文件 cosfs_config.json

主要是 cosfs 依赖的 COS SDK 使用，参数说明:

```c++
"AppID":1251668577,
"SecretID":"AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO",
"SecretKey":"FZjRSu0mJ9YJijVXXY57MAdCl4uylaA7",
"Region":"sh",                    //所属 COS 区域，上传下载操作的 URL 均与该参数有关
"SignExpiredTime":360,            //签名超时时间，单位：秒
"CurlConnectTimeoutInms":10000,   //CURL 连接超时时间，单位：毫秒
"CurlGlobalConnectTimeoutInms":360000, //CURL 连接执行最大时间，单位：毫秒
"UploadSliceSize":1048576,        //分片大小，单位：字节，可选的有512k,1M,2M,3M (需要换算成对应字节数)
"IsUploadTakeSha":0,              //上传文件时是否需要携带 sha 值
"DownloadDomainType":2,           //下载域名类型：1: cdn, 2: cos, 3: innercos, 4: self domain
"SelfDomain":"",                  //自定义域名
"UploadThreadPoolSize":5          //单文件分片上传线程池大小
"AsynThreadPoolSize":2            //异步上传下载线程池大小
"LogoutType":0                    //打印输出，0:不输出,1:输出到屏幕,2:打印 syslog
```

**一般只需要修改如下COS信息参数**
AppID、SecretID、SecretKey、Region、DownloadDomainType

### 运行

(1) 挂载 bucket 到本地

```c++
./cosfs bucket /mnt/mointpoint/ -o cfgfile=cos_config.json  

//【/mnt/mointpoint/】为用户本地路径，由用户指定
//【bucket】为用户在 COS 上 bucket 名称，由用户指定
```

(2) 挂载 bucket 下的某个目录到本地

```c++
./cosfs bucket:/folder /mnt/mointpoint/ -o cfgfile=cosfs_config.json 

//【/mnt/mointpoint/】为用户本地路径，由用户指定
//【bucket：/folder】为用户在 COS 上 bucket 及目录名称，由用户指定
```

### 卸载

先要安装 fuse(yum install fuse) ,才能执行

``` 
fusermount -u /mnt/mointpoint/
```

如果提示设备忙,则需退出 /mnt/mointpoint/ ,如果还是无法卸载,则执行

```
umount -l /mnt/mointpoint/
```


**备注：**
目前支持读相关操作,暂时不支持写操作：
linux命令:  cd, ls, ll, cat, more, cp
系统接口:  open(), read(), stat(), close(), lseek()


