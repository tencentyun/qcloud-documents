## 现象描述
在 Linux 云服务器中创建新文件时，出现 **no space left on device** 报错。

## 可能原因
<table>
<thead>
  <tr>
    <th>可能原因</th>
    <th>处理措施</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>硬盘空间处于已满状态</td>
    <td ><a href="#diskSpaceFull">检查硬盘空间是否已满</a></td>
  </tr>
  <tr>
    <td>文件系统 inode 满</td>
    <td><a href="#inodeFull"> 检查文件系统是否 inode 满</a></td>
  </tr>
 <tr>
    <td>df du 处于不一致状态</td>
    <td><a href="#dfdu"> 检查 df du 是否不一致</a></td>
  </tr>
</tbody>
</table>

## 故障处理[](id:ProcessingSteps)
通过腾讯云的 VNC 登录进入服务器内部进行检查。
### 检查硬盘空间是否已满[](id:diskSpaceFull)

1. 登录云服务器，详情请参见 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
2. [](id:Step2)执行以下命令，查看硬盘使用率。
```shellsession
df -h
```
3. 定位硬盘使用率较高的挂载点，并执行以下命令进入该挂载点。
```shellsession
cd 对应挂载点
```
例如，如需 cd 系统盘挂载点，则执行 `cd /`。
4. 执行以下命令，查找占用空间较大的目录。
```shellsession
du -x --max-depth=1 | sort -n
```
根据定位到占用空间最大的目录容量情况，执行以下步骤：
   - 如果目录容量远低于硬盘总空间，请 [检查 df du 是否不一致](#dfdu) 步骤继续排查问题。
   - 如果目录容量较大，请执行 [步骤2](#Step2) 定位到占用空间较大的文件，综合业务情况评估是否可删除。若无法删除，请通过 [扩容云硬盘](https://cloud.tencent.com/document/product/213/34068) 扩大硬盘存储空间。


### 检查文件系统是否 inode 满[](id:inodeFull)
1. 登录云服务器，详情请参见 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
2. [](id:Step2)执行以下命令，查看硬盘使用率。
```shellsession
df -i
```
3. 定位硬盘使用率较高的挂载点，并执行以下命令进入该挂载点。
```shellsession
cd 对应挂载点
```
例如，如需 cd 系统盘挂载点，则执行 `cd /`。
4. 执行以下命令，查找文件个数最多的目录，解决该问题。该命令较耗时，请耐心等待。
```shellsession
find / -type f | awk -F / -v OFS=/ '{$NF="";dir[$0]++}END{for(i in dir)print dir[i]" "i}' | sort -k1 -nr | head
```


### 检查 df du 是否不一致[](id:dfdu)

#### 解决进程占用文件句柄问题
执行以下命令，查看占用文件的进程。
```shellsession
lsof ｜ grep delete
```
请根据返回结果，执行以下步骤：
 - kill 对应进程。
 - 重启服务。
 - 若较多进程占用文件句柄，可重启服务器。


#### 解决 mount 挂载嵌套问题 
1. 执行 mount 命令，mount 占用空间大的磁盘到 `/mnt`。例如：
```shellsession
mount /dev/vda1 /mnt
```
2. 执行以下命令，进入 `/mnt`。
```shellsession
cd /mnt
```
3. 执行以下命令，查找占用空间较大的目录。
```shellsession
du -x --max-depth=1 | sort -n
```
根据返回结果，综合业务情况评估是否可删除目录或文件。
4. 执行 umount 命令，umount 磁盘。例如：
```shellsession
umount /mnt
```
