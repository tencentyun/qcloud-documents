### 安装过于缓慢如何处理？
为保证安装速度和稳定性，建议您使用 cnpm 来完成安装，通过命令 `npm install -g cnpm --registry=https://registry.npm.taobao.org` 安装 cnpm，然后将所有使用的 npm 命令替换为 cnpm 即可。

### 输入 Serverless 指令为何不生效？
初始化项目时，必须保证当前目录下无 `serverless.yml` 文件，否则 CLI 会判断当前目录已经是 Serverless 项目，无法初始化应用。
