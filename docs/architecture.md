# VenueBot AI - System Architecture

VenueBot AI is a microservice-based SaaS application orchestrated via Docker Compose. It consists of five main services that work together to handle bookings, AI reasoning, and background reporting.

## 1. The Backend API (FastAPI)
The core REST API that serves all frontend clients (React Web Dashboard, and future Mobile Apps). It handles:
*   **Authentication:** JWT tokens and bcrypt password hashing.
*   **CRUD Operations:** Managing Resources (Tables, Halls, Study Spots) and Menu Items.
*   **AI Agent Endpoint:** Receives natural language chat from customers and routes it to the LangGraph AI.

## 2. The AI Engine (LangGraph + Groq)
We use LangGraph to build a ReAct (Reasoning + Acting) agent powered by Groq's Llama-3 model.
*   **Tools:** The AI is equipped with custom Python tools (`check_availability`, `create_booking`, `order_food_for_booking`).
*   **Flow:** When a user sends a message, the AI decides which tool to use. The tool queries the PostgreSQL database directly. The AI then formulates a natural language response based on the real data.

## 3. The Database (PostgreSQL)
A relational database storing the core business logic:
*   `users`: Customers, Staff, and Owners.
*   `resources`: Tables, Halls, Study Spots (with capacity and pricing).
*   `menu_items`: Food and drinks (with `prep_time_minutes` used for alarms).
*   `bookings`: The core reservation data.
*   `orders`: Food orders linked to bookings, including the calculated `alarm_time`.

## 4. Background Workers (Celery + Redis)
We use Celery for asynchronous task processing so the main FastAPI server is never blocked by heavy operations.
*   **Redis:** Acts as the message broker (the "mailbox").
*   **Celery Worker:** Executes the task of generating Matplotlib charts and sending emails via SMTP.
*   **Celery Beat:** A scheduler that automatically drops a "Generate Report" task into Redis on the 1st of every month at 2:00 AM.

## 5. Frontend Web Dashboard (React + Tailwind v4)
The Owner Portal. It uses Axios to communicate with the FastAPI backend, stores the JWT in `localStorage`, and displays the live floor plan and generated report charts.

---
### The Automated Staff Alarm Flow
1.  A customer tells the AI: *"I want a Latte at 10:00 AM."*
2.  The AI calls `order_food_for_booking`.
3.  The backend looks up the Latte in the `menu_items` table and sees `prep_time_minutes = 5`.
4.  The backend calculates: `10:00 AM - 5 minutes = 9:55 AM`.
5.  An `Order` row is created in the database with `alarm_time = 9:55 AM` and `status = 'pending'`.
6.  The Staff Mobile App (Phase 2) will poll the `GET /api/v1/staff/alarms` endpoint and ring when the current time passes 9:55 AM.