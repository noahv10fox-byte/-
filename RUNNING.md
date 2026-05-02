#  PROFESSIONAL ANTIVIRUS - RUNNING GUIDE

##  QUICK WAY TO GET STARTED

### Option 1: Run with Full Interface (Recommended)

```bash
cd c:\Python-projects\AntiVirus
python Antivirus.py
```

**Steps:**
1. Create a new account
2. Log in
3. Explore the control panel with all features

### Option 2: View Automatic Demo

```bash
cd c:\Python-projects\AntiVirus
python demo.py
```

**This will automatically run:**
- Authentication System
- Threat Scanner
- Ransomware Detector
- Firewall Manager
- Network Monitor
- Intrusion Prevention System (IPS)
- Analysis of Configuration
- Threat Database

---

##  IMPLEMENTED FEATURES

###  1. Authentication System
- [x] Create new account
- [x] Secure login
- [x] SHA256 hash for passwords
- [x] Change password
- [x] Password validation (minimum 6 characters)
- [x] Session management

###  2. Threat Scanner
- [x] Quick scan (signatures)
- [x] Slow scan (behaviors)
- [x] Deep scan (heuristic)
- [x] Malware detection
- [x] Ransomware detection
- [x] SHA256 hash analysis
- [x] Recursive directory scanning

###  3. Specialized Ransomware Detector
- [x] Identify suspicious extensions
- [x] Detect mass encryption
- [x] Search for ransom README files
- [x] Entropy analysis for encrypted files
- [x] Critical severity alerts

###  4. Intelligent Firewall
- [x] Rule management (inbound/outbound)
- [x] Blocking by port and protocol
- [x] List of suspicious ports
- [x] Enable/disable firewall
- [x] Connection logging
- [x] Suspicious traffic detection

###  5. Network Monitor
- [x] Connection Log
- [x] Traffic Anomaly Analysis
- [x] Data Exfiltration Detection
- [x] Network Statistics
- [x] Top Ports and Destinations
- [x] Connection Filtering

###  6. Intrusion Prevention System (IPS)
- [x] Port Scanning Detection
- [x] Brute Force Attack Detection
- [x] SQL Injection Detection
- [x] XSS Detection
- [x] Malware Signature Detection
- [x] Privilege Escalation Detection
- [x] Automatic IP Blocking
- [x] Intrusion Attempt Logging

###  7. Security Configuration Analysis
- [x] Windows Defender Verification
- [x] Firewall Status
- [x] User Access Control (UAC)
- [x] Automatic Updates
- [x] Network Sharing
- [x] RDP Configuration
- [x] USB Autorun
- [x] Password Policy
- [x] Security Score (0-100)
- [x] Personalized Recommendations

###  8. Threat Database
- [x] Ransomware Signatures (WannaCry, Petya, Ryuk, REvil, etc.)
- [x] Malware Signatures
- [x] Suspicious Behavior Patterns
- [x] Vulnerable Configurations
- [x] Automatic Updates

###  9. Complete CLI Interface
- [x] Elegant Main Menu
- [x] Intuitive Navigation
- [x] Input Validation
- [x] Clear Error Messages
- [x] Operation Confirmations
- [x] Integrated Help System

---

##  STRUCTURE OF FILES

```
AntiVirus/
├── Antivirus.py #  Main Interface (run this)
├── demo.py # Automatic Demo
├── README.md # Full Documentation
├── QUICK_START.md # Quick Start Guide
├── requirements.txt # Dependencies (none)
│
├── modules/ # 🔧 System Modules
│ ├── __init__.py
│ ├── auth.py # Authentication
│ ├── database.py # Database
│ ├── scanner.py # Scanner
│ ├── ransomware_detector.py # Ransomware detector
│ ├── firewall.py # Firewall
│ ├── network_monitor.py # Network monitor
│ ├── intrusion_prevention.py #IPS
│ └── config_analyzer.py # Configuration analysis
│
└── data/ # 💾 Persistent data
    ├── users.json
    ├── threats_db.json
    ├── firewall_rules.json
    ├── network_logs.json
    ├── ips_logs.json
    └── logs.json
```

