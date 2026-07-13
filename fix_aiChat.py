import sys, re

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Change aiChat from AI问答 to AI Agent
c = re.sub(r'aiChat:\s*"AI\u95ee\u7b54"', 'aiChat: "AI Agent"', c)
# Also change the English version if it exists
c = re.sub(r'aiChat:\s*"AI Chat"', 'aiChat: "AI Agent"', c)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
