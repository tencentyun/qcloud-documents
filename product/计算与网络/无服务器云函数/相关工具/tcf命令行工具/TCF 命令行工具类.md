## 安装相关

###  setuptools 版本过旧怎么办？

#### 现象

```
error in tcf setup command: 'install_requires' must be a string or list of strings containing valid project/version requirement specifiers
```

#### 解决方法

执行以下命令：
```
pip install -U setuptools
```

### 已存在的 distutils 安装包无法升级怎么办？

#### 现象

```
Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
```

#### 解决方法

执行以下命令：
```
pip install -I PyYAML==x.x.x(在 requirements.txt 中查看具体版本)
```


