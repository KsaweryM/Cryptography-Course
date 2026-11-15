# Checks and sources behind the slides of Lecture 6

Not for students.

- `make_files.py`: makes every ready file of the tasks (Ed25519 keys from fixed seeds, the certificates of
  Tasks 4 and 5, copies of `signing.py` and `cert_tools.py`, the two real certificates of Task 7) and `bob.pem`
  for the slides. `python3 make_files.py` (cryptography 41 or newer). Ed25519 signatures are deterministic, so
  every run gives the same bytes.
- `signing.py`, `cert_tools.py`: the masters of the helper modules copied into the task folders.
- `bob.pem`: the certificate of bob.example (the result of Task 3), the source of the values on the slides in
  "The X.509 certificate" and "Encoding".
- `cov_leaf.pem`, `cov_we1.pem`: the certificate of www.coventry.ac.uk and its issuer WE1, saved on
  15 November 2026 with `openssl s_client -connect www.coventry.ac.uk:443 -servername www.coventry.ac.uk -showcerts`.
- `bbc_leaf.pem`: the certificate of www.bbc.co.uk, saved the same day in the same way.
