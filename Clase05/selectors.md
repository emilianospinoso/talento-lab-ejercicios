# Guía de selectores – Calculadora Talento Lab

| Elemento visible       | Atributo robusto  | Selector CSS     | Ejemplo Selenium (Python)                              |
| ---------------------- | ----------------- | ---------------- | ------------------------------------------------------ |
| Input “Primer número”  | id="num1"         | `#num1`          | driver.find_element(By.ID, "num1")                     |
| Input “Segundo número” | id="num2"         | `#num2`          | driver.find_element(By.ID, "num2")                     |
| Radio “Sumar”          | id="op-sumar"     | `#op-sumar`      | driver.find_element(By.ID, "op-sumar").click()         |
| Grupo Operaciones      | fieldset          | `fieldset.campo` | driver.find_element(By.CSS_SELECTOR, "fieldset.campo") |
| Botón “Calcular”       | id="btn-calcular" | `#btn-calcular`  | driver.find_element(By.ID, "btn-calcular")             |
