package main

import "fmt"

func removeDuplicates(nums []int) int {
	k := 0
	lastValue := nums[0] - 1
	second := false
	length := len(nums)
	offset := 0
	i := 0
	for i+offset < length {
		if nums[i+offset] > lastValue {
			lastValue = nums[i+offset]
			second = false
			nums[i] = nums[i+offset]
			k += 1
			i += 1
		} else {
			if second == false {
				second = true
				nums[i] = nums[i+offset]
				k += 1
				i += 1
			} else {
				offset += 1
			}
		}
	}
	return k
}

func main() {
	myNums := []int{1, 1, 1, 2, 2, 2, 3, 3}
	fmt.Println(myNums)
	fmt.Println(removeDuplicates(myNums))
	fmt.Println(myNums)
}
