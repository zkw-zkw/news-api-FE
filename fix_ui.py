import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()

# Improve news-item styling
old = """.news-item {
  display: flex;
  padding: 12px 16px;
  border-bottom: 1px solid #f2f2f2;
  background-color: #fff;
}"""

new = """.news-item {
  display: flex;
  padding: 14px 16px;
  margin: 0 12px 8px;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}"""

c = c.replace(old, new)

# Improve news-title
c = c.replace("font-weight: 500;\n  margin: 0 0 8px;", "font-weight: 500;\n  margin: 0 0 6px;")

# Improve news-desc
c = c.replace("font-size: 14px;\n  color: #666;\n  margin: 0 0 8px;", "font-size: 13px;\n  color: #999;\n  margin: 0 0 6px;")

# Improve news-image border-radius
c = c.replace(".news-image img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  border-radius: 4px;", ".news-image img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  border-radius: 6px;")

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("NewsItem done")
