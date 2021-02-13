# Made By github.com/Lehoooo
####################################
from selenium import webdriver
import pytesseract
import time
from pynput.keyboard import Controller
import pyautogui
from PIL import Image

keyboard = Controller()
###################################
driver = webdriver.Firefox()

driver.get("https://www.monkeytype.com")
time.sleep(5)

# change to words
driver.find_element_by_xpath('/html/body/div[18]/div[2]/div[1]/div[3]/div[2]/div/div[2]').click()
driver.find_element_by_xpath('/html/body/div[18]/div[2]/div[1]/div[3]/div[3]/div/div[2]').click()

# cursor removal
element = driver.find_element_by_xpath('//*[@id="caret"]')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)
# retry button removal
element = driver.find_element_by_xpath('//*[@id="restartTestButton"]')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)
#################################### screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")
#################################### cropping
img = Image.open("screen.png")
left = 0
top = 500
right = 2500
bottom = 1500

img_res = img.crop((left, top, right, bottom))

img_res.save("screen2.png")
###################################
################################### ocr
filename = 'screen2.png'
text = pytesseract.image_to_string(filename).strip().replace("\n", " ")
################################### type it
print("typing now")
for c in text:
    #    print(c) # uncomment if you want to print the ocr results
    keyboard.type(c)
