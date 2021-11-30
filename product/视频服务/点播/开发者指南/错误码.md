## 错误码列表
### 视频处理类错误码

| 错误码 | 含义 |
| -- | -- |
| InvalidInput | 输入参数不合法，请检查输入参数。 |
| InvalidInput.InvalidTimeOffset | 输入参数不合法：指定的时间点不合法。 |
| InvalidInput.DefinitionNotExist | 输入参数不合法：指定的模板 ID 不存在。 |
|InvalidInput.ConfigurationUnsupported|输入参数不合法：配置无效，包括但不限于：<li>用户未注册。</li><li>输入参数取值非法（格式、取值范围等）。</li><li>参数模板配置有问题。</li><li>未指定视频处理任务。</li>|
|InvalidInput.TaskDuplicated|输入参数不合法：任务重复，如同一个视频不允许重复发起微信小程序发布任务。|
|InvalidInput.PermissionDenied|输入参数不合法：没有权限，请申请产品功能权限后使用。|
|InvalidInput.ResultFileSizeTooLarge|输入参数不合法：输入多文件拼接后结果文件过大。|
| SourceFileError | 源文件错误：如视频数据损坏，请确认源文件是否正常。 |
| SourceFileError.NoVideoMedia | 源文件错误：没有视频轨画面。 |
| SourceFileError.NoVideoResolution | 源文件错误：无法获取源文件的分辨率。 |
|SourceFileError.ContentMalformed|源文件错误：输入内容存在问题，如文件不存在、文件损坏、媒体文件无法解码。|
|SourceFileError.ContentUnsupported|源文件错误：输入的格式有问题，如不受支持的文件格式、文件大小、文件时长。|
|SourceFileError.DownloadNotAccessible|源文件错误：尝试下载输入文件时，这些文件无法访问，请检查源的可用性。|
|InternalError | 内部服务错误，建议重试。 |
