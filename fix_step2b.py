import sys, re

c = open(sys.argv[1], "r", encoding="utf-8").read()

# Remove the more div from template
c = re.sub(
    r'    <!-- 更多选项独立div -->\n    <div class="more-options">\n      <div class="more-tab" @click="goToCategory">\n        {{ \\("home\.more"\) }} <van-icon name="arrow" />\n      </div>\n    </div>\n    ',
    '',
    c
)

# Remove goToCategory function
c = c.replace(
    '// 跳转到分类页面\nconst goToCategory = () => {\n  router.push(\'/category\')\n}\n\n',
    ''
)

# Remove handleTabClick function
c = c.replace(
    '// 处理标签点击事件\nconst handleTabClick = (index) => {\n  // 如果不是点击"更多"选项，则关闭下拉菜单\n  if (displayCategories.value[index].name !== \'更多\') {\n    showDropdown.value = false\n    newsStore.changeCategory(displayCategories.value[index].id)\n  }\n}\n\n',
    ''
)

# Remove selectMoreCategory function
c = c.replace(
    '// 选择更多分类中的某个分类\nconst selectMoreCategory = (category) => {\n  showDropdown.value = false\n  newsStore.changeCategory(category.id)\n  \n  // 找到选中分类在原始分类中的索引\n  const index = newsStore.categories.findIndex(cat => cat.id === category.id)\n  if (index !== -1) {\n    // 直接设置activeTab为对应索引\n    activeTab.value = index\n  }\n}\n',
    ''
)

# Remove changeCategory function (at the end of script)
c = c.replace(
    '// 切换分类\nconst changeCategory = (categoryId) => {\n  // 如果点击的是"更多"选项\n  if (categoryId === 10) {\n    goToCategory()\n    return\n  }\n  \n  newsStore.changeCategory(categoryId)\n}\n',
    ''
)

# Remove related CSS
for old in [
    '.more-options {\n  position: relative;\n  margin-right: 16px;\n}\n\n',
    '.more-tab {\n  display: flex;\n  align-items: center;\n  padding: 8px 12px;\n  background-color: #f5f5f5;\n  border-radius: 16px;\n  font-size: 13px;\n  color: #666;\n  cursor: pointer;\n}\n\n',
    '.dropdown-menu {\n  position: absolute;\n  right: 15px;\n  top: 40px;\n  min-width: 100px;\n  background-color: #fff;\n  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);\n  border-radius: 4px;\n  z-index: 999;\n}\n\n',
    '.dropdown-item {\n  padding: 10px 15px;\n  text-align: center;\n  border-bottom: 1px solid #f5f5f5;\n}\n\n',
    '.dropdown-item:last-child {\n  border-bottom: none;\n}\n\n',
    '.dropdown-item:hover {\n  background-color: #f5f5f5;\n}\n',
]:
    c = c.replace(old, '')

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
