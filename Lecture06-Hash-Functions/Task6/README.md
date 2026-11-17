# Task 6: a Git object id

## The situation

Bob keeps Alice's pancake recipe, `recipe.txt`, in a Git repository. Git does not name the file by its file name inside its database; it names it by a digest of its content, the **object id**. Bob ran `git hash-object recipe.txt` and got `e2fcdc71d93339fed5fc9b69eecf7c2b4712665c`. Can you get the same 40 hex digits with `hashlib` alone? And what happens to the id when Mallory changes one character of the recipe?

![A violet file recipe.txt (108 bytes): "Pancakes for four, 2 eggs, 250 ml milk...". In front of it a grey header "blob 108" followed by a zero byte. Both together go into a dark box SHA-1; out comes a brown object id "= ?" (40 hex digits), compared with what Git printed, e2fcdc71...4712665c. Below, Mallory in pink changes "2 eggs" into "3 eggs", and the new id is "= ?".](figure.svg)

## Goal

Compute Git's object id of a file yourself and compare it with the output of Git; see what one changed character does to it.

## Ready for you

- `git_id.py`: `GIT_SAYS`, the output of `git hash-object recipe.txt` (Git 2.43, 2026-11-17), and `content`, the bytes of the file.
- `recipe.txt`: the recipe, 108 bytes.

Git uses **SHA-1**, an older hash function with a 20-byte (160-bit) digest, written as 40 hex digits: `hashlib.sha1(data).hexdigest()`.

## Steps

1. The header: `b"blob " + str(len(content)).encode() + b"\0"`. `str(len(content)).encode()` writes the length in decimal ASCII digits, like `sprintf(buf, "%d", n)` in C; `b"\0"` is one zero byte, as at the end of a C string.
2. `object_id = hashlib.sha1(header + content).hexdigest()`. `header + content` joins the two byte strings, like two `memcpy` calls into one buffer.
3. `changed = content.replace(b"2 eggs", b"3 eggs")`, then the object id of `changed` in the same way.

## Expected output

`the same: True`, then an id after Mallory's change that has nothing in common with the first one.

<details>
<summary>Check your answer</summary>

```
header: b'blob 108\x00' (9 bytes)
my object id:  e2fcdc71d93339fed5fc9b69eecf7c2b4712665c
git says:      e2fcdc71d93339fed5fc9b69eecf7c2b4712665c
the same: True
after Mallory: ac97bb421067a34b98a0a7b7eded80535b9749d4
```

Git and you get the same id, because the id depends only on the content. If one character changes, the id changes completely, so Git notices any change of any file, and two equal files are stored only once.

</details>

## Run

```
python3 git_id.py
```

About 7 minutes. Python 3.8 or newer, no extra libraries. If you have Git: `git hash-object recipe.txt` prints the same id.
