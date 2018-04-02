结束互动课堂后，开发者可以使用课堂录制 SDK 对结束的课堂进行离线录制，录制内容包括白板画面以及老师学生的摄像头画面。

## 一. 下载 `ReplayGroup` 中漫游消息
开始录制课堂视频前，需要下载历史的白板操作数据和音视频录制数据。可以由业务服务器使用云通信的 API 接口 [拉取群漫游消息](https://cloud.tencent.com/document/product/269/2738) 下载指定群组的漫游消息后，下发给课堂录制客户端。

后台 SDK 中下载漫游消息的操作如下：
```php
 //TimRestApi.php
 	/**
	 * 下载群组的漫游消息
	 * @param string $group_id 要操作的群组id
	 * @return array json格式的消息列表，失败时返回ErrorCode和ActionStatus
	 */
	public function download_group_message($group_id)
	{
		$rsp = array(
			'ErrorCode' => 0,
			'ActionStatus' => 'OK',
			'RspMsgList' => array()
		);

		// 1.开始第一次拉取漫游消息
		$msg = array(
			'GroupId' => $group_id,
			"ReqMsgNumber" => 20
		);
		$req_data = json_encode($msg);

		$ret = $this->api("group_open_http_svc", "group_msg_get_simple", $this->identifier, $this->usersig, $req_data);
		$ret = json_decode($ret, true);
		if ($ret['ErrorCode'] != 0) {
			$rsp = $ret;
			return $rsp;
		}

		$msg_list = array();
		$ret_msg = array();
		if (array_key_exists('RspMsgList', $ret)) {
			$ret_msg = $ret['RspMsgList'];
		}
		$next_seq = 0;

		if (count($ret_msg) > 0) {
			foreach ($ret_msg as $msg) {
				$msg_list[] = $msg;
			}
			$next_seq = end($ret_msg)['MsgSeq'];
		}

		SdkLog::info('download fist ramble msg: groupid=' . $group_id . ', next_seq=' . $next_seq);
		// 2.进行迭代地拉取漫游消息
		while ($next_seq > 0) {
			$msg = array(
				'GroupId' => $group_id,
				"ReqMsgNumber" => 20,
				'ReqMsgSeq' => $next_seq-1
			);
			$req_data = json_encode($msg);

			$ret = $this->api("group_open_http_svc", "group_msg_get_simple", $this->identifier, $this->usersig, $req_data);
			$ret = json_decode($ret, true);
			if ($ret['ErrorCode'] != 0) {
				$rsp = $ret;
				return $rsp;
			}

			$ret_msg = array();
			if (array_key_exists('RspMsgList', $ret)) {
				$ret_msg = $ret['RspMsgList'];
			}
			$next_seq = 0;

			if (count($ret_msg) > 0) {
				foreach ($ret_msg as $msg) {
					$msg_list[] = $msg;
				}
				$next_seq = end($ret_msg)['MsgSeq'];
			}
			SdkLog::info('download ramble msg: groupid=' . $group_id . ', next_seq=' . $next_seq);
		}

		$rsp['RspMsgList'] = $msg_list;
		return $rsp;
	}
```

## 二. 记录课堂录制结果
课堂录制客户端完成录制后，互动直播服务器会将课堂视频的 URL 信息回调给业务服务器，业务服务器可以获取到课堂视频的 URL 信息。由于互动直播后台会每 30 分钟生成一次录制文件，所以业务后台要等待所有录制文件的 URL 全部回调后才可以结束记录。

后台 SDK 处理互动课堂回调的操作如下：
```
	$fake_conf_id = $this->groupId;
	$replay = Replay::get_replay_by_fake_conf_id($fake_conf_id);
	
	// 回调事件表示为开始录制
	if ($this->eventType == 1)
	{
	// 判断为课堂录制的视频事件回调
	if ($replay != null) {
		$cur_num = $replay->get_url_num();
		$replay->set_url_num($cur_num + 1);
		$replay->save();
	}
	}
	else if ($this->eventType == 100) // 3.2 事件类型100表示录制完成处理
	{
	if ($replay == null) { // 课堂中的视频回调，教育ConfManager处理
		// ...
	}
	else { // 录制回放中的视频回调，将url存入replay中
		$urls = json_decode($replay->get_urls(), true);
		$urls[] = $this->videoUrl;
		$replay->set_urls(json_encode($urls));
		if ($replay->get_state() == Replay::CONF_STATE_FINISH_RECORDING
			|| $replay->get_url_num() == count($urls)) {
			$replay->set_state(Replay::CONF_STATE_READY);
		}
		$replay->save();
	}
```