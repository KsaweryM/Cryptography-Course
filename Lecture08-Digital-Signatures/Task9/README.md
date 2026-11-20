# Task 9: whose key?

## The situation

Dave uses Alice's Notes app. To update, the app downloads three files from the update server: `update.sh`, its Ed25519 signature `update.sig`, and the public key `public_key.pem`. The folder `alice_server/` is what Alice's real server gives. The folder `mallory_server/` is what Dave gets when Mallory controls the server: her update, her signature, and her own public key, under the same file names. When Dave installed the app, Alice also built her public key into it (`BUILT_IN_KEY`).

![Two server folders: alice_server/ with update.sh, update.sig (by Alice), public_key.pem (Alice's); mallory_server/ with update.sh, update.sig (by Mallory), public_key.pem (Mallory's). Dave has the built-in key 64ecb2f9...9778ec42. Questions: each server checked with the key from the server: ?; Mallory's key = built-in key?; Mallory's update with the built-in key?](figure.svg)

## Goal

Check both servers the way a careless updater does (with the key from the server) and the way a careful one does (with the built-in key).

## Ready for you

- `signing.py` (Ed25519, as in Task 2): `load_public_key(path)`, `verify(public_key, data, signature)`, `key_hex(public_key)` (the 32 bytes of a public key as hex), `public_key_from_hex(text)`.
- `updater.py`: `read_file(path)` and `BUILT_IN_KEY`.

## Steps

Write your code in place of the `None` after each `TODO` in `updater.py`:

1. Read `alice_server/update.sh` and `alice_server/update.sig`, load `alice_server/public_key.pem`, and `verify`.
2. The same three lines for `mallory_server/`.
3. Compare `key_hex` of the key from Mallory's server with `BUILT_IN_KEY`.
4. Check Mallory's update and signature with `public_key_from_hex(BUILT_IN_KEY)`.

Before step 2, predict: will Mallory's update pass?

## Expected output

<details>
<summary>Check your answer</summary>

```
Alice's server, key from the server:   True
Mallory's server, key from the server: True
the key from Mallory's server is Alice's key: False
Mallory's server, built-in key:        False
```

With the key from the server, Mallory's update passes: her signature fits her key. A signature binds a message to a key; it does not say whose key it is. The key built into the app stops her. For a browser that talks to millions of servers, building in every key is impossible: Lecture 9 shows how certificates solve it.

</details>

## Run

```
python3 updater.py
```

About 7 minutes. Python 3 and the library `cryptography`.
