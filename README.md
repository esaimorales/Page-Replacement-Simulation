# Page-Replacement-Simulation
A Python implementation of various Page Replacement algorithms.

Implementations for the following algorithms are provided:
- _Least Frequently Used_ (lfu.py)
- _Least Recently Used_ (lru.py)
- _Second Chance_ (sc.py)
- _Random_ (rand.py)

A sample page call procedure is given in _numbers.txt_.

## How to Run:
```
python file_name.py CACHE_SIZE < numbers.txt
```
## Results
| Cache Size | LFU | LRU | Second Chance | Random |
| ---------- | --- | --- | ------------- | ------ |
| 10         |7963 |4248 |4248           |4561    |
| 50         |7690 |3942 |3967           |4057    |
| 100        |7313 |3727 |3747           |3843    |
| 250        |6483 |3405 |3384           |3463    |
| 500        |5300 |2904 |2911           |3011    |
