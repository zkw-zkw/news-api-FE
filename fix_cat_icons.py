import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Replace the van-tab template to add icon slot
old_tpl = """        <van-tab 
          v-for="(category, index) in displayCategories" 
          :key="category.id" 
          :title="getCategoryTranslation(category.name)"
          @click="newsStore.changeCategory(category.id)"
        >"""

new_tpl = """        <van-tab 
          v-for="(category, index) in displayCategories" 
          :key="category.id" 
          @click="newsStore.changeCategory(category.id)"
        >
          <template #title>
            <span style="margin-right:4px">{{ getCategoryIcon(category.name) }}</span>{{ getCategoryTranslation(category.name) }}
          </template>"""

c = c.replace(old_tpl, new_tpl)

# Add getCategoryIcon function after getCategoryTranslation
old_func = "const getCategoryTranslation = (categoryName) => {"
new_func = "const getCategoryIcon = (categoryName) => {\n  const iconMap = {\n    '\u5934\u6761': '\U0001f4f0',\n    '\u793e\u4f1a': '\U0001f30d',\n    '\u56fd\u5185': '\U0001f1e8\U0001f1f3',\n    '\u56fd\u9645': '\U0001f310',\n    '\u5a31\u4e50': '\U0001f3ac',\n    '\u4f53\u80b2': '\u26bd',\n    '\u519b\u4e8b': '\u2694\ufe0f',\n    '\u79d1\u6280': '\U0001f4bb',\n    '\u8d22\u7ecf': '\U0001f4b0'\n  };\n  return iconMap[categoryName] || '\U0001f4cb';\n};\n\n" + old_func

c = c.replace(old_func, new_func)

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
