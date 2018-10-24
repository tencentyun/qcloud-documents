## 使用说明
此脚本用于获取指定域名、指定日期的日志数据包（日期范围为30天以内）。

[点击下载](https://mc.qcloudimg.com/static/archive/b958077bcfeb0a4a35995f4790a91f7c/GetDayLog.zip)

**运行环境**：

+ python2.7
+ linux 系统


### 使用准备
在使用上述python脚本时，您需要安装 requests 库，可使用如下命令：
```
pip install requests
```

### 参数说明

```
host 域名
-u SECRET_ID
-p SECRET_KEY
--day 日期
--dstpath 日志下载路径
```

+ SecretId 和 SecretKey 在[云API密钥](https://console.cloud.tencent.com/capi) 处获取；
+ 仅支持30天内日志下载；
+ 默认情况下，指定日期日志存放地址为当前路径。


### 使用示例

```
python GetDayLog.py www.test.com -u XXXXXXXXXXXXXXX -p XXXXXXXXXXXXXX --day 20161130 --dstpath /home/test/
```

使用成功后，可在指定目录下看到所需日志文件，文件名称为：

```
20161130-www.test.com.gz
```

