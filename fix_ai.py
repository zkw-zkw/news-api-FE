import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()

# Remove aiChatConfig import
c = c.replace("import { aiChatConfig } from '../config/api';", "")

# Remove apiEndpoint and apiKey refs  
c = c.replace(
    "const apiEndpoint = ref(aiChatConfig.apiEndpoint);\nconst apiKey = ref(aiChatConfig.apiKey);",
    "// Now using backend API"
)

# Remove apiKey check
c = c.replace(
    "  if (!apiKey.value || apiKey.value === 'your-api-key-here') {\n    showToast('API Key未配置，请联系管理员');\n    return\n  }",
    ""
)

# Replace old fetchAIResponse with backend call
old_fetch = """const fetchAIResponse = async (userMessage) => {
  const allMessages = messages.value
    .filter(m => m.role === 'user' || m.role === 'assistant')
    .map(m => ({ role: m.role, content: m.content }));

  try {
    const response = await fetch(apiEndpoint.value, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey.value}`,
      },
      body: JSON.stringify({
        model: aiChatConfig.model,
        messages: allMessages,
        stream: false,
      }),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.error?.message || `HTTP error! status: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    
    const processChunks = async () => {
      let buffer = '';
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
      }
      
      try {
        const json = JSON.parse(buffer);
        const aiResponse = json.choices?.[0]?.message?.content || '';
        messages.value[messages.value.length - 1].content = aiResponse;
      } catch (e) {
        throw new Error('\u89e3\u6790\u54cd\u5e94\u5931\u8d25');
      }
    };

    await processChunks();
  } catch (error) {
    throw error;
  }
}"""

new_fetch = """const fetchAIResponse = async (userMessage) => {
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
}"""

c = c.replace(old_fetch, new_fetch)
open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
