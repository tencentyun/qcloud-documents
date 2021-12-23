为了满足 Linux 用户的使用需求、编写和运行 Shell/Python 脚本、更自由地处理数据以及使用开源工具，MRP 支持 Cloud Shell 功能。在您使用之前，您需要先创建或加入一个项目，且该项目已开通 Shell 功能。



## 步骤1：编辑实验
1. 进入 [MRP 控制台](https://console.cloud.tencent.com/mrp)，单击左侧导航栏中的 **Cloud Shell**，页面底部将会弹出 Cloud Shell 操作区域。用户可在操作区域内编辑操作指令。Cloud Shell 中的基本操作指令与 Linux 相同，例如：展开目录‘ls’、创建文件夹‘mkdir’、文件夹跳转‘cd’等。
2. 在 Cloud Shell 中：
 - 当某目录下存在 INCAR、POSCAR、POTCAR 和 KPOINTS 文件，则该目录可被认为是一个 VASP 计算实验。
 - 当某文件夹中文件总数不超过10个，单个文件的大小不超过100M可被认为是一个 LAMMPS 实验。
3. Shell 支持上传文件功能，输入上传命令 ‘rz’ ，页面中弹出上传弹窗，用户将需要上传的文件拖入弹窗中，单击**确定**即可上传。同时用户上传的文件支持利用 vim 工具进行编辑。

## 步骤2：提交实验
1. 获取服务器机型信息 mrp cvm：输入命令后，页面将展示 MRP 平台当前可以调用的云服务器相关信息。信息内容包括：机型、CPU 和 GPU数目、内存、付费模式。其中 POSTPAID_BY_HOUR 和 SPOTPAID 分别表示按量付费和竞价实例，单位均为元/小时；--表示当前的计费模式下没有可调用的对应机型。
2. 提交实验 mrp submit：执行提交命令后，当前目录下的文件会被上传到用户的 [对象存储（COS）](https://cloud.tencent.com/document/product/213/4961) 和 [云服务器（CVM）](https://cloud.tencent.com/document/product/213)中，提交的实验会在实验列表中显示。

### mrp submit 命令参数

|  参数    | 是否可选                         | 参数释义                                                     |
| ---- | -------------------------------- | ------------------------------------------------------------ |
| -n   | 可选                  | 指定腾讯云服务器 CVM 的数量，默认值为1。                                    |
| -d   | 必填                             | device 的缩写，指定腾讯云服务器 CVM 的机型。                      |
| -c   | 可选 | 指定计费模式，当前包括竞价实例（SPOTPAID）和按量计费（POSTPAID_BY_HOUR）两种取值，默认值为  POSTPAID_BY_HOUR。 |
| -t   | 可选         | type 的缩写，指定计算软件的类型，包括 vasp_std、vasp_gam、vasp_ncl 和 lammps 四种可选类型，默认值为 vasp_std |
| -ppn | 可选  | 指定计算时每台腾讯云服务器 CVM 使用的核数，默认值为当前机器的总核数。对 GPU 版本的 VASP 计算，-ppn 的值始终等于 GPU 机型的卡数，不需要额外指定。  |
| -in  | 可选                             | 提交 lammps 实验时使用，用于指定 lammps 计算时的 in 文件。（为了保证实验的准确性，建议用户填写）。 |

### 实验示例
为了用户更好地理解提交实验指令，以下给出提交 VASP 和 LAMMPS 实验的示例：
- **VASP 提交示例**：
 - 示例：mrp submit -n 2 -d SA2.8XLARGE64 -c SPOTPAID -t vasp_std -ppn 16
 - 释义：调用2台竞价实例的 SA2.8XLARGE64 的机器做 VASP 计算，每台机器使用的总核数为16，vasp 版本为 vasp_std。
- **LAMMPS 提交示例**：
 - 示例：mrp submit -n 1 -d SA2.8XLARGE64 -c SPOTPAID -t lammps -ppn 4 -in in.melt
 - 释义：调用1台竞价实例的 SA2.8XLARGE64 的机器做 LAMMPS 计算，每台机器使用的总核数为4，in 文件为 in.melt。

## 步骤3：提交完成
1. 用户编辑完成 mrp submit 命令，单击回车即可提交实验。
2. 实验提交后，用户可在控制台 [实验列表](https://console.cloud.tencent.com/mrp) 页中查看实验状态，单击“实验名称”可查看实验计算详情。
3. 实验计算完成后，用户可查看并处理实验计算数据。详情请参考 [数据处理](https://cloud.tencent.com/document/product/1526/66698)。
