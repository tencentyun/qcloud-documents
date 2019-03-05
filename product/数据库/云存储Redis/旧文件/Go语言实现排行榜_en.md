
```
package main

import (
	"fmt"
	"math/rand"
	"time"
	"strconv"
	"strings"
	"github.com/garyburd/redigo/redis"
)

func checkErr(err error) {
	if err != nil {
		panic(err.Error())
	}
}

func randomName(length int) string {
	rand.Seed(time.Now().UnixNano())
	rn := make([]string, length)
	for start := 0; start < length; start++ {
		ch := rand.Intn(3)
		switch ch {
		case 0:
			rn = append(rn, strconv.Itoa(rand.Intn(10)))
		case 1:
			rn = append(rn, string(rand.Intn(26) + 65))
		default:
			rn = append(rn, string(rand.Intn(26) + 97))
		}
	}
	return strings.Join(rn, "")
}

func main() {
	const TOTAL_SIZE = 10000
	redisServer := "localhost:6379"
	client, err := redis.Dial("tcp", redisServer)
	checkErr(err)
	defer client.Close()
	key := "Game Rank"
	client.Do("DEL", key)
	playerList := make([]string, 0)
	for i := 0; i < TOTAL_SIZE; i++ {
		playerList = append(playerList, randomName(8))
	}
	fmt.Println("*Input all " + strconv.Itoa(TOTAL_SIZE) + " players*")
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	for i := 0; i < len(playerList); i++ {
		score := r.Intn(5000)
		member := playerList[i]
		if i < 10 {
			fmt.Println("player: " + member + ", score: " + strconv.Itoa(score))
		}
		client.Do("ZADD", key, score, member)
	}
	fmt.Println("*more player......*")
	fmt.Println()
	fmt.Println("*" + key + "*")
	fmt.Println("*Top 100 players*")
	scoreList, err := redis.Strings(client.Do("ZREVRANGE", key, 0, 99, "WITHSCORES"))
	checkErr(err)
	loop := 0
	for i := 0; i < len(scoreList) - 1; i += 2 {
		player := scoreList[i]
		score := scoreList[i + 1]
		if loop < 10 {
			fmt.Println("player: " + player + ", score: " + score)
		}
		loop++
	}
	fmt.Println("*more player......*")
	fmt.Println("*" + key + "*")
	selectPlayer := playerList[0]
	rank, err := redis.Int(client.Do("ZREVRANK", key, selectPlayer))
	checkErr(err)
	fmt.Println("The rank of player " + selectPlayer + " is " + strconv.Itoa(rank))
}
```
The result is as follows:
![](https://mc.qcloudimg.com/static/img/f6743aeb0757050eb65db9b2c684c0a7/image.png)
