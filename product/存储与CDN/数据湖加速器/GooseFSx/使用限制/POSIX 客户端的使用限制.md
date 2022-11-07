本文主要介绍数据加速器 GooseFSx POSIX 客户端的使用限制。

## 适用的操作系统

GooseFSx 的 POSIX 客户端支持 Linux 和 Windows 操作系统，推荐的操作系统版本如下表所示：

<table>
   <tr>
      <th>操作系统类型</td>
      <th>操作系统</td>
      <th>发行版</td>
      <th>内核版本</td>
   </tr>
   <tr>
      <td rowspan=16>Linux</td>
      <td rowspan=2>TLinux</td>
      <td>TLinux 2.6</td>
      <td>all</td>
   </tr>
   <tr>
      <td>TLinux 2.4</td>
      <td>all</td>
   </tr>
   <tr>
      <td rowspan=13>RHEL 或 CentOS</td>
      <td>8.4</td>
      <td>4.18.0-305.19.1.el8_4</td>
   </tr>
   <tr>
      <td>8.3</td>
      <td>4.18.0-240.22.1.el8_3</td>
   </tr>
   <tr>
      <td>8.2</td>
      <td>4.18.0-193.28.1.el8_2</td>
   </tr>
   <tr>
      <td>8.1</td>
      <td>4.18.0-147.8.1.el8_1</td>
   </tr>
   <tr>
      <td>8</td>
      <td>4.18.0-80.11.2.el8_0</td>
   </tr>
   <tr>
      <td>7.9</td>
      <td>3.10.0-1160.42.2.el7</td>
   </tr>
   <tr>
      <td>7.8</td>
      <td>3.10.0-1127.19.1.el7</td>
   </tr>
   <tr>
      <td>7.7</td>
      <td>3.10.0-1062.18.1.el7</td>
   </tr>
   <tr>
      <td>7.6</td>
      <td>3.10.0-957.54.1.el7</td>
   </tr>
   <tr>
      <td>7.5</td>
      <td>3.10.0-862.14.4.el7</td>
   </tr>
   <tr>
      <td>7.4</td>
      <td>3.10.0-693.2.2.el7</td>
   </tr>
   <tr>
      <td>7.3</td>
      <td>3.10.0-514.26.2.el7</td>
   </tr>
   <tr>
      <td>7.2</td>
      <td>3.10.0-514.26.2.el7</td>
   </tr>
   <tr>
      <td>Ubuntu</td>
      <td>20.04.3 LTS</td>
      <td>5.4.0-86-generic</td>
   </tr>
   <tr>
      <td rowspan=2>Windows</td>
      <td rowspan=2>Windows</td>
      <td>Windows 2016</td>
      <td>all</td>
   </tr>
   <tr>
      <td>Windows 2019</td>
      <td>all</td>
   </tr>
</table>

>? 若您的操作系统版本不在此表中，您可咨询 [在线客服](https://cloud.tencent.com/act/event/Online_service?from=doc_582) 寻求帮助。
>

## POSIX 客户端规格

| **项目**                          | **规格** | **说明**                                                     |
| --------------------------------- | -------- | ------------------------------------------------------------ |
| 单 GooseFSx 实例支持 POSIX 客户端个数 | 256        | 256个 POSIX 客户端可同时挂载一个 GooseFSx 实例。                      |
| 单 POSIX 客户端挂载 GooseFSx 实例个数 | 1      | 一个 POSIX 客户端只能挂载一个 GooseFSx 实例。 |
| POSIX 客户端最小配置 | 4核8GB        | POSIX 客户端推荐最小配置4核8GB内存。                      |
| POSIX 客户端开放端口 | <li>TCP：1191、22、10080、8445、60000-61000；<li> ICMP：ALL     |    POSIX 客户端开放必要端口，与 POSIX 客户端管理节点建立连接。详见 [POSIX 客户端安全组规则](https://cloud.tencent.com/document/product/1424/77956#rule)。                     |

>? 
> - 若在此表不能满足您的需求，或您有其他需求，您可咨询 [在线客服](https://cloud.tencent.com/act/event/Online_service?from=doc_582) 寻求帮助。
> - 请勿删除或覆盖 POSIX 客户端的 authorized_keys 文件，建议使用 `ssh copy` 命令追加写文件 authorized_keys，请勿使用 `scp` 命令覆盖写文件 authorized_keys。
> 
