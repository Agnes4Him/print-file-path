import os

# PRINT LOCAL FILE PATH

folder = os.getcwd()
contents = os.listdir(folder)
for content in contents:
    if content.endswith(".py"):
        current_file = content
full_path = "{}/{}".format(folder, current_file)
print (full_path)