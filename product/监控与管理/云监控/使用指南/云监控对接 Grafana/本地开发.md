## 开发步骤
1. 环境准备
 - [Docker](https://docs.docker.com/get-docker/)
 - [Magefile](https://magefile.org/) 版本要求大于等于 1.11
 - [Go](https://golang.org/dl/) 版本要求大于等于 1.16
 - [Node.js](https://nodejs.org/en/download/) 版本要求大于等于 14
2. Fork 此项目后克隆到本地：
```bash
git clone https://github.com/YOUR_GIT_USER_NAME/tencentcloud-monitor-grafana-app.git
```
3. 安装依赖：
```bash
npm install
go mod vendor
```
4. 启动前端开发环境：
```bash
npm run watch
```
5. 启动后端开发环境：
```bash
mage -v
```
6. 在命令行中运行：
```bash
docker-compose up
```
7. 完成后，访问 `http://localhost:3000`即可。
8. 开发完成后通过 [Pull Request](https://github.com/TencentCloud/tencentcloud-monitor-grafana-app/pulls) 的方法提交代码请求合并。


## 在本地 Grafana 上运行
此外，您也可以将本项目克隆至本地 Grafana 的插件目录，重启本地 Grafana。请确保本地 Grafana 版本大于等于 7.3。
