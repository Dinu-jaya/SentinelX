# SentinelX
SentinelX is a smart exam paper integrity system combines document fingerprinting, secure transport and real-time tracking to detect and trace exam paper leaks. The platform integrates micro-typographic document fingerprinting, IoT-enabled tamper detection, GPS ,centralized dashboard to ensure end-to-end security throughout the exam paper lifecycle
SentinelX
Intelligent Exam Paper Integrity & Traceability System
Overview

SentinelX is an integrated security platform designed to safeguard confidential examination papers throughout their lifecycle—from printing to the examination hall.

The system combines intelligent document fingerprinting with IoT-based transport monitoring to ensure that examination papers remain secure and traceable at every stage.

If an unauthorized access attempt occurs during transportation, SentinelX immediately reports the incident with precise location and timestamp information. If a paper is leaked, the system analyzes the leaked image and identifies the corresponding distribution batch, enabling authorities to investigate the source efficiently.

Problem Statement

Examination paper leaks compromise the integrity of public examinations, resulting in financial losses, delayed recruitment, and diminished public trust.

Current methods focus primarily on physical security and lack the ability to:

Detect unauthorized access during transportation
Trace leaked papers back to their distribution source
Provide centralized real-time monitoring
Maintain an auditable chain of custody

SentinelX addresses these challenges through a unified hardware and software solution.

Key Features
Secure Document Fingerprinting
Unique fingerprint embedded into every printed batch
Invisible to human readers
Recoverable from scanned or photographed documents
Batch-level traceability
Smart Transport Box
ESP32-powered secure transport case
GPS tracking
GSM-based alert system
Tamper detection
Authorized checkpoint verification
Monitoring Dashboard
Live GPS tracking
Tamper alerts
Batch management
Incident timeline
Leak investigation portal
Leak Investigation

Upload a leaked question paper image.

The system:

Detects the embedded fingerprint
Identifies the corresponding batch
Retrieves assigned exam center
Displays complete audit history
Technology Stack
Frontend
React
Tailwind CSS
Leaflet Maps
Axios
Backend
Spring Boot (Java)
REST APIs
JWT Authentication
Watermark Engine
Python
OpenCV
OCR
ReportLab
Hardware
ESP32
Neo-6M GPS
SIM800L GSM
Reed Switch
Buzzer
Database
PostgreSQL
