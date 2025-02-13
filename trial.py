import functools


def rabin(t, s):
    if len(s) > len(s):
        return -1

    # compute hash code for search and and text (of length s)
    BASE = 26
    t_hash = functools.reduce(
        lambda prev, curr: prev * BASE + ord(curr), t[: len(s)], 0
    )
    s_hash = functools.reduce(lambda prev, curr: prev * BASE + ord(curr), s, 0)
    power = BASE ** (len(s) - 1)

    for i in range(len(s), len(t)):
        # check is t_hash == s_hash and check for collision
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)
        # compute t_hash again efficiently
        t_hash -= power * ord(t[i - len(s)])
        t_hash = t_hash * BASE + ord(t[i])

    # check last seq
    if t_hash == s_hash and t[-len(s) :] == s:
        return len(t) - len(s)

    return -1


print(rabin("CGACGS", "CGS"))
