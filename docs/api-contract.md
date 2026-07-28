# SentinelX API Contract

This document defines the communication contract between the Watermark, Hardware, Backend, and Frontend modules.

---

## Base URL

```
http://localhost:5000/api
```

---

# 1. Create Watermark Batch

**Endpoint**

```
POST /batches
```

**Called By**

- Watermark Embed Module

**Request Body**

```json
{
  "batch_id": 47,
  "exam_center": "Coimbatore-3",
  "exam_date": "2026-08-07"
}
```

**Response**

```json
{
  "success": true,
  "message": "Batch created successfully"
}
```

---

# 2. Hardware Event

**Endpoint**

```
POST /boxes/:box_id/event
```

**Called By**

- ESP32 Hardware

**Request Body**

```json
{
  "event": "TAMPER_ALERT",
  "lat": 13.05,
  "lng": 80.21,
  "timestamp": "2026-08-07T10:30:00Z"
}
```

Possible values of `event`

- TAMPER_ALERT
- AUTHORIZED_OPEN
- LOCATION_UPDATE

**Response**

```json
{
  "success": true
}
```

---

# 3. Get Box Status

**Endpoint**

```
GET /boxes
```

**Called By**

- Frontend Dashboard

**Response**

```json
[
  {
    "box_id": "BOX001",
    "batch_id": 47,
    "state": "ARMED",
    "last_lat": 13.05,
    "last_lng": 80.21
  }
]
```

---

# 4. Get Alerts

**Endpoint**

```
GET /alerts
```

**Called By**

- Frontend Dashboard

**Response**

```json
[
  {
    "box_id": "BOX001",
    "event_type": "TAMPER_ALERT",
    "lat": 13.05,
    "lng": 80.21,
    "timestamp": "2026-08-07T10:30:00Z"
  }
]
```

---

# 5. Extract Watermark

**Endpoint**

```
POST /watermark/extract
```

**Called By**

- Frontend Lookup Tool

**Request**

Multipart Form Data

```
image=<uploaded image>
```

**Response (Detected)**

```json
{
  "detected": true,
  "batch_id": 47,
  "exam_center": "Coimbatore-3"
}
```

**Response (Not Detected)**

```json
{
  "detected": false
}
```

---

# Notes

- All requests and responses use JSON unless uploading files.
- Backend runs on port 5000.
- Frontend should only use these endpoints.
- Watermark module should not directly access MongoDB.
- Hardware communicates only through the backend API.
