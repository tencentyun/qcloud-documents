本文为您详细介绍如何通过 SecureCRT 实现密钥直连和单点登录资源。


## 准备工作


本文演示机器及相关准备工作，请参见概述文档 [准备工作](https://cloud.tencent.com/document/product/1025/38514#.E5.87.86.E5.A4.87.E5.B7.A5.E4.BD.9C) 章节。


## 操作步骤

### 步骤1：生成密钥对
1. 打开 SecureCRT 工具，选择【Options】>【Global Options】。
2. 在打开的配置框中选中【SSH2】， 并单击【Create Identity File】。
![](https://main.qcloudimg.com/raw/c2a0fbf59643738c506bd558f322c88b.png)
3. 选择【下一步】>【下一步】，并选择 Key Type 为 RSA。
![](https://main.qcloudimg.com/raw/76310dd2992d8791eeafbc2c9b4ef59b.png)
4. 下一步设置密钥对加密口令（可填可不填）。
5. 若设置了密钥，则下一步需要设置密钥长度，推荐长度2048。
![](https://main.qcloudimg.com/raw/2dffb4dbb4b149cc6bae6fda220bd05e.png)
6. 单击【下一步】，等待绿色进度条完成，单击【下一步】。
![](https://main.qcloudimg.com/raw/13dd310d7d716f2e2585096017be178b.png)
7. 设置密钥生成格式及保存位置，最后单击【完成】，生成公私钥密钥文件。
![](https://main.qcloudimg.com/raw/e4b27cc335d9bdbd5d4bb63c47e66554.png)


### 步骤2：实现密钥直连登录
1. 打开 SecureCRT 工具，选择【Options】>【Global Options】>【SSH2】，将私钥文件导入工具中。
![](https://main.qcloudimg.com/raw/57b28db46c65a5e0019de5cc48d31e5f.png)
2. 单击【OK】，配置即可生效，进行密钥直连目标机。
![](https://main.qcloudimg.com/raw/dde5874988d3e5798c7d4144e03df84e.png)
<img src="https://main.qcloudimg.com/raw/a340fb44e40c41ace13c37ea2fa79c3d.png"  width="80%">

### 步骤3：实现密钥单点登录
1. 打开 SecureCRT 工具，选择【Options】>【Global Options】>【SSH2】，将 Enable OpenSSHell agent forwarding 选项勾选上。
<img src="https://main.qcloudimg.com/raw/796fa653c9c669702b834b67f2ce7fa1.png"  width="80%">
2. 选择【Tools】>【Manage Agent Keys】。
<img src="https://main.qcloudimg.com/raw/a47db4ad1428ca4535c73fd925cf1e12.png"  width="80%">
3. 将私钥文件加入到 Agent 服务中，即可生效进行目标设备的单点登录。
 <img src="https://main.qcloudimg.com/raw/17d01226a639c19a9353a406b44f7106.png"  width="80%"> 
>!SecureCRT 工具 Manage Agent Keys 组件添加私钥文件，关闭工具后失效，需每次单点登录前打开 SecureCRT 工具手动添加私钥文件，并保持 SecureCRT 工具运行。
4. 打开浏览器，登录堡垒机。在登录界面，选择登录的账号和登录工具，单击【连接】。
 <img src="https://main.qcloudimg.com/raw/dcf204f21377e471d583085b31dca044.png"  width="80%">
5. 即可实现单点登录。                                                                                                                                             

	<img src="https://main.qcloudimg.com/raw/922b353eddfca911d839b2a390285f41.png"  width="80%">

