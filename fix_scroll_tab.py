import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

old_block = """      if (idx >= 0) activeTab.value = idx
    }
  })"""

new_block = """      if (idx >= 0) activeTab.value = idx
    }
    setTimeout(() => {
      const sp = parseInt(sessionStorage.getItem('homeScroll'))
      if (sp > 0) { window.scrollTo(0, sp) }
    }, 300)
  })"""

c = c.replace(old_block, new_block)
open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
