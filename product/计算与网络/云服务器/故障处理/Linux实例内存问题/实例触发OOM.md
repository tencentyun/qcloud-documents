## 现象描述
Linux 云服务器在内存使用率未占满的情况下触发了 OOM（Out Of Memory）。如下图所示：
![](https://main.qcloudimg.com/raw/72cbd63ac445a1caa8d82fa1e55ba5a5.png)

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
    <td>内存使用率过高</td>
    <td ><a href="#eax">检查内存使用率是否过高</a></td>
  </tr>
  <tr>
    <td>进程数超限</td>
    <td><a href="#step4">检查进程数是否超限</a></td>
  </tr>
  <tr>
    <td>系统可用内存低于 min_free_kbytes 值</td>
    <td><a href="#step02">检查系统可用内存是否低于 min_free_kbytes 值</a></td>
  </tr>
</tbody>
</table>

## 故障处理[](id:ProcessingSteps)
### 检查内存使用率是否过高[](id:eax)
参见 [内存使用率过高问题处理](https://cloud.tencent.com/document/product/213/54644#ProcessingSteps) ，查看实例是否内存使用率过高。若实例内存使用率正常，请 [检查进程数是否超限](#step4)。

### 检查进程数是否超限[](id:step4)
1. 参见 [日志报错 fork：Cannot allocate memory](https://cloud.tencent.com/document/product/213/54645)，核实进程数是否超限。若总进程数未超限，则执行下一步。
2. 登录云服务器，执行以下命令查看 `min_free_kbytes` 值。
```bash
sysctl -a | grep min_free
```
`min_free_kbytes` 值单位为 kbytes，下图所示 `min_free_kbytes = 1024000` 即为1GB。
![](https://main.qcloudimg.com/raw/18ac6c04962abfbf67132eab1a604167.png)
3. 执行以下命令，使用 VIM 编辑器打开 `/etc/sysctl.conf` 配置文件。
```bash
vim /etc/sysctl.conf
```
4. 按 **i** 进入编辑模式，修改 `vm.min_free_kbytes` 配置项。若该配置项不存在，则直接在配置文件中增加即可。
<dx-alert infotype="explain" title="">
建议修改 `vm.min_free_kbytes` 值为不超过总内存的1%即可。
</dx-alert>
5. 按 **Esc** 并输入 **:wq** 后，按 **Enter** 保存并退出 VIM 编辑器。
6. 执行以下命令，使配置生效即可。
```bash
sysctl -p
```

### 检查系统可用内存是否低于 min_free_kbytes 值[](id:step02)
可能是由系统可用内存低于 `min_free_kbytes` 值导致。`min_free_kbytes` 值表示强制 Linux 系统最低保留的空闲内存（Kbytes），如果系统可用内存低于设定的 `min_free_kbytes` 值，则默认系统启动 oom-killer 或强制重启。具体行为由内核参数 `vm.panic_on_oom` 值决定：
 - 若 `vm.panic_on_oom=0`，则系统会提示 OOM，并启动 oom-killer 杀掉占用最高内存的进程。
 - 若 `vm.panic_on_oom =1`，则系统会自动重启。
