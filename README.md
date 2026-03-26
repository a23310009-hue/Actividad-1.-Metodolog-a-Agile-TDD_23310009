# Sistema de Recordatorios para Adultos Mayores

Este proyecto implementa la metodología TDD (Test Driven Development) en una funcionalidad básica de una aplicación orientada al cuidado de la salud de adultos mayores.

La funcionalidad desarrollada consiste en generar recordatorios de citas médicas a partir del nombre del paciente, la fecha y la hora.

## Relación con el proyecto

Este módulo forma parte de una app enfocada en adultos mayores, cuyo objetivo es apoyar el seguimiento de su salud mediante recordatorios automáticos de citas médicas y una interfaz sencilla.

## Ciclo Red-Green-Refactor aplicado

### Red
Se creó primero una prueba unitaria para definir el comportamiento esperado de la función `generar_recordatorio`. En esta etapa, la prueba falla porque la implementación aún no existe.

### Green
Se desarrolló la implementación mínima necesaria para que la prueba pasara correctamente.

### Refactor
Se mejoró la función agregando validación de datos incompletos, sin alterar el comportamiento correcto del caso válido.

## Pruebas realizadas

- Generación de recordatorio con datos válidos
- Validación de datos vacíos
- Validación de datos incompletos

## Archivos del proyecto

- `recordatorios.py`
- `test_recordatorio.py`
- `README.md`
