import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Remove icon props
c = c.replace(' icon="home-o"', "")
c = c.replace(' icon="chat-o"', "")
c = c.replace(' icon="user-o"', "")

# Add emoji spans before text
c = c.replace(
    ">{{ $t(\x27nav.home\x27) }}</van-tabbar-item>",
    '><span style="font-size:20px">\U0001f3e0</span> {{ $t(\x27nav.home\x27) }}</van-tabbar-item>'
)
c = c.replace(
    ">{{ $t(\x27nav.aiChat\x27) }}</van-tabbar-item>",
    '><span style="font-size:20px">\U0001f916</span> {{ $t(\x27nav.aiChat\x27) }}</van-tabbar-item>'
)
c = c.replace(
    ">{{ $t(\x27nav.my\x27) }}</van-tabbar-item>",
    '><span style="font-size:20px">\U0001f464</span> {{ $t(\x27nav.my\x27) }}</van-tabbar-item>'
)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
