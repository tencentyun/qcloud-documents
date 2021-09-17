### COSCMD 工具无法使用，该如何操作？

请查看以下问题是否都满足。
1. 操作系统是否是 Windows、Linux 和 macOS 系统。
2. 本地字符格式是否为 UTF-8，若否，则操作中文版的文件会出现异常。
3. 本机时间是否已经与国际标准时间校准，如误差过大，将导致无法正常使用。

更多详情请参见 [COSCMD 工具](https://cloud.tencent.com/document/product/436/10976)。

### COSCMD 工具是否支持正则表达式？

不支持。

### 使用 COSCMD 工具，成功创建含有大写字符的存储桶，进行其他操作时使用大写字符报错？

COSCMD 工具会将大写字符自动转换为小写字符，存储桶名称只支持小写字母、数字、中划线及其组合，最多支持50个字符。更多限制信息，请参考 [规格与限制](https://cloud.tencent.com/document/product/436/14518) 文档。

### 使用 COSCMD 工具上传/下载根目录文件，是否支持排除某个目录？

支持，需要使用`--ignore /folder/*`参数。
例如下载时排除 folder 目录，可使用`coscmd download --ignore /folder/*`命令过滤。当忽略某一类后缀时，必须最后要输入`,` 或者加入`""`。


### 当需要传输大量文件时，如何提高传输速度？
可适当调整 MAX_THREAD 参数值，默认配置为5。线程数取决于机器性能，通常情况下设置为30，即可跑满带宽。例如将并发线程调整为30，执行命令行如下。
```plaintext
coscmd config -m 30
```

### COSCMD 工具是否支持使用 \* 号指定特定前缀对象的下载?

不支持。需要按照以下命令格式下载：
```plaintext
coscmd download prefix/ localpath/ -r
```



### COSCMD list 是否支持按照文件上传时间列出文件？

不支持根据文件的上传时间列出文件，您可以通过指定前缀列出，详情请参见 [COSCMD 工具](https://cloud.tencent.com/document/product/436/10976) 文档。

### COSCMD 可以同时管理不同账号的存储桶吗？

使用 cos.conf 配置文件只能配置一个账号下的存储桶，若您需要管理不同账号下的存储桶，可参考以下命令切换配置后，再进行管理操作。
```
coscmd config -a SecretID -s SecretKey -b BucketName-APPID -r region
```
SecretID 和 SecretKey 可以在 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 获取，BucketName-APPID 是存储桶名称，region 为存储桶所在地域。

### COSCMD 是否支持在配置文件中指定多个 bucket ？

COSCMD 配置文件仅支持指定一个 bucket，如果您需要对不同的存储桶进行操作，可以在 COSCMD 命令指定存储桶名称和所属地域。 

- 通过`-b <bucketname-appid>`参数指定存储桶名称，存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式。
- 通过`-r <region>`指定 Region， 可以指定存储桶的所属地域。

### COSCMD 上传文件时支持校对重命名吗？

使用 COSCMD 上传同名文件，会覆盖较旧的同名文件，不支持校对是否存在同名文件的功能。

### 使用 COSCMD 工具传输大量文件如何提高传输速度？

可适当调整 MAX_THREAD 参数值，默认配置为5。线程数取决于机器性能，通常情况下设置为30，即可跑满带宽。例如将并发线程调整为30，执行命令行如下。

```
coscmd config -m 30
```

### COSCMD 工具上传文件是否会进行文件内容校验？

不会进行内容校验，默认进行覆盖上传。如需跳过已存在文件，需添加 -rs 参数。

### COSCMD 上传文件时如何跳过已存在文件？

COSCMD 上传时通过添加 -rs 参数跳过 md5 相同的文件。详情请参考 [COSCMD工具](https://cloud.tencent.com/document/product/436/10976) 文档中的 [上传文件夹](https://cloud.tencent.com/document/product/436/10976#.E4.B8.8A.E4.BC.A0.E6.96.87.E4.BB.B6.E5.A4.B9) 示例。

### 使用 COSCMD 工具下载如何跳过相同文件？

使用 -s 或者 --sync 参数，可以在下载文件夹时跳过本地已存在的相同文件（前提是下载的文件是通过 COSCMD 的 upload 接口上传的，文件携带有 x-cos-meta-md5 头部）。完整命令示例：`coscmd download -rs  --skipmd5 cos_path local_path`。

### COSCMD 支持同时上传多个文件夹吗？

不支持同时上传多个文件夹，每次只能上传一个文件夹，您可以把需要上传的多个文件夹统一放到一个文件夹内进行上传，但在本地复制文件时需要花费时间。

