<template>
  <div class="search-page">
    <div class="search-header">
      <span class="back-btn" @click="$router.back()">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="#333"><path d="M15.4 16.6L10.8 12l4.6-4.6L14 6l-6 6 6 6z"/></svg>
      </span>
      <div class="search-input-wrap">
        <input v-model="keyword" ref="inputRef" class="search-input" placeholder="搜索新闻..." @keydown.enter="doSearch" />
        <span v-if="keyword" class="clear-btn" @click="keyword='';results=[]">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="#999"><path d="M18.3 5.7L12 12l6.3 6.3-1.4 1.4L12 13.4l-6.3 6.3-1.4-1.4L10.6 12 4.3 5.7l1.4-1.4L12 10.6l6.3-6.3z"/></svg>
        </span>
      </div>
    </div>
    <div class="search-body">
      <div v-if="!keyword && !results.length" class="search-tip">输入关键词搜索新闻</div>
      <div v-if="loading" class="search-tip">搜索中...</div>
      <div v-if="!loading && results.length" class="result-list">
        <div v-for="item in results" :key="item.id" class="news-item" @click="$router.push('/news/detail/' + item.id)">
          <div class="news-image">
            <img :src="item.image" :alt="item.title">
          </div>
          <div class="news-content">
            <h3 class="news-title">{{ item.title }}</h3>
            <p class="news-desc">{{ item.description }}</p>
            <div class="news-info">
              <span>{{ item.author }}</span>
              <span>{{ item.publishTime }}</span>
              <span>{{ item.views || 0 }} 阅读</span>
            </div>
          </div>
        </div>
      </div>
      <div v-if="!loading && keyword && !results.length" class="search-tip">没有找到相关新闻</div>
    </div>
  </div>
</template>
<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const keyword = ref('')
const results = ref([])
const loading = ref(false)
const inputRef = ref(null)
let searchTimer
watch(keyword, (val) => {
  if (searchTimer) clearTimeout(searchTimer)
  if (val.trim()) {
    searchTimer = setTimeout(doSearch, 300)
  } else {
    results.value = []
  }
})
const doSearch = async () => {
  if (!keyword.value.trim()) return
  loading.value = true
  try {
    const kw = keyword.value.trim()
    const allItems = []
    for (let id = 1; id <= 8; id++) {
      try {
        const r = await (await fetch("/api/news/list?categoryId=" + id + "&pageSize=20")).json()
        const items = r?.data?.list || r?.data?.data || r?.data || []
        if (Array.isArray(items)) allItems.push(...items)
      } catch(e) {}
    }
    const lower = kw.toLowerCase()
    results.value = allItems.filter(item => {
      const t = (item.title || "").toLowerCase()
      const d = (item.description || "").toLowerCase()
      return t.includes(lower) || d.includes(lower)
    })
  } catch(e) { console.error(e) }
  finally { loading.value = false }
}
onMounted(async () => {
  await nextTick()
  if (inputRef.value) inputRef.value.focus()
  if (route.query.q) { keyword.value = route.query.q; doSearch() }
})
</script>
<style scoped>
.search-page { background: #fff; min-height: 100vh; }
.search-header { display: flex; align-items: center; gap: 10px; padding: 8px 12px; border-bottom: 1px solid #f0f0f0; }
.back-btn { width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; }
.search-input-wrap { flex: 1; display: flex; align-items: center; background: #f5f5f5; border-radius: 20px; padding: 0 12px; }
.search-input { flex: 1; border: none; outline: none; font-size: 14px; padding: 10px 0; background: transparent; }
.clear-btn { width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; }
.search-body { padding: 12px; }
.search-tip { text-align: center; padding: 40px 0; color: #999; font-size: 14px; }
.result-list { display: flex; flex-direction: column; gap: 0; }
.news-item { display: flex; gap: 12px; padding: 12px 16px; border-bottom: 1px solid #f2f2f2; cursor: pointer; background: #fff; }
.news-item:active { background: #fafafa; }
.news-image { width: 110px; height: 80px; flex-shrink: 0; }
.news-image img { width: 100%; height: 100%; object-fit: cover; border-radius: 4px; }
.news-content { flex: 1; min-width: 0; overflow: hidden; }
.news-title { font-size: 16px; font-weight: 500; margin: 0 0 8px; line-height: 1.4; color: #000; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
.news-desc { font-size: 14px; color: #666; margin: 0 0 8px; line-height: 1.4; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.news-info { font-size: 12px; color: #999; display: flex; gap: 10px; }
</style>
