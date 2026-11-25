# Task 12: SHA-3 and SHAKE

## The situation

Bob wants to try SHA-3, the sponge. First he checks Python's SHA3-256 against the test value of the standard FIPS 202. Then he tries SHAKE256, the member of the SHA-3 family that gives an output of any length: Bob needs 16 bytes for a short file id, 32 for a digest, 64 for key material. Does he get three unrelated values? And is the 32-byte SHAKE256 just SHA3-256 under another name?

![On the left the violet message "Hello, Bob!" goes into a dark box "sponge, 200-byte state" (a wide part "rate 136 bytes" and a grey part "capacity 64 bytes"). Out come four brown outputs: SHA3-256, 32 bytes, and SHAKE256 of 16, 32 and 64 bytes, each with "= ?". Between the SHAKE outputs the question "related?", between SHA3-256 and the 32-byte SHAKE256 the question "the same?".](figure.svg)

## Goal

Check SHA3-256 against FIPS 202; compare SHAKE256 outputs of 16, 32 and 64 bytes; compare SHA3-256 with the 32-byte SHAKE256.

## Ready for you

- `shake.py`: the test value `FIPS_SHA3_ABC`, the message `DATA` and the printing.

`hashlib.sha3_256(data)` works like `hashlib.sha256(data)`. `hashlib.shake_256(data).hexdigest(n)` asks the sponge for `n` bytes of output and returns them as `2n` hex digits.

## Steps

1. SHA3-256 of `b"abc"` as hex; compare it with `FIPS_SHA3_ABC`.
2. Predict first: how are the 16-, 32- and 64-byte outputs of SHAKE256 of `DATA` related? Print all three.
3. Predict first: is SHA3-256 of `DATA` equal to the 32-byte SHAKE256 of `DATA`? Print both and the comparison.

## Expected output

<details>
<summary>Check your answer</summary>

```
SHA3-256(abc): 3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532
the same as FIPS 202: True
SHAKE256, 16 bytes: 40f5cc49590a8d989f17be9eca705de2
SHAKE256, 32 bytes: 40f5cc49590a8d989f17be9eca705de2b617b959f0d3124e4ce21005b1272641
SHAKE256, 64 bytes: 40f5cc49590a8d989f17be9eca705de2b617b959f0d3124e4ce21005b12726419d1790de82b5e32f1ecac0eda0ee13c9ddc77cd6b0c540d9536fdeb8d5b6a99e
SHA3-256:           b58543c145f315ad2c9210b45c29c13e6c9fc5396a140d3b07f766925fda360e
SHAKE256, 32 bytes: 40f5cc49590a8d989f17be9eca705de2b617b959f0d3124e4ce21005b1272641
the same: False
```

A shorter output is the beginning of a longer one: the sponge absorbs the message once and then only reads (squeezes) more bytes from its state. So use one length for one purpose. SHA3-256 and SHAKE256 use the same permutation and the same 136-byte blocks, but their padding starts with different bits (FIPS 202: `01` for SHA3-256, `1111` for SHAKE), so the same message gives unrelated outputs.

</details>

## Run

```
python3 shake.py
```

About 5 minutes. Python 3.8 or newer (SHA-3 is in `hashlib` since Python 3.6), no extra libraries.

Want to see it move? The simulator: [ksawerym.github.io/Cryptography-simulators/hash/#9](https://ksawerym.github.io/Cryptography-simulators/hash/#9).
