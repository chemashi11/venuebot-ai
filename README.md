# VenueBot AI 🍽️📚

**An Intelligent Booking & Operations SaaS Platform for Hybrid Businesses (Restaurants + Study Spaces + Event Halls).**

## 🚀 The Problem
Hybrid businesses struggle with double bookings, mismatched food prep times, and staff missing critical notifications. Managing restaurant tables, event halls, and quiet study zones requires a unified, intelligent system that doesn't just take orders, but coordinates operations.

## 💡 The Solution
VenueBot AI is a full-stack SaaS platform that uses **LLM-powered AI Agents** to:
1.  **Automate Bookings:** Handle customer reservations via natural language chat.
2.  **Resolve Conflicts:** Prevent noisy events from overlapping with quiet study sessions.
3.  **Time Kitchen Prep:** Automatically calculate food prep times and schedule "ringing" alarms for staff via the backend.
4.  **Report Autonomously:** Generate business intelligence charts and email them to the owner on the 1st of every month.

## 🏗️ Architecture & Tech Stack
-   **Backend:** Python, FastAPI, PostgreSQL, SQLAlchemy
-   **AI Engine:** LangChain, LangGraph, Groq (Llama-3)
-   **Web Dashboard:** React (Vite), TailwindCSS v4
-   **Automation:** Celery (Background Tasks), Redis (Message Broker)
-   **Deployment:** Docker, Docker Compose

*(For a deep dive into how the microservices connect, see [docs/architecture.md](docs/architecture.md))*

## 📂 Project Structure
-   `/backend`: FastAPI server, AI Agents, Celery Tasks, Database Models.
-   `/web-dashboard`: The Owner's premium React analytics and management portal.
-   `/docs`: Architecture and API documentation.

*(Note: The Flutter mobile apps for Customers and Staff are planned for Phase 2. The backend APIs are fully ready to support them).*

## 🎨 Design System
Our UI is built to feel like a premium, high-end restaurant:
-   **Primary:** Deep Espresso Brown (`#3E2723`)
-   **Secondary:** Warm Amber/Gold (`#FFB300`)
-   **Background:** Soft Cream (`#FFF8E1`)
-   **Study Zone Accent:** Sage Green (`#81C784`)
-   **Typography:** *Playfair Display* (Headings) and *Inter* (Body)
-   **Animations:** Subtle hover lifts, fade-ins on page load, and a "typing" indicator in the AI chat.

## ⚙️ How to Run Locally

### Prerequisites
*   Docker and Docker Compose installed
*   A free [Groq API Key](https://console.groq.com/)
*   A Gmail account with an [App Password](https://myaccount.google.com/apppasswords) (for email reporting)

### Step 1: Clone and Configure
```bash
git clone https://github.com/chemashi11/venuebot-ai.git
cd venuebot-ai