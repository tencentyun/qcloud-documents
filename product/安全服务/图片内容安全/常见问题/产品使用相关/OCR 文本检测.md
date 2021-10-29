### 图片中的文字是否可以识别？是否额外收费？
可以识别，不额外收费。您可以在线体验 [OCR 功能演示 Demo](https://cloud.tencent.com/act/event/ocrdemo)。

### OCR 的审核结果也会显示在文本控制台，会同时消耗文本套餐包吗？
OCR 检测出来的结果会显示在文本控制台的明细内，不会消耗文本套餐量。

### OCR 限制多少字节？
与文本内容安全相同，5000字节以内。

### OCR 是否支持英文和其他小语种、方言等审核？
目前暂不支持英语和其他小语种、方言（如粤语）等审核。如有需求，客户可提供自定义的英文和其他小语种的词库内容，添加到客户自定义词库中进行拦截。

### 图片 OCR 是否可以关闭模型打击？
可以关闭，但需要后台配置。如有需求可以 [提交工单](https://console.cloud.tencent.com/workorder/category)  申请配置。

### OCR 是否可以自行添加违规词、自行新增恶意类型？
- OCR 支持添加违规词。
 1. 在 [自定义库管理](https://console.cloud.tencent.com/cms/image/lib) > **自定义词库** 页面，创建自定义词库并添加违规词，详情请参见 [配置自定义词库](https://cloud.tencent.com/document/product/1125/37109#step5)。
 2. 创建自定义词库后，需要创建一个自定义审核策略，并将自定义词库配置到策略中，词库才会生效，详情请参见 [配置策略](https://cloud.tencent.com/document/product/1125/37109#step4)。
- 目前不支持新增恶意类型。
