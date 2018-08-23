package trygopy

import "math"

func isPrime(p int) bool {
	for i := 2; i <= int(math.Sqrt(float64(p))); i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}

func HeavyCalc(k int) int {
	s := 1
	for i := 0; i < k; i++ {
		s++
		for !isPrime(s) {
			s++
		}
	}
	return s
}
