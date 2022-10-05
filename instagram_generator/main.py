import selenium, colorama, os, sys, time, random, string, re, json
import pyperclip as pc
from pynput import keyboard
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n", "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z"]
characters = ["1", "2", "3", "4", "5", "6", "0", "@", "!", "'", "(", ")", "[", "]", "a", "b", "c", "d", "e", "f", "g", "i", "j", "A", "B", "C", "D", "E", "F", "G", "I", "J"]

config = json.load(open('config.json', 'r'))
day = config['day']
month = config['month']
year = config['year']

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
def random_password(char_num):
       return ''.join(random.choice(characters) for _ in range(char_num))

while(True):


       password = random_password(13)
       usernames = random_char(15)
       fullname = random_char(6) + " " + random_char(7)
       driver = webdriver.Chrome(executable_path="chromedriver.exe")
       sdriver = webdriver.Chrome(executable_path="chromedriver.exe")
       
       #Get the email  
       
       print(f"{Fore.GREEN} Getting the email...")
       print(Fore.WHITE)
       sdriver.get("https://tempmail.vip/en")
       time.sleep(2)
       sdriver.find_element(By.CSS_SELECTOR, ".custom-email-botton").click()

       #Create the account

       driver.get("https://www.instagram.com/accounts/emailsignup/")
       os.system('cls')
       print(f"{Fore.GREEN}[+] Creating the account...")
       print(Fore.WHITE)
       driver.find_element(By.CSS_SELECTOR, ".bIiDR").click() #Allow this only if on the creation page, they ask you to valid the consent
       time.sleep(1)
       driver.find_element(By.NAME, "emailOrPhone").send_keys(Keys.CONTROL, 'v')
       driver.find_element(By.NAME, "fullName").send_keys(fullname)
       driver.find_element(By.NAME, "username").send_keys(usernames)
       driver.find_element(By.NAME, "password").send_keys(password)
       driver.find_element(By.XPATH, "//button[@type=\"submit\"]").click()
       time.sleep(1)
       driver.find_element(By.XPATH, f"//option[@title='{month}']").click()
       driver.find_element(By.XPATH, f"//option[@title='{day}']").click()
       driver.find_element(By.XPATH, f"//option[@title='{year}']").click()
       driver.find_element(By.CSS_SELECTOR, ".sqdOP.L3NKy._4pI4F.y3zKF ").click()
       time.sleep(2)
       print(f"{Fore.GREEN}[+] Getting the verification code...")
       print(Fore.WHITE)

       #Email Verification

       time.sleep(25)
       sdriver.get("https://tempmail.vip/en")
       time.sleep(4)
       verification = sdriver.find_element(By.CSS_SELECTOR, ".subject_email").get_attribute("textContent")
       only_number = re.findall("\d+", verification)[0]
       driver.find_element(By.NAME, "email_confirmation_code").send_keys(only_number)
       driver.find_element(By.XPATH, "//button[@type=\"submit\"]").click()
       print(f"{Fore.GREEN}[!] Account created!")

       pasttext = pc.paste()
       text = f"{pasttext}:{usernames}:{password}"
       with open('account.txt', 'a') as thefile:
              thefile.write(f"{text} \n")
       time.sleep(30) #Time To wait until the account get confirmed by instagram
       sdriver.close()
       driver.close()
