import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Add persistence logic after messages ref
old = """// 聊天消息
const messages = ref([
  { role: '\''assistant'\'', content: '\''你好！我是新闻资讯AI助手，可以帮你搜索新闻、查看分类热度等。请问有什么可以帮你的？'\'' }
]);"""

# Actually let me find the exact text
idx = c.find("const messages = ref(")
end = c.find(");", idx)
old_block = c[idx:end+2]

new_block = old_block + """

// 持久化对话记录
watch(messages, (val) => {
  sessionStorage.setItem('\''aiMessages'\'', JSON.stringify(val))
}, { deep: true })
try {
  const saved = sessionStorage.getItem('\''aiMessages'\'')
  if (saved) {
    const parsed = JSON.parse(saved)
    if (Array.isArray(parsed) && parsed.length > 0) {
      messages.value = parsed
    }
  }
} catch(e) {}"""

c = c.replace(old_block, new_block)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
