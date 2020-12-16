### 开发环境在中国境外时如何部署？
由于 Serverless Framework 在部署时会默认检测是否为中国用户，如果开发环境在中国境外，但希望使用中国版体验的 Serverless Framework，可以在 .env 文件中增加配置 `SERVERLESS_PLATFORM_VENDOR=tencent` 即可指定默认提供中国版体验。

### 部署时进入国际版？
如果您的部署环境配置了代理，可能会出现该问题，请确认您的开发环境是否在中国境内，然后在 .env 文件中增加配置 `SERVERLESS_PLATFORM_VENDOR=tencent` 即可。

### 开发环境在中国境外部署缓慢如何处理？
Serverless Framework 部署引擎目前在是在中国境内，因此境外部署时，在上传文件过程中可能会非常缓慢，可以通过在 `.env` 文件中增加配置 `GLOBAL_ACCELERATOR_NA=true` 开启境外加速 。

### 用户环境无外网权限，必须通过代理才能访问外网，该如何部署？
在 .env 文件中增加以下配置即可：
```
HTTP_PROXY=http://127.0.0.1:12345  #请将'12345'替换为您的代理端口
HTTPS_PROXY=http://127.0.0.1:12345  #请将'12345'替换为您的代理端口
```

### 使用 Windows Powershell 部署无权限如何处理？
Windows powershell 的权限管理比较严格，需要执行 set-executionpolicy remotesigned 命令后即可正常部署。此外，Windows 环境下建议通过 serverless deploy 全拼方式部署。
