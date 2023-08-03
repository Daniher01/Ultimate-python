from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
load_dotenv()

# ? objeto para permitir que el explorador se mantenga abierto
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# ? se va a envargar de hacer la manipulaciones del explorador
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get("http://sistema.tuimagenrx.cl/")

# ? darle instrucciones al browser para que realice acciones
""" 
En este caso las instrucciones van a ser
- seleccionar el boton de usery password
- ingresar credenciales
- captar el username 
"""

# ingresar el input de usuario y password
user_input = browser.find_element(By.ID, "validationTooltipUsername")
password_input = browser.find_element(By.ID, "validationTooltip03")

user_input.send_keys(os.environ.get("gh_user"))
password_input.send_keys(os.environ.get("gh_pass"))
password_input.send_keys(Keys.RETURN)

# captar el nombre de usuario
profile = browser.find_element(
    By.CLASS_NAME,
    "d-none.d-xl-inline-block.ms-1.fw-medium"
)

label = profile.get_attribute("innerHTML")
print(label)

browser.quit()
