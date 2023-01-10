用户对应的角色勾选 API 接口的访问权限以后，用户才能发起或调用 API 接口实现的逻辑，例如数据的增删查改，组件触发对应 API 接口时，如果具备此方法调用权限，则执行此方法；如果不具备此方法调用权限，则拦截此方法执行，并提示“当前用户无权限访问 API 接口，请联系管理员授权访问权限”。如果用户有 API 接口权限不满足的提示，开发者或企业管理员可以在 API 接口权限单击方法权限设置进行修改，入口如下图：
<img src = "https://qcloudimg.tencent-cloud.cn/raw/60a8096d1375696fa9989eace38a797d.png"  style = "width:80%"> 
可以选中此角色允许访问的方法。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/c6a6e9927a7fdeb55a326375aeade3ef.png"  style = "width:80%"> 
