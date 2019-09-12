## 概要信息

Batch 中执行日志（StdOut、StdErr）和远程存储映射都涉及填写COS/CFS路径，相比 http 方式访问 COS bucket 或者 文件，会稍有差异，详细见下。

## 1. COS路径说明

### 仅支持 COS XML API 访问域名

![](https://mc.qcloudimg.com/static/img/9e0e71c620551fd4271f5e026978d068/1.png)

COS 支持访问域名包含适用于 XML API 和 JSON API 的两种，Batch 填写的时候仅支持 XML API 形式的域名，如上图红框标识部分。

### 前缀需要以cos:// 开头

![](https://mc.qcloudimg.com/static/img/9e0e71c620551fd4271f5e026978d068/1.png)

比如上图的地址，在 Batch 的路径填写里，需要添加 cos:// 开头，具体形式见下

``` 
cos://testbatch-1252462967.cos.ap-beijing-1.myqcloud.com/ 
```

``注意：需要以 / 结尾``

### 挂载子目录

![](https://mc.qcloudimg.com/static/img/5dfebdda44fa0417c03090675a58a099/2.png)

子目录直接以常规文件目录的方式添加在 Bucket 的域名后面即可，比如上图的 Bucket 下的文件夹，进行目录挂载时 COS 路径填写方式见下

``` 
cos://testbatch-1252462967.cos.ap-beijing-1.myqcloud.com/testdir/ 
```

### 支持同地域Bucket

COS 是具有地域属性的，需要保证您的 Batch 作业和 COS Bucket 在同一地域，这样才能最高效的让数据在存储和云服务器之间传输。

## 2. CFS路径说明

远程存储映射里，可以配置自动挂载 CFS / NAS 路径到本地路径。

![](https://mc.qcloudimg.com/static/img/7721d8b14f775055615d430528008cb9/3.png)

### 前缀需要以 cfs:// 或 nfs:// 开头

比如上图的地址，在 Batch 的路径填写里，需要添加 cfs:// 或者 nfs:// 开头，具体形式见下

``` 
cfs://10.66.140.208/ 
```

``注意：需要以 / 结尾，并且保证您的 CFS / NAS 和 Batch 作业配置在同一网络内``







