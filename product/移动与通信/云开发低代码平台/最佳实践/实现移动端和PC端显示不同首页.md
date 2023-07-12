在搭建应用时我们可能会遇到不同端显示不同内容的需求，例如在移动端希望显示 A 页面，在 PC 端希望显示 B 页面，下面实践示例将对此类情况进行说明。
1. 创建一个应用，在应用中创建三个页面，分别是首页、移动端页面、PC 端页面。
![](https://qcloudimg.tencent-cloud.cn/raw/67d9e243a56dd423e3ad84cc57bbf903.png)
2. 在移动端页面添加一个文本组件，内容标注成**移动端页面**，在 PC 端页面添加一个文本组件，内容标注成 **PC 端页面**，这样可以区分不同页面。
 - 移动端
![](https://qcloudimg.tencent-cloud.cn/raw/62957b4ead5a20cdaa72ffd692c4dcf7.png)
 - PC 端
![](https://qcloudimg.tencent-cloud.cn/raw/25c3a47daaf1b7ba9ae3a4c1721bee65.png)
3. 打开代码编辑器，在首页 lifecycle 的 onPageLoad(query) 中添加判断应用端的代码。
![](https://qcloudimg.tencent-cloud.cn/raw/04d4b5e46f5660c6f08dac637dfda59d.png)
代码内容：
```JavaScript
const isMobile = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPad|iPod|iOS|ios|Android|Mobile|IEMobile)/i);
if(isMobile){
     app.navigateTo({
      pageId: 'u_yi_dongduan',    // 页面 Id 
      params: {key: 'value'},
    });
}else{
    app.navigateTo({
      pageId: 'pc_duan_shou_ye',    // 页面 Id 
      params: {key: 'value'},
    });
}
```
这段代码的功能逻辑是先通过 **navigator.userAgent.match** 方法判断当前应用端是否是移动端，然后根据判断结果进行不同页面的跳转。通过 JS 判断当前应用是什么端的方法有很多，用户也可以自行查询替换。
4. 设置完成以后发布该应用，通过不同端的切换可以看到不同的页面。
 - 移动端
![](https://qcloudimg.tencent-cloud.cn/raw/0df1ab60e3e577c5355fdd5df9b1c6b2.png)
 - PC 端
![](https://qcloudimg.tencent-cloud.cn/raw/3f1620873bce50765a7973554acfd276.png)
