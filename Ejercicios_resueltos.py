from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Firefox() 
driver.get("http://frog-zone.com/article/selenium2-nivel-avanzado")

#Ejercicio 1: Localizar los 3 parrafos (utiliza el metodo 'find_elements_by_class_name') y unirlos en el "textarea"
parrafos = driver.find_elements_by_class_name('parrafo')
textarea = driver.find_element_by_xpath('//*[@id="selenium"]/textarea')
for parrafo in parrafos:
	textarea.send_keys(parrafo.text)

#Ejercicio 2: Introduce los elementos de la lista por orden en los "textbox"
lista = driver.find_element_by_id('lista-elementos').find_elements_by_xpath('.//*')
textboxs =driver.find_elements_by_xpath('//*[@id="selenium"]/div[1]/div/input')
for x in range(3):
	textbox = textboxs[x]
	textbox.send_keys(lista[x].text)

#Ejercicio 3: Selecciona el segundo "radiobutton"
driver.find_element_by_xpath('//*[@id="selenium"]/div[2]/label[2]/input').click()

#Enviar los resultados
driver.find_element_by_xpath('//*[@id="selenium"]/input').click()

end_of_program = input('Finalizar ejercucion!')
driver.close() 