import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()
# Remove the wrongly placed search route (it's before the import)
c = c.replace("  {\n    path: '/search',\n    name: 'Search',\n    component: () => import('../views/Search.vue'),\n    meta: { title: '\u641c\u7d22', keepAlive: false }\n  },\n", "")
# Insert it after "const routes = ["
new_route = "  {\n    path: '/search',\n    name: 'Search',\n    component: () => import('../views/Search.vue'),\n    meta: { title: '\u641c\u7d22', keepAlive: false }\n  },\n"
c = c.replace("const routes = [", "const routes = [\n" + new_route)
open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Fixed")
