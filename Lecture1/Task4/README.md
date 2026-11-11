# Task 4: a cheap generator

A company uses a stream cipher with a weak generator. Your analysis shows that its keystream is just 4 numbers (0 to 255), repeated again and again. You know that the plaintext starts with the name `Anna`.

Fill in the `TODO`s in `cheap.py`: find the 4 numbers, then decrypt the whole message.

Hint: `i % 4` is the remainder after dividing `i` by 4, so it goes 0, 1, 2, 3, 0, 1, ...

## Run

```
python3 cheap.py
```

Python 3, no extra libraries.
