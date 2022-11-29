如果用户要实现页面表单或列表打印时，可以通过低代码自定义 JS 方法把要打印的内容转换成图片，然后使用 `window.print()` 方法进行页面打印。

## 核心代码如下
```javascript
export default async function({event, data}) {
  console.log('打印', event, data)
  /**把内容转换成图片格式进行打印 */
  await new Promise((resolve,reject) => {
    const s = document.createElement('script')
    s.src= 'https://html2canvas.hertzen.com/dist/html2canvas.min.js'
    s.onload = resolve
    s.onerror = reject
    document.head.appendChild(s)
  })
   
  const element = document.querySelector(`#idXX`) // 选择到要打印的组件id或者class，转换为canvas，其中 idXXX 表示要打印的元素
  
  const hide_element = element.querySelector(`#idXXX`);// 选择要隐藏的元素，其中 idXXX 表示要隐藏的元素
  hide_element.style.visibility = 'hidden'
  
  if(!element) {
    throw new Error('要打印的内容不存在')
  }
  const { width, height } = element.getBoundingClientRect()
  const canvas = await window.html2canvas(element)

  // 打印
  let winPrint = window.open('', '', `left=0,top=0,width=${width},height=${height},toolbar=0,scrollbars=0,status=0`);
  winPrint.document.body.appendChild(canvas);
  winPrint.document.close();
  winPrint.focus();
  winPrint.print();
  hide_element.style.visibility = 'visible';// 恢复被隐藏的元素 ，其中 idXXX 表示要隐藏的元素
  winPrint.close();
}
```

## 最佳实践案例
创建空白页面，加入**标题**组件，标题属性为**合同打印**。
![](https://qcloudimg.tencent-cloud.cn/raw/55449916b5949d51af7a9bd716df9ae9.png)
增加**表单容器组件**，绑定目标数据源（举例：合同数据模型）。
![](https://qcloudimg.tencent-cloud.cn/raw/1afe7b093a83948197dff079786b2ff9.png)
增加**按钮**组件，命名**打印**。
![](https://qcloudimg.tencent-cloud.cn/raw/ca2eb0fcb5d2d012d17109d06eb53faf.png)
给“打印”按钮添加“点击”事件。
![](https://qcloudimg.tencent-cloud.cn/raw/cf360c4ce706bd2e8b04fca3c3ab1e71.png)
打开低码编辑器，在自定义方法 **print** 中拷贝上面的**核心代码**。
![](https://qcloudimg.tencent-cloud.cn/raw/33ea44d5c835b9f7f9f136591b13180f.png)
打开调试工具，找出到打印区域 div 的 id，当前举例 id 是“root”。
![](https://qcloudimg.tencent-cloud.cn/raw/9653aade4a39223af1f275000c792729.png)
如果希望在打印的时候不显示“提交”、“打印”按钮，可以找出这两组按钮 div 的 id，当前举例 id 是“id92”。
![](https://qcloudimg.tencent-cloud.cn/raw/84d71b1c86bb5aea864476529ffe47b6.png)
在代码编辑器中添加打印区域 id 和隐藏区域 id。
![](https://qcloudimg.tencent-cloud.cn/raw/dff2a5c1efbebb4096ef43e3c77ee3b2.png)
保存以后，回到表单页面，选择打印按钮，如下图实现打印。
![](https://qcloudimg.tencent-cloud.cn/raw/e59e2a889b86d63cb9a1e8a5f2ee818e.png)

