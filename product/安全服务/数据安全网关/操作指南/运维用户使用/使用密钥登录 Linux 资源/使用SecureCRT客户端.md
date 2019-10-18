

## 操作步骤

### 步骤1：生成密钥对
1. 打开 SecureCRT 工具，选择【Options】>【Global Options】。
2. 在打开的配置框中选中【SSH2】， 并单击【Create Identity File】。
![](https://main.qcloudimg.com/raw/c2a0fbf59643738c506bd558f322c88b.png)
3. 单击【下一步】>【下一步】，并选择 Key Type 为 RSA。
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
