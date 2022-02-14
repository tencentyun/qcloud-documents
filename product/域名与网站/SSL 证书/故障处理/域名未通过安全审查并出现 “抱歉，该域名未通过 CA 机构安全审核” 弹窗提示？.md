
## 现象描述
申请免费域名型（DV）SSL 证书时订单审核失败并收到以下提示：
```
抱歉，该域名未通过 CA 机构安全审查，无法申请域名型证书。请购买企业型或增强型证书，您也可尝试使用其他域名申请证书。
```

## 可能原因
由于 CA 机构的反钓鱼机制，一般是域名信息中包含敏感词，例如 bank、pay 等，会引起安全审查失败，同时部分不常用的根域名也可能会审核失败，例如，`www.qq.pw`、`www.qcloud.pw` 等以 .pw 根域名后缀的无法通过审核。以下为可能导致无法通过的域名敏感词汇，仅作示例，具体由 CA 机构定义：

<table >
<colgroup>
<col >
<col >
<col >
<col >
</colgroup>
<thead>
  <tr>
    <th>内、外网IP地址</th>
    <th>主机名</th>
    <th>live（不包含 .live 顶级域名）</th>
    <th>bank</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>banc</td>
    <td>ban.c</td>
    <td>alpha</td>
    <td>test</td>
  </tr>
  <tr>
    <td>example</td>
    <td>credit</td>
    <td>pw (包含 .pw 顶级域名)</td>
    <td>apple</td>
  </tr>
  <tr>
    <td>ebay</td>
    <td>trust</td>
    <td>root</td>
    <td>amazon</td>
  </tr>
  <tr>
    <td>android</td>
    <td>visa</td>
    <td>google</td>
    <td>discover</td>
  </tr>
  <tr>
    <td>financial</td>
    <td>wordpress</td>
    <td>pal</td>
    <td>hp</td>
  </tr>
  <tr>
    <td>lv</td>
    <td>free</td>
    <td>SCP</td>
    <td></td>
  </tr>
</tbody>
</table>


## 解决方案
您可参考以下两种方法解决问题：
- 购买非 DV 型 SSL 证书进行绑定您的域名。
- 申请其他不包含敏感词的域名。

