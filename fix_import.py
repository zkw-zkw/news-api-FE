import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

c = c.replace(
    "import { ref, onMounted, nextTick, watch } from 'vue';",
    "import { ref, onMounted, nextTick, watch } from 'vue';\nimport { useRouter } from 'vue-router';"
)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
