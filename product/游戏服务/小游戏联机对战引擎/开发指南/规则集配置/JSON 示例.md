本文档主要介绍四种游戏场景的 JSON 示例 demo。



## 斗地主 1V1V1
- 匹配条件：按用户所拥有的积分值区间进行组队，在同一个积分区间内的玩家可被匹配在同一个斗地主房间
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

## 3V3 比赛。

- 组队条件：年龄在同一个阶段的人组成一队；1 - 12岁一组，13 - 18岁一组，19 - 30岁一组，31 - 100岁一组。  
- 队与队的匹配条件：每个团队平均技能相差在2以内的匹配在一个房间。

```
{
	"version": "V1.0",
	"teams": [{
		"name": "3v3", //3v3的比赛
		"maxPlayers": 3, //每支队伍最大人数3
		"minPlayers": 3, //每支队伍最小人数3
		"number": 2 //一共两个队
	}],
	"playerAttributes": [{
			"name": "age", //年龄，匹配时传入的参数
			"type": "number"
		},
		{
			"name": "skill", //技能，匹配时传入的参数
			"type": "number"
		}
	],
	"rules": [{
		"type": "segment",
		"expression": "teams[i].players.age", //根据年龄进行组队
		"value": [
			[1, 12],
			[13, 18],
			[19, 30],
			[31, 100]
		],
		"waitTimeSteps": [{
			"waitTimeSeconds": 10, //等待10s若匹配不上，放宽规则
			"value": [
				[1, 30],
				[31, 100]
			]
		}]
	}, {
		"type": "deviation",
		"expression": "avg(teams[*].players.skill)", //每个团队的平均技能
		"value": 2, //技能相差不大于2
		"waitTimeSteps": [{
			"waitTimeSeconds": 10, //等待10s若匹配不上，放宽规则
			"value": 5
		}]
	}],
	"timeout": 40
}
```


## 实时对战 5V5
队伍之间的平均分相差3以内，如果超过40秒未匹配上，将平均分相差调整到10，整个匹配的超时时间是2分钟。

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
按地域和技能进行匹配，相同地域的玩家被分到同一个房间；同一个房间内两队的技能平均值相差不超过3。

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
## 非对称匹配 1V5
房间中有1个国王，5个士兵；在同一个队的士兵，战斗力(power)在同一个区间内；国王队和士兵队的技能(skill)差值为2。

示例代码如下：
```
{
	"version": "V1.0",
	"teams": [
		{
			"name": "king",
			"maxPlayers": 1,
			"minPlayers": 1,
			"number": 1
		},
		{
			"name": "soldiers",
			"maxPlayers": 5,
			"minPlayers": 5,
			"number": 1
		}
	],
	"playerAttributes": [
		{
			"name": "wantToBeKing",
			"type": "number"
		},
		{
			"name": "power",
			"type": "number"
		},
		{
			"name": "skill",
			"type": "number"
		}
	],
	"rules": [
		{
			"type": "segment",
			"expression": "teams[king].players.wantToBeKing",
			"value": [
				[1,1]
			]
		},
		{
			"type": "segment",
			"expression": "teams[soldiers].players.wantToBeKing",
			"value": [
				[0,	0]
			]
		},
		{
			"type": "segment",
			"expression": "teams[soldiers].players.power",
			"value": [
				[1,3],
				[4,6],
				[7,10]
			]
		},
		{
			"type": "deviation",
			"expression": "avg(teams[*].players.skill)",
			"value": 2
		}
	]
}
```
