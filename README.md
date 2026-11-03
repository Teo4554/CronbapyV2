# CronbapyV2 📊🧠

**Calculadora en terminal (CLI) para medir la consistencia interna (Alfa de Cronbach) en Python puro.**  
*An interactive command-line tool for psychometric reliability analysis.*

---

## 🇪🇸 Sobre el proyecto

**CronbapyV2** nace como una herramienta ligera y directa para usar desde la terminal. Está pensada para quienes hacemos investigación en Psicología y Ciencias Sociales y necesitamos calcular el **Alfa de Cronbach ($\alpha$)** de un test o cuestionario de forma rápida, metiendo los datos a mano y sin depender de programas pesados como SPSS.

### 💡 Nota sobre la autoría y el desarrollo
*   **La lógica es mía al 100%:** Como estudiante de psicología, diseñé y programé desde cero toda la matemática del script. Esto incluye cómo el programa procesa los datos en matrices, la suma vertical de los puntajes por participante y el cálculo riguroso de las varianzas muestrales ($N-1$).
*   **La IA como asistente de diseño:** Para que la herramienta no fuera la típica pantalla negra aburrida, usé Gemini para darle un lavado de cara estético (los colores ANSI en la terminal, la estructura de banners y el formato limpio a 4 decimales). Todo este proceso se hizo **bajo mi estricta supervisión, dirección y usando prompts específicos** para lograr el acabado que yo quería.

---

## 🇺🇸 About the Project

**CronbapyV2** is a lightweight, interactive command-line tool designed for researchers in Psychology and Social Sciences. It calculates **Cronbach's Alpha ($\alpha$)** natively in pure Python, making it easy to check a questionnaire's reliability by typing participant scores directly into the terminal without opening heavy software like SPSS.

### 💡 Authorship & Development Note
*   **100% Original Logic:** As a psychology student, I designed and coded the entire mathematical engine from scratch. This includes matrix data processing, vertical participant-wise summation, and corrected sample variance ($N-1$) workflows.
*   **AI-Assisted Aesthetics:** To avoid a dull, plain-text terminal interface, I used Gemini to add visual Polish (ANSI colors, section banners, and 4-decimal output formatting). This styling phase was carried out **under my strict supervision, direction, and custom prompting** to get the exact user experience I envisioned.

---

## 🛠️ Lo que hace especial a este script / Features

*   **Python puro y duro:** No necesitas instalar librerías raras ni pesadas. Corre en cualquier lado.
*   **Diseño con colores (UX en terminal):** Usa códigos ANSI para resaltar en verde los éxitos, en amarillo las preguntas y en cian los datos clave. Es mucho más cómodo a la vista.
*   **Resultados listos para paper:** Los decimales salen formateados a 4 dígitos, tal cual se pide en los reportes académicos y normas APA.
*   **Historial limpio:** Te muestra un resumen de las varianzas recolectadas y la matriz de respuestas antes de darte el resultado final.

---

## 🚀 Cómo correrlo / How to Run

1. **Clona el repositorio / Clone the repo:**
   ```bash
   git clone https://github.com/Teo4554/CronbapyV2.git
   cd CronbapyV2
   ```

2. **Dale play / Run it:**
   ```bash
   python cronbapy.py
   ```

---

## 📐 La matemática detrás / The Formula

El programa ejecuta de manera exacta la ecuación estándar del Alfa de Cronbach:

$$ \alpha = \left( \frac{K}{K - 1} \right) \left( 1 - \frac{\sum S_i^2}{S_t^2} \right) $$

Donde:
*   $K$: Número de ítems evaluados.
*   $\sum S_i^2$: Suma de las varianzas de cada ítem por separado.
*   $S_t^2$: Varianza de los puntajes totales acumulados por los sujetos.

---

## 👤 Autor / Author

*   **Estudiante de Psicología** - *Idea original, lógica y desarrollo del algoritmo.*
*   ¡Escríbeme si te interesan la psicometría, la ciencia de datos o la programación científica!
