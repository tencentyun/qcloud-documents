- [通过 JSON API 创建的存储桶和上传的对象，是否可以使用 XML API 管理？](#Q1)
- [XML API 与 JSON API 之间的关系？](#Q2)
- [XML API 和 JSON API 是否有性能差异？](#Q3)
- [XML API 与 JSON API 的密钥是否通用？](#Q4)
- [XML API 与 JSON API 的签名是否通用？](#Q5)
- [XML API 与 JSON API 设置的 ACL 权限是否通用？](#Q6)
- [XML API 与 控制台设置的 ACL 权限是否通用？](#Q7)
- [不小心通过云 API 密钥控制台修改了密钥，会有什么影响？](#Q8)
- [XML API 的签名鉴权和之前有什么不一样？](#Q9)
- [目前 XML API 有哪些功能？](#Q10)
- [V5 版本的 XML API 有什么新的功能？](#Q11)

-----


<span id="Q1"></span>
#### 1. 通过 JSON API 创建的存储桶和上传的对象，是否可以使用 XML API 管理？
可以，XML API 是基于 COS V4 的架构，可以通过 XML API 操作由 JSON API 产生的数据。
<span id="Q2"></span>
#### 2. XML API 与 JSON API 之间的关系？
V4 版本的 JSON API 接口即从 2016 年 9 月起用户接入 COS 使用的 API，上传域名为`<Region>.file.myqcloud.com`。V4 版本的 JSON API 接口将保持维护状态，可以正常使用但是不发展新特性。其与标准 XML API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容，域名不一致。
<span id="Q3"></span>
#### 3. XML API 和 JSON API 是否有性能差异？
同属一套架构，性能上无差异。
<span id="Q4"></span>
#### 4. XML API 与 JSON API 的密钥是否通用？
相互通用， 密钥可通过 [云 API 密钥控制台](https://console.qcloud.com/capi) 查看。
<span id="Q5"></span>
#### 5. XML API 与 JSON API 的签名是否通用？
相互不通用，XML API 和 JSON API 各自有各自的签名方式。详情请参考：
- [JSON API 签名](https://www.qcloud.com/document/product/436/6054)
- [XML API 签名](https://www.qcloud.com/document/product/436/7778)

<span id="Q6"></span>
#### 6. XML API 与 JSON API 设置的 ACL 权限是否通用？
相互不通用，XML API 和 JSON API 各自有各自的 ACL 权限。
<span id="Q7"></span> 
#### 7. XML API 与 控制台设置的 ACL 权限是否通用？
相互不通用，控制台的 ACL 与 JSON API 设置的 ACL 权限一致，目前控制台和 XML API 各自有各自的 ACL 权限。
<span id="Q8"></span>
#### 8. 不小心通过 [云 API 密钥控制台](https://console.qcloud.com/capi) 修改了密钥，会有什么影响？
密钥修改后，可能导致数据侧和 CDN 侧密钥不同步。如果遇到问题暂时无法解决，CDN 相关问题可通过重新绑定 CDN 加速域名，数据侧无法访问的问题可通过重新创建存储桶解决。
<span id="Q9"></span>
#### 9. XML API 的签名鉴权和之前（之前也有 XML API？？？？）有什么不一样？
支持跨账户授权，支持根账户之间的相互授权操作，支持根账户与子账户之间的相互授权操作。
<span id="Q10"></span>
#### 10. 目前 XML API 有哪些功能？
存储桶级别：创建、删除、查询、列出；
对象级别：创建、分块上传、追加上传、下载、查询、修改属性、删除。
<span id="Q11"></span>
#### 11. V5 版本的 XML API 有什么新的功能？
批量删除，跨域操作，生命周期管理，手动复制，跨区域自动复制，静态网站，表单上传，版本管理，回调，日志记录。
