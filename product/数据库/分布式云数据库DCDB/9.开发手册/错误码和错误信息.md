
proxy 增加如下错误编码：

	#define ER_PROXY_GRAM_ERROR_BEGIN 600
	
	#define ER_PROXY_SANITY_ERROR 601           // "Sanity error: %s"
	#define ER_PROXY_GS_NOT_SUPPORT 602         // sql 类型不支持
	#define ER_PROXY_ORDERBY_INDEX_NEG 603      // order by index is negative
	#define ER_PROXY_ORDERBY_INDEX_TOO_BIG 604  // order by index is too big
	#define ER_PROXY_ORDERBY_TYPE_UNSUPPORT 605 // 不支持到 order by 用法
	#define ER_PROXY_GROUPBY_INDEX_NEG 606      // group by index is negative
	#define ER_PROXY_GROUPBY_INDEX_TOO_BIG 607  // group by index is too big
	#define ER_PROXY_GROUPBY_TYPE_UNSUPPORT 608 // 不支持的 group by 用法
	#define ER_PROXY_GET_AUTO_ID_FAILED 609     // 获取自增 id 失败
	#define ER_PROXY_TEANS_ROLLED_BACK 610      // 事务已经被回滚
	#define ER_PROXY_ONE_SET 611                // 当前 sql 应该被发往一个后端，但是不是
	#define ER_PROXY_CLIENT_HS_ERROR 612        // 解析客户端握手包出错
	#define ER_PROXY_ACCESS_DENIED_ERROR 613    // the length of readu_auth_switch_result is not 20，不应该出现
	#define ER_PROXY_TRANS_NOT_ALLOWED 614      // 事务中不允许执行的命令
	#define ER_PROXY_TRANS_READ_ONLY 615        // 只读事务中不允许执行的命令
	#define ER_PROXY_TRANS_ERROR_DIFFENT_SET 616    // 非 xa 事务中，只读 sql 使用了多个后端
	#define ER_PROXY_STRICT_ERROR 617           // strict 模式下，一次仅允许修改一个 set
	#define ER_PROXY_SC_TOO_LONG 618            // 后端断开时间过长，链接断开
	#define ER_PROXY_START_TRANS_FAILED 619     // 开启新的 xa 事务失败
	#define ER_PROXY_SC_RETRY 620               // server 已经 close，请重试上一条 sql
	#define ER_PROXY_SC_TRANS_IN_ROLLBACK_ONLY 621  // server 已经 close，当前事务处于 rollback
	#define ER_PROXY_SC_COMMIT_LATER 622        // server 已经 close，事务会在稍后提交
	#define ER_PROXY_SC_ROLLBACL_LATER 623      // server 已经 close，事务会在稍后回滚
	#define ER_PROXY_SC_IN_COMMIT_OR_ROLLBACK 624   //  server 在事务提交/回滚阶段 close
	#define ER_PROXY_SC_NEED_ROLLBACK 625       // server 已经 close，需要回滚当前事务
	#define ER_PROXY_SC_STATE_WILL_ROLLBACK 626 // server 已经 close，将会会滚
	#define ER_PROXY_XA_UNSUPPORT 627           // xa 目前不支持的命令
	#define ER_PROXY_XA_INVALID_COMMAND 628     // xa 命令不合法
	#define ER_PROXY_XA_GTID_INIT_ERROR 629     // gtid log 初始化失败
	#define ER_PROXY_XA_GET_SET_IP_PORT_FAILED 630  // 获取 set 地址失败
	#define ER_PROXY_XA_UPDATE_GTID_LOG_FAILED 631  // 更新 gtid log 失败
	#define ER_PROXY_MYSQL_PARSER_ERROR 632     // 嵌入式库 sql 解析失败
	#define ER_PROXY_ILLEGAL_ID 633             // kill id 不合法
	#define ER_PROXY_NOT_SUPPORT_CURSOR 634     // CURSOR_TYPE_READ_ONLY 暂不支持
	#define ER_PROXY_UNKNOWN_PREPARE_HANDLER 635    // 执行的 prepare 不明确
	#define ER_PROXY_SET_PARA_FAIL 636          // Set parameters failed
	#define ER_PROXY_SUBPARTITION_DEAY 637      // 处理二级分区发生错误
	#define ER_PROXY_NO_SUBPARTITION_ROUTE 638  // 没有获取到二级分区表的路由信息
	#define ER_PROXY_LOCK_MORE_TABLE 639        // 一次只可以锁定一张二级分区表
	#define ER_PROXY_GET_ROUTER_LOCK_FAIL 640   // 获取路由锁失败
	#define ER_PROXY_PART_NAME_EMPTY 641        // 分区名称为空
	#define ER_PROXY_SUB_PART_TABLE_IS_NONE 642 // 没有二级分区
	#define ER_PROXY_PART_TYPE_DENY 643         // 二级分区类型不支持
	#define ER_PROXY_PART_NAME_ILLEGAL 644      // 分区名不合法
	#define ER_PROXY_DROP_ALL_PARTITION_FAIL 645    //  删除所有分区失败，尝试直接删除表
	#define ER_PROXY_GET_OLD_PART_NUM_FAIL 646  // 获取表的分片数失败
	#define ER_PROXY_EMPTY_SQL 647              // empty sql，不会返回给客户端
	#define ER_PROXY_ERROR_SHARDKEY 648         // sk 必须为某一列
	#define ER_PROXY_ERROR_SUB_SHARDKEY 649     // 二级分区键失败
	#define ER_PROXY_SQLUSE_NOT_SUPPORT 650     // proxy 不支持这种用法
	#define ER_PROXY_DBFW_WHITE_LIST_DENY 651   // 不在白名单，被防火墙拒绝
	#define ER_PROXY_DBFW_DENY 652              // 防火墙拒绝
	#define ER_PROXY_INCORRECT_ARGS 653         // stmt 参数不正确
	#define ER_PROXY_SYSTABLE_UNSUPPORT_NON_READ_SQL 654    // 不支持非只读 sql 访问系统表
	#define ER_PROXY_TABLE_NOT_EXIST 655        // 表不存在
	#define ER_PROXY_SHARD_JOIN_UNSUPPORT_TYPE 656  // shard join 暂不支持的用法
	#define ER_PROXY_RECURSIVE_JOIN_DENY 657    // 递归 join 不支持
	#define ER_PROXY_JOIN_INTERNAL_ERROR 658    // join 异常
	#define ER_PROXY_SQL_TOO_COMPLEX 659        // sql 太复杂，groupshard 暂不支持
	#define ER_PROXY_INVALID_ARG_FOR_GTID_STATE 660 // gtid_state() 参数不合法
	#define ER_PROXY_CANT_SET_GLOBAL_AUTOCOMMIT_GS 661  // Global autocommit cannot be set in groupshard
	#define ER_PROXY_INVALID_VALUE_FOR_AUTOCOMMIT 662   // autocommit 值设置不合法
	#define ER_PROXY_XID_ERROR 663              // xid 不合法
	#define ER_PROXY_XID_GENERAT_FAILED 664     // xid 不能由用户指定
	#define ER_PROXY_CANT_EXEC_IN_INTER_TRANS 665   // "The command cannot be executed in internal transction"
	#define ER_PROXY_XID_TIME_ERROR 666         // "Unexpected time part of xid"
	#define ER_PROXY_XID_TIMEDIFF_TOO_LONG 667  // "timediff > 1800s, it's not safe to execute boost"
	#define ER_PROXY_SAVEPOINT_NOT_EXIST 668    // SAVEPOINT 不存在
	#define ER_PROXY_SC_TRANS_IN_ROLLED 669     // 事务已经会滚，由于 serevr 已经 close
	#define ER_PROXY_CANT_BOOST_IN_TRANS 670    // 事务中不允许执行 SQLCOM_BOOST
	#define ER_PROXY_TRANS_EXPECTED 671         // "A transaction is expected, this maybe a bug"
	#define ER_PROXY_EXTERNAL_TRANS 672         // 外部 xa 中不允许执行
	#define ER_PROXY_AUTO_INC_FAIL 673          // "Deal auto inc failed"
	#define ER_PROXY_CHECK_JOIN_FAIL 674        // "Check join failed"
	#define ER_PROXY_TABLE_TYPE_NOT_MATCH 675   // "Do not support shard-table operations in noshard instance"
	#define ER_PROXY_UNSUPPORT_NS_IN_INSERT 676 // "Do not support noshard and noshard_allset in insert sql"
	#define ER_PROXY_ALTER_SEQ_ID_FAIL 677      // Alter seq id failed
	#define ER_PROXY_ALTER_ID_ILLEGAL 678       // Alter seq id is illegal
	#define ER_PROXY_CANT_CHANGE_STEP 679       // "Current table use zk to get auto inc, do not support to change step: \'%s\'"
	#define ER_PROXY_ALTER_STEP_FAIL 680        // Alter step failed
	#define ER_PROXY_TOO_MUCH_TABLES 681        // 表的数量超过限制
	#define ER_PROXY_TABLE_EXISTED 682          // 表已经存在
	#define ER_PROXY_CREATE_STABLE_FAILED 683   // 创建shard表失败，复杂 sql 不能用来创建 shard 表
	#define ER_PROXY_DDL_DENY 684               // ddl 不允许的操作
	#define ER_PROXY_SHADKEY_ERROR 685          // SQL should not relate to subpartition tables
	#define ER_PROXY_NO_SK 686                  // reject nosk
	#define ER_PROXY_COMBINE_SQL_KEY 687        // Something went wrong
	#define ER_PROXY_GET_SK_ERROR 688           // sk 获取失败
	#define ER_PROXY_SHOW_FAILED 689            // proxy show 命令错误
	#define ER_PROXY_SET_FAILED 690             // proxy set 命令错误
	#define ER_PROXY_UNLOCK_FORMAT_ERROR 691    // sql 格式不正确
	#define ER_PROXY_UNLOCK_ROUTER_FAIL 692     // 释放路由锁失败
	#define ER_PROXY_LOCK_ROUTER_FAIL 693       // 加路由锁失败
	#define ER_PROXY_PROXY_CMD_FAIL 694         // 不支持的/*proxy*/ 命令
	#define ER_PROXY_PROCESS_RULE_FILE_FAILED 695   // dump_error
	#define ER_PROXY_GET_AUTO_NUM_ERROR 696     // 获取自增值失败
	#define ER_PROXY_SEQUENCE_NOT_EXIST 697     // sequence 不存在
	#define ER_PROXY_SEQUENCE_ERROR 698         // sequence 不合法
	#define ER_PROXY_SEQUENCE_ALREADY_EXIST 699 // sequence 已经存在
	#define ER_PROXY_SQL_RETRY 700              // sql 还未提交或回滚
	#define ER_PROXY_XA2PC_ABORT 701            // 2pc 失败，事务将会会滚
	#define ER_PROXY_XA2PC_COMMIT 702           // 2pc 失败，后续提交
	#define ER_PROXY_XA2PC_UNCERTAIN 703        // 2pc 失败，结果未知
	#define ER_PROXY_KILL_ERROR 704             // kill 失败
	#define ER_PROXY_TRACE_DENY	705		  // trace 模式下不允许执行的sql
	#define ER_PROXY_SQL_IMCOMPLETE 706		 // 事务状态不完整
	#define ER_PROXY_SHARDKEY_HASH_ERROR 709	// sk hash错误
	
	#define ER_PROXY_GRAM_ERROR_END 799         
	
	// system error -----------------------------------------------------------------------
	#define ER_PROXY_SYSTEM_ERROR_BEGIN 900
	
	#define ER_PROXY_SLICING 901                // slice 被修改，可能在扩容阶段，拒掉当前 sql
	#define ER_PROXY_NO_DEFAULT_SET 902         // set 为空
	#define ER_PROXY_GET_ADDRESS_FAILED 903     // 还未初始化完成，获取后端地址失败，稍后重试
	#define ER_PROXY_SQL_SIZE_ERROR_IN_GET_CANDIDATE_ADDRESS 904 // 获取后端地址出错（发往后端个数不正确）
	#define ER_PROXY_GET_ADDRESS_ERROR 905      // 获取后端地址出错
	#define ER_PROXY_CANDIDATE_ADDRESS_EMPTY 906 // 未获取到后端地址
	#define ER_PROXY_CANT_GET_SOCK 907          // socket 获取失败	
	#define ER_PROXY_GET_SET_SOCK_FAIL 908      // socket 获取失败
	#define ER_PROXY_CONNECT_ERROR 909          // 后端连接失败
	#define ER_PROXY_NO_SQL_ASSIGN_TO_SET 910   // 分发 sql 异常
	#define ER_PROXY_STATUS_ERROR 911           // group 状态异常，断开链接
	#define ER_PROXY_CONN_BROKEN_ERROR 912      // server close，sql 状态不正常
	#define ER_PROXY_UNKNOWN_ERROR 913          // proxy 未知错误
	#define ER_PROXY_ALL_SLAVES_UNAVAILABLE 914 // 所有备机不可用
	#define ER_PROXY_ALL_SLAVES_CHANGE 915      // 备机异常
	
	#define ER_PROXY_ERROR_END 916


>?其中900以上为系统错误，会通过 [云监控平台](https://console.cloud.tencent.com/monitor/overview) 进行告警。
