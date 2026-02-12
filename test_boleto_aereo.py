"""
Unit tests for the Boleto Aereo system.
"""

import unittest
from datetime import datetime, timedelta
from boleto_aereo import BoletoAereo, SistemaReservas


class TestBoletoAereo(unittest.TestCase):
    """Test cases for BoletoAereo class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.fecha_vuelo = datetime.now() + timedelta(days=7)
        self.boleto = BoletoAereo(
            nombre_pasajero="Test Passenger",
            identificacion="TEST123",
            numero_vuelo="TEST001",
            origen="Madrid",
            destino="Barcelona",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="10A",
            precio=100.0,
            clase="Económica"
        )
    
    def test_crear_boleto(self):
        """Test ticket creation."""
        self.assertEqual(self.boleto.nombre_pasajero, "Test Passenger")
        self.assertEqual(self.boleto.identificacion, "TEST123")
        self.assertEqual(self.boleto.numero_vuelo, "TEST001")
        self.assertEqual(self.boleto.origen, "Madrid")
        self.assertEqual(self.boleto.destino, "Barcelona")
        self.assertEqual(self.boleto.numero_asiento, "10A")
        self.assertEqual(self.boleto.precio, 100.0)
        self.assertEqual(self.boleto.clase, "Económica")
        self.assertEqual(self.boleto.estado, "Confirmado")
    
    def test_codigo_reserva_generado(self):
        """Test that reservation code is generated."""
        self.assertIsNotNone(self.boleto.codigo_reserva)
        self.assertTrue(self.boleto.codigo_reserva.startswith("BA"))
        self.assertEqual(len(self.boleto.codigo_reserva), 8)
    
    def test_mostrar_boleto(self):
        """Test ticket display."""
        display = self.boleto.mostrar_boleto()
        self.assertIn("BOLETO AEREO", display)
        self.assertIn("Test Passenger", display)
        self.assertIn("TEST001", display)
        self.assertIn("Madrid", display)
        self.assertIn("Barcelona", display)
    
    def test_cancelar_boleto(self):
        """Test ticket cancellation."""
        self.assertEqual(self.boleto.estado, "Confirmado")
        resultado = self.boleto.cancelar_boleto()
        self.assertTrue(resultado)
        self.assertEqual(self.boleto.estado, "Cancelado")
        
        # Try to cancel again
        resultado = self.boleto.cancelar_boleto()
        self.assertFalse(resultado)
    
    def test_obtener_resumen(self):
        """Test getting ticket summary."""
        resumen = self.boleto.obtener_resumen()
        self.assertEqual(resumen['pasajero'], "Test Passenger")
        self.assertEqual(resumen['vuelo'], "TEST001")
        self.assertEqual(resumen['asiento'], "10A")
        self.assertEqual(resumen['precio'], 100.0)
        self.assertEqual(resumen['estado'], "Confirmado")
    
    def test_str_representation(self):
        """Test string representation."""
        str_repr = str(self.boleto)
        self.assertIn("Test Passenger", str_repr)
        self.assertIn("TEST001", str_repr)


class TestSistemaReservas(unittest.TestCase):
    """Test cases for SistemaReservas class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sistema = SistemaReservas()
        self.fecha_vuelo = datetime.now() + timedelta(days=7)
    
    def test_crear_boleto(self):
        """Test creating a ticket through the system."""
        boleto = self.sistema.crear_boleto(
            nombre_pasajero="Test Passenger",
            identificacion="TEST123",
            numero_vuelo="TEST001",
            origen="Madrid",
            destino="Barcelona",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="10A",
            precio=100.0
        )
        
        self.assertIsInstance(boleto, BoletoAereo)
        self.assertEqual(len(self.sistema), 1)
    
    def test_buscar_boleto(self):
        """Test searching for a ticket."""
        boleto = self.sistema.crear_boleto(
            nombre_pasajero="Test Passenger",
            identificacion="TEST123",
            numero_vuelo="TEST001",
            origen="Madrid",
            destino="Barcelona",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="10A",
            precio=100.0
        )
        
        codigo = boleto.codigo_reserva
        encontrado = self.sistema.buscar_boleto(codigo)
        self.assertEqual(encontrado, boleto)
        
        no_encontrado = self.sistema.buscar_boleto("INVALID")
        self.assertIsNone(no_encontrado)
    
    def test_listar_boletos(self):
        """Test listing all tickets."""
        self.sistema.crear_boleto(
            nombre_pasajero="Passenger 1",
            identificacion="TEST1",
            numero_vuelo="TEST001",
            origen="Madrid",
            destino="Barcelona",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="10A",
            precio=100.0
        )
        
        self.sistema.crear_boleto(
            nombre_pasajero="Passenger 2",
            identificacion="TEST2",
            numero_vuelo="TEST002",
            origen="Madrid",
            destino="Valencia",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="10B",
            precio=80.0
        )
        
        boletos = self.sistema.listar_boletos()
        self.assertEqual(len(boletos), 2)
    
    def test_total_ventas(self):
        """Test calculating total sales."""
        boleto1 = self.sistema.crear_boleto(
            nombre_pasajero="Passenger 1",
            identificacion="TEST1",
            numero_vuelo="TEST001",
            origen="Madrid",
            destino="Barcelona",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="10A",
            precio=100.0
        )
        
        boleto2 = self.sistema.crear_boleto(
            nombre_pasajero="Passenger 2",
            identificacion="TEST2",
            numero_vuelo="TEST002",
            origen="Madrid",
            destino="Valencia",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="10B",
            precio=80.0
        )
        
        # Total should be 180.0
        self.assertEqual(self.sistema.total_ventas(), 180.0)
        
        # Cancel one ticket
        boleto1.cancelar_boleto()
        
        # Total should now be 80.0 (only confirmed tickets)
        self.assertEqual(self.sistema.total_ventas(), 80.0)
    
    def test_len(self):
        """Test getting the number of tickets."""
        self.assertEqual(len(self.sistema), 0)
        
        self.sistema.crear_boleto(
            nombre_pasajero="Test",
            identificacion="TEST",
            numero_vuelo="TEST001",
            origen="A",
            destino="B",
            fecha_vuelo=self.fecha_vuelo,
            numero_asiento="1A",
            precio=100.0
        )
        
        self.assertEqual(len(self.sistema), 1)


if __name__ == "__main__":
    unittest.main()
