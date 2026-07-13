import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Add search icon after van-nav-bar
c = c.replace(
    "<van-nav-bar :title=\"$t('home.title')\" fixed />",
    "<van-nav-bar :title=\"$t('home.title')\" fixed />\n    <div class=\"ni ni-r\" onclick=\"window.searchClick()\"><svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"none\" stroke=\"#333\" stroke-width=\"2\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><line x1=\"16.5\" y1=\"16.5\" x2=\"21\" y2=\"21\" stroke-linecap=\"round\"/></svg></div>"
)

# Add searchClick function
c = c.replace(
    "const router = useRouter()",
    "const router = useRouter()\nconst searchClick = () => { window.location.href = '/search' }\nwindow.searchClick = searchClick"
)

# Add CSS for search icon
c = c.replace(
    "</style>",
    ".ni { position: fixed; top: 0; z-index: 100; width: 44px; height: 46px; display: flex; align-items: center; justify-content: center; cursor: pointer; background: rgba(255,255,255,.95); border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }\n.ni-r { left: calc(50% + 166px); }\n:deep(.van-nav-bar--fixed) { max-width: 420px !important; left: 50% !important; transform: translateX(-50%) !important; right: auto !important; }\n</style>"
)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Home.vue done")
