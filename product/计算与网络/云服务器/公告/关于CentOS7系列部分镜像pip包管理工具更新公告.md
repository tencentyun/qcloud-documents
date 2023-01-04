## 背景信息
腾讯云公共镜像 CentOS 7 系列的部分镜像中，默认安装 CentOS 发行版自带的Python 2-pip 8.1.2，此版本 pip 不具备选择兼容 Python 版本的能力，安装软件默认选择最新的包，而最新的 pip 和部分常用应用工具的最新版本（例如 NumPy）已经不支持 Python 2，这将导致您在执行命令升级 pip（pip install pip --upgrade）和安装一些应用工具时可能出现不兼容报错。为了保障最便捷的使用体验，腾讯云对公共镜像 CentOS 7 系列中部分镜像进行了 pip 更新。

## 更新内容及范围
本次 CentOS 7 系列更新的公共镜像范围如下列表所示，列表中的公共镜像默认安装 Python 2，其 pip 由 pip 8.1.2 升级至 [pip 20.3.4](https://pypi.org/project/pip/20.3.4/)。
<dx-alert infotype="explain" title="">
本次更新将分阶段进行全量完成更新时间为2022年12月12日，您在对应的公共镜像更新后新购买实例即已自动更新，您在对应的公共镜像更新前购买的实例不会自动更新，您可以参考操作指引进行手动升级。
</dx-alert>

| 镜像版本 | 镜像ID |
|---------|---------|
| CentOS 7.9 64位 |img-180g963d | 
| CentOS 7.6 64位 |img-9qabwvbn | 
| CentOS 7.9 64位+SG1-pv1.5 |	img-all2luul | 
| CentOS 7.9 64位+SG1-pv1.6 |img-ojhiw86l | 
| CentOS 7.4(arm64) |	img-k4xgkxa5| 

## 操作指引
###  pip 升级
您可以执行如下命令查看您实例的 pip 版本。
```plaintext
pip --version
```
若您实例的 pip2 版本低于 pip 9.0，您在执行 pip 升级和安装一些应用工具时可能会出现报错，您可以先执行如下命令升级 pip 到 pip2 的最新版本 pip 20.3.4。
```plaintext
pip2 install --upgrade pip==20.3.4
```
### 安装 pip2
您可以执行如下命令安装最新版本的 pip2。
```plaintext
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 ./get-pip.py -i http://mirrors.tencentyun.com/pypi/simple --trusted-host mirrors.tencentyun.com
```
如果在使用中遇到产品相关问题，您可咨询 [在线客服](https://cloud.tencent.com/act/event/Online_service?from=doc_282) 寻求帮助。
