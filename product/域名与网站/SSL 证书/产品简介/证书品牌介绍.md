## 证书品牌以及型号
腾讯云目前支持四种品牌 SSL 证书的售卖，详细如下：
<table>
<tr>
<th>证书品牌</th>
<th>描述</th>
</tr>
<tr>
<td>SecureSite</td>
<td><li>SecureSite 是全球最大的信息安全厂商和服务商，最权威的数字证书颁发机构，为企业、个人用户和服务供应商提供广泛的内容和网络安全解决方案。</li><li>全球500强中有93%选择了 VeriSign SSL 数字证书，SecureSite 于2010年8月收购 VeriSign，并于2012年4月对 VeriSign 的产品名称和品牌标识进行变更，目前 VeriSign 认证服务均由 SecureSite 提供。</li></td>
</tr>
<tr>
<td>GeoTrust</td>
<td><li>GeoTrust 是全球第二大数字证书颁发机构（CA），也是身份认证和信任认证领域的领导者，该公司各种先进的技术使得任何大小的机构和公司都能安全地低成本地部署 SSL 数字证书和实现各种身份认证。</li><li>从2001年成立到2006年占领全球市场25%的市场份额， VeriSign 于2006年5月 - 2006年9月以1.25亿美元收购 GeoTrust，目前也同为 SecureSite 旗下 SSL 证书的性价比高的品牌。</li></td>
</tr>
<tr>
<td>TrustAsia</td>
<td><li>亚洲诚信是亚数信息科技（上海）有限公司应用于信息安全领域的品牌，是 SecureSite 的白金合作伙伴，专业为企业提供包含数字证书在内的所有网络安全服务。</li><li>TrustAsia 品牌 SSL 证书由 SecureSite 根证书签发。</li></td>
</tr>
<tr>
<td>GlobalSign</td>
<td><li>GlobalSign 成立于1996年，是一家声誉卓著，备受信赖的 CA 中心和 SSL 数字证书提供商，在全球总计颁发超过2000万张数字证书。</li><li>GlobalSign 的专业实力获得中国网络市场众多服务器、域名注册商、系统服务供应商的青睐，成为其数字证书服务的合作伙伴。</li></td>
</tr>
</table>

## 品牌差异
不同品牌的证书在浏览器地址栏、加密强度、赔付保障上均存在差异，最重要的差异点在于根证书。例如，GeoTrust 通配符是 GeoTrust 根证书签发的，而 SecureSite 通配符是 SecureSite 根证书签发的。SecureSite 根证书可以兼容市面上所有的浏览器，对移动端的支持也是最好的，而 Trustasia 通配符也是 SecureSite 的根证书，GlobalSign 通配符是 GlobalSign 的根证书签发的。

单纯从技术角度，SecureSite（原 Verisign）和 GeoTrust 的区别如下：
- 算法支持上 SecureSite（支持 RSA、DSA、ECC 三种算法）优于 GeoTrust（支持 RSA、DSA 两种算法）。
- 兼容性 SecureSite 优于 GeoTrust，SecureSite 可兼容市面上所有的浏览器，对移动端的支持也是极好的。
- OCSP 响应速度上 SecureSite 优于 GeoTrust。
- CA 安全性方面 SecureSite 优于 GeoTrust，SecureSite 是国际知名安全厂商，CA 的安全级别也是国际第一的安全系数。
- SecureSite 证书除实现加密传输以外，还另外有恶意软件扫描和漏洞评估的附加功能。
- SecureSite 对证书有商业保险赔付保障，金额最高为175万美金，GeoTrust 最高为150万美金。
