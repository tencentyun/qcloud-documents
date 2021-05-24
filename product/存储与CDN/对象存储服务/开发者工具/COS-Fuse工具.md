## 功能说明
COSFS 是基于 libfuse 实现的一个用户态的文件系统，通过 COSFS 可以将远程的腾讯云 COS 挂载在用户机器上，像访问本地磁盘一样访问腾讯云 COS，用户或者程序操作本地文件系统相当于直接操作腾讯云 COS。目前仅支持文件读取。

## 使用环境

### 系统环境

Linux

### 依赖动态库

dl z ssl crypto stdc++ pthread

### 静态库(程序包已携带)

cosdk fuse curl jsoncpp

## 使用方法

### 获取程序包

当前版本： COSFS-v3.3.0 [点击下载](https://github.com/tencentyun/cosfs-v3.3.0) 


### 编译

``` 
cmake .
make
```

### 配置文件 cosfs_config.json

格式如下:

``` c++
{
"appid":10000***,
"secret_id":"AKIDxxxxxxxabcdefPNPur5B27qcuRajCEmzKV93U7k8VceqW",
"secret_key":"THrKYU2J9kMEy5JBQt7Bt0N4pYSKWGAz",
"domain":"cos"
}
```


**参数说明:**

appid/secret_id/secret_key: cos 帐号信息

domain: 定义从 cos 上读取文件时走的路径，取值如下

- cos：表示直接访问 cos, 访问的 URL 格式为：http://[bucket]-[appid].cos.myqcloud.com/[文件路径]
- cdn: 表示走 CDN 访问，访问的 URL 格式为： http://[bucket]-[appid].file.myqcloud.com/[文件路径]
- 自定义域名，访问的 URL 格式为： http://[自定义域名]/[文件路径]

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

使用以下命令进行卸载

``` 
fusermount -u /mnt/mointpoint/
```

或者

``` 
umount -l /mnt/mointpoint/
```

**备注：**

目前支持读相关操作,暂时不支持写操作：

linux 命令:  cd, ls, ll, cat, more, cp

系统接口:  open(), read(), stat(), close(), lseek()

