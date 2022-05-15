import re

class Parser:
    def __init__(self,filePath,name="Me"):
        self.filePath = filePath
        self.name = name
        self.regex = r'!\[[^\]]*\]\((.*?)\s*("(?:.*[^"])")?\s*\)'# found on stackoverflow, finds embedded images the accuracy is not so high

    def parse(self):
        parsedText=""
        with open(self.filePath,"r") as file:
            content = file.readlines()
            for line in content:
                content = line.split(f"{self.name}:")
                if len(content)>1:
                    if(re.findall(self.regex,content[1])):
                        continue
                    parsedText+=content[1].replace("\n","")
        with open("test.txt","w") as f:
            f.write(parsedText)
        return parsedText
