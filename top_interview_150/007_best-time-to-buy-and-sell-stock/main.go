package main

import "fmt"

func maxProfit(prices []int) int {
	maxProfit := 0
	currentLowest := prices[0]
	for i := 0; i < len(prices); i++ {
		if prices[i] > currentLowest {
			if prices[i]-currentLowest > maxProfit {
				maxProfit = prices[i] - currentLowest
			}
		} else {
			currentLowest = prices[i]
		}
	}
	return maxProfit
}

func main() {
	myNums := []int{7, 1, 5, 3, 6, 4}
	fmt.Println(myNums)
	fmt.Println(maxProfit(myNums))
}
