## 限制与说明
### 限制规格

<table> 
    <tr align="center">
        <td width="10.5%" rowspan="2" >产品类型</td>
        <td width="10%" colspan="2">通用标准型</td>
        <td width="10%" colspan="2">通用性能型</td>
        <td width="10%" colspan="2">Turbo 标准型</td>
        <td width="10%" colspan="2">Turbo 性能型</td>
    <tr align="center">
        <td width="10%" >产品规格</td>
        <td width="10%" >推荐范围</td>
        <td width="10%" >产品规格</td>
        <td width="10%">推荐范围</td>
       <td width="10%" >产品规格</td>
        <td width="10%">推荐范围</td>
       <td width="10%">产品规格</td>
        <td width="10%">推荐范围</td>
    </tr>
    <tr align="center">
        <td>系统容量上限</td>
        <td>160TiB</td>
        <td>140TiB<br></td>
        <td>32TiB</td>
        <td>24TiB<br></td>
        <td>100PiB</td>
        <td>4PiB<br></td>
        <td>100PiB</td>
        <td>2PiB<br></td>
    </tr>
    <tr align="center" >
        <td>系统起步容量</td>
        <td colspan="2">无要求</td>
        <td colspan="2">100GiB</td>
        <td colspan="2">40TiB</td>
        <td colspan="2">20TiB</td>
   </tr>
    <tr align="center" >
        <td>系统带宽上限</td>
        <td>300MiB/s</td>
        <td>240MiB/s</td>
        <td>2GiB/s</td>
        <td>1.6GiB/s</td>
        <td>100GiB/s</td>
        <td>10GiB/S</td>
        <td>100GiB/s</td>
        <td>10GiB/s</td>
    </tr>
    <tr align="center" >
        <td>系统文件数上限</td>
        <td>Min[1.5万*已使用容量(GiB)，10亿]</td>
        <td>Min[1万*已使用容量(GiB)，8亿]</td>
        <td>Min[2万*已部署容量(GiB)，15亿]</td>
        <td>Min[1.5万*已部署容量(GiB)，10亿]</td>
        <td>Min[1.5万*已部署容量(GiB)，10亿]</td>
        <td>Min[1万*已部署容量(GiB)，8亿]</td>
        <td>Min[3万*已部署容量(GiB)，15亿]</td>
        <td>Min[2万*已部署容量(GiB)，10亿]</td>
    <tr align="center" >
        <td>系统目录数上限</td>
        <td>1000万</td>
        <td>800万</td>
        <td>1500万</td>
        <td>1000万</td>
        <td>1000万</td>
        <td>800万</td>
        <td>1500万</td>
        <td>1000万</td>
    <tr align="center" >
        <td>文件名长度上限</td>
        <td>255字节</td>
        <td>255字节</td>
        <td>255字节</td>
        <td>255字节</td>
        <td>255字节</td>
        <td>255字节</td>
        <td>255字节</td>
        <td>255字节</td>
    <tr align="center" >
        <td>绝对路径长度上限</td>
        <td>4096字节</td>
        <td>4096字节</td>
        <td>4096字节</td>
        <td>4096字节</td>
        <td>4096字节</td>
        <td>4096字节</td>
        <td>4096字节</td>
        <td>4096字节</td>
    <tr align="center" >
        <td>目录深度上限</td>
        <td>1000</td>
        <td>16</td>
        <td>1000</td>
        <td>16</td>
        <td>1000</td>
        <td>16</td>
        <td>1000</td>
        <td>16</td>
    <tr align="center" >
        <td>单目录文件/子目录数量上限</td>
        <td>100万</td>
        <td>80万</td>
        <td>100万</td>
        <td>80万</td>
        <td>100万</td>
        <td>80万</td>
        <td>100万</td>
        <td>80万</td>
    <tr align="center" >
        <td>同时可打开文件数上限</td>
        <td>65536</td>
        <td>1000</td>
        <td>65536</td>
        <td>1000</td>
        <td>65536</td>
        <td>1000</td>
        <td>65536</td>
        <td>1000</td>
    <tr align="center" >
        <td>单文件锁数量上限</td>
        <td>512</td>
        <td>512</td>
        <td>512</td>
        <td>512</td>
        <td>512</td>
        <td>512</td>
        <td>512</td>
        <td>512</td>
    <tr align="center" >
        <td>客户端数量上限</td>
        <td>1000</td>
        <td>100</td>
        <td>1000</td>
        <td>100</td>
        <td>2000</td>
        <td>1000</td>
        <td>2000</td>
        <td>1000</td>
    </tr>
    <tr align="center" >
        <td>单客户端挂载文件系统数量上限</td>
        <td>1000</td>
        <td>16</td>
        <td>1000</td>
        <td>16</td>
        <td>16</td>
        <td>8</td>
        <td>16</td>
        <td>8</td>
    </tr>
    <tr align="center" >
        <td>计费限制</td>
        <td colspan="2">根据实际使用计费<br>（预付费除外）</td>
        <td colspan="2">根据实际使用计费<br>（预付费除外）</td>
        <td colspan="2">根据购买容量计费</td>
        <td colspan="2">根据购买容量计费</td>
    </tr>
    <tr align="center" >
        <td>支持协议</td>
        <td colspan="2">NFS/SMB</td>
        <td colspan="2">NFS</td>
        <td colspan="4">POSIX/MPI</td>
    </tr>
    <tr align="center" >
        <td>支持操作系统</td>
        <td colspan="4">Linux/Windows</td>
        <td colspan="4">Linux</td>
    </tr>
