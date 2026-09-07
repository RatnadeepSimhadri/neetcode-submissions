def concatenate(s1: str, s2: str) -> str:
    ans = s1 + s2
    return "Too long!" if len(ans) > 10 else ans


# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
