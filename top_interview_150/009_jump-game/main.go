package main

import "fmt"

func canJump(nums []int) bool {
	var obstacleZeroAt int
	var obstacleUnavoidable = false
	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] == 0 && i != len(nums)-1 && obstacleUnavoidable == false {
			obstacleZeroAt = i
			obstacleUnavoidable = true
		}
		if obstacleUnavoidable == true && nums[i] > obstacleZeroAt-i {
			obstacleUnavoidable = false
		}
	}
	return !obstacleUnavoidable
}

func main() {
	fmt.Println("Hello Kitty!")
	//myNums := []int{7, 1, 5, 3, 6, 4}
	//fmt.Println(myNums)
	//fmt.Println(maxProfit(myNums))
}
