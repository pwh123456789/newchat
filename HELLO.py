from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import  time
# options = webdriver.ChromeOptions()
# prefs = {'profile.default_content_setting_values':{'notifications':2}}   #可以去掉系统通知
# options.add_experimental_option('prefs',prefs)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.get('https://vcc-qa.vxichina.cn/api/oauth2/login')
time.sleep(5)
# driver.find_element_by_css_selector('#userName').send_keys('admin2')
# driver.find_element_by_css_selector('#password').send_keys('111111')
# driver.find_element_by_css_selector('#submit').click()
# time.sleep(3)
# #driver.find_element_by_css_selector('.pa').click()
# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
# driver.find_element_by_xpath('//span[text()="组织"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//div[@title="新增节点"]').click()
# time.sleep(1)
#driver.find_element_by_xpath('//form[@class="el-form"]/div[1]/div/div/input').send_keys('自动')
#driver.find_element_by_xpath('//div[@class="el-dialog__body"]/../div[3]/div/button[2]').click()
#time.sleep(2)
#driver.find_element_by_xpath('//span[text()="自动"]').click()
#driver.find_element_by_css_selector('.user__action>button:first-child')
#driver.find_element_by_xpath('//form[@class="el-form"]/div[1]/div/div/input').send_keys("ui")
#driver.find_element_by_xpath('//form[@class="el-form"]/div[2]/div/div/input').send_keys("uitest")
#driver.find_element_by_xpath('//div[@class="el-dialog__body"]/../div[3]/div/button[2]').click()





#driver.switch_to.alert()
# driver.switch_to.alert().accept()
# time.sleep(1)


# driver.find_element_by_xpath('//div[@class="list__wrapper"]/div[3]/div[1]/div/div[1]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//div[contains(@placeholder,"请输入")]').send_keys('您好')
# driver.find_element_by_css_selector('.el-button-group button:nth-child(1)').click()
# driver.find_element_by_css_selector('div.menu>div:last-child').click()
# time.sleep(2)
# driver.find_element_by_css_selector('div[title="创建广播"]').click()
# time.sleep(2)
# driver.find_element_by_css_selector('input[type="text"][placeholder="请输入标题"]').send_keys('自动')
# driver.find_element_by_css_selector('.operate').click()
# e1 = driver.find_element_by_xpath('//span[text()="test1"]/../..')
# ActionChains(driver).click(e1).perform()
# time.sleep(1)
# driver.find_element_by_xpath('//span[text()="qx"]/../../label/span/span').click()
# driver.find_element_by_css_selector('.el-dialog__footer>div>button:nth-child(2)>span').click()
# time.sleep(1)
# driver.switch_to.frame(0)
# driver.find_element_by_css_selector('#tinymce').send_keys('你好')
# driver.switch_to.default_content()
# driver.find_element_by_xpath('//span[text()="发布"]').click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='组织']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//div[@class='left__header--search']/div/input").send_keys('pwh')
# time.sleep(2)
# l1 = driver.find_elements_by_xpath('//span[@title="pwh"]')
# l1[0].click()
# driver.find_element_by_xpath('//span[text()="发送消息"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//div[@placeholder="请输入..."]').send_keys("自动发送")
# driver.find_element_by_css_selector('.el-button-group>button:nth-child(1)').click()
