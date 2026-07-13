import sys, os

# Fix zh-CN
f1 = os.path.join(sys.argv[1], "zh-CN.js")
c1 = open(f1, "r", encoding="utf-8").read()
c1 = c1.replace("aiChat:\"AI\u95ee\u7b54\"", "aiChat:\"AI Agent\"")
open(f1, "w", encoding="utf-8").write(c1)
print("zh-CN done")

# Fix en-US
f2 = os.path.join(sys.argv[1], "en-US.js")
c2 = open(f2, "r", encoding="utf-8").read()
c2 = c2.replace("aiChat:\"AI Chat\"", "aiChat:\"AI Agent\"")
open(f2, "w", encoding="utf-8").write(c2)
print("en-US done")
