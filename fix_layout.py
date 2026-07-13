import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()

# 1. Add :class to .home div
c = c.replace('<div class="home">', "<div class=\"home\" :class=\"{ grid: layoutMode === 'grid' }\">")

# 2. Add layoutMode and toggleLayout after searchClick
c = c.replace(
    "window.searchClick = searchClick",
    "window.searchClick = searchClick\nconst layoutMode = ref(localStorage.getItem('layout') || 'list')\nconst toggleLayout = () => { layoutMode.value = layoutMode.value === 'list' ? 'grid' : 'list'; localStorage.setItem('layout', layoutMode.value) }"
)

# 3. Add toggle icon after search icon
c = c.replace(
    "<div class=\"ni ni-r\" onclick=\"window.searchClick()\"><svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"none\" stroke=\"#333\" stroke-width=\"2\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><line x1=\"16.5\" y1=\"16.5\" x2=\"21\" y2=\"21\" stroke-linecap=\"round\"/></svg></div>",
    "<div class=\"ni ni-l\" @click=\"toggleLayout\"><svg viewBox=\"0 0 24 24\" width=\"20\" height=\"20\" fill=\"none\" stroke=\"#333\" stroke-width=\"2\"><rect x=\"3\" y=\"3\" width=\"8\" height=\"8\" rx=\"1\"/><rect x=\"13\" y=\"3\" width=\"8\" height=\"8\" rx=\"1\"/><rect x=\"3\" y=\"13\" width=\"8\" height=\"8\" rx=\"1\"/><rect x=\"13\" y=\"13\" width=\"8\" height=\"8\" rx=\"1\"/></svg></div>\n    <div class=\"ni ni-r\" onclick=\"window.searchClick()\"><svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"none\" stroke=\"#333\" stroke-width=\"2\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><line x1=\"16.5\" y1=\"16.5\" x2=\"21\" y2=\"21\" stroke-linecap=\"round\"/></svg></div>"
)

# 4. Add CSS for .ni-l and grid layout
c = c.replace(
    ".ni-r { left: calc(50% + 166px); }",
    ".ni-r { left: calc(50% + 166px); }\n.ni-l { left: calc(50% - 210px); }\n.home.grid :deep(.van-list) { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }\n.home.grid :deep(.news-item) { flex-direction: column; width: 100%; padding: 8px; }\n.home.grid :deep(.news-image) { width: 100%; height: 100px; }\n.home.grid :deep(.news-title) { font-size: 14px; -webkit-line-clamp: 2; }"
)

# 5. Add ref import
c = c.replace(
    "import { ref, onMounted, watch, computed, onBeforeUnmount } from 'vue'",
    "import { ref, onMounted, watch, computed, onBeforeUnmount } from 'vue'"
)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
