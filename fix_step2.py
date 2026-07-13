import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# 1. Remove "更多" div from template
old_tpl = """    <!-- 更多选项独立div -->
    <div class="more-options">
      <div class="more-tab" @click="goToCategory">
        {{ \('home.more') }} <van-icon name="arrow" />
      </div>
    </div>
    """
c = c.replace(old_tpl, "")

# 2. Remove moreCategories computed
old_more = """// 计算属性：更多下拉菜单中显示的分类（只显示军事、科技、财经分类）
const moreCategories = computed(() => {
  return newsStore.categories.filter(category => 
    category.name === '军事' || 
    category.name === '科技' || 
    category.name === '财经'
  );
})

"""
c = c.replace(old_more, "")

# 3. Remove goToCategory
old_goto = """// 跳转到分类页面
const goToCategory = () => {
  router.push('/category')
}

"""
c = c.replace(old_goto, "")

# 4. Remove handleTabClick
old_tab = """// 处理标签点击事件
const handleTabClick = (index) => {
  // 如果不是点击"更多"选项，则关闭下拉菜单
  if (displayCategories.value[index].name !== '更多') {
    showDropdown.value = false
    newsStore.changeCategory(displayCategories.value[index].id)
  }
}

"""
c = c.replace(old_tab, "")

# 5. Remove selectMoreCategory
old_select = """// 选择更多分类中的某个分类
const selectMoreCategory = (category) => {
  showDropdown.value = false
  newsStore.changeCategory(category.id)
  
  // 找到选中分类在原始分类中的索引
  const index = newsStore.categories.findIndex(cat => cat.id === category.id)
  if (index !== -1) {
    // 直接设置activeTab为对应索引
    activeTab.value = index
  }
}
"""
c = c.replace(old_select, "")

# 6. Remove changeCategory (the local one that checks categoryId === 10)
old_change = """// 切换分类
const changeCategory = (categoryId) => {
  // 如果点击的是"更多"选项
  if (categoryId === 10) {
    goToCategory()
    return
  }
  
  newsStore.changeCategory(categoryId)
}
"""
c = c.replace(old_change, "")

# 7. Remove related CSS
old_css = """/* 更多选项独立div */
.more-options {
  position: relative;
  margin-right: 16px;
}

.more-tab {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  background-color: #f5f5f5;
  border-radius: 16px;
  font-size: 13px;
  color: #666;
  cursor: pointer;
}

.dropdown-menu {
  position: absolute;
  right: 15px;
  top: 40px;
  min-width: 100px;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  border-radius: 4px;
  z-index: 999;
}

.dropdown-item {
  padding: 10px 15px;
  text-align: center;
  border-bottom: 1px solid #f5f5f5;
}

.dropdown-item:last-child {
  border-bottom: none;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}
"""
c = c.replace(old_css, "")

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
