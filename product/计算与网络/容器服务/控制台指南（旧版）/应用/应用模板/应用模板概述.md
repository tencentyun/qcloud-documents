在腾讯云容器服务中可以将多个服务的部署信息，通过YAML形式的描述文本保存到应用模板中。通过应用模板和不同环境下的配置，可以快速的在不同环境中部署应用中的服务。更多关于应用管理的内容可以参考[应用管理概述][12]。

## 应用模板主要操作

- [创建应用模板][3]
- [删除应用模板][4]
- [更新应用模板][5]
- [查看应用模板][6]


## 编排语法能力说明

应用模板中依赖于编排语法对服务的部署信息进行说明。编排语法本质对服务部署信息描述的一套规则，用户按照这个规则来描述服务的部署信息，编排引擎对描述信息进行解析后，按照解析得到的参数对服务进行部署。

腾讯云容器服务应用模板的编排语法底层支持kubernetes的原生编排语法，关于kubernetes的编排语的详细说明可以参考[基础语法][8]。在kubernetes的编排语法的基础上支持变量替换，变量替换的详细说明可以参考[变量替换][9]。同时考虑到容器服务平台本身的能力，提供容器服务平台相关的扩展语法，具体的关于扩展语法的说明可以参考[扩展语法][10]。出于功能稳定闭环的考虑，容器平台对kubernetes的编排语法做了一定的限制。具体的限制说明可以参考[限制说明][11]。

  [1]: https://cloud.tencent.com/document/product/457/11951
  [2]: https://cloud.tencent.com/document/product/457/11944
  [3]: https://cloud.tencent.com/document/product/457/11949
  [4]: https://cloud.tencent.com/document/product/457/11950
  [5]: https://cloud.tencent.com/document/product/457/11954
  [6]: https://cloud.tencent.com/document/product/457/11955
  [7]: https://cloud.tencent.com/document/product/457/12199
  [8]: https://cloud.tencent.com/document/product/457/11957
  [9]: https://cloud.tencent.com/document/product/457/11956
  [10]: https://cloud.tencent.com/document/product/457/11956
  [11]: https://cloud.tencent.com/document/product/457/11959
  [12]: https://cloud.tencent.com/document/product/457/12198