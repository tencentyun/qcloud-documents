## 概要信息
Batch 中执行日志（StdOut、StdErr）和远程存储映射都涉及填写 COS/CFS 路径，相比 HTTP 方式访问 COS Bucket 或者文件会稍有差异。

##  COS 路径说明

### 仅支持 COS XML API 访问域名
Batch 填写的时候仅支持 XML API 形式的域名。如下图所示：
![](https://main.qcloudimg.com/raw/a678139c758058e419e90418deba7501.png)



### 前缀需要以 cos:// 开头
已获取的 COS 路径。如下图所示：
![](https://main.qcloudimg.com/raw/b8f6104573627c26fbe96900cc350632.png)
在 Batch 的路径填写里，需要添加 `cos://` 开头、需要以 `/` 结尾，得出以下形式路径：
``` 
cos://batchdemo-125178xxxx.cos.ap-guangzhou.myqcloud.com/
```



### 挂载子目录
子目录可直接以常规文件目录的方式添加在 Bucket 路径后即可，Bucket 中已创建的子目录如下图所示：
![](https://main.qcloudimg.com/raw/ff8eda23225ce9e69ec2d6613f677596.png)
进行目录挂载时 COS 路径填写方式如下：
``` 
cos://batchdemo-125178xxxx.cos.ap-guangzhou.myqcloud.com/logs/
cos://batchdemo-125178xxxx.cos.ap-guangzhou.myqcloud.com/input/
cos://batchdemo-125178xxxx.cos.ap-guangzhou.myqcloud.com/output/
```

### 支持同地域 Bucket
COS 是具有地域属性的，需确保您的 Batch 作业和 COS Bucket 在同一地域，这样才能最高效的让数据在存储和云服务器之间传输。

## CFS 路径说明
远程存储映射里，可以配置自动挂载 CFS/NAS 路径到本地路径。如下图所示：
![](https://main.qcloudimg.com/raw/414ac8013f2f31587d75420ec0dc700f.png)

### 前缀需要以 cfs:// 或 nfs:// 开头
已获取 CFS 路径，例如 `10.66.xxx.xxx`。在 Batch 的路径填写里，需以 `cfs://` 或者 `nfs://` 开头，具体形式如下：

<dx-alert infotype="notice" title="">
需要以`/`结尾，并且确保您的 CFS/NAS 和 Batch 作业配置在同一网络内。
</dx-alert>
``` 
cfs://10.66.xxx.xxx/ 
```




