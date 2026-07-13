import sys
c = open("D:\\Desktop\\news-api-FE\\src\\config\\api.js", "r", encoding="utf-8").read()
c = c.replace("http://", "")
open("D:\\Desktop\\news-api-FE\\src\\config\\api.js", "w", encoding="utf-8").write(c)
print("Done")
