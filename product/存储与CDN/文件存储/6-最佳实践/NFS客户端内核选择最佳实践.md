
NFS 客户端是基于内核态的客户端，因部分内核版本的 BUG，会导致 NFS 服务无法正常使用，为了保证您更好的使用体验，请使用我们推荐的内核版本。
## 已知的客户端问题
### 内核网络栈缺陷导致文件系统无响应（优先级：高）
当系统的内核版本为2.6.32-696~2.6.32-696.10.1（包括2.6.32-696，但不包括2.6.32-696.10.1）时，NFS 服务端繁忙，内核请求重传，有概率触发内核网络栈缺陷，造成操作无响应。
当操作无响应时，请重启 CVM 实例。更多信息，请参见 [RHEL6.9:NFSv4 TCP transport stuck in FIN_WAIT_2 forever](https://access.redhat.com/solutions/3053801)。 
### 内核缺陷导致文件系统无响应（优先级：高）
- 当系统的内核版本为以下几个版本时，NFS 服务端故障转移，可能造成 NFS 客户端的打开、读、写操作出现死锁情况，从而导致文件系统持续无响应。 
  
  - Redhat 6、CentOS 6 2.6.32-696.3.1.el6。
  - Redhat 7、CentOS 7 3.10.0-229.11.1.el7之前的所有内核版本。
 -    Ubuntu 15.10 Linux 4.2.0-18-generic。
当操作无响应时，请重启 CVM 实例。更多信息，请参见 [RHEL7:NFSv4 client loops with WRITE/NFS4ERR_STALE_STATEID - if NFS server restarts multiple times within the grace period](https://access.redhat.com/solutions/1427473)。 
- 当系统的内核版本为以下几个版本时，网络发生分区或抖动，造成连接重连，NFS 客户端可能由于没有正确处理错误码而持续无响应。现象是文件系统无响应且系统 message 中反复打印 bad sequence-id error。 
  - Redhat 6、CentOS 6 2.6.32-696.16.1.el6之前的所有内核版本。
  - Redhat 7、CentOS 7 3.10.0-693.el7之前的所有内核版本。
当操作无响应时，请重启 CVM 实例。更多信息，请参见 [RHEL6/RHEL7:NFS4 client receiving NFS4ERR_BAD_SEQID drops nfs4 stateowner resulting in infinite loop of READ/WRITE+NFS4ERR_BAD_STATEID](https://access.redhat.com/solutions/3073231)。 
- 当操作系统内核版本为 CentOS 和 RedHat 5.11.x 所有内核时，执行 ls 命令、包含通配符 * 或 ? 的命令以及其他需要对目录进行遍历的操作，均会由于内核缺陷导致卡顿或无响应。 请您升级内核版本，避免此问题。


### 不支持 chown 命令和系统调用（优先级：低）
系统的内核版本为2.6.32时，不支持 NFS 客户端执行 chown 命令和系统调用。 
 
 
### ls 操作无法终止（优先级：低）
- 当系统的内核版本为2.6.32-696.1.1.el6及之前版本时，在系统中执行 ls 操作的同时还在进行添加、删除文件、子目录操作，将导致 ls 操作永远无法终止。 
请升级内核版本，避免此问题。
- 当系统的内核版本为4.18.0-305.12.1时，目录遍历操作如ls等，可能无法终止，请升级内核至4.18.0-305.19.1修复此问题。更多信息，请参见 [kernel-4.18.0-305.19.1.el8_4.x86_64](https://rpmfind.net/linux/RPM/centos/8-stream/baseos/x86_64/Packages/kernel-4.18.0-305.19.1.el8_4.x86_64.html?spm=a2c4g.11186623.0.0.516020bc5dma7X)。 


## NFS文件系统推荐镜像

### Linux系统镜像 




<table>
<tr>
<th>操作系统类型</th>
<th>操作系统版本</th>
<tr>
<tr>
<td>CentOS</td>
<td>

- CentOS 6.9 64位：2.6.32-696.16.1.el6.x86_64及以上
-  CentOS 6.10 64位：2.6.32-754.17.1.el6.x86_64及以上
- CentOS 7.2 64位：3.10.0-514.26.2.el7.x86_64及以上
- 	CentOS 7.3 64位：3.10.0-514.26.2.el7.x86_64及以上
- 	CentOS 7.4 64位：3.10.0-693.2.2.el7.x86_64及以上
- CentOS 7.5 64位：3.10.0-862.14.4.el7.x86_64及以上
- CentOS 7.6 64位：3.10.0-957.21.3.el7.x86_64及以上
- CentOS 7.7 64位：3.10.0-1062.18.1.el7.x86_64及以上
- CentOS 8.x 64位：4.18.0-147.5.1.el8_1.x86_64及以上
</td>
<tr>
<tr>
<td>Tencent OS Linux</td>
<td>

 - TencentOS Server 2.2(Tkernel 3)
 - TencentOS Server 2.4 (Tkernel 4)
 - TencentOS Server 2.6(Final)
 -  TencentOS Server 3.1(Tkernel 4)
</td>
<tr>
<tr>
<td>Debian</td>
<td>


- Debian 9.6 64位：4.9.0-8-amd64及以上
- Debian 9.8 64位：4.9.0-8-amd64及以上
- Debian 9.10 64位：4.9.0-9-amd64及以上
</td>
<tr>
<tr>
<td>Ubuntu</td>
<td>
- Ubuntu 14.04 64位：4.4.0-93-generic及以上
- Ubuntu 16.04 64位：4.4.0-151-generic及以上
- Ubuntu 18.04 64位：4.15.0-52-generic及以上
- Ubuntu 20.04 64位：5.4.0-31-generic及以上
</td>
<tr>
<tr>
<td>OpenSuse</td>
<td>


OpenSuse 42.3 64位：4.4.90-28-default及以上
</td>
<tr>
<tr>
<td>Suse</td>
<td>


- Enterprise Server 12 SP2 64位：4.4.74-92.35-default及以上
- Enterprise Server 12 SP4 64位：4.12.14-95.16-default及以上

</td>
<tr>
<tr>
<td>CoreOS</td>
<td>


- CoreOS 1745.7.0 64位：4.19.56-coreos-r1及以上
- CoreOS 2023.4.0 64位：4.19.56-coreos-r1及以上

</td>
<tr>
</table>




### Windows系统镜像 
<table>
<tr>
<th>操作系统类型</th>
<th>操作系统版本</th>
<tr>
<tr>
<td>Windows Server 2012</td>
<td>

- Windows Server 2012 R2 数据中心版 64位中文版
- Windows Server 2012 R2 数据中心版 64位英文版

</td>
<tr>
<tr>
<td>Windows Server 2016</td>
<td>

- Windows Server 2016 数据中心版 64位中文版
- Windows Server 2016 数据中心版 64位英文版

</td>
<tr>
<tr>
<td>Windows Server 2019</td>
<td>


- Windows Server 2019 数据中心版 64位中文版
- Windows Server 2019 数据中心版 64位英文版

</td>
<tr>

</table>

