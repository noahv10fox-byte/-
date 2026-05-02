 PROFESSIONAL ANTIVIRUS - QUICK START GUIDE
=================================================

## SETUP

### 1️ Run the Antivirus
```bash
python Antivirus.py
```

### 2️ Create Your Account
- Select option: **1. Create account**
- Username: Enter any name (minimum 3 characters)
- Password: Create a strong password (minimum 6 characters)
- Confirm the password

### 3️ Log In
- Select option: **2. Log in**
- Enter your username and password

### 4️ Explore the Main Panel
You now have access to all the tools:

1. **Scan Files/Directories** -  RECOMMENDED FIRST
2. Ransomware Detector
3. Firewall Manager
4. Network Monitor
5. Intrusion Prevention System (IPS)
6. Configuration Analysis -  View your security score
7. Threat Database
8. View Logs
9. Settings

---

##  RECOMMENDED TASKS

### Task 1: Perform Your First Scan
1. Select **1. Scan Files/Directories**
2. Choose **1. Quick Scan**
3. Enter a folder path, for example:

C:\Windows\Temp

Or a specific file:

C:\Users\YourUsername\Downloads\file.exe

4. View the scan results

### Task 2: View Your Security Score
1. Select **6. Configuration Analysis**
2. Choose **2. View Security Score**
3. Learn the current status of your system

### Task 3: Configure Firewall
1. Select **3. Firewall Manager**
2. Choose **1. View Active Rules**
3. View the default rules
4. (Optional) Add a new rule

### Task 4: Review Database
1. Select **7. Threat Database**
2. Explore known ransomware and malware signatures

### Task 5: Change Password
1. Select **9. Settings**
2. Choose **1. Change Password**
3. Follow the process

---

##  FUNCTIONALITY TESTS

### Test 1: Ransomware Detector
```
Path: C:\Users\YourUsername\Documents
- The system will search for suspicious extensions (.encrypted, .locked, etc.)
```

### Test 2: Deep Scan
```
Path: C:\Users\YourUsername\AppData\Local\Temp
- Full heuristic analysis
- Detection of suspicious patterns
```

### Test 3: Configuration Analysis
```
Go to: Option 6 > Option 1
- It will analyze your Windows security
- It will give you recommendations
```

---

##  UNDERSTANDING THE SCANNING LEVELS

###  Quick Scan
-  Time: 1-5 seconds per file
-  Checks for: Malware and ransomware signatures
-  Coverage: 85%

###  Slow Scan
-  Time: 5-15 seconds per file
-  Checks for: Suspicious behavior in content
-  Coverage: 92%

###  Deep Scan
-  Time: 15-60 seconds per file
-  Checks for: Advanced heuristic analysis, code injection
-  Coverage: 98%

---

##  MAIN FEATURES TO TEST

### 1. Authentication System
-  Create an account with validation
-  Secure Login/Logout
-  Password Change
-  SHA256 Hashing

### 2. Threat Scanner
-  Quick/Slow/Deep Scan
-  Malware Detection
-  Ransomware Detection
-  Entropy Analysis

### 3. Ransomware Detector
-  Suspicious Extension Scan
-  Bulk Encryption Detection
-  Ransom README File Detection

### 4. Firewall
-  Rule Management
-  Port/Protocol Blocking
-  Suspicious Port Detection

### 5. Network Monitor
-  Connection Logging
-  Anomaly Detection
-  Exfiltration Detection
-  Traffic Statistics

### 6. IPS System
-  Port Scanning Detection
-  Brute Force Detection
-  SQL Injection Detection
-  XSS Detection
-  IP Blocking

### 7. Configuration Analysis
-  Windows Defender Verification
-  Firewall Status
-  UAC Verification
-  Automatic Updates
-  Security Score

### 8. Database Threat Data
-  Signature Update
-  Threat Query
-  Pattern Information

---

##  WHERE YOUR DATA IS LOCATED

All data is stored in the `data/` folder:

```
data/
├── users.json → Your (hashed) credentials
├── threats_db.json → Threat database
├── firewall_rules.json → Your firewall rules
├── network_logs.json → Network logs
├── ips_logs.json → Intrusion logs
├── config_analysis.json → Configuration analysis Configuration
└── logs.json → System Logs
```

---

##  QUICK MENU OPTIONS

```
MAIN MENU
├─ 1. Scan Files/Directories
│ ├─ 1. Quick Scan
│ ├─ 2. Slow Scan
│ └─ 3. Deep Scan
├─ 2. Ransomware Detector
│ ├─ 1. Scan Directory
│ ├─ 2. Detect Activity
│ └─ 3. Detect Encryption
├─ 3. Firewall Manager
│ ├─ 1. View Rules
│ ├─ 2. Add rule
│ ├─ 3. Delete rule
│ └─ 4. Enable/Disable
├─ 4. Network Monitor
│ ├─ 1. Log connection
│ ├─ 2. Analyze traffic
│ ├─ 3. Detect exfiltration
│ ├─ 4. View connections
│ └─ 5. View statistics
├─ 5. IPS System
│ ├─ 1. View Attempts
│ ├─ 2. View Blocked IPs
│ ├─ 3. Block IP
│ ├─ 4. Unblock IP
│ └─ 5. Statistics
├─ 6. Configuration Analysis
│ ├─ 1. Full Analysis
│ ├─ 2. Score
│ ├─ 3. Recommendations
│ └─ 4. Generate Report
├─ 7. Database
│ ├─ 1. Update
│ ├─ 2. View Ransomware
│ ├─ 3. View Malware
│ └─ 4. View behaviors
├─ 8. View Logs
├─ 9. Settings
│ ├─ 1. Change password
│ ├─ 2. Preferences
│ └─ 3. About
└─ 10. Log out
```

---

##  TROUBLESHOOTING

###  "File not found"
- Verify that the path exists
- Use absolute paths: `C:\Users\...`
- On Linux/Mac: `/home/user/...`

###  "Insufficient permissions"
- Run as Administrator
- Some files are locked from the system

###  "Error writing data"
- Ensure the `data/` folder Exists
- Checks write permissions

###  "Login failed"
- Checks case sensitivity
- Password is case-sensitive

---

##  ADVANCED TIPS

### Tip 1: Scan Full System
```
Option 1 → Deep Scan
Path: C:\
This will take longer but is very thorough
```

### Tip 2: Monitor Downloads Only
```
Option 1 → Quick Scan
Path: C:\Users\YourUsername\Downloads
Run regularly
```

### Tip 3: Create Custom Rules
```
Option 3 → Add rule
Type: inbound
Protocol: TCP
Port: 3389 (RDP)
Action: block
Reason: "Prevent remote access"
```

### Tip 4: View Network Traffic
```
Option 4 → Log connection
Source IP: 192.168.1.100
Destination IP: 8.8.8.8
Port: 443
```

---

##  USEFUL INFORMATION

**Version**: 1.0
**Requirements**: Python 3.7+
**License**: MIT
**Platforms**: Windows, Linux, macOS

---

##  LEARN MORE

Read the file **README.md** for complete documentation
Check the **logs** in `data/logs.json` for history

---

## WELCOME! 

Enjoy protecting your system!

Press Enter in any menu to go back.
