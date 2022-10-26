
<dx-alert infotype="explain" title="">
- 镜像更新记录以发布时间为顺序。
- 镜像发布按照地域灰度。若创建云服务器时，镜像不是更新记录中的最新版本，则可能是还未发布至该地域。
- 若您在控制台未找到更新记录中的某个镜像，可能是该镜像还未全量开放，详细信息请咨询 [腾讯云助手](https://cloud.tencent.com/product/tca)。
</dx-alert>

## 镜像更新记录

<table>
<thead>
<tr>
<th width="60%"><strong>更新特性</strong></th>
<th><strong>更新日期</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul class="params">
<li>禁用 firewalld\sssd\rngd 服务</li>
<li>卸载 microcode_ctl/nss-softokn/avahi 软件包</li>
<li>设置 keymap</li>
<li>设置 timezone</li>
<li>设置 kdump 启动依赖 cloudinit.target</li>
<li>repo 中配置 mirrors.tencentyun.com 为第一 url</li>
<li>/etc/rc.d/rc.local 文件权限修改为755</li>
<li>修复 /var/lib/ 下部分目录权限错误的问题</li>
</ul>
</td>
<td>2022-09-16</td>
</tr>
<tr>
<td>
<ul class="params">
<li>更新内核至 5.4.119-19.0010</li>
<li>更新其他用户态软件</li>
<li>更新镜像时间戳</li>
</ul>
</td>
<td>2022-07-27</td>
</tr>
<tr>
<td>
<ul class="params">
<li>OpenCloudOS 8.5上线公有云</li>
</ul>
</td>
<td>2022-03-04</td>
</tr>
</tbody></table>                                                 


<style>
 .params{margin-bottom:0px !important}
</style>

 

