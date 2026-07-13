import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()
# Add template #icon slot wrapper around emoji spans
import re
# Find home tab item and add icon slot
c = re.sub(r'<van-tabbar-item to="/home">\s*<span[^>]*>\U0001f3e0</span>\s*',
           '<van-tabbar-item to="/home"><template #icon><span style="font-size:20px">\U0001f3e0</span></template>',
           c)
c = re.sub(r'<van-tabbar-item to="/aichat">\s*<span[^>]*>\U0001f916</span>\s*',
           '<van-tabbar-item to="/aichat"><template #icon><span style="font-size:20px">\U0001f916</span></template>',
           c)
c = re.sub(r'<van-tabbar-item to="/my">\s*<span[^>]*>\U0001f464</span>\s*',
           '<van-tabbar-item to="/my"><template #icon><span style="font-size:20px">\U0001f464</span></template>',
           c)
open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
