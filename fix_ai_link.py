import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Add @click handler to messages container
c = c.replace("messages-container\" ref=\"messagesContainer\">", "messages-container\" ref=\"messagesContainer\" @click=\"handleLinkClick\">")

# Add useRouter import after existing imports
c = c.replace(
    "import { ref, computed, watch, onMounted, nextTick } from 'vue';",
    "import { ref, computed, watch, onMounted, nextTick } from 'vue';\nimport { useRouter } from 'vue-router';"
)

# Add router and handleLinkClick function before formatMessage
old_format = "const formatMessage = (content) => {"
new_format = '''const router = useRouter();
const handleLinkClick = (e) => {
  const link = e.target.closest("a");
  if (link && link.getAttribute("href") && link.getAttribute("href").startsWith("/")) {
    e.preventDefault();
    router.push(link.getAttribute("href"));
  }
};

const formatMessage = (content) => {'''
c = c.replace(old_format, new_format)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
