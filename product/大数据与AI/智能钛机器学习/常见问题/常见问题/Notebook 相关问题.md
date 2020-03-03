>?此页面的 Notebook 常见问答，仅适用于重庆地域。

### 在平台 Notebook 里访问 COS 存储桶的数据文件，路径应该怎么填写？
新建 Notebook 的时候会选择 bucket，我们会把 bucket 里面的文件挂载到 Notebook 容器中的 /cos_person 目录下，访问的时候，在路径前面加上 /cos_person 就可以了。

### 新建一个 Notebook，打开后却报502错误，应该怎么处理？
此种情况很可能是您 COS 目录下的 Notebook 文件夹存在大数据文件，目前第一次启动 Notebook 容器时，会把 cos /Notebook 文件夹里的数据 copy 到容器里面的 /Notebook 目录里，数据量大的话就会卡住，从而报错。
建议：COS 目录下的 Notebook 文件夹存放的数据文件不要过大。

### Notebook 里用户没有 root 权限，自定义安装包时报错，应该怎么处理？
根据提示加上--user 即可解决。
如直接：pip install lightgbm，会报下图错误。
修改成：pip install --user lightgbm。
![](https://main.qcloudimg.com/raw/da99bc5471b5aa2e4f02dad76c1b4d5d.png)
安装后若使用不了，可以尝试重启下 Notebook 容器内核。
![](https://main.qcloudimg.com/raw/3835073fb6cd5f1c4b9966e283307375.png)

### Notebook 容器创建时失败，一般是什么原因造成的？
目前试运营阶段，给大家配置的资源是有限制的，所以当您创建 Notebook 容器时选择的资源超过了您当前可用资源，容器创建便会失败。如遇其他情况，请联系工作人员处理。

### 运行中的 Notebook 突然失败或报503错误，一般是什么原因造成的？
一般是 Notebook 容器里运行的程序所需要的资源超过了现有的资源环境，导致异常终止。请调试程序，合理使用资源，如遇其他情况可联系工作人员处理。

### Notebook 容器运行失败，应该怎么处理？
Notebook 容器运行失败后不能再打开，可做删除处理。但里面生成的数据已经同步到您的 COS 存储桶里了，您只需再新建一个容器，新建时选择同一个 COS 存储桶即可，历史数据会同步到新容器里。

### 若重启 Notebook，之前自定义的安装包是否还存在？
不存在，需要重新进行安装。
