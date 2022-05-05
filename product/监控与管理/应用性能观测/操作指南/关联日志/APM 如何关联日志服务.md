应用性能观测与腾讯云日志服务（CLS）打通，您可以在日志服务中关联调用链的 TraceID 信息，当应用出现故障时，可以通过调用链的 TraceID 快速关联到业务日志，及时定位分析并解决问题。 

## 前提条件

已了解并使用腾讯云日志服务，详情可参见 [日志服务相关指引](https://cloud.tencent.com/document/product/614)。

**支持上报方式（其它语言和协议将会陆续支持）**
- [Skywalking 协议上报（Java）](https://cloud.tencent.com/document/product/1463/57870)
- [Java 自研探针上报](https://cloud.tencent.com/document/product/1463/58198)


## 操作步骤
### 步骤1：在日志中关联 TraceID
不同语言不同协议注入 TraceID 方式不同，详情请查看以下文档指引，关联 TraceID。
- [关联 TraceID-skywalking 协议（Java）](https://cloud.tencent.com/document/product/1463/68741)
- [ 关联 TraceID-自研探针（Java）](https://cloud.tencent.com/document/product/1463/68737)

### 步骤2：在系统配置页面关联日志
1. 进入 [应用性能观测控制台-系统配置](https://console.cloud.tencent.com/apm/monitor/settings)。
2. 选择对应的业务系统，在日志关联页面配置相关信息。
 - 开启关联日志。
 - 选择对应的日志地域、日志集和日志主题。
3. 配置完后单击**保存**即可。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1785475da96eba265aa330733d42c60c.png)
	 
### 步骤3：在链路查询页面查看日志信息
1. 进入 [应用性能观测控制台-链路查询](https://console.cloud.tencent.com/apm/monitor/span)。
2. 选择对应的业务系统，找到对应的 TraceID，单击 TraceID 进入链路详情。
3. 在右侧窗口切换日志菜单，即可查看日志相关信息，排查故障。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e3feeb5df62e4e7d5712410249cc45cb.png)
