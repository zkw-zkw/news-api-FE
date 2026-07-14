<template>
  <div class="home" :class="{ grid: layoutMode === 'grid' }">
    <van-nav-bar :title="$t('home.title')" fixed />
    <div class="ni ni-l" @click="toggleLayout"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#333" stroke-width="2"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg></div>
    <div class="ni ni-r" onclick="window.searchClick()"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#333" stroke-width="2"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21" stroke-linecap="round"/></svg></div>
    
    
    <div class="category-tabs">
      <van-tabs v-model:active="activeTab" sticky swipeable animated>
        <van-tab 
          v-for="(category, index) in displayCategories" 
          :key="category.id" 
          @click="newsStore.changeCategory(category.id)"
        >
          <template #title>
            <span style="margin-right:4px">{{ getCategoryIcon(category.name) }}</span>{{ getCategoryTranslation(category.name) }}
          </template>
          <van-pull-refresh v-model="newsStore.refreshing" @refresh="onRefresh">
            <van-list
              v-model:loading="newsStore.loading"
              :finished="newsStore.finished"
              :finished-text="$t('home.noMore')"
              @load="onLoad"
            >
              <news-item :grid="layoutMode === 'grid'" 
                v-for="item in newsStore.newsList" 
                :key="item.id" 
                :news="item" 
              />
            </van-list>
          </van-pull-refresh>
        </van-tab>
      </van-tabs>
    </div>
    
    <tab-bar />
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed, onBeforeUnmount } from 'vue'
import { useNewsStore } from '../store/modules/news'
import { useRouter, useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import NewsItem from '../components/NewsItem.vue'
import TabBar from '../components/TabBar.vue'

const newsStore = useNewsStore()
const router = useRouter()
const searchClick = () => { window.location.href = '/search' }
window.searchClick = searchClick
const layoutMode = ref(localStorage.getItem('layout') || 'list')
const toggleLayout = () => { layoutMode.value = layoutMode.value === 'list' ? 'grid' : 'list'; localStorage.setItem('layout', layoutMode.value) }
const route = useRoute()
const { t } = useI18n()
const activeTab = ref(0)
const tabsTop = ref(0)

// 监听路由变化
watch(
  () => route.query.categoryId,
  (newCategoryId) => {
    if (newCategoryId) {
      const categoryId = parseInt(newCategoryId)
      // 找到分类ID对应的索引
      const filteredCategories = newsStore.categories.filter(category => category.name !== '更多')
      const index = filteredCategories.findIndex(cat => cat.id === categoryId)
      
      if (index !== -1) {
        // 设置activeTab为对应索引
        activeTab.value = index
        // 切换分类
        newsStore.changeCategory(categoryId)
      }
    }
  },
  { immediate: true }
)

onMounted(() => {
  // 获取新闻分类
  newsStore.getCategories().then(() => {
    // 获取新闻列表
    newsStore.getNewsList()
    if (newsStore.currentCategory && displayCategories.value?.length) {
      const idx = displayCategories.value.findIndex(c => c.id === newsStore.currentCategory)
      if (idx >= 0) activeTab.value = idx
    }
  })
  
  // 初始化位置
  setTimeout(updateTabsPosition, 300)
  
  // 添加滚动事件监听
  window.addEventListener('scroll', handleScroll)
})

// 计算属性：显示的分类（只显示非"更多"分类）
const displayCategories = computed(() => {
  // 获取所有非"更多"分类
  return newsStore.categories.filter(category => category.name !== '更多');
})

// 获取分类名称的翻译
const getCategoryIcon = (categoryName) => {
  const iconMap = {
    '头条': '📰',
    '社会': '🌍',
    '国内': '🇨🇳',
    '国际': '🌐',
    '娱乐': '🎬',
    '体育': '⚽',
    '军事': '⚔️',
    '科技': '💻',
    '财经': '💰'
  };
  return iconMap[categoryName] || '📋';
};

const getCategoryTranslation = (categoryName) => {
  const categoryMap = {
    '头条': 'headline',
    '社会': 'society',
    '国内': 'domestic',
    '国际': 'international',
    '娱乐': 'entertainment',
    '体育': 'sports',
    '军事': 'military',
    '科技': 'technology',
    '财经': 'finance',
    '更多': 'more'
  };
  
  const key = categoryMap[categoryName];
  return key ? t(`home.categories.${key}`) : categoryName;
}
    

// 获取分类导航栏的位置并设置滚动监听
const updateTabsPosition = () => {
  const tabsElement = document.querySelector('.van-tabs__wrap')
  if (tabsElement) {
    tabsTop.value = tabsElement.getBoundingClientRect().top
  }
}

// 滚动事件处理
const handleScroll = () => {
  updateTabsPosition()

}

onMounted(() => {
  newsStore.getNewsList()
  
  // 初始化位置
  setTimeout(updateTabsPosition, 300)
  
  // 添加滚动事件监听
  window.addEventListener('scroll', handleScroll)
})

// 组件销毁前移除事件监听
onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})

// 监听分类变化
watch(activeTab, (newVal) => {
  const categoryId = newsStore.categories[newVal].id
  newsStore.changeCategory(categoryId)
})

// 下拉刷新
const onRefresh = () => {
  newsStore.getNewsList(true)
}

// 上拉加载更多
const onLoad = () => {
  newsStore.getNewsList()
}

</script>

<style scoped>
.home {
  padding-top: 46px;
  padding-bottom: 50px;
  background-color: #f7f8fa;
  min-height: 100vh;
}

.category-tabs {
  margin-bottom: 10px;
  position: relative;
}

:deep(.van-tabs__wrap) {
  background-color: #fff;
}

:deep(.van-tab) {
  font-size: 14px;
}

:deep(.van-tab--active) {
  font-weight: bold;
  color: #1989fa;
}

.more-options {
  position: fixed;
  right: 0;
  background-color: #fff;
  padding: 0;
  border-radius: 4px 0 0 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  /* 通过计算属性动态设置top */
  top: v-bind('tabsTop + "px"');
  height: 44px; /* 与van-tabs__wrap高度一致 */
  display: flex;
  align-items: center;
}

.more-tab {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #1989fa;
  font-weight: bold;
  height: 100%;
  padding: 0 10px;
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
.ni { position: fixed; top: 0; z-index: 100; width: 44px; height: 46px; display: flex; align-items: center; justify-content: center; cursor: pointer; background: rgba(255,255,255,.95); border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }
.home.grid :deep(.van-list) { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
 .ni-l { left: calc(50% - min(210px, 50vw)); }
 .ni-r { left: calc(50% + min(210px, 50vw) - 44px); }
 :deep(.van-nav-bar--fixed) { max-width: 420px !important; left: 50% !important; transform: translateX(-50%) !important; right: auto !important; }
</style>
