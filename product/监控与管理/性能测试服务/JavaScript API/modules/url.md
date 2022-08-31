## Namespaces（命名空间）
- [&quot;pts/url&quot;](https://cloud.tencent.com/document/product/1484/75837)

### Interfaces（接口）
- [URL](https://cloud.tencent.com/document/product/1484/75825)
- [URLSearchParams](https://cloud.tencent.com/document/product/1484/75827)


## Variables（变量）

[](id:url)
### URL

URL: { prototype: [URL](https://cloud.tencent.com/document/product/1484/75825); createObjectURL: *any*; revokeObjectURL: *any* }


#### Type declaration

- ##### prototype: [URL](https://cloud.tencent.com/document/product/1484/75825)

- ##### createObjectURL:function
- createObjectURL(obj: *Blob* | *MediaSource*): *string* 

 **Parameters**

   - ##### obj: *Blob* | *MediaSource*

  Returns *string*

  ##### revokeObjectURL:function

   - revokeObjectURL(url: *string*): *void*
  
 **Parameters**

  - ##### url: *string*

 #### Returns *void*



### URLSearchParams
URLSearchParams: { prototype: [URLSearchParams](https://cloud.tencent.com/document/product/1484/75827); toString: *any* }


#### Type declaration
- prototype: [URLSearchParams](https://cloud.tencent.com/document/product/1484/75827)
- toString:function
- toString(): *string*

 Returns *string*
