"""
Example usage of the Boleto Aereo (Air Ticket) system.
This script demonstrates how to create and manage air tickets.
"""

from datetime import datetime, timedelta
from boleto_aereo import BoletoAereo, SistemaReservas


def main():
    """Main example function demonstrating the air ticket system."""
    
    print("=" * 60)
    print("SISTEMA DE BOLETOS AEREOS - DEMOSTRACIÓN")
    print("=" * 60)
    print()
    
    # Create a reservation system
    sistema = SistemaReservas()
    
    # Example 1: Create a single ticket
    print(">>> Ejemplo 1: Crear un boleto")
    print("-" * 60)
    
    fecha_vuelo1 = datetime.now() + timedelta(days=7)
    boleto1 = sistema.crear_boleto(
        nombre_pasajero="Juan Pérez García",
        identificacion="12345678A",
        numero_vuelo="IB2024",
        origen="Madrid (MAD)",
        destino="Barcelona (BCN)",
        fecha_vuelo=fecha_vuelo1,
        numero_asiento="12A",
        precio=150.00,
        clase="Económica"
    )
    
    print(boleto1.mostrar_boleto())
    print()
    
    # Example 2: Create multiple tickets
    print("\n>>> Ejemplo 2: Crear múltiples boletos")
    print("-" * 60)
    
    fecha_vuelo2 = datetime.now() + timedelta(days=14)
    boleto2 = sistema.crear_boleto(
        nombre_pasajero="María López Fernández",
        identificacion="87654321B",
        numero_vuelo="AA1234",
        origen="Nueva York (JFK)",
        destino="Los Angeles (LAX)",
        fecha_vuelo=fecha_vuelo2,
        numero_asiento="5C",
        precio=450.00,
        clase="Ejecutiva"
    )
    
    fecha_vuelo3 = datetime.now() + timedelta(days=21)
    boleto3 = sistema.crear_boleto(
        nombre_pasajero="Carlos Rodríguez Sánchez",
        identificacion="11223344C",
        numero_vuelo="UA5678",
        origen="Chicago (ORD)",
        destino="Miami (MIA)",
        fecha_vuelo=fecha_vuelo3,
        numero_asiento="22F",
        precio=280.00,
        clase="Económica"
    )
    
    print(f"Total de boletos creados: {len(sistema)}")
    print()
    
    # Example 3: List all tickets
    print("\n>>> Ejemplo 3: Listar todos los boletos")
    print("-" * 60)
    
    for boleto in sistema.listar_boletos():
        resumen = boleto.obtener_resumen()
        print(f"• {resumen['codigo_reserva']}: {resumen['pasajero']}")
        print(f"  {resumen['vuelo']} - {resumen['ruta']}")
        print(f"  Fecha: {resumen['fecha']} | Asiento: {resumen['asiento']} | Precio: ${resumen['precio']:.2f}")
        print(f"  Estado: {resumen['estado']}")
        print()
    
    # Example 4: Search for a ticket
    print("\n>>> Ejemplo 4: Buscar un boleto por código")
    print("-" * 60)
    
    codigo_buscar = boleto2.codigo_reserva
    boleto_encontrado = sistema.buscar_boleto(codigo_buscar)
    
    if boleto_encontrado:
        print(f"Boleto encontrado: {boleto_encontrado}")
        print()
    else:
        print(f"No se encontró el boleto con código: {codigo_buscar}")
        print()
    
    # Example 5: Cancel a ticket
    print("\n>>> Ejemplo 5: Cancelar un boleto")
    print("-" * 60)
    
    print(f"Estado antes de cancelar: {boleto3.estado}")
    if boleto3.cancelar_boleto():
        print(f"Boleto cancelado exitosamente")
        print(f"Estado después de cancelar: {boleto3.estado}")
    else:
        print("No se pudo cancelar el boleto")
    print()
    
    # Example 6: Calculate total sales
    print("\n>>> Ejemplo 6: Calcular ventas totales")
    print("-" * 60)
    
    total = sistema.total_ventas()
    print(f"Total de ventas (boletos confirmados): ${total:.2f}")
    print(f"Número de boletos confirmados: {sum(1 for b in sistema.listar_boletos() if b.estado == 'Confirmado')}")
    print()
    
    # Example 7: Display a complete ticket
    print("\n>>> Ejemplo 7: Mostrar boleto completo")
    print("-" * 60)
    print(boleto2.mostrar_boleto())
    
    print("\n" + "=" * 60)
    print("FIN DE LA DEMOSTRACIÓN")
    print("=" * 60)


if __name__ == "__main__":
    main()
