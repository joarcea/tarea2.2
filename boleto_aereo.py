"""
Boleto Aereo - Air Ticket Booking System
This module implements a simple air ticket booking system.
"""

from datetime import datetime
from typing import Optional


class BoletoAereo:
    """
    Represents an air ticket (boleto aereo) with passenger and flight information.
    """
    
    def __init__(
        self,
        nombre_pasajero: str,
        identificacion: str,
        numero_vuelo: str,
        origen: str,
        destino: str,
        fecha_vuelo: datetime,
        numero_asiento: str,
        precio: float,
        clase: str = "Económica"
    ):
        """
        Initialize an air ticket.
        
        Args:
            nombre_pasajero: Passenger's full name
            identificacion: Passenger's ID or passport number
            numero_vuelo: Flight number (e.g., "AA1234")
            origen: Origin city/airport
            destino: Destination city/airport
            fecha_vuelo: Flight date and time
            numero_asiento: Seat number (e.g., "12A")
            precio: Ticket price
            clase: Travel class (Económica, Ejecutiva, Primera)
        """
        self.nombre_pasajero = nombre_pasajero
        self.identificacion = identificacion
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_vuelo = fecha_vuelo
        self.numero_asiento = numero_asiento
        self.precio = precio
        self.clase = clase
        self.codigo_reserva = self._generar_codigo_reserva()
        self.estado = "Confirmado"
    
    def _generar_codigo_reserva(self) -> str:
        """
        Generate a unique reservation code based on passenger info and timestamp.
        
        Returns:
            A unique reservation code
        """
        import hashlib
        data = f"{self.nombre_pasajero}{self.identificacion}{datetime.now().timestamp()}"
        hash_code = hashlib.md5(data.encode()).hexdigest()[:6].upper()
        return f"BA{hash_code}"
    
    def mostrar_boleto(self) -> str:
        """
        Display the ticket information in a formatted way.
        
        Returns:
            Formatted ticket information as a string
        """
        separador = "=" * 60
        ticket_info = f"""
{separador}
                    BOLETO AEREO
{separador}

Código de Reserva: {self.codigo_reserva}
Estado: {self.estado}

INFORMACIÓN DEL PASAJERO:
  Nombre:         {self.nombre_pasajero}
  Identificación: {self.identificacion}

DETALLES DEL VUELO:
  Vuelo:          {self.numero_vuelo}
  Origen:         {self.origen}
  Destino:        {self.destino}
  Fecha/Hora:     {self.fecha_vuelo.strftime("%d/%m/%Y %H:%M")}
  Asiento:        {self.numero_asiento}
  Clase:          {self.clase}

INFORMACIÓN DE PAGO:
  Precio:         ${self.precio:.2f}

{separador}
        """
        return ticket_info.strip()
    
    def cancelar_boleto(self) -> bool:
        """
        Cancel the ticket.
        
        Returns:
            True if cancellation was successful, False otherwise
        """
        if self.estado == "Cancelado":
            return False
        self.estado = "Cancelado"
        return True
    
    def obtener_resumen(self) -> dict:
        """
        Get a summary of the ticket as a dictionary.
        
        Returns:
            Dictionary with ticket information
        """
        return {
            "codigo_reserva": self.codigo_reserva,
            "pasajero": self.nombre_pasajero,
            "vuelo": self.numero_vuelo,
            "ruta": f"{self.origen} → {self.destino}",
            "fecha": self.fecha_vuelo.strftime("%d/%m/%Y %H:%M"),
            "asiento": self.numero_asiento,
            "precio": self.precio,
            "estado": self.estado
        }
    
    def __str__(self) -> str:
        """String representation of the ticket."""
        return f"Boleto {self.codigo_reserva}: {self.nombre_pasajero} - {self.numero_vuelo} ({self.origen} → {self.destino})"
    
    def __repr__(self) -> str:
        """Technical representation of the ticket."""
        return (f"BoletoAereo(nombre_pasajero='{self.nombre_pasajero}', "
                f"numero_vuelo='{self.numero_vuelo}', "
                f"origen='{self.origen}', destino='{self.destino}')")


class SistemaReservas:
    """
    Manages multiple air ticket reservations.
    """
    
    def __init__(self):
        """Initialize the reservation system."""
        self.boletos = []
    
    def crear_boleto(
        self,
        nombre_pasajero: str,
        identificacion: str,
        numero_vuelo: str,
        origen: str,
        destino: str,
        fecha_vuelo: datetime,
        numero_asiento: str,
        precio: float,
        clase: str = "Económica"
    ) -> BoletoAereo:
        """
        Create and register a new air ticket.
        
        Returns:
            The newly created ticket
        """
        boleto = BoletoAereo(
            nombre_pasajero=nombre_pasajero,
            identificacion=identificacion,
            numero_vuelo=numero_vuelo,
            origen=origen,
            destino=destino,
            fecha_vuelo=fecha_vuelo,
            numero_asiento=numero_asiento,
            precio=precio,
            clase=clase
        )
        self.boletos.append(boleto)
        return boleto
    
    def buscar_boleto(self, codigo_reserva: str) -> Optional[BoletoAereo]:
        """
        Search for a ticket by reservation code.
        
        Args:
            codigo_reserva: Reservation code to search for
            
        Returns:
            The ticket if found, None otherwise
        """
        for boleto in self.boletos:
            if boleto.codigo_reserva == codigo_reserva:
                return boleto
        return None
    
    def listar_boletos(self) -> list:
        """
        List all tickets in the system.
        
        Returns:
            List of all tickets
        """
        return self.boletos
    
    def total_ventas(self) -> float:
        """
        Calculate total sales from all confirmed tickets.
        
        Returns:
            Total sales amount
        """
        return sum(b.precio for b in self.boletos if b.estado == "Confirmado")
    
    def __len__(self) -> int:
        """Return the number of tickets in the system."""
        return len(self.boletos)
