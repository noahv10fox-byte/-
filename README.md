#  PROFESSIONAL ANTIVIRUS v1.0

## Description

A complete and functional antivirus in Python with professional cybersecurity features including:

###  Main Features

#### 1. **Antimalware Scanner**
- **Quick Scan**: Checks for known malware and ransomware signatures
- **Slow Scan**: Deeper file analysis, including suspicious behavior
- **Deep Scan**: Advanced heuristic analysis with injection pattern detection

#### 2. **Ransomware Detector**
- Identifies typical ransomware extensions
- Detects mass file encryption
- Searches for ransom README files
- Entropy analysis to detect encrypted files

#### 3. **Intelligent Firewall**
- Inbound/outbound rule management
- Blocking by port and protocol
- Connection logging
- Detection of suspicious ports

#### 4. **Network Monitor**
- Network connection logging
- Traffic analysis for anomalies
- Data exfiltration detection
- Real-time network statistics

#### 5. **Intrusion Prevention System (IPS)**
- Port scanning detection
- Brute-force attack detection
- SQL injection detection
- Cross-Site Scripting (XSS) detection
- Privilege escalation detection
- Automatic blocking of malicious IPs

#### 6. **Configuration Analysis**
- Windows Defender verification
- Firewall status
- User Account Control (UAC)
- Automatic updates
- Network sharing
- RDP configuration
- Password policy
- Overall security score

#### 7. **Threat Database Management**
- Known ransomware signatures
- Known malware signatures
- Suspicious behavior patterns
- Vulnerable Configurations
- Automatic Updates

#### 8. **Authentication System**
- New Account Registration
- Secure Login
- Password Change
- SHA256 Hashing for Passwords
- Session Management

---

##  Requirements

- Python 3.7 or higher
- Standard libraries only (no additional installation required)

---

##  Installation and Use

### 1. Clone/Download the project

```bash
cd c:\the name of your folder
\AntiVirus
```

### 2. Run the antivirus

```bash
python Antivirus.py
```

### 3. First launch

- Select "Create account" to register
- Use your username and password (minimum 6 characters)
- Log in with your credentials

---

## 📖 User Guide

### Main Panel

Once authenticated, you will access the control panel with the following options:

#### 1. **Scan files/directories**
```
- Choose scan type (Quick/Slow/Deep)
- Enter the file or folder path
- The system analyzes and reports threats
```

#### 2. **Ransomware Detector**
```
- Scan full directory
- Detect suspicious activity
- Detect mass encryption
```

#### 3. **Firewall Manager**
```
- View active rules
- Add new rules
- Delete existing rules
- Enable/Disable firewall
```

#### 4. **Network Monitor**
```
- Log connections
- Analyze traffic
- Detect exfiltration
- View active connections
- Network statistics
```

#### 5. **IPS System**
```
- View intrusion attempts
- Manage blocked IPs
- Block/Unblock IPs
- View attack statistics
```

#### 6. **Configuration Analysis**
```
- Full system analysis
- Security score
- Recommendations
- Generate report
```

#### 7. **Threat Database**
```
- Update database
- View known signatures
- Check for suspicious behavior
```

#### 8. **Settings**
```
- Change password
- Scanning preferences
- Program information
```

---

##  Usage Examples

### Scan a file
1. Select option 1 from the main menu
2. Choose "Quick Scan"
3. Enter the path: `C:\Users\Username\Downloads\file.exe`
4. The system analyzes and reports whether it is safe or malicious

### Detect ransomware in a folder
1. Select option 2 from the main menu
2. Choose "Scan directory"
3. Enter: `C:\Users\Username\Documents`
4. Get encryption analysis

### Configure Firewall
1. Select option 3 from the main menu
2. Choose "Add Rule"
3. Configure: inbound, TCP, port 3389, block, "RDP Threat"

---

##  Directory Structure

```
AntiVirus/
├── Antivirus.py # Main CLI Interface
├── modules/
│ ├── __init__.py
│ ├── database.py # Database Management
│ ├── auth.py # User Authentication
│ ├── scanner.py # Scanning Engine
│ ├── ransomware_detector.py # Ransomware Detector
│ ├── firewall.py # Firewall Manager
│ ├── network_monitor.py # Network Monitor
│ ├── intrusion_prevention.py # IPS System
│ └── config_analyzer.py # Analysis Configuration
└── data/ # Data Directory
├── users.json # User Information
├── threats_db.json # Threat Database
├── firewall_rules.json # Firewall Rules
├── network_logs.json # Network Logs
├── ips_logs.json # IPS Logs
└── logs.json # General Logs
```

---

## Security

### Passwords
- Passwords are hashed with SHA256
- At least 6 characters are validated
- Secure password change available

### Data
- All information is stored locally in JSON
- Automatic security event logs
- Log of failed login attempts Access

---

## Included Threat Signatures

### Known Ransomware
- CryptoWall
- WannaCry
- Petya
- Ryuk
- REvil

### Suspicious Behaviors
- SAM Access
- Mass File Encryption
- MBR Modification
- Execution from TEMP Directory
- Code Injection

### Vulnerable Configurations
- Open RDP
- UAC Disabled
- Windows Defender Disabled
- Firewall Disabled
- USB Autorun Enabled

---

## Security Score

The score is calculated from 0-100:
- **A (90-100)**: Excellent
- **B (80-89)**: Good
- **C (70-79)**: Acceptable
- **D (60-69)**: Poor
- **F (0-59)**: Critical

---

## Advanced Features

### Heuristic Detection
- Entropy analysis for encrypted files
- Injection pattern detection
- File behavior analysis

### Threat Intelligence
- Updatable database
- Malware and ransomware signatures
- Malicious behavior patterns
- Known insecure configurations

### Traffic Analysis
- Network anomaly detection
- Data exfiltration identification
- Suspicious port analysis
- Connection statistics

---

## Logs and Reports

The system maintains logs of:
- Login attempts
- Scans performed
- Threats detected
- Firewall changes
- Network traffic
- Intrusion attempts
- Configuration changes

All logs are automatically saved in the `data/` directory

---

##  Configuration by Default

- **Scan Level**: Fast
- **Auto Update**: Enabled
- **Notifications**: Enabled
- **Firewall**: Enabled
- **IPS**: Active

---

##  Update Database

1. From the main menu, select option 7
2. Select "Update Database"
3. The system downloads the latest signatures (simulated in this version)

---

##  Support

To report problems or suggestions:
- Check the logs in `data/logs.json`
- Verify that you have permissions in the antivirus folder
- Make sure you are using Python 3.7 or higher

---

##  License

MIT License - Free to use and modify

---

## Credits

Developed by CIBERESPAI Team

---

## Future Improvements

- [ ] VirusTotal Integration
- [ ] Cloud Scanning
- [ ] File Quarantine
- [ ] System Defragmentation and Cleanup
- [ ] Graphical User Interface (GUI)
- [ ] Schedule Automatic Scans
- [ ] Cloud Sync
- [ ] Multi-Language Support

---

##  Disclaimer

This antivirus is an educational and demonstration tool. For production protection, it is recommended to use certified commercial solutions such as:
- Windows Defender
- Norton
- McAfee
- Kaspersky
- Avast

This software is provided "as is" without warranties of any kind.
