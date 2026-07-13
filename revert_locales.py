import sys, os

d = sys.argv[1]
# Revert zh-CN
f1 = os.path.join(d, "zh-CN.js")
c1 = open(f1, "r", encoding="utf-8").read()
c1 = c1.replace('aiChat:"AI Agent"', 'aiChat:"AI\u95ee\u7b54"')
open(f1, "w", encoding="utf-8").write(c1)

# Revert en-US
f2 = os.path.join(d, "en-US.js")
c2 = open(f2, "r", encoding="utf-8").read()
c2 = c2.replace('aiChat:"AI Agent"', 'aiChat:"AI Chat"')
open(f2, "w", encoding="utf-8").write(c2)

print("Reverted")
