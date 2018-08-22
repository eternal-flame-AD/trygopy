package main

import (
	"fmt"
	"time"

	"github.com/eternal-flame-AD/trygopy/trygopy"
)

func main() {
	start := time.Now()
	fmt.Println(trygopy.HeavyCalc(800000))
	duration := time.Since(start)
	fmt.Printf("Elapsed: %s", duration.String())
}
