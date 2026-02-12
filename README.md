# tarea2.2 - Sistema de Boletos Aereos

Sistema de gestión de boletos aéreos (air ticket booking system) implementado en Python.

## Descripción

Este proyecto implementa un sistema completo para la gestión de boletos aéreos que incluye:

- **Clase BoletoAereo**: Representa un boleto aéreo individual con toda la información del pasajero, vuelo y reserva
- **Clase SistemaReservas**: Gestiona múltiples boletos y proporciona funcionalidades de búsqueda y reportes

## Características

- Creación de boletos con información completa del pasajero y vuelo
- Generación automática de códigos de reserva únicos
- Visualización formateada de boletos
- Cancelación de boletos
- Búsqueda de boletos por código de reserva
- Cálculo de ventas totales
- Soporte para diferentes clases de viaje (Económica, Ejecutiva, Primera)

## Uso

### Ejemplo básico

```python
from datetime import datetime, timedelta
from boleto_aereo import BoletoAereo, SistemaReservas

# Crear sistema de reservas
sistema = SistemaReservas()

# Crear un boleto
fecha_vuelo = datetime.now() + timedelta(days=7)
boleto = sistema.crear_boleto(
    nombre_pasajero="Juan Pérez",
    identificacion="12345678A",
    numero_vuelo="IB2024",
    origen="Madrid (MAD)",
    destino="Barcelona (BCN)",
    fecha_vuelo=fecha_vuelo,
    numero_asiento="12A",
    precio=150.00,
    clase="Económica"
)

# Mostrar el boleto
print(boleto.mostrar_boleto())
```

### Ejecutar ejemplos

```bash
python3 ejemplo.py
```

### Ejecutar tests

```bash
python3 -m unittest test_boleto_aereo.py -v
```

## Estructura del Proyecto

- `boleto_aereo.py` - Módulo principal con las clases BoletoAereo y SistemaReservas
- `ejemplo.py` - Script de demostración con ejemplos de uso
- `test_boleto_aereo.py` - Suite de tests unitarios
- `README.md` - Este archivo

## Requisitos

- Python 3.6 o superior

## Autor

Sistema desarrollado para tarea2.2
