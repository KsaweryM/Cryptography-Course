# Task 2: lock the key file

## The situation

`server.key` is the private key of a web server: whoever has this file can pretend to be the server. Right now it is a plain PEM file that every user of the machine may read (`-rw-r--r--`). Mallory has an account on the same machine. She only needs to copy the file.

Two cheap protections: **encrypt the file** with a passphrase, and let **only the owner** read it (mode `600`).

![A web server with two key files. server.key, mode -rw-r--r--, starts with -----BEGIN PRIVATE KEY----- and base64 text; now anyone on the server can read it. Mallory copies it, and now she is the server. Below, server-locked.key, mode -rw-------, starts with -----BEGIN ENCRYPTED PRIVATE KEY----- and question marks: your job, a passphrase and mode 600. Mallory copies that one too: what does she get without the passphrase?](figure.svg)

## Goal

Write an encrypted copy of the key, check what Mallory gets from it without the passphrase, and allow only the owner to read the file.

## Ready for you

- `server.key`: an RSA key of 2048 bits, not encrypted.
- `PASSPHRASE` in `protect_key.py`.
- From the `cryptography` library: `serialization.load_pem_private_key(data, password=...)` reads a key; `key.private_bytes(...)` writes one.

## Steps

Write your code in place of the `TODO` comments in `protect_key.py`:

1. Read `server.key` and print its first line and its mode: `oct(os.stat("server.key").st_mode & 0o777)` (like `stat()` in C). Load it with `password=None` and print `key.key_size`.
2. Write the key to `server-locked.key`, encrypted with `serialization.BestAvailableEncryption(PASSPHRASE)`. Print the first line of the new file.
3. Play Mallory: load `server-locked.key` with `password=None`, then with `b"123456"`. Each try raises an exception; catch it with `try: ... except (TypeError, ValueError) as e:` and print `type(e).__name__` and `e`. Then load it with `PASSPHRASE`.
4. `os.chmod("server-locked.key", 0o600)` and print the new mode.

Hints: `data.split(b"\n")[0]` is the first line of `data`; `open(name, "wb").write(data)` writes bytes to a file.

## Expected output

The plain file loads without a password; the locked one does not, and its mode becomes `0o600`.

<details>
<summary>Check your answer</summary>

```
server.key starts with:   -----BEGIN PRIVATE KEY-----
server.key mode:          0o664
loaded without a password, RSA 2048 bits

server-locked.key starts with: -----BEGIN ENCRYPTED PRIVATE KEY-----

password None : TypeError: Password was not given but private key is encrypted
password b'123456' : ValueError: Bad decrypt. Incorrect password?
password PASSPHRASE : loaded, RSA 2048 bits

server-locked.key mode:   0o600
```

The first mode depends on your system (`0o644` on most Linux machines). On Windows, `chmod` can only make a file read-only, so the last line shows `0o666` or `0o444`: there the access rules (ACLs) do this job. The passphrase still has to live somewhere when the server starts; that is why big sites keep keys in hardware (HSM).

</details>

## Run

```
python3 protect_key.py
```

About 8 minutes. Python 3 and the `cryptography` library (`pip install cryptography`).
