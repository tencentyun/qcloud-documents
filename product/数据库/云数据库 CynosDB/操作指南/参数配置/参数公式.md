TDSQL-C MySQL 版部分参数新增了公式化参数值能力，方便参数更智能地适配数据库，当实例规格发生变更时，使用公式设置的参数值会适应规格的变更而自动变化，使数据库始终保持最优或最稳定的状态。

## 注意事项
- 本次参数公式仅支持参数值为数值类型的参数，其余数据类型的参数值不支持公式化。
- 参数设置公式化数值后将随着实例规格的变更而变化，若您设置的公式计算出的参数值超过该参数限制的取值范围（最小值到最大值），则该参数取值会按照参数范围最近的边界值选取，即，若低于最小值，则参数取范围最小值，若高于最大值，则参数取范围最大值。
 示例：
 - 某参数根据设置的公式计算出的参数值为7，而该参数限制的取值范围为1 - 6，则参数取值为6。
 - 某参数根据设置的公式计算出的参数值为5，而该参数限制的取值范围为6 - 10，则参数取值为6。
- 导出为配置文件/从配置文件导入，均不支持公式化参数值，导出时将自动调整为整数值型。
- 为保证数据库可用性，目前仅支持部分参数进行公式化设置，更多参数敬请期待后续迭代。

## 参数公式说明
<table>
<thead><tr><th>参数公式化组成</th><th>名称</th><th>说明</th></tr></thead>
<tbody>
<tr>
<td rowspan="2">变量</td>
<td>DBinitMemory</td><td>实例规格的内存大小，整数型，单位为MB。</td></tr>	
<td>DBInitCpu</td><td>实例规格的 CPU 核数，整数型，单位为核。</td></tr>	
<tr>
<td rowspan="2">运算符</td>
<td>除法运算符（/）</td><td>用被除数除以除数，返回整数型商。如果计算结果为小数，会截断取整数部分。</td></tr>	
<td>乘法运算符（*）</td><td>两个乘数相乘，返回整数型积。如果计算结果为小数，会截断取整数部分。</td></tr>	
<tr>
<td rowspan="2">函数</td>
<td>MIN（）</td><td>返回整数型或者参数公式列表中最小的值。</td></tr>	
<td>MAX（）</td><td>返回整数型或者参数公式列表中最大的值。</td></tr>
</tbody></table>

**示例**：
若公式为 MAX(DBInitCpu/2,4)，则表明参数值为该实例的 CPU 除以2，与4进行对比，返回最大值。

## 支持参数公式的参数
以下参数为当前版本支持的参数公式，默认公式的数值部分均可自定义修改，您可根据业务需求自定义调整。

<table>
<thead><tr><th>参数</th><th>说明</th><th>默认公式</th></tr></thead>
<tbody>
<tr>
<td>binlog_cache_size</td><td>在事务期间，用于保存更改的二进制日志的内存缓冲区的大小。</td><td>MIN(DBInitMemory/4000 * 32768,2097152)</td></tr>	
<td>max_heap_table_size</td><td>此变量为设置 MEMORY 允许用户创建的表增长到的最大大小。
</td><td>MIN( DBInitMemory/1000 * 4194304,134217728)</td></tr>
<td>innodb_buffer_pool_size</td><td>缓冲池的大小（以字节为单位），InnoDB 缓存表和索引数据的内存区域。</td><td>min((DBInitMemory - 500), DBInitMemory*3/4)*1000000</td></tr>
<td>innodb_buffer_pool_instances</td><td>InnoDB 缓冲池划分的区域数。</td><td>MIN(DBInitMemory/2000,16)</td></tr>
<td>innodb_read_io_threads</td><td>InnoDB 中用于读操作的 I/O 线程数。</td><td>MAX(DBInitCpu/2,4)</td></tr>
<td>innodb_write_io_threads</td><td>InnoDB 中用于写操作的 I/O 线程数。</td><td>MAX(DBInitCpu/2,4)</td></tr>
<td>join_buffer_size</td><td>用于普通索引扫描、范围索引扫描和执行全表扫描的表连接的缓冲区的最小大小。</td><td>MIN(DBInitMemory*128,262144)</td></tr>
<td>max_connections</td><td>最大连接数。</td><td>MIN(DBInitMemory/4+500,100000)</td></tr>
<td>table_definition_cache</td><td>打开的表缓存实例的数量。</td><td>MAX(DBInitMemory*512/1000,2048)</td></tr>
<td>table_open_cache</td><td>表描述符缓存大小，可减少文件打开/关闭次数。</td><td>MIN(MAX(DBInitMemory*512/1000,2048), 65536)</td></tr>
<td>table_open_cache_instances</td><td>指 MySQL 缓存 table 句柄的分区的个数。</td><td>MIN(DBInitMemory/1000,16)</td></tr>
<td>thread_pool_size</td><td>该参数设置线程池中线程组的数量，默认值时表示线程组数与 CPU 数量一致。</td><td>MIN(DBInitCpu,64)</td></tr>
<td>thread_cache_size</td><td>应该在缓存中保留多少线程以供重用。</td><td>MIN(DBInitMemory/125+8,512)</td></tr>
<td>tmp_table_size</td><td>内部内存临时表的最大大小。</td><td>MIN(DBInitMemory/1000*4194304,134217728)</td></tr>
</tbody></table>


