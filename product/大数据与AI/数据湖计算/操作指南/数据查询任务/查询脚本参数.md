为方便用户使用脚本参数进行查询，数据湖计算DLC支持配置日期参数进行查询。
数据湖计算 DLC 标准日期格式为：yyyymmddhh24miss，通过${}命令将日期设为变量，变量分为日期、时间两个部分，结果为两部分之和。
- 日期部分，可以是任意日期格式或者系统预定义变量，如 yyyymmdd、yyyymm、yyyy-mm-dd、yy、dataDate。
- 日期变化部分，可以+/-N个周期，支持N/Nd、Nm、Nw、Nh、Nmi。兼容支持计算公式，如7*N、N/24。
举例

| 获取加减周期 | 方法 | 兼容格式 |举例| 
|---------|---------|---------|---------|
| 后 N 年	| ${yyyymmdd+Ny}|-| -| 
| 前 N 年	| ${yyyymmdd-Ny}	| -	| 前一年：${yyyymmdd-12m}：20190920| 
| 后 N 月	| -| ${yyyymmdd+Nm}	| -| $[add_months(yyyymmdd,N)]	| -| 
| 前 N 月	| ${yyyymmdd-Nm}	| $[add_months(yyyymmdd,-N)]	| <nobr>${yyyymmdd-1m}：20200820<br>${yyyymm}：202009<br>${dataDate-1m}：20200820| 
| 后 N 周	| ${yyyymmdd+Nw}	| ${yyyymmdd+7*N}	| -| 
| 前 N 周| 	${yyyymmdd-Nw}	| ${yyyymmdd-7*N}	| -| 
| 后 N 天| 	${yyyymmdd+N/Nd}	| 	-| -| 
| 前 N 天	| ${yyyymmdd-N/Nd}		| -| ${yyyymmdd-1}、${dataDate-1}| 
| 后 N 小时	| ${yyyymmddhh24+Nh}	| $[yyyymmddhh24+N/24]	| -| 
| 前 N 小时	| ${yyyymmddhh24-Nh}	| $[yyyymmddhh24-N/24]	| <nobr>${yyyymmddhh24-1h}：2020092014<br>${dataDate-1h}： 2020092014| 
| 后 N 分钟	| ${yyyymmddhh24mi+Nmi}	| $[yyyymmddhh24+N/24/60]	| -| 
| 前 N 分钟	| ${yyyymmddhh24mi-Nmi}	| $[yyyymmddhh24-N/24/60]| 	${yyyymmddhh24mi-10mi}、${dataDate-10mi}| 

>! 使用时需保证变量或变量中+/-前的格式符合日期标准格式，否则将无法被系统识别使用。
