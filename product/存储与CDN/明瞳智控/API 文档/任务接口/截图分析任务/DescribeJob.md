## 功能描述
用于查询指定的任务。

## 请求

#### 请求示例

```plaintext
GET /project/<ProjectId>/jobs?ids=<JobId>&tag=AI HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。


#### 请求体
该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <JobsDetail>
    </JobsDetail>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息列表 |  Container |

Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                   | 类型      |
| :----------------- | :------------------ | :------------------------------------- | :-------- |
| Code               | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义     | String    |
| Message            | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义   | String    |
| JobId              | Response.JobsDetail | 任务的 ID                               | String    |
| Tag                | Response.JobsDetail | 任务的 Tag: AI                          | String    |
| State              | Response.JobsDetail | 任务的状态，为 Success、Failed 其中一个 | String    |
| CreationTime       | Response.JobsDetail | 任务的创建时间                         | String    |
| EndTime            | Response.JobsDetail | 任务的结束时间                         | String    |
| ProjectId          | Response.JobsDetail | 任务所属的项目 ID                       | String    |
| Input              | Response.JobsDetail | 该任务的输入资源地址                   | Container |
| Operation          | Response.JobsDetail | 该任务的规则和结果                     | Container |

Container 节点 Input 的内容：

| 节点名称（关键字） | 父节点                    | 描述               | 类型      |
| ------------------ | ------------------------- | ------------------ | --------- |
| Url                | Response.JobsDetail.Input | 媒体文件的下载地址 | String    |
| Decrypt            | Response.JobsDetail.Input | 媒体文件的解密方式 | Container |

Container 类型 Decrypt 的具体数据描述如下：

| 节点名称（关键字） | 父节点                            | 描述                                            | 类型   |
| ------------------ | --------------------------------- | ----------------------------------------------- | ------ |
| Key                | Response.JobsDetail.Input.Decrypt | 解密的 Key，当 Method 为 XIAOYI 时，此值对应 pwd      | String |
| Salt               | Response.JobsDetail.Input.Decrypt | 额外的处理参数，当 Method 为 XIAOYI 时，此值对应 uid | String |
| Method             | Response.JobsDetail.Input.Decrypt | 解密方法。可选值为 XIAOYI                      | String |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                        | 描述             | 类型      |
| ------------------ | ----------------------------- | ---------------- | --------- |
| AI                 | Response.JobsDetail.Operation | 任务参数         | Container |
| AIResult           | Response.JobsDetail.Operation | 分析结果         | Container |
| Notify             | Response.JobsDetail.Operation | 任务结果通知地址 | Container |

Container 类型 AI 的具体数据描述如下：

| 节点名称（关键字） | 描述                                    | 类型      |
| ------------------ | --------------------------------------- | --------- |
| Mode               | 分析类型。可选值为 SnapshotAnalysis  | String    |
| SnapshotAnalysis | 当 Mode 为 SnapshotAnalysis 时此值有效   | Container |

Container 类型 AI.SnapshotAnalysis 的具体数据描述如下：

| 节点名称（关键字） | 描述                           | 类型   |
| ------------------ | ------------------------------ | ------ |
| Type               | 分析类型。可选值为 Pet  | String |
| TimeInterval       | 时间间隔。                    | Integer |

Container 类型 AIResult 的具体数据描述如下：

| 节点名称（关键字） | 描述                                    | 类型      |
| ------------------ | --------------------------------------- | --------- |
| Mode               | 分析类型。可选值为 SnapshotAnalysis  | String    |
| SnapshotAnalysis | 当 Mode 为 SnapshotAnalysis 时此值有效   | Container |

Container 节点 AIResult.SnapshotAnalysis 的内容：

| 节点名称（关键字） | 描述                                         | 类型      |
| ------------------ | -------------------------------------------- | --------- |
| PetDetectResult    | 宠物识别结果，还有 BodyJointsDetectResult、CarDetectResult、CarTags、ChefcoatDetectResult 和 FacemaskDetectResult 五种类型可以选择| Container   |

Container 节点 PetDetectResult 的内容：

| 节点名称（关键字） | 描述                                                   | 类型      |
| ------------------ | ------------------------------------------------------ | --------- |
| FrameID            | 截帧 ID （从0开始）                                     | Integer    |
| Pets               | 识别的宠物                                            | Container   |
| Time               | 截图时间，单位 ms                                      | Integer |

Container 节点 Pets 的内容：

| 节点名称（关键字） | 描述                                                   | 类型      |
| ------------------ | ------------------------------------------------------ | --------- |
| Location            | 位置                                                | Container    |
| Name               | 宠物名称                                              | String   |
| Score               | 精彩度分数                                            | Integer |

Container 节点 Location 的内容：

| 节点名称（关键字） | 描述                                                   | 类型      |
| ------------------ | ------------------------------------------------------ | --------- |
| Height            | 高度                                                | Integer    |
| Width              | 宽度                                                | Integer   |
| X                 | X 坐标，原点为视频左上角，X 轴为横向。                      | Integer |
| Y                 | Y 坐标，原点为视频左上角，Y 轴为纵向。                      | Integer |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。


## 实际案例

#### 请求

```plaintext
GET /project/p893bcda225bf4945a378da6662e81a89/jobs?ids=jccddc41c27e711ebbff5874bc5b36868&tag=AI HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:iss.ap-beijing.myqcloud.com

