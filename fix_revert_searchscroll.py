import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Remove the :class binding for ni-hidden
c = c.replace(":class=\"{ 'ni-hidden': !showSearch }\" ", "")

# Remove showSearch ref and lastScrollY
c = c.replace("\nconst showSearch = ref(true)\nlet lastScrollY = 0", "")

# Revert handleScroll to original
c = c.replace(
    "  const currentY = window.scrollY || document.documentElement.scrollTop\n  showSearch.value = currentY <= lastScrollY || currentY < 10\n  lastScrollY = currentY",
    ""
)

# Remove .ni-hidden CSS
c = c.replace("\n.ni-hidden { opacity: 0; transform: translateY(-10px); pointer-events: none; }", "")

# Remove transition from .ni
c = c.replace(" transition: opacity 0.3s ease, transform 0.3s ease;", "")

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Reverted")
