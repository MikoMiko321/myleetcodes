package main

import "fmt"

func getNextElemAddress(nums []int, current int, k int) (nextElemAddress int) {
	var overflow int
	if len(nums)-current > k {
		nextElemAddress = current + k
	} else {
		overflow = k - (len(nums) - current)
		nextElemAddress = overflow % len(nums)
	}
	return nextElemAddress
}

func rotate(nums []int, k int) {
	var numsCopy []int

	for _, num := range nums {
		numsCopy = append(numsCopy, num)
	}

	for i := 0; i < len(nums); i++ {
		nums[getNextElemAddress(numsCopy, i, k)] = numsCopy[i]
	}
}

func main() {
	myNums := []int{1, 2, 3, 4, 5, 6}
	fmt.Println(myNums)
	rotate(myNums, 4)
	fmt.Println(myNums)
}
