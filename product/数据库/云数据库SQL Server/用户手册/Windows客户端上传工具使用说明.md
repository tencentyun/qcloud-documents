## 工具使用方法
1、将 “[Windows客户端上传工具](https://mc.qcloudimg.com/static/archive/924f2030cc27762d677c533ae533b1b1/upload.zip)” 下载至本地后，将其解压到任意文件夹（注：文件夹路径请勿包涵中文），解压后的文件目录结构如下：
![](https://mc.qcloudimg.com/static/img/716da8b5ece00ca2be062e2b637ff40d/1-1.png)

2、为了保证客户的数据安全。在备份上传之前，需要编辑配置文件 etc\conf.json，填写客户自己的API密钥（[secretId和secretKey](https://cloud.tencent.com/help/%E4%BA%91API%E8%AE%BF%E9%97%AE%E5%AF%86%E9%92%A5%E5%9C%A8%E5%93%AA%E9%87%8C%E8%8E%B7%E5%8F%96%EF%BC%8C%E8%AE%BF%E9%97%AE%E5%AF%86%E9%92%A5%E6%9C%80%E5%A4%9A%E6%9C%89%E5%A4%9A%E5%B0%91%E4%B8%AA)），请务必保存好自己的API密钥，切勿泄漏。为了保证传输过程的稳定，此工具已经支持断点续传功能；
注：conf.json文件请存储为“ UTF8 无 BOM 格式”（在 windows 下建议用 notepad++ 转换编码）

![](https://mc.qcloudimg.com/static/img/8cd149b24b1be3df87371081fa8cad39/1-2.png)

3、进入Windows命令行（“开始>搜索程序和文件>输入 cmd”），进入 Windows 命令行；

![](https://mc.qcloudimg.com/static/img/57dadbb324f56172f7a5c0f825e91d9b/1-3.png)

4、在 Windows 命令行中进入解压后的“ Windows 客户端上传工具”目录，调用 bin 目录下的 upload-tool.exe 完成上传操作。upload-tool.exe 有两个参数 –r 和 –p。–p 表示备份文件在本地的绝对路径；–r表示中转存储所处的地域（请选择您的腾讯云数据库所在地域）；
![](https://mc.qcloudimg.com/static/img/a4390e737e6367d860e2037c7b5068f3/1-4.png)

## 地域对照

| 地域 | -r 参数 |
|---------|---------
| 广州 | gz | 
| 上海 | sh |
| 香港 | hk | 
| 上海金融 | shjr | 
| 北京 | bj | 
| 深圳金融 | szjr | 

注：标识区分大小写
