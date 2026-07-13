import sys, re
c = open(sys.argv[1], "r", encoding="utf-8").read()
# Remove CSS blocks
c = c.replace(".more-options {\n  position: relative;\n  margin-right: 16px;\n}\n\n", "")
c = c.replace(".more-tab {\n  display: flex;\n  align-items: center;\n  padding: 8px 12px;\n  background-color: #f5f5f5;\n  border-radius: 16px;\n  font-size: 13px;\n  color: #666;\n  cursor: pointer;\n}\n\n", "")
# Remove dead functions using regex
c = re.sub(r'// 跳转到分类页面\nconst goToCategory = \(\) => \{[\s\S]*?\}\n\n', "", c)
c = re.sub(r'// 处理标签点击事件\nconst handleTabClick = \(index\) => \{[\s\S]*?\}\n\n', "", c)
c = re.sub(r'// 选择更多分类中的某个分类\nconst selectMoreCategory = \(category\) => \{[\s\S]*?\}\n', "", c)
c = re.sub(r'// 切换分类\nconst changeCategory = \(categoryId\) => \{[\s\S]*?\}\n', "", c)
open(sys.argv[1], "w", encoding="utf-8").write(c)
print("Done")
