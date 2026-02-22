# 🪐 Python Module — Cosmic Data
## MAP — Modelado y Validación Declarativa con Pydantic v2

---

## 1. Objetivo del módulo

Este módulo introduce el **modelado estructurado de datos** utilizando
**Pydantic v2** como motor de validación declarativa.

El propósito no es únicamente validar campos,
sino comprender cómo:

- Definir contratos de datos explícitos
- Centralizar reglas de validación
- Garantizar coherencia estructural
- Diseñar modelos auto-validados

Supone una transición desde validaciones manuales con `if`
hacia un enfoque declarativo y arquitectónico.

---

## 2. Conceptos técnicos trabajados

- `BaseModel`
- Type hints como contrato estructural
- `Field()` con restricciones:
  - `min_length`
  - `max_length`
  - `ge` / `le`
  - `pattern`
- `Enum` para valores controlados
- `@model_validator(mode="after")`
- Modelos anidados
- Validación cruzada entre campos
- Manejo estructurado de errores (`ValidationError`)

---

## 3. Desglose por ejercicios

### ex0 — SpaceStation

**Enfoque:**
Validación a nivel de campo.

Se aplican restricciones declarativas sobre:
- Longitud de cadenas
- Rangos numéricos
- Patrones mediante expresiones regulares

**Aprendizaje clave:**
La validación simple puede declararse directamente en la definición
del modelo sin lógica imperativa adicional.

---

### ex1 — AlienContact

**Enfoque:**
Reglas de negocio dependientes de múltiples campos.

Se introduce:
- `Enum` para restringir tipos de contacto
- `@model_validator(mode="after")` para validar coherencia interna

Ejemplos de reglas:
- Contactos físicos deben estar verificados
- Contactos telepáticos requieren mínimo 3 testigos
- Señales fuertes requieren mensaje recibido

**Aprendizaje clave:**
Las reglas relacionales pertenecen al modelo,
no al flujo de control externo.

---

### ex2 — SpaceCrew

**Enfoque:**
Modelos anidados y validación agregada.

Se modela una misión compuesta por:
- Lista de miembros (`CrewMember`)
- Reglas de coherencia global

Reglas implementadas:
- La misión debe incluir liderazgo
- En misiones largas, al menos 50% del equipo debe tener experiencia
- Todos los miembros deben estar activos

**Aprendizaje clave:**
La validación puede representar coherencia sistémica,
no solo corrección individual de campos.

---

## 4. Evolución conceptual

Este módulo representa un cambio de enfoque:

Antes:
- Validación dispersa
- Comprobaciones manuales
- Dependencia del flujo de ejecución

Ahora:
- Validación centralizada
- Modelo como contrato ejecutable
- Integridad garantizada en el momento de instanciación

El modelo se convierte en el punto único de verdad.

---

## 5. Valor arquitectónico

El uso de Pydantic permite:

- Reducción de duplicación
- Mayor claridad estructural
- Errores explícitos y trazables
- Escalabilidad en sistemas reales
- Diseño orientado a esquema

Los modelos actúan como **esquemas ejecutables**,
garantizando consistencia desde la definición.

---

## 6. Conclusión

Este módulo demuestra que:

- La estructura importa más que el control de flujo.
- Las reglas deben formar parte del modelo.
- La validación es diseño, no parche.

Se consolida una mentalidad orientada a arquitectura,
coherencia y contratos explícitos de datos.