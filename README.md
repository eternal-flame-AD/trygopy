# trygopy

[gopy](https://github.com/go-python/gopy)测试

```bash
./bind.sh

go install github.com/go-python/gopy

go build main.go

time python main.py
12195257
0:00:24.133682
python main.py  24.15s user 0.02s system 99% cpu 24.214 total

time ./main
12195257
Elapsed: 24.13421726s
./main  24.08s user 0.02s system 99% cpu 24.137 total
```