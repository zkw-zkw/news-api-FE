import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Add :class binding for showSearch
c = c.replace(
    "onclick=\"window.searchClick()\">",
    ":class=\"{ 'ni-hidden': !showSearch }\" onclick=\"window.searchClick()\">"
)

# Add showSearch ref and lastScrollY
c = c.replace(
    "const activeTab = ref(0)",
    "const activeTab = ref(0)\nconst showSearch = ref(true)\nlet lastScrollY = 0"
)

# Modify handleScroll to track scroll direction
c = c.replace(
    "const handleScroll = () => {\n  updateTabsPosition()\n}",
    "const handleScroll = () => {\n  updateTabsPosition()\n  const currentY = window.scrollY || document.documentElement.scrollTop\n  showSearch.value = currentY <= lastScrollY || currentY < 10\n  lastScrollY = currentY\n}"
)

# Add transition and .ni-hidden CSS
c = c.replace(
    "transition: opacity 0.3s ease, transform 0.3s ease;",
    "transition: opacity 0.3s ease, transform 0.3s ease;"
)
c = c.replace(
    ".ni { position: fixed; top: 0; z-index: 100; width: 44px; height: 46px; display: flex; align-items: center; justify-content: center; cursor: pointer; background: rgba(255,255,255,.95); border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,.08); transition: opacity 0.3s ease, transform 0.3s ease; }",
    ".ni { position: fixed; top: 0; z-index: 100; width: 44px; height: 46px; display: flex; align-items: center; justify-content: center; cursor: pointer; background: rgba(255,255,255,.95); border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,.08); transition: opacity 0.3s ease, transform 0.3s ease; }\n.ni-hidden { opacity: 0; transform: translateY(-10px); pointer-events: none; }"
)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
