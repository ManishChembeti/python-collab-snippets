def subArraySum(arr, n, sum_):

	currentSum = arr[0]
	start = 0
	i = 1
	while i <= n:

		while currentSum > sum_ and start < i-1:

			currentSum = currentSum - arr[start]
			start += 1

		if currentSum == sum_:
			print("Sum found between indexes % d and % d" % (start, i-1))

			return 1

		if i < n:
			currentSum = currentSum + arr[i]
		i += 1
	print("No subarray found")
	return 0


if __name__ == '__main__':
	arr = [15, 2, 4, 8, 9, 5, 10, 23]
	n = len(arr)
	sum_ = 23

subArraySum(arr, n, sum_)

