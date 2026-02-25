
🪐 Python Module — Cosmic Data
MAP — Modelado Declarativo y Validación Estructural con Pydantic v2
1. Propósito del módulo

Este módulo introduce el modelado estructurado de datos mediante Pydantic v2, entendiendo el modelo como un contrato ejecutable.

El objetivo no es solo validar entradas, sino comprender cómo:

Declarar esquemas tipados y auto-validados

Centralizar reglas estructurales y de negocio

Garantizar coherencia en el momento de instanciación

Separar validación del flujo imperativo

Representa la transición de validaciones manuales (if, try) a un enfoque declarativo y arquitectónico.

2. Fundamentos técnicos trabajados

BaseModel como núcleo estructural

Type hints como contrato formal

Field() para restricciones declarativas:

min_length / max_length

ge / le

pattern

Enum como conjunto cerrado de valores

@model_validator(mode="after") para reglas cruzadas

Modelos anidados

Validación relacional entre entidades

Gestión estructurada de errores (ValidationError)

3. Progresión por ejercicios
🔹 ex0 — SpaceStation

Validación declarativa a nivel de campo

Se aplican restricciones directamente en el esquema del modelo.

Aprendizaje:

La validación simple pertenece a la definición del dato, no al flujo de ejecución.

🔹 ex1 — AlienContact

Validación relacional y reglas de negocio

Se introduce:

Enum para restringir dominios

@model_validator(after) para coherencia global

Las reglas dependen de la combinación de campos:

Contactos físicos deben estar verificados

Contactos telepáticos requieren mínimo 3 testigos

Señales fuertes requieren mensaje

Aprendizaje:

Las reglas de negocio viven en el modelo, no en el controlador.

🔹 ex2 — SpaceCrew

Modelos anidados y coherencia sistémica

Se modela una entidad compuesta (SpaceMission) que contiene:

Múltiples CrewMember

Reglas de seguridad agregadas

Validaciones globales:

Presencia obligatoria de liderazgo

Experiencia mínima en misiones largas

Actividad obligatoria del equipo

Aprendizaje:

La validación puede representar integridad estructural del sistema completo.

4. Evolución conceptual

Antes:

Validación dispersa

Lógica imperativa repetitiva

Dependencia del orden de ejecución

Ahora:

Validación centralizada

Modelo como fuente única de verdad

Integridad garantizada en el momento de creación

El modelo deja de ser un contenedor pasivo y pasa a ser un esquema ejecutable.

5. Valor arquitectónico

Este enfoque permite:

Reducir duplicación de lógica

Diseñar contratos explícitos

Detectar errores en frontera

Escalar estructuras complejas

Construir sistemas coherentes desde el dato

Pydantic convierte el modelo en:

Una aduana estructural que impide la entrada de datos inconsistentes.

6. Conclusión

Este módulo consolida una mentalidad:

Declarar antes que comprobar

Diseñar antes que parchear

Modelar antes que ejecutar

La validación deja de ser defensiva y se convierte en parte del diseño.