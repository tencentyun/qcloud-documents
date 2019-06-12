## 安装相关

###  setuptools 版本过旧

表现：`error in scf setup command: 'install_requires' must be a string or list of strings containing valid project/version requirement specifiers`

解决方法：`pip install -U setuptools`

### 已存在的 distutils 安装包无法升级

表现：```Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.```

解决方法： `pip install -I PyYAML==x.x.x`（在requirements.txt中查看具体版本）

## 使用相关

### yaml 配置文件内有多个函数描述时，如何指定函数进行本地调试

表现：`Error: You must provide a function identifier (function's Logical ID in the template). Possible options in your template: ['xxxB', 'xxxA']`

解决方法：调用 local invoke 命令时带有函数名，如 `scf local invoke -t template.yaml xxxA`

### 部署时出现 [SSL: CERTIFICATE_VERIFY_FAILED] 错误

表现：使用 deploy 时，部署函数失败，报`[SSL: CERTIFICATE_VERIFY_FAILED]` 证书验证错误，

问题原因：mac 10.12 + python 3.6 及以上环境中，python 不再读取系统路径证书，导致读取证书失败，调用腾讯云 云 API 部署时 SSL 验证失败。

解决方法：在 python 安装目录下，执行 `Install Certificates.command` 脚本，会自动安装 certifi 包，解决证书问题。
