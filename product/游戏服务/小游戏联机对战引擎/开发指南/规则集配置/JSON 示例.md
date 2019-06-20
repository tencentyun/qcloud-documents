本文档主要介绍三种游戏场景的 JSON 示例 demo。


## 斗地主 1V1V1
- 匹配条件：按用户所拥有的积分值区间进行组队。
- 积分区间分别为：0 - 100积分、101 - 1000积分、1001 - 5000积分、5001 - 10000积分。

示例代码如下：
```
{
	"version": "V1.0",
	"teams": [{
		"name": "1v1v1",
		"maxPlayers": 3,
		"minPlayers": 3,
		"number": 1
	}],
	"playerAttributes": [{
		"name": "score",
		"type": "number"
	}],
	"rules": [{
		"type": "segment",
		"expression": "teams[i].players.score",
		"value": [
			[0, 100],
			[101, 1000],
			[1001, 5000],
			[5001, 10000]
		]
	}],
	"timeout": 20
}
```

## 实时对战 5V5
队伍之间的平均分相差在3以内，如果超过40秒未匹配上，将平均分相差调整到10，整个匹配的超时时间是2分钟。

示例代码如下：
```
{
	"version": "V1.0",
	"teams": [{
		"name": "5v5",
		"maxPlayers": 5,
		"minPlayers": 5,
		"number": 2
	}],
	"playerAttributes": [{
		"name": "score",
		"type": "number"
	}],
	"rules": [{
		"type": "deviation",
		"expression": "avg(teams[*].players.score)",
		"value": 3,
		"waitTimeSteps": [{
			"waitTimeSeconds": 40,
			"value": 10
		}]
	}],
	"timeout": 120
}
```

## 答题游戏 3V3
按地域和技能进行匹配。

示例代码如下：
```
{
	"version": "V1.0",
	"teams": [{
		"name": "3v3",
		"maxPlayers": 3,
		"minPlayers": 3,
		"number": 2
	}],
	"playerAttributes": [{
			"name": "area",
			"type": "number"
		},
		{
			"name": "skill",
			"type": "number"
		}
	],
	"rules": [{
		"type": "segment",
		"expression": "teams[i].players.area", //相同的地域进行组队
		"value": [
			[1, 1],
			[2, 2],
			[3, 3],
			[4, 4]
		]
	}, {
		"type": "segment",
		"expression": "avg(teams[*].players.area)", //相同的地域进行匹配
		"value": [
			[1, 1],
			[2, 2],
			[3, 3],
			[4, 4]
		]
	}, {
		"type": "deviation",
		"expression": "avg(teams[*].players.skill)", //两队的技能平均值相差不超过3
		"value": 3
	}],
	"timeout": 120
}
```
