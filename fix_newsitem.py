import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()

# Add grid prop
c = c.replace(
    "    required: true\n  }",
    "    required: true\n  },\n  grid: {\n    type: Boolean,\n    default: false\n  }"
)

# Add :class binding to template
c = c.replace(
    '<div class="news-item" @click="goToDetail">',
    '<div class="news-item" :class="{ \'grid-mode\': grid }" @click="goToDetail">'
)

# Add grid CSS before closing style tag
c = c.replace(
    ".news-image img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  border-radius: 4px;\n}",
    ".news-image img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  border-radius: 4px;\n}\n\n.news-item.grid-mode {\n  flex-direction: column-reverse;\n  padding: 8px;\n  border-bottom: none;\n  border: 1px solid #f2f2f2;\n}\n\n.news-item.grid-mode .news-image {\n  width: 100%;\n  height: 100px;\n}\n\n.news-item.grid-mode .news-content {\n  margin-right: 0;\n  margin-top: 6px;\n}\n\n.news-item.grid-mode .news-title {\n  font-size: 14px;\n  margin-bottom: 4px;\n}"
)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("NewsItem done")
