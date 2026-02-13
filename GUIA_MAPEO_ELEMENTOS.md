# 🔍 GUÍA: CÓMO MAPEAR ELEMENTOS EN UNA PÁGINA WEB

## 📖 ¿Qué es Mapear Elementos?

**Mapear** = Identificar y localizar los elementos de una página (botones, campos de texto, etc.) para poder interactuar con ellos en Selenium.

## 🎯 Pasos para Mapear Elementos:

### Paso 1: Abrir Chrome DevTools

1. Abre la página: https://www.saucedemo.com/
2. **Presiona F12** o **Click derecho → Inspeccionar**
3. Verás el HTML de la página

### Paso 2: Inspeccionar un Elemento

#### Método 1: Con el selector (RECOMENDADO)
1. Click en el ícono de **flecha** (arriba izquierda de DevTools)
2. Mueve el cursor sobre el elemento que quieres mapear
3. Haz click
4. Verás el HTML resaltado

#### Método 2: Click derecho directo
1. Click derecho sobre el elemento (ej: campo usuario)
2. **Inspeccionar**
3. Te lleva directamente al HTML

## 🏷️ TIPOS DE LOCALIZADORES (Formas de identificar elementos):

### 1️⃣ **ID** (El mejor - único)
```html
<input id="user-name" type="text">
```
**Python:**
```python
USERNAME_INPUT = (By.ID, "user-name")
```
✅ **Ventaja:** Único, rápido, confiable  
❌ **Desventaja:** No todos los elementos tienen ID

---

### 2️⃣ **NAME**
```html
<input name="username" type="text">
```
**Python:**
```python
USERNAME_INPUT = (By.NAME, "username")
```
✅ **Ventaja:** Común en formularios  
❌ **Desventaja:** Puede no ser único

---

### 3️⃣ **CLASS_NAME**
```html
<div class="login_logo">Swag Labs</div>
```
**Python:**
```python
LOGO = (By.CLASS_NAME, "login_logo")
```
✅ **Ventaja:** Fácil de encontrar  
❌ **Desventaja:** Puede haber múltiples elementos con la misma clase

---

### 4️⃣ **CSS_SELECTOR** (Muy flexible)
```html
<input id="user-name" class="input_error" type="text">
```
**Python:**
```python
# Por ID
USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")

# Por clase
USERNAME_INPUT = (By.CSS_SELECTOR, ".input_error")

# Combinado
USERNAME_INPUT = (By.CSS_SELECTOR, "input#user-name")

# Por atributo
USERNAME_INPUT = (By.CSS_SELECTOR, "input[type='text']")
```
✅ **Ventaja:** Muy potente y flexible  
⚠️ **Desventaja:** Requiere conocer CSS

---

### 5️⃣ **XPATH** (El más potente)
```html
<input id="user-name" type="text">
```
**Python:**
```python
# Por ID
USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")

# Por tipo
USERNAME_INPUT = (By.XPATH, "//input[@type='text']")

# Por texto
LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")

# Por posición
FIRST_INPUT = (By.XPATH, "(//input)[1]")

# Navegación relativa
USERNAME_INPUT = (By.XPATH, "//form//input[@id='user-name']")
```
✅ **Ventaja:** Puede encontrar cualquier cosa  
❌ **Desventaja:** Puede ser frágil si cambia la estructura

---

### 6️⃣ **TAG_NAME**
```html
<button>Login</button>
```
**Python:**
```python
BUTTON = (By.TAG_NAME, "button")
```
⚠️ **Úsalo solo si:** Hay un único elemento de ese tipo

---

### 7️⃣ **LINK_TEXT / PARTIAL_LINK_TEXT** (Solo para links)
```html
<a href="/productos">Ver Productos</a>
```
**Python:**
```python
# Texto completo
LINK = (By.LINK_TEXT, "Ver Productos")

# Texto parcial
LINK = (By.PARTIAL_LINK_TEXT, "Productos")
```

---

## 🎓 EJEMPLO PRÁCTICO: SauceDemo Login

### Página: https://www.saucedemo.com/

Vamos a mapear cada elemento:

#### 1. **Campo de Usuario**
```html
<!-- Inspecciona y verás: -->
<input 
  class="input_error form_input" 
  placeholder="Username" 
  type="text" 
  data-test="username" 
  id="user-name" 
  name="user-name" 
  autocorrect="off" 
  autocapitalize="none">
```

**Opciones de mapeo:**

```python
# Opción 1: Por ID (MEJOR)
USERNAME_INPUT = (By.ID, "user-name")

# Opción 2: Por NAME
USERNAME_INPUT = (By.NAME, "user-name")

# Opción 3: Por data-test
USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test='username']")

# Opción 4: Por placeholder
USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")

# Opción 5: Por tipo y clase
USERNAME_INPUT = (By.CSS_SELECTOR, "input.form_input[type='text']")
```

**Recomendado:** `(By.ID, "user-name")` ✅

---

#### 2. **Campo de Contraseña**
```html
<input 
  class="input_error form_input" 
  placeholder="Password" 
  type="password" 
  data-test="password" 
  id="password" 
  name="password" 
  autocorrect="off" 
  autocapitalize="none">
```

