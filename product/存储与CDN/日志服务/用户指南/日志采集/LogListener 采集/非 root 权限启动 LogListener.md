## 操作场景

本文档指导您设置非 root 权限启动 LogListener。

## 操作步骤

1. 使用 root 权限依次执行如下命令，安装 LogListener。
```plaintext
wget https://mirrors.tencent.com/install/cls/loglistener-linux-x64-2.6.2.tar.gz 
```
 ```plaintext
tar -zxvf loglistener-linux-x64-2.6.2.tar.gz -C /usr/local 
```
 ```plaintext
cd /usr/local/loglistener-2.6.2/tools
```
 ```plaintext
./loglistener.sh install
```
 更多安装详情，请参见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414)。
2. 执行如下命令，打开 ./tools/loglistenerd.temple 服务文件。
```plaintext
vim ./tools/loglistenerd.temple
```
3. 按 **i** 切换至编辑模式，在 ./tools/loglistenerd.temple 服务文件中去掉 check_root 权限检查。
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
5. 使用 root 权限执行如下命令，修改安装目录的权限。
```plaintext
chown -R user1:user1 /usr/local/loglistener-2.6.2/
```
6. 执行如下命令，切换到子用户。以 user1 为例。
```plaintext
su -user1
```
7. 执行如下命令，完成 LogListener 的初始化。
```plaintext
cd /usr/local/loglistener-2.6.2/tools./loglistener.sh init -secretid AKIDPEtPyKabfW8Z3Uspdz83xxxxxxxxxxx -secretkey whHwQfjdLnzzCE1jIf09xxxxxxxxxxxx -region ap-xxxxxx
```
8. 使用子用户权限执行如下命令，启动 LogListener。
```plaintext
/etc/init.d/loglistenerd start
```
    
