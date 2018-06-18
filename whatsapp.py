from selenium import webdriver

driver = webdriver.Chrome("/home/cp/chromedriver")  # your chrome driver path
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter the message you want to send : ')
count = int(input('Enter the No. of message : '))

input('Enter anything after done all process')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msgbox = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msgbox.send_keys(msg)
    button = driver.find_element_by_class_name('_2lkdt')
    button.click()
