# Campus Event ERP – Odoo Module (BITS Pilani Hackathon)

A custom Odoo mini‑ERP to manage student clubs, campus events, budgets, sponsors, and purchase requests in one place.

---

## 1. What this project is

- A **custom Odoo module** named `campus_event_erp`, not a standalone app  
- Built for **Windows Odoo installation** (tested with Odoo 17)  
- Focused on BITS‑style campus fests (Oasis), club events, and approvals

Core capabilities:

- Clubs and members (with faculty advisor, budgets)
- Events with dates, venues, media, and attachments
- Budget lines per event
- Purchase requests with approval state
- Sponsors and sponsorship amounts
- Computed financials (planned budget, actual spend, sponsorship, net cost)

---

## 2. Quick Setup (Windows, local Odoo)

### Prerequisites

- Windows 10/11  
- Odoo installed from official Windows installer  
- PostgreSQL set up by the Odoo installer  
- Admin database created (e.g. `admin`)

### Install steps

1. **Clone / Download**

   - Clone this repo or download ZIP and extract, e.g. to  
     `C:\Development\Odoo_hackathon\`

2. **Copy module**

   - Copy:

     `C:\Development\Odoo_hackathon\server\Hackathon\campus_event_erp\`

   - Into your Odoo addons folder, for example:

     `C:\Program Files\Odoo\server\addons\campus_event_erp\`

   - Or keep it in place and include the `Hackathon` path in `addons_path`.

3. **Configure `odoo.conf`**

   Edit the config used by your Odoo server and ensure:

   ```ini
   [options]
   addons_path = C:\Program Files\Odoo\server\addons,C:\Development\Odoo_hackathon\server\Hackathon

   db_host = localhost
   db_port = 5432
   db_user = postgres
   db_password = YOUR_POSTGRES_PASSWORD
   db_name = admin

   data_dir = C:\Users\YOUR_USERNAME\AppData\Local\OpenERP S.A.\Odoo
   http_port = 8069
   logfile = C:\Development\Odoo_hackathon\server\logs\odoo.log
   ```

   Adjust paths, username, and database name to match your machine.

4. **Restart Odoo**

   From an elevated Command Prompt:

   ```bat
   net stop Odoo
   net start Odoo
   ```

5. **Install the module**

   - Open `http://localhost:8069`  
   - Log in as admin  
   - Go to **Apps** → search for **Campus Club Event Manager** or `campus_event_erp`  
   - Click **Install**

   After install you should see a **Campus Management** menu with Clubs, Events, Purchase Requests, Sponsors, Reporting.

---

## 3. Main functional modules

### 3.1 Clubs & Members

**Model files**

- `models/campus_club.py`  
- `models/campus_club_member.py` (inside same file)

**CampusClub (`campus.club`)**

- `name`: Club name (required)  
- `code`: Short unique code (e.g. RAGA, DANC)  
- `faculty_advisor_id`: `res.partner` (faculty contact)  
- `currency_id`: `res.currency` (defaults to company currency)  
- `total_budget`: Monetary, overall club budget  
- `event_ids`: One2many to `campus.event`  
- `member_ids`: One2many to `campus.club.member`  
- `active`: Boolean flag  
- SQL constraint: club code must be unique

**Actions**

- `action_open_events()`: Open all events for this club (tree/form)  
- `action_open_members()`: Open all members for this club (tree/form)

**CampusClubMember (`campus.club.member`)**

- `club_id`: Many2one to `campus.club` (required)  
- `partner_id`: Many2one to `res.partner` (student contact)  
- `role`: Selection – president, treasurer, core, volunteer  
- `join_date`: Join date (defaults to today)  
- `is_core`: Boolean, computed: true for president, treasurer, core

---

### 3.2 Events & Budgets

**Model file**

- `models/campus_event.py`

**CampusEventBudgetLine (`campus.event.budget.line`)**

- `name`: Line label (e.g. “Stage & Lights”)  
- `event_id`: Many2one to `campus.event`  
- `category`: Selection – decor, catering, printing, tech, prizes, other  
- `amount`: Monetary  
- `currency_id`: `res.currency` (defaults to company)

**CampusEvent (`campus.event`)**

Basic fields:

- `name`: Event name (required)  
- `club_id`: Many2one to `campus.club` (required)  
- `date`: Event start date (required)  
- `end_date`: Event end date (optional)  
- `venue`: Text venue description  
- `state`: Selection – idea, to_approve, approved, completed, cancelled  
- `planned_attendees`, `actual_attendees`: Integers

