 aid 是 Aegis SDK 为每个用户设备分配的唯一标识，存储在小程序的 storage 。用于区分用户计算 UV 等。只有用户清理小程序缓存 aid 才会更新。

## 前提条件
参见 [安装和初始化](https://cloud.tencent.com/document/product/1464/58566) 文档，选择任意一种方式完成前端性能监控 SDK 的安装和初始化。

## aid

您可以根据下列算法自定义 aid 上报规则：

<dx-codeblock>
:::  js
aid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
const r = (Math.random() * 16) | 0;
const v = c === 'x' ? r : (r & 0x3) | 0x8;
return v.toString(16);
:::
</dx-codeblock>
