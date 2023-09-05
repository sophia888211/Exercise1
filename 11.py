with open("file_to_read.txt", "r") as file:
        content = file.read()

count = content.count("terrible")

new_content = ""
words = content.split()
for i, word in enumerate(words):
        if word == "terrible":
                if (i + 1) % 2 == 0:
                        new_content += "pathetic "
        else:
                new_content += "marvellous "

else:
        new_content += word + " "

with open("result1.txt", "w") as file:
        file.write(new_content)

print("Total times the word 'terrible' appears:", count)

