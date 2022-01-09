print("hello world II")
print("whats up world II?")
print("what the heck?")
my_files=["eran.mp3", "yuval.txt" ,"avigal.txt" ,"ilanit.mp3"]
def is_mp3_file(filename):
    return filename.endswith(".mp3")

print(list(filter(is_mp3_file, my_files)))
