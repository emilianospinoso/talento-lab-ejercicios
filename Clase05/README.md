# Clase 05 – Maqueta HTML/CSS de la Calculadora

Esta página estática sirve como “campo de entrenamiento” para la próxima
clase de Selenium. Todos los elementos tienen **id** y **name** únicos para
selectores estables.

## Cómo probar

1. Clona el repo y navega a `Clase05/`.
2. Abre `index.html` en cualquier navegador moderno (doble clic o `Ctrl+O`).
3. Usa **DevTools** (`F12`) → pestaña _Elements_ para inspeccionar y copiar selectores.

### Verificar selectores rápidamente

En la consola de DevTools ejecuta, por ejemplo:

document.querySelector("#num1").style.outline = "2px solid red";
