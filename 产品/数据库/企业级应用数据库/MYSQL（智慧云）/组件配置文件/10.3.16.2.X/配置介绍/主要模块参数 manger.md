```
<server>
    <local>
        <listen dev="eth1" port="37000" /> <!--网络监听： dev表示网卡接口  port暂时没有用上 -->
        <zookeeper quiet="1" iplist="10.238.24.227:2181,10.224.133.203:2181" db_use_iplist="" timeout="10000" rootdir="/test_poc_lvs" /> <!--zookeeper配置：quiet=”1” 表示 zk 进入安静模式，不会打印不必须要的信息; iplist
 表示 zk 的的 IP 列表;  rootdir 表示 zookeeper 上的根目录; timeout 表示 连接超时时间；db_use_iplist 表示 安装db模块的时候让db相应模块使用的iplist，为空时表示默认使用iplist； -->
        <kafkazk iplist="10.238.24.227:2181" rootdir="/kafka" /> <!--kafka集群zookeeper地址，是审计模块需要用的，一般保持与zookeeper的配置一致即可 -->
        <manager>
            <!--manager 模块的相关配置。  -->
            <Log>
                <!--Log日志的配置。  -->
                <log_info name="../log/sys_manager" log_size="1000000000" log_level="0" /> <!--log_info 是系统日志的配置，name 表示 sys 日志的存放位置，log_size 表示一个日志文件大小，log_level 表示日志级别。  -->
                <log_stat name="../log/stat_manager" log_size="1000000000" log_level="0" /> <!--log_stat 是状态日志的配置，name 表示 stat 日志的存放位置，log_size 表示一个日志文件大小，log_level 表示日志级别。  -->
            </Log>

            <tdsql_db version="10.1.9" /> <!--  数据库默认安装版本：version 为默认安装的版本。在任务没有指定数据库版本的时候，这个值才生效。 -->
            <gw_mode mode="1" start_port="15001" end_port="30000" reserved_count="10" used_count="8" dns_mode="lvs" /> <!-- gw_mode为开启网关分离模式配置：mode表示是否开启，start_port表示网关端口的起始地址，end_port表示网关端
口结束地址，reserved_count表示每次创建proxy group的步长，used_count表示每次创建proxy group的实际使用的端口数目；dns_mode表示采用的接入层模式，其中当改值为mysql表示是dns后台是数据库（如果为该配置的话还需要配置dns db的
地址）；该值为http时，表示通过http接口通知dns变更 ； 该值为lvs表示采用lvs模式（私有云采用的默认配置）。url表示dns_mode为http时，配置的http接口url。  -->

            <pwd_mode mode="file" /> <!-- pwd_mode表示机器密码获取方式：mode为file时，采用sshpass配置项的配置 -->

            <sshpass user="tdsql" password="Tpg2012++" port="36000" oc_enable="true" /> <!--sshpass 为 manager 连接后端机器配置：user 为连接的用户名，password 为连接的密码，port 为连接使用的端口号，oc_enable表示是否开启octool
传输命令的方式（使用该方式后端DB机器需要部署oc_agent模块）。  -->

            <stat logtodb="true" /> <!-- stat 为 manager 执行流程入库配置，logtodb 为是否入库 -->
            <db timeout="5" dbname="TDSQL_STAT" stat_tbname="M_JOB_FLOW1" user="manager" pass="1234">
                <!--与scheduler stat的配置类似 -->
                <master ip="10.238.24.227" port="4999" /> <!--  -->
            </db>
            <cgroup_mode value="on" /> <!--cgroup模式：是否开启cgroup进行资源隔离  -->
            <check_coldBackup days="7" /> <!--冷备检测：删除实例时检测最近几天是否有冷备  -->
            <gs_mode total_num="256" /> <!--groupshard分片数默认配置：total_num 为 groupshard 支持的最大分片数（任务请求中的分片不能超过这个值）。  -->
            <ms_maxdelay value="120" /> <!--扩容允许的最大主备延迟：小于设定值才能发起扩容  -->
            <assign_port value="4001" /> <!--数据库端口分配：value 表示端口起始位置。  -->
            <manager_db user="tdsqlsys_kp_new" password="CRDbJB/YAmIeIX6mWgsUg/9TfjU=" /> <!--连接数据库的用户：执行加用户等任务时需要使用，使用默认配置，千万不要变更  -->
            <db_entryption value="on" /> <!--数据库加密：只对能使用数据库文件加密的数据库版本生效，on表示开启，off表示关闭  -->
            <system_db value="" /> <!--默认系统库表： 判断是否是空库时使用；是预留的可扩展配置,库之间用逗号隔开，目前不用填写。 -->
        </manager>
    </local>
</server>
```
