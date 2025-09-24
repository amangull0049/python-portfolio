word = "donkey"

with open("word.txt") as f:
    content = f.read()
    
newContent = content.replace(word, "#####")

with open("word.txt", "w") as f:
    f.write(newContent)