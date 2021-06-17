本文介绍通过 LogListener 采集服务器快速导入其他日志主题的采集配置规则。

## 操作场景

LogListener 采集配置是指 LogListener 采集服务器在进行日志采集前所设置的采集路径、使用限制、采集模式等采集规则。采集配置规则导入功能支持用户新增或修改采集配置时导入已有日志主题的采集配置，快速配置 LogListener 采集规则，免去多日志主题配置重复的繁琐操作，提高采集配置效率。

>? 
> - 默认情况下，一个文件只能被一个 LogListener 配置采集。
> - 如果一个文件需对应多个采集配置，请给源文件添加一个软链接，并将其加到另一组采集配置中。
> - LogListener 2.3.9及以上版本才可以添加多个采集路径。

## 操作步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击【日志主题】，进入日志主题页面。
3. 选择已有的日志主题，单击该日志主题ID/名称，进入日志主题信息页面。
4. 选择【采集配置】页签，进入**采集配置**页面。
5. 单击左上角【导入配置规则】。
![image-20210603175204014](https://main.qcloudimg.com/raw/e67c53745011efd30cb5e8d915b283a1.png)
6. 在弹出浮窗显示配置规则列表窗口，选择目标日志主题的配置规则，单击【确定】即可导入当前日志主题的采集配置中。
![](https://main.qcloudimg.com/raw/543c04f4efeddd530f672894982fcca0.png)
>?
> - 列表默认展示当前地域所有日志主题支持跨地域日志主题配置规则导入。
> - 未配置采集路径的日志主题不可导入当前日志主题采集配置规则中。
>

## 采集模式

LogListener 支持通过 [单行全文格式](https://cloud.tencent.com/document/product/614/17421)、[多行全文格式](https://cloud.tencent.com/document/product/614/17422)、[单行完全正则格式](https://cloud.tencent.com/document/product/614/52365)、[多行完全正则格式](https://cloud.tencent.com/document/product/614/52366)、[JSON格式](https://cloud.tencent.com/document/product/614/17419)、[分隔符格式](https://cloud.tencent.com/document/product/614/17420) 采集文本日志。

