## 工具使用方法
1、“将“Windows客户端上传工具”下载至本地后，将其解压到任意文件夹（注：文件夹路径请勿包涵中文），解压后的文件目录结构如下：
![](https://mc.qcloudimg.com/static/img/716da8b5ece00ca2be062e2b637ff40d/1-1.png)

2、为了保证客户的数据安全。在备份上传之前，需要编辑配置文件etc\conf.json，并填写目的实例的API密钥（[secretId和secretKey](https://console.qcloud.com/capi)）。为了保证传输过程的稳定，此工具已经支持断点续传功能；
![](https://mc.qcloudimg.com/static/img/8cd149b24b1be3df87371081fa8cad39/1-2.png)

3、进入Windows命令行（“开始>搜索程序和文件>输入cmd”），进入Windows命令行；

![](https://mc.qcloudimg.com/static/img/57dadbb324f56172f7a5c0f825e91d9b/1-3.png)

4、在Windows命令行中进入解压后的“Windows客户端上传工具”目录，调用bin目录下的upload-tool.exe 完成上传操作。upload-tool.exe 有两个参数 –r 和 –p。–p表示备份文件在本地的绝对路径；–r表示中转存储所处的地域（请选择您的腾讯云数据库所在地域）；
![](https://mc.qcloudimg.com/static/img/9e018eab3450346193e7b2f69c4ac65c/1-4.png)

## 地域对照

| 地域 | -r参数 |
|---------|---------
| 广州 | gz | 
| 上海 | sh |
| 香港 | hk | 
| 上海金融 | shjr | 
| 北京 | bj | 
| 深圳金融 | szjr | 

注：标识区分大小写