</table>


### 相关说明

#### Turbo 系列说明
- Turbo 系列通过私有客户端进行挂载，在安装客户端并使用命令 mount 后，与使用本地文件系统的方式没有区别。
- Turbo 系列采用容量购买的方式进行使用和计费。如购买40T的 Turbo 标准型，创建完成后，无论使用量为多少，均按40TiB的容量按小时计费。如使用一小时，其计费为：40\*1024\*0.6/24/30=34.13元，若需要删除可随时销毁文件系统。
- 为保证扩容后系统负载的均衡，在使用至集群80%容量左右时，应启动扩容。扩容支持在线扩容，整体过程业务无感知。
- Turbo 系列不支持对原文件系统缩容，可新建 Turbo 实例进行迁移后，然后对老实例进行删除的方式达到缩容的目的。
- Turbo 系列在初次创建时，因涉及到独立集群的重新搭建，约需20分钟左右，请耐心等待。
- Turbo 系列默认只支持root用户挂载使用，若需要普通用户挂载，可提交工单与我们联系。
- 若需要更高规格（支持更多文件数、目录数等）的 Turbo 系列，可提交工单与我们联系。


#### UID 与 GID 说明

- 当使用 NFS v3.0协议时，如果本地账户不存在文件所属的 UID 或 GID，则会直接显示 UID 和 GID；若 Linux 本地账户中存在文件所属的 UID 或 GID，则将会根据本地的 UID 和 GID 映射关系显示相应的用户名和组名。
- 当使用 NFS v4.0协议时，如果 Linux 内核版本高于3.0，则 UID 和 GID 规则与 NFS v3.0协议相同；若本地内核版本低于 3.0，则所有文件的 UID 和 GID 都将显示 nobody。

>! 在 Linux 内核版本低于3.0下使用 NFS v4.0 协议挂载文件系统时，建议不要对文件或目录执行 change owner 或 change group 操作，否则该文件或目录的 UID 和 GID 将变为 nobody。
>


#### CIFS/SMB 协议支持情况
- 协议版本支持：支持 CIFS，SMB 1.0及以上的 SMB 协议版本。但不建议使用 SMB 1.0协议挂载，因为 SMB 1.0与 SMB 2.0及以后的版本相比，由于协议设计的巨大差异在性能和功能的上有严重的不足，同时，由于支持 SMB 1.0或更早协议版本的 Windows 产品都已经完全退出微软支持的生命周期。
- 不支持用户用 NFS 和 SMB 访问同一个文件系统，不支持通过广域网直接访问 SMB 文件系统。
- 只提供在文件系统级的读写权限控制，不提供文件/目录级别的 ACL 权限控制。
- 不支持 Sparse files，文件压缩，网卡状态查询， 重解析点（Reparse Point）等 IOCTL/FSCTL 操作。
- 不支持交换数据流（Alternate Data Streams）。
- 不支持 SMB Direct，SMB Multichannel，SMB Directory Leasing，Persistent File Handle 等 SMB 3.0 及以上版本的一些协议功能。
 <!--
 * NFS v4.0 不支持的 Attributes 包括：FATTR4_MIMETYPE， FATTR4_QUOTA_AVAIL_HARD，FATTR4_QUOTA_AVAIL_SOFT，FATTR4_QUOTA_USED，FATTR4_TIME_BACKUP，FATTR4_TIME_CREATE，客户端将显示 NFS4ERR_ATTRNOTSUPP 错误。
 * NFS v4.0 不支持的 OP 包括：OP_DELEGPURGE，OP_DELEGRETURN，NFS4_OP_OPENATTR，客户端将显示 NFS4ERR_NOTSUPP 错误。
 * NFSv4 暂不支持 Lock 和 Delegation 功能。
 -->
