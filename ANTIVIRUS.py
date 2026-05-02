#!/usr/bin/env python3
"""
ANTIVIRUS PROFESIONAL - Sistema completo de protección
Autor: Security Team
Versión: 1.0
"""

import os
import sys
import time
import getpass
from pathlib import Path

# Importar módulos
from modules.auth import AuthenticationManager
from modules.database import DatabaseManager
from modules.scanner import Scanner
from modules.ransomware_detector import RansomwareDetector
from modules.firewall import FirewallManager
from modules.network_monitor import NetworkMonitor
from modules.intrusion_prevention import IntrusionPrevention
from modules.config_analyzer import ConfigAnalyzer

class AntivirusInterface:
    """Interfaz principal del antivirus"""
    
    def __init__(self):
        self.auth = AuthenticationManager()
        self.db = DatabaseManager()
        self.running = False
        self.clear_screen()
    
    def clear_screen(self):
        """Limpia la pantalla"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Imprime encabezado"""
        print("=" * 70)
        print(" " * 15 + "🛡️  ANTIVIRUS PROFESIONAL v1.0  🛡️")
        print("=" * 70)
    
    def print_menu(self, options, title="Menú"):
        """Imprime menú formateado"""
        print(f"\n[{title}]")
        print("-" * 50)
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        print("-" * 50)
    
    def get_choice(self, max_option):
        """Obtiene opción del usuario"""
        while True:
            try:
                choice = input("\nSelecciona opción: ").strip()
                if choice.isdigit() and 1 <= int(choice) <= max_option:
                    return int(choice)
                print(f"❌ Opción inválida. Ingresa un número entre 1 y {max_option}")
            except KeyboardInterrupt:
                print("\n\n⚠️  Operación cancelada por el usuario")
                return None
            except Exception as e:
                print(f"❌ Error: {e}")
    
    # === MENÚ PRINCIPAL ===
    def main_menu(self):
        """Menú principal sin autenticar"""
        self.clear_screen()
        self.print_header()
        
        options = [
            "Crear cuenta",
            "Iniciar sesión",
            "Salir"
        ]
        
        self.print_menu(options, "BIENVENIDO")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.register_user()
        elif choice == 2:
            self.login_user()
        elif choice == 3:
            print("\n✅ ¡Hasta luego!")
            sys.exit(0)
    
    def register_user(self):
        """Registra nuevo usuario"""
        self.clear_screen()
        self.print_header()
        print("\n[CREAR CUENTA NUEVA]\n")
        
        username = input("Usuario: ").strip()
        if not username:
            print("❌ El usuario no puede estar vacío")
            input("Presiona Enter para continuar...")
            return
        
        password = getpass.getpass("Contraseña: ")
        if not password:
            print("❌ La contraseña no puede estar vacía")
            input("Presiona Enter para continuar...")
            return
        
        password_confirm = getpass.getpass("Confirmar contraseña: ")
        
        result = self.auth.register(username, password, password_confirm)
        
        if result["success"]:
            print(f"\n✅ {result['message']}")
            print("Ahora puedes iniciar sesión con tu cuenta")
        else:
            print(f"\n❌ {result['message']}")
        
        input("\nPresiona Enter para continuar...")
    
    def login_user(self):
        """Autentica usuario"""
        self.clear_screen()
        self.print_header()
        print("\n[INICIAR SESIÓN]\n")
        
        username = input("Usuario: ").strip()
        password = getpass.getpass("Contraseña: ")
        
        result = self.auth.login(username, password)
        
        if result["success"]:
            print(f"\n✅ {result['message']}")
            input("Presiona Enter para continuar...")
            self.dashboard()
        else:
            print(f"\n❌ {result['message']}")
            input("Presiona Enter para intentar de nuevo...")
    
    # === DASHBOARD ===
    def dashboard(self):
        """Panel de control principal"""
        while True:
            self.clear_screen()
            self.print_header()
            user = self.auth.get_current_user()
            print(f"\n👤 Usuario: {user}\n")
            
            options = [
                "Escanear archivos/directorios",
                "Detector de Ransomware",
                "Gestor de Firewall",
                "Monitor de Red",
                "Sistema de Prevención de Intrusiones",
                "Análisis de Configuración",
                "Base de Datos de Amenazas",
                "Ver Logs",
                "Configuración",
                "Cerrar sesión"
            ]
            
            self.print_menu(options, "PANEL DE CONTROL")
            choice = self.get_choice(len(options))
            
            if choice == 1:
                self.scanner_menu()
            elif choice == 2:
                self.ransomware_menu()
            elif choice == 3:
                self.firewall_menu()
            elif choice == 4:
                self.network_monitor_menu()
            elif choice == 5:
                self.intrusion_prevention_menu()
            elif choice == 6:
                self.config_analyzer_menu()
            elif choice == 7:
                self.threats_database_menu()
            elif choice == 8:
                self.view_logs()
            elif choice == 9:
                self.settings_menu()
            elif choice == 10:
                self.auth.logout()
                print("\n✅ Sesión cerrada")
                input("Presiona Enter para continuar...")
                break
    
    # === ESCÁNER ===
    def scanner_menu(self):
        """Menú del escáner"""
        self.clear_screen()
        self.print_header()
        print("\n[ESCÁNER DE AMENAZAS]\n")
        
        options = [
            "Escaneo rápido",
            "Escaneo lento",
            "Escaneo profundo",
            "Atrás"
        ]
        
        self.print_menu(options, "TIPO DE ESCANEO")
        choice = self.get_choice(len(options))
        
        if choice in [1, 2, 3]:
            levels = {1: "quick", 2: "slow", 3: "deep"}
            self.perform_scan(levels[choice])
        elif choice == 4:
            return
    
    def perform_scan(self, scan_level):
        """Realiza escaneo"""
        self.clear_screen()
        self.print_header()
        print(f"\n[ESCANEO {scan_level.upper()}]\n")
        
        path = input("Ruta a escanear (archivo o directorio): ").strip()
        
        if not path:
            print("❌ Ruta no proporcionada")
            input("Presiona Enter para continuar...")
            return
        
        path = Path(path)
        
        if not path.exists():
            print("❌ Ruta no encontrada")
            input("Presiona Enter para continuar...")
            return
        
        scanner = Scanner()
        
        print(f"\n⏳ Escaneando {scan_level}...")
        
        if path.is_file():
            result = scanner.scan_file(path, scan_level)
        else:
            result = scanner.scan_directory(path, scan_level, recursive=True)
        
        self._print_scan_results(result)
    
    def _print_scan_results(self, result):
        """Imprime resultados del escaneo"""
        print("\n" + "=" * 50)
        print("RESULTADOS DEL ESCANEO")
        print("=" * 50)
        
        if result.get("files_scanned"):
            print(f"\n📁 Archivos escaneados: {result['files_scanned']}")
            print(f"⚠️  Amenazas encontradas: {result['threats_found']}")
        else:
            print(f"\n📁 Archivo: {result['file']}")
            print(f"📊 Tamaño: {result['size']} bytes")
            print(f"🔒 Seguro: {'Sí ✅' if result['is_safe'] else 'No ❌'}")
            
            if result.get("threats_found"):
                print(f"\n⚠️  AMENAZAS DETECTADAS ({len(result['threats_found'])}):")
                for threat in result["threats_found"]:
                    print(f"  - {threat['name']} ({threat['type']}) - Riesgo: {threat['severity']}")
        
        print("\n" + "=" * 50)
        input("Presiona Enter para continuar...")
    
    # === RANSOMWARE ===
    def ransomware_menu(self):
        """Menú del detector de ransomware"""
        self.clear_screen()
        self.print_header()
        print("\n[DETECTOR DE RANSOMWARE]\n")
        
        options = [
            "Escanear directorio",
            "Detectar actividad sospechosa",
            "Detectar encriptación masiva",
            "Atrás"
        ]
        
        self.print_menu(options, "OPCIONES RANSOMWARE")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.ransomware_scan_directory()
        elif choice == 2:
            self.ransomware_detect_activity()
        elif choice == 3:
            self.ransomware_detect_mass_encryption()
        elif choice == 4:
            return
    
    def ransomware_scan_directory(self):
        """Escanea directorio por ransomware"""
        self.clear_screen()
        print("\n[ESCANEO DE RANSOMWARE]\n")
        
        path = input("Ruta a escanear: ").strip()
        
        if not path or not Path(path).exists():
            print("❌ Ruta no válida")
            input("Presiona Enter para continuar...")
            return
        
        detector = RansomwareDetector()
        print("\n⏳ Escaneando...")
        result = detector.perform_full_ransomware_scan(path)
        
        print("\n" + "=" * 50)
        print("RESULTADOS - RANSOMWARE")
        print("=" * 50)
        print(f"\n📁 Directorio: {result['directory']}")
        print(f"🔒 Seguro: {'Sí ✅' if result['is_safe'] else 'No ❌'}")
        print(f"⚠️  Alertas: {result['total_alerts']}")
        
        if result['alerts']:
            print("\nALERTAS DETECTADAS:")
            for alert in result['alerts']:
                print(f"  - {alert['reason']} (Severidad: {alert['severity']})")
        
        print("\n" + "=" * 50)
        input("Presiona Enter para continuar...")
    
    def ransomware_detect_activity(self):
        """Detecta actividad de ransomware"""
        self.clear_screen()
        print("\n[DETECTAR ACTIVIDAD DE RANSOMWARE]\n")
        
        path = input("Ruta a escanear: ").strip()
        
        if not path or not Path(path).exists():
            print("❌ Ruta no válida")
            input("Presiona Enter para continuar...")
            return
        
        detector = RansomwareDetector()
        alerts = detector.detect_ransomware_activity(path)
        
        print("\n" + "=" * 50)
        print(f"Alertas encontradas: {len(alerts)}")
        
        for alert in alerts:
            print(f"\n⚠️  {alert['reason']}")
            print(f"   Archivo: {alert['file']}")
            print(f"   Severidad: {alert['severity']}")
        
        print("=" * 50)
        input("Presiona Enter para continuar...")
    
    def ransomware_detect_mass_encryption(self):
        """Detecta encriptación masiva"""
        self.clear_screen()
        print("\n[DETECTAR ENCRIPTACIÓN MASIVA]\n")
        
        path = input("Ruta a escanear: ").strip()
        
        if not path or not Path(path).exists():
            print("❌ Ruta no válida")
            input("Presiona Enter para continuar...")
            return
        
        detector = RansomwareDetector()
        alerts = detector.detect_mass_encryption(path)
        
        print("\n" + "=" * 50)
        print(f"Eventos sospechosos: {len(alerts)}")
        
        for alert in alerts:
            print(f"\n🚨 {alert['reason']}")
            print(f"   Severidad: {alert['severity']}")
        
        print("=" * 50)
        input("Presiona Enter para continuar...")
    
    # === FIREWALL ===
    def firewall_menu(self):
        """Menú del firewall"""
        self.clear_screen()
        self.print_header()
        print("\n[GESTOR DE FIREWALL]\n")
        
        options = [
            "Ver reglas activas",
            "Añadir regla",
            "Eliminar regla",
            "Habilitar/Deshabilitar",
            "Atrás"
        ]
        
        self.print_menu(options, "FIREWALL")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.firewall_view_rules()
        elif choice == 2:
            self.firewall_add_rule()
        elif choice == 3:
            self.firewall_remove_rule()
        elif choice == 4:
            self.firewall_toggle()
        elif choice == 5:
            return
    
    def firewall_view_rules(self):
        """Muestra reglas del firewall"""
        self.clear_screen()
        print("\n[REGLAS DEL FIREWALL]\n")
        
        fw = FirewallManager()
        rules = fw.get_rules()
        
        print("=" * 80)
        print(f"{'Tipo':<10} | {'Protocolo':<10} | {'Puerto':<8} | {'Acción':<10} | {'Razón':<30}")
        print("=" * 80)
        
        for rule in rules:
            print(f"{rule['type']:<10} | {rule['protocol']:<10} | {rule['port']:<8} | {rule['action']:<10} | {rule['reason']:<30}")
        
        print("=" * 80)
        print(f"\nTotal de reglas: {len(rules)}")
        input("\nPresiona Enter para continuar...")
    
    def firewall_add_rule(self):
        """Añade regla al firewall"""
        self.clear_screen()
        print("\n[AÑADIR REGLA FIREWALL]\n")
        
        rule_type = input("Tipo (inbound/outbound): ").strip().lower()
        if rule_type not in ["inbound", "outbound"]:
            print("❌ Tipo inválido")
            input("Presiona Enter para continuar...")
            return
        
        protocol = input("Protocolo (TCP/UDP): ").strip().upper()
        if protocol not in ["TCP", "UDP"]:
            print("❌ Protocolo inválido")
            input("Presiona Enter para continuar...")
            return
        
        try:
            port = int(input("Puerto: ").strip())
        except ValueError:
            print("❌ Puerto debe ser un número")
            input("Presiona Enter para continuar...")
            return
        
        action = input("Acción (allow/block): ").strip().lower()
        if action not in ["allow", "block"]:
            print("❌ Acción inválida")
            input("Presiona Enter para continuar...")
            return
        
        reason = input("Razón: ").strip()
        
        fw = FirewallManager()
        result = fw.add_rule(rule_type, protocol, port, action, reason)
        
        print(f"\n✅ {result['message']}")
        input("Presiona Enter para continuar...")
    
    def firewall_remove_rule(self):
        """Elimina regla del firewall"""
        self.clear_screen()
        print("\n[ELIMINAR REGLA]\n")
        
        try:
            port = int(input("Puerto a eliminar: ").strip())
            rule_type = input("Tipo (inbound/outbound): ").strip().lower()
        except ValueError:
            print("❌ Entrada inválida")
            input("Presiona Enter para continuar...")
            return
        
        fw = FirewallManager()
        result = fw.remove_rule(port, rule_type)
        
        print(f"\n✅ {result['message']}")
        input("Presiona Enter para continuar...")
    
    def firewall_toggle(self):
        """Habilita/deshabilita firewall"""
        self.clear_screen()
        print("\n[ESTADO DEL FIREWALL]\n")
        
        fw = FirewallManager()
        is_enabled = fw.is_firewall_enabled()
        
        print(f"Estado actual: {'Habilitado ✅' if is_enabled else 'Deshabilitado ❌'}")
        
        options = ["Habilitar" if not is_enabled else "Deshabilitar", "Atrás"]
        self.print_menu(options, "OPCIONES")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            if is_enabled:
                result = fw.disable_firewall()
            else:
                result = fw.enable_firewall()
            print(f"\n✅ {result['message']}")
            input("Presiona Enter para continuar...")
    
    # === MONITOR DE RED ===
    def network_monitor_menu(self):
        """Menú del monitor de red"""
        self.clear_screen()
        self.print_header()
        print("\n[MONITOR DE RED]\n")
        
        options = [
            "Simular conexión de red",
            "Analizar tráfico",
            "Detectar exfiltración",
            "Ver conexiones activas",
            "Ver estadísticas",
            "Atrás"
        ]
        
        self.print_menu(options, "MONITOR DE RED")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.network_log_connection()
        elif choice == 2:
            self.network_analyze_traffic()
        elif choice == 3:
            self.network_detect_exfiltration()
        elif choice == 4:
            self.network_view_connections()
        elif choice == 5:
            self.network_statistics()
        elif choice == 6:
            return
    
    def network_log_connection(self):
        """Simula/registra conexión de red"""
        self.clear_screen()
        print("\n[REGISTRAR CONEXIÓN]\n")
        
        source_ip = input("IP origen (ej: 192.168.1.100): ").strip()
        dest_ip = input("IP destino (ej: 8.8.8.8): ").strip()
        
        try:
            port = int(input("Puerto: ").strip())
        except ValueError:
            print("❌ Puerto debe ser un número")
            input("Presiona Enter para continuar...")
            return
        
        protocol = input("Protocolo (TCP/UDP): ").strip().upper()
        process = input("Proceso (opcional): ").strip()
        
        nm = NetworkMonitor()
        result = nm.log_connection(source_ip, dest_ip, port, protocol, process)
        
        print(f"\n✅ Conexión registrada: {dest_ip}:{port} ({protocol})")
        input("Presiona Enter para continuar...")
    
    def network_analyze_traffic(self):
        """Analiza tráfico de red"""
        self.clear_screen()
        print("\n[ANÁLISIS DE TRÁFICO]\n")
        
        nm = NetworkMonitor()
        analysis = nm.analyze_traffic()
        
        print("=" * 50)
        print(f"Total de conexiones: {analysis['total_connections']}")
        print(f"IPs sospechosas: {len(analysis['suspicious_ips'])}")
        print(f"Puertos sospechosos: {len(analysis['suspicious_ports'])}")
        print(f"Anomalías totales: {len(analysis['anomalies'])}")
        
        if analysis['anomalies']:
            print("\n⚠️  ANOMALÍAS DETECTADAS:")
            for anomaly in analysis['anomalies']:
                print(f"  - {anomaly}")
        
        print("=" * 50)
        input("Presiona Enter para continuar...")
    
    def network_detect_exfiltration(self):
        """Detecta exfiltración de datos"""
        self.clear_screen()
        print("\n[DETECTAR EXFILTRACIÓN]\n")
        
        nm = NetworkMonitor()
        alerts = nm.detect_exfiltration()
        
        print(f"Alertas de exfiltración: {len(alerts)}\n")
        
        for alert in alerts:
            print(f"⚠️  {alert['type']}")
            print(f"   Destino: {alert['destination']}")
            print(f"   Conexiones: {alert['connection_count']}")
            print(f"   Severidad: {alert['severity']}\n")
        
        input("Presiona Enter para continuar...")
    
    def network_view_connections(self):
        """Muestra conexiones activas"""
        self.clear_screen()
        print("\n[CONEXIONES ACTIVAS]\n")
        
        nm = NetworkMonitor()
        connections = nm.get_active_connections()
        
        print(f"Conexiones: {len(connections)}\n")
        
        for conn in connections[:10]:  # Mostrar primeras 10
            print(f"  {conn['source_ip']} → {conn['dest_ip']}:{conn['port']} ({conn['protocol']})")
        
        if len(connections) > 10:
            print(f"  ... y {len(connections) - 10} conexiones más")
        
        input("\nPresiona Enter para continuar...")
    
    def network_statistics(self):
        """Muestra estadísticas de red"""
        self.clear_screen()
        print("\n[ESTADÍSTICAS DE RED]\n")
        
        nm = NetworkMonitor()
        stats = nm.get_network_statistics()
        
        print(f"Total de conexiones: {stats['total_connections']}")
        print(f"Destinos únicos: {stats['unique_destinations']}")
        print(f"Protocolos usados: {', '.join(stats['protocols_used'])}")
        
        print(f"\nPuertos más usados:")
        for port, count in stats['top_ports']:
            print(f"  Puerto {port}: {count} conexiones")
        
        print(f"\nDestinos más usados:")
        for dest, count in stats['top_destinations']:
            print(f"  {dest}: {count} conexiones")
        
        input("\nPresiona Enter para continuar...")
    
    # === PREVENCIÓN DE INTRUSIONES ===
    def intrusion_prevention_menu(self):
        """Menú del sistema IPS"""
        self.clear_screen()
        self.print_header()
        print("\n[SISTEMA DE PREVENCIÓN DE INTRUSIONES (IPS)]\n")
        
        options = [
            "Ver intentos detectados",
            "Ver IPs bloqueadas",
            "Bloquear IP",
            "Desbloquear IP",
            "Estadísticas",
            "Atrás"
        ]
        
        self.print_menu(options, "IPS")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.ips_view_attempts()
        elif choice == 2:
            self.ips_view_blocked()
        elif choice == 3:
            self.ips_block_ip()
        elif choice == 4:
            self.ips_unblock_ip()
        elif choice == 5:
            self.ips_statistics()
        elif choice == 6:
            return
    
    def ips_view_attempts(self):
        """Muestra intentos de intrusión"""
        self.clear_screen()
        print("\n[INTENTOS DE INTRUSIÓN DETECTADOS]\n")
        
        ips = IntrusionPrevention()
        logs = ips.get_intrusion_logs(limit=20)
        
        print(f"Total de intentos: {len(logs)}\n")
        
        for log in logs[-10:]:
            print(f"⚠️  {log['type']}")
            print(f"   Severidad: {log['severity']}")
            print(f"   Acción: {log['action']}\n")
        
        input("Presiona Enter para continuar...")
    
    def ips_view_blocked(self):
        """Muestra IPs bloqueadas"""
        self.clear_screen()
        print("\n[IPS BLOQUEADAS]\n")
        
        ips = IntrusionPrevention()
        blocked = ips.get_blocked_ips()
        
        print(f"Total IPs bloqueadas: {len(blocked)}\n")
        
        for ip_block in blocked:
            print(f"🚫 {ip_block['ip']}")
            print(f"   Razón: {ip_block['reason']}")
            print(f"   Bloqueada: {ip_block['blocked_at']}\n")
        
        input("Presiona Enter para continuar...")
    
    def ips_block_ip(self):
        """Bloquea una IP"""
        self.clear_screen()
        print("\n[BLOQUEAR IP]\n")
        
        ip = input("IP a bloquear: ").strip()
        reason = input("Razón (opcional): ").strip()
        
        ips = IntrusionPrevention()
        result = ips.block_ip(ip, reason)
        
        print(f"\n✅ {result['message']}")
        input("Presiona Enter para continuar...")
    
    def ips_unblock_ip(self):
        """Desbloquea una IP"""
        self.clear_screen()
        print("\n[DESBLOQUEAR IP]\n")
        
        ip = input("IP a desbloquear: ").strip()
        
        ips = IntrusionPrevention()
        result = ips.unblock_ip(ip)
        
        print(f"\n✅ {result['message']}")
        input("Presiona Enter para continuar...")
    
    def ips_statistics(self):
        """Muestra estadísticas IPS"""
        self.clear_screen()
        print("\n[ESTADÍSTICAS IPS]\n")
        
        ips = IntrusionPrevention()
        stats = ips.get_statistics()
        
        print(f"Total ataques detectados: {stats['total_attacks_detected']}")
        print(f"IPs bloqueadas: {stats['blocked_ips']}")
        
        print("\nTipos de ataque:")
        for attack_type, count in stats['attack_types'].items():
            print(f"  - {attack_type}: {count}")
        
        input("\nPresiona Enter para continuar...")
    
    # === ANÁLISIS DE CONFIGURACIÓN ===
    def config_analyzer_menu(self):
        """Menú de análisis de configuración"""
        self.clear_screen()
        self.print_header()
        print("\n[ANÁLISIS DE CONFIGURACIÓN DE SEGURIDAD]\n")
        
        options = [
            "Realizar análisis completo",
            "Ver puntuación de seguridad",
            "Ver recomendaciones",
            "Generar reporte",
            "Atrás"
        ]
        
        self.print_menu(options, "CONFIGURACIÓN")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.config_full_analysis()
        elif choice == 2:
            self.config_security_score()
        elif choice == 3:
            self.config_recommendations()
        elif choice == 4:
            self.config_generate_report()
        elif choice == 5:
            return
    
    def config_full_analysis(self):
        """Realiza análisis de configuración completo"""
        self.clear_screen()
        print("\n[ANÁLISIS DE CONFIGURACIÓN]\n")
        print("⏳ Analizando configuración del sistema...")
        
        analyzer = ConfigAnalyzer()
        report = analyzer.analyze_all()
        
        print("\n" + "=" * 50)
        print("RESULTADOS DEL ANÁLISIS")
        print("=" * 50)
        
        for check_name, check_data in report["checks"].items():
            status = "✅" if check_data["status"] == "enabled" else "⚠️"
            print(f"\n{status} {check_data['name']}")
            print(f"   Recomendación: {check_data['recommendation']}")
        
        print("\n" + "=" * 50)
        input("Presiona Enter para continuar...")
    
    def config_security_score(self):
        """Muestra puntuación de seguridad"""
        self.clear_screen()
        print("\n[PUNTUACIÓN DE SEGURIDAD]\n")
        
        analyzer = ConfigAnalyzer()
        score = analyzer.get_security_score()
        
        print(f"📊 Puntuación: {score['score']}/100")
        print(f"📈 Calificación: {score['grade']}\n")
        
        vuln = score['vulnerabilities']
        print("Vulnerabilidades:")
        print(f"  🔴 Críticas: {vuln['critical']}")
        print(f"  🟠 Altas: {vuln['high']}")
        print(f"  🟡 Medias: {vuln['medium']}")
        print(f"  🟢 Bajas: {vuln['low']}")
        
        input("\nPresiona Enter para continuar...")
    
    def config_recommendations(self):
        """Muestra recomendaciones"""
        self.clear_screen()
        print("\n[RECOMENDACIONES DE SEGURIDAD]\n")
        
        analyzer = ConfigAnalyzer()
        recommendations = analyzer.get_recommendations()
        
        print(f"Total recomendaciones: {len(recommendations)}\n")
        
        for rec in recommendations:
            print(f"⚠️  {rec['check']}")
            print(f"   Severidad: {rec['severity']}")
            print(f"   {rec['recommendation']}\n")
        
        input("Presiona Enter para continuar...")
    
    def config_generate_report(self):
        """Genera reporte de configuración"""
        self.clear_screen()
        print("\n[GENERANDO REPORTE]\n")
        print("⏳ Generando reporte de seguridad...")
        
        analyzer = ConfigAnalyzer()
        report = analyzer.generate_report()
        
        print("\n" + "=" * 50)
        print("REPORTE DE SEGURIDAD")
        print("=" * 50)
        print(f"\nGenerado: {report['generated_at']}")
        print(f"Puntuación: {report['security_score']['score']}/100")
        print(f"Calificación: {report['security_score']['grade']}")
        print(f"Total recomendaciones: {report['total_recommendations']}")
        print("\n" + "=" * 50)
        
        input("Presiona Enter para continuar...")
    
    # === BASE DE DATOS DE AMENAZAS ===
    def threats_database_menu(self):
        """Menú de base de datos de amenazas"""
        self.clear_screen()
        self.print_header()
        print("\n[BASE DE DATOS DE AMENAZAS]\n")
        
        options = [
            "Actualizar base de datos",
            "Ver firmas de ransomware",
            "Ver firmas de malware",
            "Ver comportamientos sospechosos",
            "Atrás"
        ]
        
        self.print_menu(options, "BASE DE DATOS")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.threats_update()
        elif choice == 2:
            self.threats_view_ransomware()
        elif choice == 3:
            self.threats_view_malware()
        elif choice == 4:
            self.threats_view_behaviors()
        elif choice == 5:
            return
    
    def threats_update(self):
        """Actualiza base de datos"""
        self.clear_screen()
        print("\n[ACTUALIZAR BASE DE DATOS]\n")
        print("⏳ Actualizando base de datos de amenazas...")
        
        result = self.db.update_threats_database()
        
        print(f"\n✅ {result['message']}")
        input("Presiona Enter para continuar...")
    
    def threats_view_ransomware(self):
        """Muestra firmas de ransomware"""
        self.clear_screen()
        print("\n[FIRMAS DE RANSOMWARE]\n")
        
        threats = self.db.get_threats_database()
        ransomware = threats.get("ransomware_signatures", [])
        
        print(f"Total: {len(ransomware)}\n")
        
        for threat in ransomware:
            print(f"  • {threat['name']}")
            print(f"    Patrón: {threat['pattern']}\n")
        
        input("Presiona Enter para continuar...")
    
    def threats_view_malware(self):
        """Muestra firmas de malware"""
        self.clear_screen()
        print("\n[FIRMAS DE MALWARE]\n")
        
        threats = self.db.get_threats_database()
        malware = threats.get("malware_signatures", [])
        
        print(f"Total: {len(malware)}\n")
        
        for threat in malware:
            print(f"  • {threat['name']}")
            print(f"    Riesgo: {threat['risk']}\n")
        
        input("Presiona Enter para continuar...")
    
    def threats_view_behaviors(self):
        """Muestra comportamientos sospechosos"""
        self.clear_screen()
        print("\n[COMPORTAMIENTOS SOSPECHOSOS]\n")
        
        threats = self.db.get_threats_database()
        behaviors = threats.get("suspicious_behaviors", [])
        
        print(f"Total: {len(behaviors)}\n")
        
        for behavior in behaviors:
            print(f"  • {behavior['behavior']}")
            print(f"    Severidad: {behavior['severity']}\n")
        
        input("Presiona Enter para continuar...")
    
    # === LOGS ===
    def view_logs(self):
        """Muestra logs del sistema"""
        self.clear_screen()
        print("\n[LOGS DEL SISTEMA]\n")
        
        logs = self.db.get_logs(limit=30)
        
        print(f"Últimos {len(logs)} eventos:\n")
        
        for log in logs[-10:]:
            print(f"  [{log['timestamp']}] {log['event']}")
        
        print("\n")
        input("Presiona Enter para continuar...")
    
    # === CONFIGURACIÓN ===
    def settings_menu(self):
        """Menú de configuración"""
        self.clear_screen()
        self.print_header()
        print("\n[CONFIGURACIÓN]\n")
        
        options = [
            "Cambiar contraseña",
            "Preferencias de escaneo",
            "Sobre",
            "Atrás"
        ]
        
        self.print_menu(options, "CONFIGURACIÓN")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            self.settings_change_password()
        elif choice == 2:
            self.settings_scan_preferences()
        elif choice == 3:
            self.settings_about()
        elif choice == 4:
            return
    
    def settings_change_password(self):
        """Cambia contraseña"""
        self.clear_screen()
        print("\n[CAMBIAR CONTRASEÑA]\n")
        
        old_password = getpass.getpass("Contraseña actual: ")
        new_password = getpass.getpass("Nueva contraseña: ")
        new_password_confirm = getpass.getpass("Confirmar nueva contraseña: ")
        
        result = self.auth.change_password(old_password, new_password, new_password_confirm)
        
        if result["success"]:
            print(f"\n✅ {result['message']}")
        else:
            print(f"\n❌ {result['message']}")
        
        input("Presiona Enter para continuar...")
    
    def settings_scan_preferences(self):
        """Preferencias de escaneo"""
        self.clear_screen()
        print("\n[PREFERENCIAS DE ESCANEO]\n")
        
        user = self.auth.get_current_user()
        settings = self.db.get_user_settings(user)
        
        options = [
            f"Nivel de escaneo (actual: {settings.get('scan_level', 'quick')})",
            f"Auto-actualización (actual: {'Sí ✅' if settings.get('auto_update') else 'No ❌'})",
            f"Notificaciones (actual: {'Sí ✅' if settings.get('notifications') else 'No ❌'})",
            "Atrás"
        ]
        
        self.print_menu(options, "PREFERENCIAS")
        choice = self.get_choice(len(options))
        
        if choice == 1:
            levels = ["quick", "slow", "deep"]
            print("\nNiveles disponibles:")
            for i, level in enumerate(levels, 1):
                print(f"  {i}. {level}")
            level_choice = input("Selecciona: ").strip()
            if level_choice.isdigit() and 1 <= int(level_choice) <= 3:
                self.db.update_user_settings(user, {"scan_level": levels[int(level_choice) - 1]})
                print("✅ Configuración actualizada")
        elif choice == 2:
            self.db.update_user_settings(user, {"auto_update": not settings.get('auto_update')})
            print("✅ Configuración actualizada")
        elif choice == 3:
            self.db.update_user_settings(user, {"notifications": not settings.get('notifications')})
            print("✅ Configuración actualizada")
        
        input("Presiona Enter para continuar...")
    
    def settings_about(self):
        """Información sobre el antivirus"""
        self.clear_screen()
        print("\n" + "=" * 50)
        print("🛡️  ANTIVIRUS PROFESIONAL v1.0")
        print("=" * 50)
        print("""
Sistema de protección integral que incluye:
  ✓ Escáner antimalware (Rápido, Lento, Profundo)
  ✓ Detector especializado de Ransomware
  ✓ Firewall inteligente
  ✓ Monitor de red en tiempo real
  ✓ Sistema de prevención de intrusiones (IPS)
  ✓ Análisis de configuración de seguridad
  ✓ Gestión de base de datos de amenazas
  ✓ Autenticación segura

Características:
  • Detección heurística avanzada
  • Escaneo profundo con análisis de entropía
  • Prevención de técnicas de ofuscación
  • Protección contra exploits
  • Análisis de comportamiento

Desarrollado por: Security Team
Versión: 1.0
Licencia: MIT
""")
        print("=" * 50)
        input("Presiona Enter para continuar...")
    
    def run(self):
        """Ejecuta la aplicación"""
        self.running = True
        
        while self.running:
            if not self.auth.is_authenticated():
                self.main_menu()
            else:
                self.dashboard()

# === PUNTO DE ENTRADA ===
if __name__ == "__main__":
    try:
        app = AntivirusInterface()
        app.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido")
    except Exception as e:
        print(f"\n❌ Error: {e}")
