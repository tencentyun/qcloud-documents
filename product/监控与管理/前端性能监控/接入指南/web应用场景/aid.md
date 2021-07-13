 aid是 Aegis SDK 为每个用户设备分配的唯一标识，存储在浏览器的 localStorage 。用于区分用户计算 uv 等。只有用户清理浏览器缓存 aid 才会更新。

## 前提条件
参考 [安装和初始化]() 文档，选择任意一种方式完成前端性能监控 SDK 的安装和初始化。

## aid

您可以根据下列算法自定义 aid 上报规则：

<dx-codeblock>
:::  js
async getAid(callback: Function) {
// 某些情况下操作 localStorage 会报错.
  try {
    let aid = await localStorage.getItem('AEGIS_ID');
    if (!aid) {
    aid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
      const r = (Math.random() * 16) | 0;
      const v = c === 'x' ? r : (r &amp; 0x3) | 0x8;
      return v.toString(16);
    });
    localStorage.setItem('AEGIS_ID', aid);
    }
    callback?.(aid || '');
  } catch (e) {
    callback?.('');
  }
}
:::
</dx-codeblock>


>?若您需要使用自己构造的 aid 作为上报规则，需要后端对 aid 的校验规则，规则如下：`/^[@=.0-9a-zA-Z_-]{4,36}$/` 。 