**Mapeo:**
```python
# Mejor opción
PASSWORD_INPUT = (By.ID, "password")

# Alternativas
PASSWORD_INPUT = (By.NAME, "password")
PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
```

---

#### 3. **Botón Login**
```html
<input 
  type="submit" 
  class="submit-button btn_action" 
  data-test="login-button" 
  id="login-button" 
  name="login-button" 
  value="Login">
```

**Mapeo:**
```python
# Mejor opción
LOGIN_BUTTON = (By.ID, "login-button")

# Alternativas
LOGIN_BUTTON = (By.NAME, "login-button")
LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")
LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
LOGIN_BUTTON = (By.CSS_SELECTOR, "input.submit-button")
```

---

#### 4. **Mensaje de Error**
```html
<h3 data-test="error">
  <button class="error-button">❌</button>
  Epic sadface: Username and password do not match...
</h3>
```

**Mapeo:**
```python
# Por data-test
ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

# Por tag
ERROR_MESSAGE = (By.TAG_NAME, "h3")

# Por clase del botón y navegación
ERROR_MESSAGE = (By.XPATH, "//button[contains(@class, 'error-button')]/..")
```

---

#### 5. **Logo/Título**
```html
<div class="login_logo">Swag Labs</div>
```

**Mapeo:**
```python
LOGO = (By.CLASS_NAME, "login_logo")

# O con CSS
LOGO = (By.CSS_SELECTOR, ".login_logo")

# O con XPath
LOGO = (By.XPATH, "//div[@class='login_logo']")
```

---

## 🛠️ HERRAMIENTAS DE CHROME DEVTOOLS:

### 1. **Copiar Selector CSS**
1. Inspecciona el elemento
2. En DevTools, click derecho sobre el HTML
3. **Copy → Copy selector**
4. Pega en tu código

### 2. **Copiar XPath**
1. Inspecciona el elemento
2. Click derecho sobre el HTML
3. **Copy → Copy XPath**
4. Pega en tu código

### 3. **Probar selector en Console**
```javascript
// En la consola de Chrome (F12 → Console)

// Probar CSS Selector
$$('#user-name')

// Probar XPath
$x("//input[@id='user-name']")

// Si devuelve el elemento, el selector funciona ✅
```

---

## 📋 ORDEN DE PREFERENCIA (Mejores prácticas):

1. **ID** → Si existe, siempre úsalo ✅
2. **data-test o atributos personalizados** → Específicos para testing
3. **NAME** → Para formularios
4. **CSS_SELECTOR** → Flexible y rápido
5. **CLASS_NAME** → Si es única
6. **XPATH** → Último recurso (puede ser frágil)

---

## ⚠️ MALAS PRÁCTICAS (Evitar):

❌ **XPaths copiados completos de Chrome:**
```python
# MAL - Muy frágil
ELEMENT = (By.XPATH, "/html/body/div[1]/div/div/form/div[1]/input")
```

❌ **Selectores CSS muy específicos:**
```python
# MAL - Se rompe fácilmente
ELEMENT = (By.CSS_SELECTOR, "div > div > form > div:nth-child(1) > input")
```

❌ **Depender solo de clases genéricas:**
```python
# MAL - Puede haber múltiples
ELEMENT = (By.CLASS_NAME, "input")
```

---

## ✅ BUENAS PRÁCTICAS:

✅ **Usar ID cuando existe:**
```python
USERNAME = (By.ID, "user-name")  # Simple y confiable
```

✅ **Usar data-test attributes:**
```python
USERNAME = (By.CSS_SELECTOR, "[data-test='username']")  # Específico
```

✅ **XPath simple y legible:**
```python
# BIEN - XPath simple
LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
```

✅ **CSS Selector directo:**
```python
ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")  # Claro
```

---

## 🎯 EJERCICIO: Mapea estos elementos de SauceDemo

1. Campo de usuario → `(By.ID, "user-name")`
2. Campo de contraseña → `(By.ID, "password")`
3. Botón Login → `(By.ID, "login-button")`
4. Mensaje de error → `(By.CSS_SELECTOR, "[data-test='error']")`
5. Logo → `(By.CLASS_NAME, "login_logo")`

---

## 🔍 RESUMEN RÁPIDO:

| Localizador | Cuándo usar | Ejemplo |
|-------------|-------------|---------|
| **ID** | Siempre que exista | `(By.ID, "user-name")` |
| **NAME** | Formularios | `(By.NAME, "username")` |
| **CLASS_NAME** | Si es única | `(By.CLASS_NAME, "login_logo")` |
| **CSS_SELECTOR** | Flexibilidad | `(By.CSS_SELECTOR, "[data-test='login']")` |
| **XPATH** | Casos complejos | `(By.XPATH, "//input[@type='text']")` |

---

## 💡 TIPS:

1. **Siempre inspecciona antes de codificar**
2. **Prueba tus selectores en la consola de Chrome**
3. **Usa IDs cuando existan**
4. **Evita XPaths largos y frágiles**
5. **Prefiere atributos `data-test` si los tiene la app**

---

**¡Ahora ya sabes cómo mapear elementos! 🎉**

Siguiente paso: Crear el Page Object con estos localizadores.
