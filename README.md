# VenueBot AI 🍽️📚

An Intelligent Booking & Operations SaaS Platform for Hybrid Businesses (Restaurants with Study Spaces/Event Halls).

## 🚀 The Problem
Hybrid businesses struggle with double bookings, mismatched food prep times, and staff missing critical notifications. Managing restaurant tables, event halls, and quiet study zones requires a unified system.

## 💡 The Solution
VenueBot AI is a multi-platform SaaS that uses **LLM-powered AI Agents** to:
1. Automate customer bookings via a mobile app.
2. Resolve scheduling conflicts (e.g., noise from an event hall vs. a study zone).
3. Time kitchen preparation perfectly using automated staff alarms.
4. Generate automated monthly business intelligence reports emailed to the owner.

## 🏗️ Architecture
- **Backend:** Python, FastAPI, PostgreSQL, LangGraph (AI Agents)
- **Web Dashboard:** React.js, TailwindCSS, Recharts
- **Mobile Apps:** Flutter (Customer & Staff versions)
- **Automation:** Firebase Cloud Messaging (Alarms), Celery (Background Reports)
- **Deployment:** Docker, AWS

## 📂 Project Structure
- `/backend`: FastAPI server and AI Agent logic.
- `/web-dashboard`: Owner's analytics and management portal.
- `/mobile-customer`: Customer booking and ordering app.
- `/mobile-staff`: Staff task and alarm app.
- `/docs`: Architecture and API documentation.