# checks: the data of the Lecture 8 tasks

`make_files.py` makes the keys and data files of all tasks and copies the ready modules
(`signing.py`, `alice_key.py`, `bank_ready.py`, `schemes.py`) into the task folders:

```
cd Lecture8 && python3 checks/make_files.py
```

The Ed25519 and ECDSA keys come from fixed labels, so they never change. The RSA key is made once and kept in
`checks/alice_rsa_private.pem`; a second run reuses it. If you delete that file, the RSA numbers in Tasks 3, 4,
5 and 7 change, and the README files, the slides and the lecturer's guide must be updated.
`Task8/ecdsa_ready.py` is the source of the ECDSA code; the script imports it to sign the two games with one k.
At the end the script prints the constants written in the starter files of Tasks 1, 8 and 9.
