# Backend Development Tasks – SQMS

This file contains the prioritized tasks for the backend development of the Smart Queue Management System (SQMS).

## Priority 1: Foundation & Core Queue Logic (Sprint 1-2)
- [ ] **Project Setup:** Initialize Django project and define app architecture (Apps: `api`, `queue`, `users`).
- [ ] **Database Integration:** Set up Firebase Firestore client as a utility service (Django doesn't natively support Firestore as a primary DB, so custom wrappers are needed).
- [ ] **Authentication Service:** Implement Firebase Auth integration and custom Django Authentication backend with JWT role-based permissions (FR1-FR3).
- [ ] **Core Queue Logic:** Implement API views for ticket generation (FR7) and status transition endpoints (FR11, FR12, FR13).
- [ ] **Branch Management:** Implement CRUD for branches and services via Django Rest Framework (DRF) (FR20-FR22).

## Priority 2: Real-time & Communications (Sprint 3-4)
- [ ] **WebSocket Integration:** Set up Socket.io server (possibly using `django-channels` or a standalone service) for live queue updates (FR9, NFR2).
- [ ] **ETA Calculation:** Implement logic within Django services to calculate estimated wait times based on queue length (FR8).
- [ ] **Notification Service:** Integrate Twilio for SMS and Firebase FCM for push notifications (FR15-FR18).
- [ ] **Notification Triggers:** Implement signals or service layers to send alerts when <3 people remain (FR16) and when called (FR17).
- [ ] **QR Code Endpoint:** Generate dynamic URLs/data for on-site QR code scanning (FR10).

## Priority 3: Features & Analytics (Sprint 5-6)
- [ ] **Appointment Scheduling:** Implement booking logic with real-time availability checks (FR28-FR31).
- [ ] **Analytics Engine:** Build service layers to track staff performance (FR26) and aggregate wait time stats (FR24).
- [ ] **Reporting Service:** Implement PDF/CSV export for branch analytics using libraries like `reportlab` or `pandas` (FR27).
- [ ] **Walk-in Handling:** Logic for moving absent customers to the end of the queue (FR14).

## Priority 4: Security & Optimization (Sprint 7-8)
- [ ] **Security Hardening:** Configure Django security settings (HTTPS, XSS/CSRF filters) (NFR7).
- [ ] **Rate Limiting:** Implement rate limiting middleware (e.g., `django-ratelimit`) after 5 failed attempts (FR5).
- [ ] **Performance Tuning:** Optimize Firestore queries and service methods to meet <300ms response time (NFR1).
- [ ] **Backup & Logging:** Configure daily database backups and standard Django logging (NFR10).

---
*Note: Priorities are aligned with the 8-week delivery constraint.*
