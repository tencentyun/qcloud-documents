# 常见问题 FAQ

## 安装问题

###  setuptools版本过旧

表现： error in tcf setup command: 'install_requires' must be a string or list of strings containing valid project/version requirement specifiers

解决方法：pip install -U setuptools


### 已存在的distutils安装包无法升级

表现：Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.

解决方法： pip install -I PyYAML==x.x.x(在requirements.txt中查看具体版本)