Media and attachments:

- `event_logo`: Image field (poster/banner)  
- `attachment_ids`: Many2many `ir.attachment` for extra files

Relations:

- `budget_line_ids`: One2many to `campus.event.budget.line`  
- `purchase_request_ids`: One2many to `campus.purchase.request`  
- `sponsor_ids`: One2many to `campus.sponsor`  
- `currency_id`: `res.currency`

Computed monetary fields:

- `planned_budget_total`: Sum of `budget_line_ids.amount`  
- `actual_spent_total`: Sum of `purchase_request_ids.amount` for states approved/paid  
- `sponsorship_total`: Sum of `sponsor_ids.amount`  
- `net_cost`: `actual_spent_total - sponsorship_total`

State transition helpers:

- `action_to_approve()` → sets state `to_approve`  
- `action_approve()` → sets state `approved`  
- `action_complete()` → sets state `completed`  
- `action_cancel()` → sets state `cancelled`

> Venue double‑booking constraint is present in comments and can be re‑enabled later; it is disabled in the hackathon build for stability.

---

### 3.3 Purchase Requests

**Model file**

- `models/campus_purchase_request.py`

Key ideas:

- `name`: Request reference / sequence  
- `event_id`: Many2one to `campus.event`  
- `vendor_id`: Many2one to `res.partner` (supplier)  
- `category`: Linked to spending type  
- `amount`: Monetary  
- `currency_id`: `res.currency`  
- `state`: workflow (draft → submitted → approved → paid / cancelled)

Approved/paid requests automatically roll into `actual_spent_total` on the event.

---

### 3.4 Sponsors

**Model file**

- `models/campus_sponsor.py`

Key ideas:

- `name`: Internal sponsorship label  
- `event_id`: Many2one to `campus.event`  
- `partner_id`: Many2one to `res.partner` (sponsor)  
- `amount`: Monetary contribution  
- `benefits`: Text explaining sponsor benefits

Sponsor amounts roll into `sponsorship_total` on the event.

---

## 4. Views & Menus

**View files**

- `views/campus_menus.xml` – main menu and actions  
- `views/campus_club_views.xml` – clubs & members views  
- `views/campus_event_views.xml` – event list/form/kanban, image & attachments  
- `views/campus_purchase_request_views.xml` – PR views  
- `views/campus_sponsor_views.xml` – sponsor views  
- `views/campus_reporting_views.xml` – basic reporting

Top‑level menu (example):

- **Campus Management**
  - Clubs
  - Members
  - Events
  - Purchase Requests
  - Sponsors
  - Reporting

---

## 5. Security

**File**

- `security/ir.model.access.csv`

Grants basic user access to:

- `campus.club`  
- `campus.club.member`  
- `campus.event`  
- `campus.purchase.request`  
- `campus.sponsor`

A `res.groups` entry like **Campus Event Manager** (in `campus_menus.xml`) can be assigned to power users inside Odoo for tighter control.

---

## 6. VS Code Run / Debug (optional)

If you run Odoo from VS Code instead of the Windows service:

1. Add a launch config pointing to your `odoo-bin` and `odoo.conf`.
2. In the Run and Debug panel:
   - Select **“Odoo Campus Event ERP”** (or your config name).  
   - Click **Run Without Debugging** (Ctrl+F5) to start the Odoo server quickly without attaching the debugger.

Then open `http://localhost:8069` in the browser.

---

## 7. Typical demo flow

To show everything end‑to‑end:

1. Create **Contacts** for faculty, students, vendors, sponsors.  
2. Create **Clubs** with faculty advisors and budgets.  
3. Add **Members** (president, treasurer, core, volunteers).  
4. Create a realistic fest event (dates, venue, logo, attachments).  
5. Add **Budget Lines** → watch Planned Budget update.  
6. Create **Purchase Requests** and approve/pay them → show Actual Spent.  
7. Add **Sponsors** → show Sponsorship and Net Cost.  
8. Use list, form, and kanban views plus Reporting to summarize.

---

## 8. Troubleshooting (short)

- **Module not in Apps** → verify `addons_path`, restart Odoo service.  
- **DB errors** → check `db_user`, `db_password`, `db_name` in `odoo.conf`.  
- **Port conflict** → change `http_port` and use that in the browser.  
- **Weird “search must be callable / method name” errors** → never set `search=True` on fields; either remove `search` or point it to a real search method.

---
