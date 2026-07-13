import sys
c = open(sys.argv[1], "r", encoding="utf-8").read()
# Prepend the search route before the first import
search_route = "  {\n    path: '/search',\n    name: 'Search',\n    component: () => import('../views/Search.vue'),\n    meta: { title: '\u641c\u7d22', keepAlive: false }\n  },\n"
c = search_route + c
open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Router updated")
