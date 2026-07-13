import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Replace old fetchAIResponse with new backend call
idx = c.find("const fetchAIResponse =")
idx2 = c.find("};", idx)
old_block = c[idx:idx2+2]

new_block = """const fetchAIResponse = async (userMessage) => {
  try {
    const response = await fetch('/api/ai/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userMessage, stream: false }),
    });
    const data = await response.json();
    if (data.code === 200) {
      messages.value[messages.value.length - 1].content = data.data.reply;
    } else {
      throw new Error(data.message || '\u8bf7\u6c42\u5931\u8d25');
    }
  } catch (error) {
    throw error;
  }
};"""

c = c.replace(old_block, new_block)

# Remove apiKey check in sendMessage
old_check = """  if (!apiKey.value || apiKey.value === 'your-api-key-here') {
    showToast('API Key\u672a\u914d\u7f6e\uff0c\u8bf7\u8054\u7cfb\u7ba1\u7406\u5458');
    return;
  }"""
c = c.replace(old_check, "")

# Remove "// Now using backend API" line left from previous fix
c = c.replace("\n// Now using backend API", "")

# Remove model ref (only used in old fetchAIResponse)
c = c.replace("\nconst model = ref(aiChatConfig.model);", "")

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
