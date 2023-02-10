## 接口描述
- **描述：**调用 ui.setMoreMenu，设置 webview 顶部 **...** 菜单中的选项复制链接并在浏览器中打开，默认不展示，设置后展示。
- **支持的版本：**2.20.0
- **是否需要鉴权：**否



## 代码示例
```plaintext
const { ui, HeaderMenuItem } = wemeet;
ui.setMoreMenu({
  menuList: [
    HeaderMenuItem.COPY_URL,
    HeaderMenuItem.EXTERNAL_BROWSER
  ],
})
  .then(() => {
    // console.log('success');
  })
  .catch((err) => {
    // console.log(err);
  });
```
