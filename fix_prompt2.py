import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Use \n (literal backslash-n) so it becomes \n escape sequence in the file
new_rule = "\\n9. \u63d0\u5230\u65b0\u95fb\u6807\u9898\u65f6\uff0c\u7528Markdown\u94fe\u63a5\u683c\u5f0f [\u6807\u9898](/news/detail/\u6570\u5b57)\uff0c\u4f8b\u5982 [\u6211\u56fdGDP\u589e\u957f5.2%](/news/detail/4)"

c = c.replace('\u4e0d\u8981\u81ea\u5df1\u7f16\u9020\u6570\u636e"', '\u4e0d\u8981\u81ea\u5df1\u7f16\u9020\u6570\u636e' + new_rule + '"')

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
