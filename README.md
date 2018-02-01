# Page-Replacement-Simulation
Python implementation of various Page Replacement algorithms.

__Implementations for _Least Recently Used_ (lru.py), _Least Frequently Used_ (lfu.py), _Second Chance_ (sc.py), and _Random_ (rand.py) are provided.__

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
