import sys, os

# Add search route to router
c = open(os.path.join(os.path.dirname(sys.argv[1]), "index.js"), "r", encoding="utf-8").read()
new_route = '  {\n    path: "/search",\n    name: "Search",\n    component: () => import("../views/Search.vue"),\n    meta: { title: "\u641c\u7d22", keepAlive: false }\n  },\n'
c = c.replace('import { createRouter, createWebHistory }', new_route + 'import { createRouter, createWebHistory }')
print("Router updated")
