# Task 9: measure the keystream

`rc4.py` is ready. Fill in the `TODO` in `measure.py`: for 100 000 random keys of 16 bytes, count how often each of the first three keystream bytes is 0.

If every value were equally likely, each percentage would be close to 0.39%. It takes a few seconds.

## Run

```
python3 measure.py
```

Python 3, no extra libraries.
