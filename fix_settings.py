import sys

c = open(sys.argv[1], "r", encoding="utf-8").read()

# 1. Remove theme cell button from template
old_cell = '        <van-cell :title="$t(' + "'settings.themeCustomization'" + ')" is-link @click="showThemePopup = true" />\n'
c = c.replace(old_cell, "")

# 2. Remove theme popup block
old_popup = """    <!-- 主题选择弹出层 -->
    <van-popup
      v-model:show="showThemePopup"
      position="bottom"
      round
      :style="{ height: '40%' }"
    >
      <div class="popup-title">{{ $t('settings.selectTheme') }}</div>
      <div class="theme-list">
        <div 
          v-for="theme in themeList" 
          :key="theme.id" 
          class="theme-item"
          :class="{ active: currentTheme === theme.id }"
          @click="changeTheme(theme.id)"
        >
          <div class="theme-color" :style="{ backgroundColor: theme.primaryColor }"></div>
          <div class="theme-name">{{ theme.name }}</div>
        </div>
      </div>
    </van-popup>
    
"""
c = c.replace(old_popup, "")

# 3. Remove theme import
c = c.replace("import { useThemeStore } from '../store/theme';\n", "")

# 4. Remove theme store initialization
c = c.replace("const themeStore = useThemeStore();\n", "")

# 5. Remove theme refs and function
old_theme_func = """// 主题相关
const showThemePopup = ref(false);
const themeList = computed(() => themeStore.getAllThemes);
const currentTheme = computed(() => themeStore.getCurrentTheme);

// 切换主题
const changeTheme = (themeId) => {
  themeStore.setTheme(themeId);
  showToast(t('settings.themeChanged'));
  showThemePopup.value = false;
};

"""
c = c.replace(old_theme_func, "")

# 6. Remove theme CSS
old_css = """.theme-list {
  display: flex;
  flex-wrap: wrap;
  padding: 16px;
}

.theme-item {
  width: 25%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 16px;
  cursor: pointer;
}

.theme-color {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-bottom: 8px;
  border: 2px solid transparent;
}

.theme-item.active .theme-color {
  border-color: #1989fa;
}

.theme-name {
  font-size: 12px;
}

"""
c = c.replace(old_css, "")

open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
