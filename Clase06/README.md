# Clase 06 – DOM para Automatización

Este ejercicio tiene como objetivo documentar **selectores robustos** (CSS y XPath) para los campos más importantes del formulario de login o registro, de forma que resistan cambios de diseño y puedan ser reutilizados en futuras automatizaciones con Selenium.

## Contexto

Después de una semana enfocada en HTML, CSS y automatización básica, el equipo de desarrollo anunció una **refactorización importante del formulario de perfiles internos**. Como parte del equipo de QA, tu responsabilidad es garantizar que los selectores utilizados en las pruebas **no se rompan aunque cambie el diseño visual**.

> **Silvia (PO)**:  
> “Mañana los desarrolladores refactorizan la pantalla de registro. Necesito una lista de selectores que **NO dependan del layout**.”

> **Requisitos**:
>
> - Seleccionar los siguientes elementos:
>   - Usuario (nombre o email)
>   - Contraseña
>   - Botón de login/guardar
> - Si hay un `id`, usalo como CSS.
> - Si no, construí un selector CSS o XPath que sea estable.
> - Documentá el motivo de tu elección.

## ¿Qué significa “no depender del layout”?

Un selector **independiente del layout** se apoya en atributos estables como `id`, `name`, o texto visible.  
Ejemplos buenos:

- `#email`
- `input[name="password"]`
- `//button[text()='Guardar']`

En cambio, un selector que **depende del layout** se basa en posiciones o clases frágiles que suelen cambiar:

- `body > div:nth-child(2) > form > input`
- `/html/body/div[3]/button`
- `.col-md-6 .btn-primary`

# 📄 Tabla de selectores estables – Clase 06

| Elemento      | Selector                    | Tipo  | Razón de elección                                    |
| ------------- | --------------------------- | ----- | ---------------------------------------------------- |
| Usuario       | `#user-name`                | CSS   | id único, directo y semántico                        |
| Usuario       | `//*[@id='user-name']`      | XPath | alternativa estable si cambian estilos o clases      |
| Contraseña    | `input[type="password"]`    | CSS   | selector claro por tipo; único en el formulario      |
| Contraseña    | `//input[@type='password']` | XPath | simple y estable por tipo de input                   |
| Botón Iniciar | `.btn_action`               | CSS   | clase exclusiva del botón de login                   |
| Botón Iniciar | `//input[@type='submit']`   | XPath | usa atributo de tipo para ubicar el botón fácilmente |

🧪 Snippet de verificación rápida
Este fragmento de JavaScript te permite comprobar si los selectores CSS elegidos apuntan correctamente a los elementos en pantalla. Pégalo en la consola del navegador:

['#user-name', 'input[type="password"]', '.btn_action'].forEach(sel => {
const el = document.querySelector(sel);
if (el) el.style.backgroundColor = 'khaki';
});
Si los campos se iluminan en amarillo, significa que los selectores funcionan.
