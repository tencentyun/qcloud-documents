
## 现象描述
IIS Web 服务部署免费 SSL 证书时提示 “证书链中的一个或多个中间证书丢失，要解决此问题，请确保安装了所有中间证书”。
![](https://qcloudimg.tencent-cloud.cn/raw/c60b361b5c92cf6c80862c963c1fde9f.png)

## 可能原因
中间证书缺失。

## 解决办法
### 步骤1：查看证书加密算法
登录腾讯云 [SSL 证书控制台](https://console.cloud.tencent.com/certoverview)，查看您的证书加密算法类型。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0536c8fb4518555647085535130a786e.png)

### 步骤2：下载中间证书文件
根据您的证书加密算法类型下载中间证书至您的云服务器中。
- RSA 加密算法类型：[单击下载](https://upload-dianshi-1255598498.file.myqcloud.com/TrustAsia%20RSA%20DV%20TLS%20CA%20G2-02085dd70442134c6abdefd92f9d40ce16e5774c.crt)。
- ECC 加密算法类型：[单击下载](https://upload-dianshi-1255598498.file.myqcloud.com/TrustAsia%20ECC%20DV%20TLS%20CA%20G2-677875f5af3a5f066dc7d0fbb9400745e97d1a53.crt )。

### 步骤3：安装中间证书
1. 在您需要部署证书的服务器上，双击中间证书文件并在打开的窗口中单击**安装证书**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/52d9ae19f6cfa14e745eb3dcfce4fee5.png)
2. 在证书导入向导中存储位置选择**本地计算机**，并单击**下一页**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2e028bd291a12fc20177e5bb45b1a19c.png)
3. 证书存储选择**将所有的证书都放入下列存储 > 中间证书颁发机构**，并单击**下一页**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a0dc7261f9381bfa3f42da7d16864b0e.png)
4. 确认您安装的证书位置是否正确，并单击**完成**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/50b4d523eafbd9007d700b5f949274d1.png)
5. 显示 “导入成功” 即可完成设置，请再次尝试部署您的 SSL 证书。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0d08f70627c9160fde4deda813a045eb.png)