```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
	<JobsDetail>
		<Code>Success</Code>
		<CreationTime>2021-11-24T11:48:18+0800</CreationTime>
		<EndTime>2021-11-24T11:48:35+0800</EndTime>
		<Input>
			<Url>https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/1637647200-1637650800-playlist.m3u8</Url>
		</Input>
		<JobId>in5caaca2b4cd911ec8707525400276c76</JobId>
		<Message/>
		<Operation>
			<AI>
				<Mode>SnapshotAnalysis</Mode>
				<SnapshotAnalysis>
					<TimeInterval>3</TimeInterval>
					<Type>Pet</Type>
				</SnapshotAnalysis>
			</AI>
			<AIResult>
				<Mode>SnapshotAnalysis</Mode>
				<SnapshotAnalysis>
					<BodyJointsDetectResult/>
					<CarDetectResult/>
					<CarTags/>
					<ChefcoatDetectResult/>
					<FacemaskDetectResult/>
					<PetDetectResult>
						<FrameID>0</FrameID>
						<Pets>
							<Location>
								<Height>178</Height>
								<Width>297</Width>
								<X>262</X>
								<Y>16</Y>
							</Location>
							<Name>cat</Name>
							<Score>79</Score>
						</Pets>
						<Time>0</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>1</FrameID>
						<Pets>
							<Location>
								<Height>181</Height>
								<Width>277</Width>
								<X>286</X>
								<Y>14</Y>
							</Location>
							<Name>cat</Name>
							<Score>70</Score>
						</Pets>
						<Time>3066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>2</FrameID>
						<Pets>
							<Location>
								<Height>181</Height>
								<Width>277</Width>
								<X>286</X>
								<Y>13</Y>
							</Location>
							<Name>cat</Name>
							<Score>69</Score>
						</Pets>
						<Time>6066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>3</FrameID>
						<Pets>
							<Location>
								<Height>181</Height>
								<Width>259</Width>
								<X>302</X>
								<Y>14</Y>
							</Location>
							<Name>cat</Name>
							<Score>64</Score>
						</Pets>
						<Time>9066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>4</FrameID>
						<Pets>
							<Location>
								<Height>174</Height>
								<Width>258</Width>
								<X>295</X>
								<Y>24</Y>
							</Location>
							<Name>cat</Name>
							<Score>55</Score>
						</Pets>
						<Time>12066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>5</FrameID>
						<Pets>
							<Location>
								<Height>178</Height>
								<Width>278</Width>
								<X>278</X>
								<Y>16</Y>
							</Location>
							<Name>cat</Name>
							<Score>57</Score>
						</Pets>
						<Time>15066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>6</FrameID>
						<Pets>
							<Location>
								<Height>179</Height>
								<Width>272</Width>
								<X>281</X>
								<Y>16</Y>
							</Location>
							<Name>cat</Name>
							<Score>64</Score>
						</Pets>
						<Time>18066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>7</FrameID>
						<Pets>
							<Location>
								<Height>171</Height>
								<Width>272</Width>
								<X>282</X>
								<Y>26</Y>
							</Location>
							<Name>cat</Name>
							<Score>52</Score>
						</Pets>
						<Time>21066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>8</FrameID>
						<Pets>
							<Location>
								<Height>176</Height>
								<Width>281</Width>
								<X>277</X>
								<Y>17</Y>
							</Location>
							<Name>cat</Name>
							<Score>68</Score>
						</Pets>
						<Time>24066</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>9</FrameID>
						<Pets>
							<Location>
								<Height>70</Height>
								<Width>34</Width>
								<X>305</X>
								<Y>196</Y>
							</Location>
							<Name>cat</Name>
							<Score>55</Score>
						</Pets>
						<Time>24333</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>10</FrameID>
						<Pets>
							<Location>
								<Height>67</Height>
								<Width>58</Width>
								<X>294</X>
								<Y>244</Y>
							</Location>
							<Name>cat</Name>
							<Score>54</Score>
						</Pets>
						<Time>30333</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>11</FrameID>
						<Pets>
							<Location>
								<Height>67</Height>
								<Width>89</Width>
								<X>230</X>
								<Y>261</Y>
							</Location>
							<Name>cat</Name>
							<Score>74</Score>
						</Pets>
						<Time>33333</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>12</FrameID>
						<Pets>
							<Location>
								<Height>69</Height>
								<Width>111</Width>
								<X>216</X>
								<Y>218</Y>
							</Location>
							<Name>dog</Name>
							<Score>50</Score>
						</Pets>
						<Time>36333</Time>
					</PetDetectResult>
					<PetDetectResult>
						<FrameID>13</FrameID>
						<Pets>
							<Location>
								<Height>67</Height>
								<Width>71</Width>
								<X>227</X>
								<Y>173</Y>
							</Location>
							<Name>cat</Name>
							<Score>61</Score>
						</Pets>
						<Time>39333</Time>
					</PetDetectResult>
					<PhoneDetectResult/>
					<RatDetectResult/>
					<SmokingDetectResult/>
					<ToqueDetectResult/>
					<Type>Pet</Type>
				</SnapshotAnalysis>
			</AIResult>
			<Notify>
				<ContentType>XML</ContentType>
				<Url>http://82.xx.xx.21:9081/receiveCallback/2021-11-24-iss-ai</Url>
			</Notify>
		</Operation>
		<ProjectId>pa3a3d92a1702403aa70d77bea30b73e4</ProjectId>
		<StartTime>2021-11-24T11:48:19+0800</StartTime>
		<State>Success</State>
		<Tag>AI</Tag>
	</JobsDetail>
</Response>
```