---

##  USE CASES

### Case 1: Ransomware Detection
```bash
1. Run: python Antivirus.py
2. Create an account and log in
3. Option 2: Ransomware Detector
4. Option 1: Scan Directory
5. Enter folder to scan
```

### Case 2: Network Analysis
```bash
1. Run: python Antivirus.py
2. Log in
3. Option 4: Network Monitor
4. Log connections or analyze for anomalies
```

### Case 3: View Security Score
```bash
1. Run: python Antivirus.py
2. Log in
3. Option 6: Configuration Analysis
4. Option 2: View Security Score
```

### Case 4: Manage Firewall
```bash
1. Run: python Antivirus.py
2. Log in
3. Option 3: Firewall Manager
4. View/Add/Delete rules
```

---

##  IMPLEMENTED SECURITY

 **Passwords:**
- Hashed with SHA256
- Stored locally
- Minimum 6-character validation

 **Authentication:**
- Secure sessions
- Automatic session logout
- Log of failed login attempts

 **Logging:**
- All events are logged
- Logs in JSON for easy analysis
- Security event history

 **Detection:**
- Advanced heuristics
- Entropy analysis
- Malicious pattern detection
- Signatures of known threats

---

##  ANALYSIS FEATURES

### Scanner
- 3 levels of analysis
- SHA256 hash for integrity
- Behavioral analysis
- Heuristic detection

### Ransomware
- Suspicious extensions
- Bulk encryption
- README files
- Entropy analysis

### Firewall
- Customizable rules
- Full logging
- Alerts for suspicious ports

### Network
- Traffic monitoring
- Anomaly detection
- Exfiltration analysis

### IPS
- Detection of 6 types of Attacks
- IP Blocking
- Attempt Logging

---

##  TESTS

To run the demo:

```bash
python demo.py
```

This tests:
- ✅ Authentication
- ✅ File Scanning
- ✅ Ransomware Detection
- ✅ Firewall Rules
- ✅ Network Traffic
- ✅ Intrusion Prevention
- ✅ Configuration Analysis
- ✅ Threat Database

---

##  STORED DATA

All data is automatically saved in `data/`:

- **users.json**: User credentials (hashed)
- **threats_db.json**: Threat database
- **firewall_rules.json**: Firewall rules
- **network_logs.json**: Network logs
- **ips_logs.json**: Intrusion logs
- **config_analysis.json**: Configuration analysis
- **logs.json**: General system logs

---

##  DEFAULT CONFIGURATION

```json
{
"scan_level": "quick",
"auto_update": true,
"notifications": true,
"firewall": "enabled",
"ips": "active"
}
```

---

##  UPCOMING FUTURE IMPROVEMENTS

- [ ] Graphical User Interface (GUI)
- [ ] VirusTotal Integration
- [ ] Cloud Scanning
- [ ] File Quarantine
- [ ] Scheduled Automatic Scans
- [ ] Multi-Language Support
- [ ] Cloud synchronization
- [ ] Exportable reports (PDF/Excel)


---

##  QUICK COMMANDS

```bash
# Run main application
python Antivirus.py

# View demo
python demo.py

# View documentation
more README.md

# View quick start guide
more QUICK_START.md

# View requirements
more requirements.txt
```

---

##  HELP

### "How do I get started?"

→ Read QUICK_START.md

### "What does each module do?"

→ Read README.md

### "How do I view the logs?"

→ Open `data/logs.json` or select Option 8 from the menu

### "I lost my password?"

→ Delete `data/users.json` and create a new account

### "How do I update threats?"

→ Option 7 → Option 1 in the main menu

---

##  INFORMATION

- **Version**: 1.0
- **Author**: Security Team
- **License**: MIT
- **Python**: 3.7+
- **Platforms**: Windows, Linux, macOS

---

##  ENJOY!

Your professional antivirus is ready to protect your system!

```
python Antivirus.py
```

Welcome! 
