import wordcloud
c=wordcloud.WordCloud()
f = open("TheZenofPython.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
c.generate(txt)
c.to_file("d:/wd.png")