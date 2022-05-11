参考方法一：直接在 nginx 日志中查看（日志路径：/var/log/nginx/access.log）

参考方法二：使用 wireshark 查看 tcpdump 抓包获取为。



1.	在后端服务器执行以下命令进行抓包
```
sudo tcpdump -i eth0 -w dump.pcap
```
-i 指定要抓取的网卡
-w 指定结果保存位置
2. 客户端访问测试地址后，按下 ctrl + c 停止抓包
![](https://qcloudimg.tencent-cloud.cn/raw/90c5f4edd7b4ab757882ad0850ea298e.png)
3. 用 sz 命令或其他方式把 dump.pcap 文件下载到本地
```
sz dump.pcap
```
4.	wireshark 打开下载的 dump.pcap 文件，从 TCP Option 中查看客户端真实 IP。
此字段后4个字节（十六进制）即为客户端真实 IP
![](https://qcloudimg.tencent-cloud.cn/raw/e6a057e69df76b553cc307001b75f2a6.png)
