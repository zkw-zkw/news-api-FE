import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()

# Add :grid prop to news-item
c = c.replace("<news-item", "<news-item :grid=\"layoutMode === 'grid'\"")

# Remove deep selectors for news-item internals, keep van-list grid
old_css = ".home.grid :deep(.van-list) { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }\n.home.grid :deep(.news-item) { flex-direction: column; width: 100%; padding: 8px; }\n.home.grid :deep(.news-image) { width: 100%; height: 100px; }\n.home.grid :deep(.news-title) { font-size: 14px; -webkit-line-clamp: 2; }"
new_css = ".home.grid :deep(.van-list) { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }"
c = c.replace(old_css, new_css)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Home done")
