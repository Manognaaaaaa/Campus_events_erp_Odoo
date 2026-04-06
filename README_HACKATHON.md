# Odoo Hackathon Server - Campus Event ERP

A comprehensive mini-ERP system for managing student clubs, events, budgets, sponsors, and purchase requests built on the Odoo platform.

---

## Table of Contents

1. [Overview](#overview)
2. [What Is This Repository?](#what-is-this-repository)
3. [Setup Workflow Overview](#setup-workflow-overview)
4. [Project Structure](#project-structure)
5. [Installation (Local Odoo)](#installation-local-odoo)
6. [Configuration Setup](#configuration-setup)
7. [VS Code Debugging Setup](#vs-code-debugging-setup)
8. [Running the Server](#running-the-server)
9. [Campus Event ERP Module](#campus-event-erp-module)
10. [Architecture](#architecture)
11. [Development](#development)
12. [Troubleshooting](#troubleshooting)
13. [Contributing](#contributing)
14. [Support](#support)

---

## Overview

**Campus Club Event Manager** is a custom Odoo module designed for **Campus Event Management**. This repository contains the custom module code and configuration files that integrate with an existing Odoo installation to provide a complete mini-ERP system for managing:

- **Student Clubs & Organizations** - Club creation, member management, and tracking
- **Campus Events** - Event planning, scheduling, and attendance management
- **Budget Management** - Track budgets and spending across clubs and events
- **Sponsor Relations** - Manage sponsors and sponsorship commitments
- **Purchase Requests** - Handle procurement requests with approval workflows
- **Reporting & Analytics** - Comprehensive dashboards and reports

### Key Features

✅ **Club Management** - Create and manage student clubs with members and details  
✅ **Event Planning** - Comprehensive event creation, scheduling, and tracking  
✅ **Budget Control** - Track budgets, spending, and financial allocations  
✅ **Sponsor Management** - Manage sponsors and sponsorship opportunities  
✅ **Purchase Requests** - Streamlined procurement process with approvals  
✅ **Reporting** - Built-in dashboards and reporting capabilities  
✅ **Mail Integration** - Email notifications for events and approvals  

### How It Works

This is a **custom Odoo module**, not a standalone application. You need to:

1. Install Odoo on your machine using the official Windows installer
2. Clone or download this repository
3. Copy the `Hackathon/campus_event_erp/` module folder into your Odoo installation
4. Update configuration files to point to your local Odoo folder
5. Restart Odoo and install/upgrade the Campus Event Manager module

**What's Included:**
- Custom Python models for clubs, events, purchase requests, and sponsors
- User interface views and forms for all manageable entities
- Security rules and access control
- Database configuration file (odoo.conf)
- Initial data and document sequences  

---

## What Is This Repository?

This repository is **NOT a standalone Odoo installation**. It contains:

- **Custom Module** (`Hackathon/campus_event_erp/`) - The custom campus event management code
- **Configuration Files** (`odoo.conf`) - Server settings you'll customize for your machine
- **Sample Data Files** - Initial sequences and security rules
- **Documentation** - Setup and usage guides

### Intended Use

You are expected to:
1. Have Odoo pre-installed on your machine (from official installer)
2. Use this repository to **add the custom module** to your Odoo installation
3. Update configuration files to match your local environment
4. Run your Odoo instance with the integrated custom module

**In other words**: This gives you the custom module code + configuration templates, but you need Odoo already installed to use it.

---

## Setup Workflow Overview

### What You Need to Do (5 Simple Steps)

```
1. Install Odoo from Windows installer
            ↓
2. Clone/download this repository
            ↓
3. Copy campus_event_erp module to your Odoo addons folder
            ↓
4. Update odoo.conf paths for your Windows installation
            ↓
5. Restart Odoo and install module from Apps menu
```

**Estimated time:** 15-30 minutes

**Skills needed:** Just copy files and edit a text file in Notepad

### Files You'll Edit

| File | What | Why |
|------|------|-----|
| `odoo.conf` | Paths to your Odoo folders | So Odoo finds your module and files |
| `.vscode/launch.json` | Debug paths | So VS Code debugs the right Odoo |

That's it! Everything else works automatically.

---

## Project Structure

```
server/
├── Hackathon/                          # ⭐ CUSTOM MODULE - Copy this to your Odoo
│   └── campus_event_erp/              # Main Campus Event ERP module
│       ├── __init__.py                # Module initialization
│       ├── __manifest__.py            # Module metadata and dependencies
│       ├── models/                    # Business logic models
│       │   ├── __init__.py
│       │   ├── campus_club.py         # Club management model
│       │   ├── campus_event.py        # Event management model
│       │   ├── campus_purchase_request.py  # Purchase request model
│       │   └── campus_sponsor.py      # Sponsor management model
│       ├── views/                     # User interface definitions
│       │   ├── campus_menus.xml       # Menu structure
│       │   ├── campus_club_views.xml
│       │   ├── campus_event_views.xml
│       │   ├── campus_purchase_request_views.xml
│       │   ├── campus_sponsor_views.xml
│       │   └── campus_reporting_views.xml
│       ├── data/                      # Initial data
│       │   └── ir_sequence.xml        # Document numbering sequences
│       └── security/                  # Access control rules
│           └── ir.model.access.csv    # User group permissions
├── odoo-bin                           # Odoo executable (referenced in config)
├── odoo.conf                          # ⭐ SERVER CONFIG - Customize for your setup
├── setup.py                           # Python package setup
├── requirements.txt                   # Python dependencies
└── README_HACKATHON.md                # This file
```

**Key Takeaways:**
- 📁 Copy `Hackathon/campus_event_erp/` folder to your Odoo's `addons_path` directory
- ⚙️ Update `odoo.conf` paths to match your local Windows Odoo installation
- 🔧 Use `.vscode/launch.json` to debug pointing to your local Odoo setup

---

## System Requirements

### Minimum Hardware

- **Processor**: Intel Core i5 or equivalent (2.0 GHz or higher)
- **RAM**: 4 GB minimum (8 GB recommended)
- **Storage**: 10 GB free disk space (SSD recommended for better performance)
- **Network**: Stable internet connection for package installation

### Software Requirements

#### Required Software

1. **Python 3.10+**
   - Python 3.10, 3.11, 3.12, or 3.13
   - Download from https://www.python.org/downloads/
   - Ensure Python is added to system PATH

2. **PostgreSQL Database**
   - Version 12.0 or higher
   - Download from https://www.postgresql.org/download/
   - Must be running as a service

3. **Node.js & npm** (optional, for advanced development)
   - Version 14.0 or higher
   - For frontend development

#### Optional but Recommended

- **pgAdmin** - PostgreSQL management tool
- **Visual Studio Code** - Code editor with Python extensions
- **Git** - Version control system

### Operating System Support (This Custom Module)

- ✅ **Windows 10/11** (Recommended - uses Windows Odoo installer)
- ⚠️ Linux/macOS (May work, but setup differs from Windows installer)

---

## Installation (Local Odoo)

### ⚠️ Prerequisites: Odoo Must Already Be Installed

**This repository is NOT a complete Odoo installation!** You must first install Odoo from the official Windows installer. This custom module adds functionality to an existing Odoo installation.

### Step 1: Install Odoo (If Not Already Done)

1. Visit **https://www.odoo.com/app/download** (or your region's version)
2. Download the **Windows Installer** for your desired Odoo version
3. Run the installer:
   - Accept license terms
   - Choose installation directory (default: `C:\Program Files\Odoo`)
   - **PostgreSQL will be installed automatically** as part of the Odoo installer
   - Complete the installation
4. Odoo automatically starts and opens at `http://localhost:8069`
5. Create a new database during first-time setup

**After Installation:**
- Odoo is installed in `C:\Program Files\Odoo\server\` (or custom path)
- PostgreSQL runs as a Windows service
- Odoo addons are in `C:\Program Files\Odoo\server\addons\`

### Step 2: Clone or Download This Repository

Download this repository to your development folder:

```bash
# Option 1: Using Git
git clone https://github.com/your-org/campus-event-erp.git
cd campus-event-erp/server

# Option 2: Download as ZIP and extract
# Extract to a folder like C:\Development\Odoo_hackathon\server
```

### Step 3: Copy the Custom Module to Your Odoo Installation

Copy the `Hackathon/campus_event_erp/` folder to your Odoo installation:

```bash
# Source: Your downloaded repository
C:\Development\Odoo_hackathon\server\Hackathon\campus_event_erp\

# Destination: Your Odoo installation addons folder
C:\Program Files\Odoo\server\addons\campus_event_erp\
```

**Alternative:** You can keep it in your repository and update `addons_path` in `odoo.conf` to point here.

### Step 4: Update odoo.conf with Your Local Paths

See [Configuration Setup](#configuration-setup) section below for detailed instructions.

---

## Configuration Setup

### Update odoo.conf for Your Local Environment

The file `odoo.conf` contains configuration that must match your local installation. Edit it with your actual paths:

**File location to edit:**
```
C:\Development\Odoo_hackathon\server\odoo.conf
```

**Key paths to update:**

1. **addons_path** - Where your addons are located:
   ```ini
   # Update paths to match your Odoo installation
   addons_path = C:\Program Files\Odoo\server\addons,C:\Development\Odoo_hackathon\server\Hackathon
   ```
   **Note:** Use the actual path to your Odoo installation's addons folder

2. **data_dir** - Where Odoo stores uploaded files and attachments:
   ```ini
   data_dir = C:\Users\YourUsername\AppData\Local\OpenERP S.A.\Odoo
   ```
   **Note:** This is usually auto-set by Odoo installer, verify the path matches your username

3. **logfile** (optional) - Where server logs are saved:
   ```ini
   logfile = C:\Development\Odoo_hackathon\server\logs\odoo.log
   ```
   **Note:** Create `logs` folder first if it doesn't exist

### Database Settings

**Check your PostgreSQL credentials:**

The default settings created by Odoo installer are typically:
```ini
db_host = localhost
db_port = 5432
db_user = postgres
db_password = (check during Odoo setup)
db_name = admin        # Your database name (may differ)
```

**If you used different credentials during Odoo setup, update them here.**

### Verify Your Updated odoo.conf

After editing, ensure these sections are correct:

```ini
[options]
# Paths must exist and match your system
addons_path = C:\Program Files\Odoo\server\addons,C:\Development\Odoo_hackathon\server\Hackathon
data_dir = C:\Users\YourUsername\AppData\Local\OpenERP S.A.\Odoo

# Database credentials (match your PostgreSQL setup from Odoo installer)
db_host = localhost
db_port = 5432
db_user = postgres
db_password = your_password
db_name = admin

# HTTP settings
http_port = 8069
http_interface = 127.0.0.1
```

---

## VS Code Debugging Setup

### Configure .vscode/launch.json for Your Local Odoo Setup

To debug using VS Code, you need to point the debugger to your local Odoo installation.

**Create or edit `.vscode/launch.json`:**

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Odoo Campus Event ERP",
            "type": "python",
            "request": "launch",
            "program": "C:\\Program Files\\Odoo\\server\\odoo-bin",
            "args": [
                "--config=C:\\Development\\Odoo_hackathon\\server\\odoo.conf",
                "-d", "admin",
                "-u", "campus_event_erp"
            ],
            "console": "integratedTerminal",
            "cwd": "C:\\Program Files\\Odoo\\server",
            "justMyCode": false
        }
    ]
}
```

**Update these paths for your system:**
- `"program"` → Path to your Odoo installation's `odoo-bin` executable
- `"--config=..."` → Path to your `odoo.conf` file
- `"-d", "admin"` → Your database name (if different)
- `"cwd"` → Your Odoo server root directory

**Example for different setup:**
```json
"program": "C:\\Users\\JohnDoe\\AppData\\Local\\Programs\\Odoo\\server\\odoo-bin"
```

### Using the Debugger

1. Open VS Code to this repository folder
2. Go to **Run and Debug** (Ctrl+Shift+D)
3. Select **"Odoo Campus Event ERP"** from the dropdown
4. Click **Run** (green play button)
5. Odoo server starts and debugger is attached
6. Set breakpoints in Python files (click on line number)
7. Interact with the web interface to trigger breakpoints

---

## Running the Server

### Step 1: Restart Odoo to Recognize the Custom Module

After updating `odoo.conf` and copying the `campus_event_erp` module, you need to restart Odoo.

**Via Windows Services:**
1. Open **Services** (services.msc)
2. Find **Odoo** in the list
3. Right-click and select **Restart**

**Or via Command Line:**
```bash
# Open Command Prompt as Administrator, then:
net stop Odoo
net start Odoo
```

**Or via VS Code Debugger:**
1. Go to **Run and Debug** (Ctrl+Shift+D)
2. Select **\"Odoo Campus Event ERP\"**
3. Click **Run** to start the debugger

### Step 2: Install/Upgrade the Campus Event ERP Module

Once Odoo is running, install or upgrade the custom module through the web interface:

1. Navigate to **http://localhost:8069** in your browser
2. Login with **admin** / **admin** (or your credentials)
3. Go to **Apps** menu or search bar
4. Search for **\"Campus Club Event Manager\"** or **\"campus_event_erp\"**
5. Click on the module card
6. Click **Install** (if not installed) or **Upgrade** (if updating existing version)
7. Wait for the installation to complete
8. The module is now active and menus appear in the main menu

**You should now see a new \"Campus Management\" menu** with options for Clubs, Events, Purchase Requests, Sponsors, and Reports.

### Running via Command Line

If you prefer command-line startup with automatic module upgrade:

```bash
# From your Odoo installation directory (e.g., C:\\Program Files\\Odoo\\server)
# Use the odoo.conf file from this repository:

cd \"C:\\Program Files\\Odoo\\server\"

# Start server and upgrade campus_event_erp module
python odoo-bin --config=C:\\Development\\Odoo_hackathon\\server\\odoo.conf -d admin -u campus_event_erp

# Start with debug logging
python odoo-bin --config=C:\\Development\\Odoo_hackathon\\server\\odoo.conf --log-level=debug

# Run module tests
python odoo-bin --config=C:\\Development\\Odoo_hackathon\\server\\odoo.conf --test-enable -u campus_event_erp
```

### VS Code Debugging

Use the configured launch configuration for easy debugging:

1. Go to **Run and Debug** (Ctrl+Shift+D)
2. Select **\"Odoo Campus Event ERP\"** from dropdown
3. Click **Run** (green play button)
4. Set breakpoints in Python files and test through web interface
5. Debugger will pause at breakpoints

### Accessing the Web Interface

Once the server is running:

1. Open your web browser
2. Navigate to: **http://localhost:8069**
3. Login with admin credentials
4. Select your database
5. Campus Management menu should be visible

---

## Campus Event ERP Module

### Module Information

| Property | Value |
|----------|-------|
| **Name** | Campus Club Event Manager |
| **Version** | 1.0 |
| **Category** | Education |
| **Author** | Campus ERP Team |
| **Status** | Installable/Active |

### Core Models

#### 1. **Campus Club** (`campus_club.py`)
Manages student organizations and clubs.

**Key Features:**
- Club name and description
- Member management
- Contact information
- Budget allocation
- Status tracking

**Typical Fields:**
```python
- name: Char (Club name)
- description: Text (Club details)
- contact_person: Many2One (Contact)
- budget_allocation: Float (Annual budget)
- active: Boolean (Is active)
```

#### 2. **Campus Event** (`campus_event.py`)
Handles event planning and management.

**Key Features:**
- Event scheduling
- Attendance tracking
- Budget management
- Category classification
- Status workflow

**Typical Fields:**
```python
- name: Char (Event name)
- date_start: DateTime (Start date/time)
- date_end: DateTime (End date/time)
- location: Char (Event location)
- club_id: Many2One (Organizing club)
- budget: Float (Event budget)
- status: Selection (planned/confirmed/completed/cancelled)
```

#### 3. **Campus Purchase Request** (`campus_purchase_request.py`)
Streamlines procurement process.

**Key Features:**
- Item request submission
- Approval workflow
- Cost tracking
- Quantity management
- Status tracking

**Typical Fields:**
```python
- name: Char (Request reference)
- item_description: Text (What to purchase)
- quantity: Integer (Number of items)
- unit_price: Float (Price per item)
- total_cost: Float (Computed total)
- status: Selection (draft/submitted/approved/rejected/completed)
- approver_id: Many2One (Approval manager)
```

#### 4. **Campus Sponsor** (`campus_sponsor.py`)
Manages sponsorship relationships.

**Key Features:**
- Sponsor information
- Sponsorship tracking
- Amount management
- Contact details
- Event association

**Typical Fields:**
```python
- name: Char (Sponsor name)
- email: Char (Contact email)
- phone: Char (Phone number)
- sponsorship_amount: Float (Committed amount)
- company_name: Char (Company)
- events_sponsored: Many2Many (Events)
```

### Menu Structure

The module provides the following menu hierarchy:

```
📊 Campus Management
├── Clubs
│   ├── Club List
│   ├── Create Club
│   └── Club Reports
├── Events
│   ├── Event List
│   ├── Create Event
│   ├── Event Calendar
│   └── Event Reports
├── Purchase Requests
│   ├── Request List
│   ├── Create Request
│   ├── Pending Approvals
│   └── Purchase Reports
├── Sponsors
│   ├── Sponsor List
│   ├── Add Sponsor
│   ├── Sponsorship Tracking
│   └── Sponsor Reports
└── Reports
    ├── Event Summary
    ├── Budget Analysis
    ├── Spending Report
    └── Sponsor Summary
```

### Security & Access Control

Access is managed through `security/ir.model.access.csv`:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
campus_club_user,Campus Club User,model_campus_club,base.group_user,1,1,1,1
campus_event_user,Campus Event User,model_campus_event,base.group_user,1,1,1,1
campus_pr_user,Purchase Request User,model_campus_purchase_request,base.group_user,1,1,1,1
campus_sponsor_user,Campus Sponsor User,model_campus_sponsor,base.group_user,1,1,1,1
```

---

## Configuration

### Enabling/Disabling the Module

**To Install Campus Event ERP:**
```bash
python odoo-bin --config=odoo.conf -d admin -i campus_event_erp
```

**To Update the Module:**
```bash
python odoo-bin --config=odoo.conf -d admin -u campus_event_erp
```

**To Uninstall the Module:**
Access Admin Panel → Apps → Search "Campus Club Event Manager" → Click Uninstall

### Setting Up Initial Data

The module includes initial data configuration in `data/ir_sequence.xml`:

```xml
<!-- Document numbering sequences -->
<record id="seq_campus_club" model="ir.sequence">
    <field name="name">Campus Club</field>
    <field name="code">campus.club</field>
    <field name="prefix">CLUB/</field>
    <field name="number_next">1</field>
</record>
```

This automatically generates reference numbers in format: **CLUB/001**, **EVENT/001**, **PR/001**, etc.

### Email Configuration

Configure email for notifications:

```ini
# In odoo.conf
smtp_server = localhost        # or your SMTP server
smtp_port = 25                 # Standard: 25, Secure: 465, TLS: 587
smtp_user = your_email@example.com
smtp_password = your_password
smtp_ssl = False               # Set to True for secure connections
email_from = noreply@campus.edu
```

---

## Architecture

### Technology Stack

```
┌─────────────────────────────────────────────────────┐
│         Web Browser Interface (http://localhost:8069)  │
│                   (JavaScript/HTML/CSS)             │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────▼─────────────┐
        │  Odoo Web Server       │
        │  (Python/Werkzeug)     │
        └──────────┬─────────────┘
                   │
        ┌──────────▼─────────────────────────┐
        │  Odoo Framework (odoo/core)         │
        │ ├── ORM (Models)                   │
        │ ├── Fields                         │
        │ ├── HTTP Routing                   │
        │ └── Business Logic                 │
        └──────────┬──────────────────────────┘
                   │
        ┌──────────▼─────────────────────────┐
        │  Custom Modules (Hackathon/)        │
        │ ├── campus_event_erp               │
        │ │   ├── models/                    │
        │ │   ├── views/                     │
        │ │   ├── data/                      │
        │ │   └── security/                  │
        └──────────┬──────────────────────────┘
                   │
        ┌──────────▼─────────────────────────┐
        │    PostgreSQL Database              │
        │    (admin database)                 │
        └─────────────────────────────────────┘
```

### Request Flow

1. **User Request** → Web Browser sends HTTP request
2. **Routing** → Odoo routes request to appropriate controller
3. **Authentication** → User is validated against session
4. **Authorization** → Access rules checked via `ir.model.access`
5. **Model Logic** → Business logic in Python models
6. **Database Query** → ORM generates SQL and queries PostgreSQL
7. **Response** → Data formatted and sent back to browser
8. **Rendering** → Web interface displays result

### Module Loading Sequence

1. Odoo scans `addons_path` directories
2. Reads `__manifest__.py` from each module
3. Checks dependencies
4. Loads models from `models/`
5. Executes data files (`data/`)
6. Registers views (`views/`)
7. Applies security rules (`security/`)
8. Module becomes available in web interface

---

## Development

### Setting Up Development Environment

#### IDE Setup (VS Code Recommended)

1. **Install Extensions**
   - Python (Microsoft)
   - Pylance (Microsoft)
   - PostgreSQL (Chris Kolkman)
   - XML (Red Hat)

2. **Configure Python Path**
   - Create `.vscode/settings.json`:
   ```json
   {
       "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
       "python.linting.enabled": true,
       "python.linting.pylintEnabled": true,
       "[python]": {
           "editor.formatOnSave": true,
           "editor.defaultFormatter": "ms-python.python"
       }
   }
   ```

3. **Configure Debug Launch**
   - Create `.vscode/launch.json`:
   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Odoo Server",
               "type": "python",
               "request": "launch",
               "program": "${workspaceFolder}/odoo-bin",
               "args": [
                   "--config=odoo.conf",
                   "-d", "admin",
                   "-u", "campus_event_erp"
               ],
               "console": "integratedTerminal",
               "cwd": "${workspaceFolder}"
           }
       ]
   }
   ```

### Creating a New Model

**Example: Create a new model in `models/campus_venue.py`:**

```python
from odoo import models, fields, api

class CampusVenue(models.Model):
    _name = 'campus.venue'
    _description = 'Campus Event Venue'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Venue Name', required=True, tracking=True)
    capacity = fields.Integer('Seating Capacity')
    location = fields.Char('Address')
    available_date_ids = fields.One2many('campus.venue.availability', 'venue_id', 'Available Dates')
    
    @api.constrains('capacity')
    def _check_capacity(self):
        for record in self:
            if record.capacity < 1:
                raise models.ValidationError('Capacity must be at least 1')
```

### Creating Views

**Add to `views/campus_venue_views.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <!-- Tree View -->
    <record id="campus_venue_tree" model="ir.ui.view">
        <field name="name">Campus Venue List</field>
        <field name="model">campus.venue</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="capacity"/>
                <field name="location"/>
            </tree>
        </field>
    </record>

    <!-- Form View -->
    <record id="campus_venue_form" model="ir.ui.view">
        <field name="name">Campus Venue Form</field>
        <field name="model">campus.venue</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group col="4">
                        <field name="name" colspan="2"/>
                        <field name="capacity"/>
                        <field name="location" colspan="2"/>
                    </group>
                    <notebook>
                        <page string="Availability">
                            <field name="available_date_ids"/>
                        </page>
                    </notebook>
                </sheet>
                <div class="oe_chatter">
                    <field name="message_ids" widget="mail_thread"/>
                </div>
            </form>
        </field>
    </record>

    <!-- Action & Menu -->
    <record id="campus_venue_action" model="ir.actions.act_window">
        <field name="name">Venues</field>
        <field name="res_model">campus.venue</field>
        <field name="view_mode">tree,form</field>
    </record>

    <menuitem id="campus_venue_menu" parent="campus_menu_root"
        action="campus_venue_action" sequence="5"/>
</odoo>
```

### Running Tests

```bash
# Run all module tests
python odoo-bin --config=odoo.conf -d admin -i campus_event_erp --test-enable

# Run specific test
python odoo-bin --config=odoo.conf -d admin --test-tags=campus_event_erp.test_campus_club

# View test results in console output
```

### Code Style Guidelines

Follow Odoo conventions:

- **Naming**: Use snake_case for variables/functions, CamelCase for classes
- **Imports**: Group standard, third-party, and local imports
- **Docstrings**: Document all models, methods, and functions
- **Formatting**: Max line length 120 characters
- **Type Hints**: Use for clarity (optional in Odoo)

**Example:**

```python
# Good
def _calculate_event_revenue(self, event):
    """
    Calculate total revenue from sponsors for an event.
    
    Args:
        event: campus.event record
        
    Returns:
        float: Total sponsorship amount
    """
    return sum(event.sponsor_ids.mapped('sponsorship_amount'))

# Bad
def calc_rev(e):
    return sum([s.amount for s in e.spons])
```

---

## Troubleshooting

### Common Setup Issues

#### Issue 1: "Module 'campus_event_erp' not found in Apps"

**Causes:** Path misconfiguration or module not copied

**Solution:**
1. Verify `addons_path` in `odoo.conf` is correct:
   ```ini
   addons_path = C:\Program Files\Odoo\server\addons,C:\Development\Odoo_hackathon\server\Hackathon
   ```
2. Verify folder structure: `Hackathon/campus_event_erp/__manifest__.py` exists
3. Restart Odoo service:
   ```bash
   net stop Odoo
   net start Odoo
   ```
4. In Apps menu, click refresh icon or search directly for "Campus"

#### Issue 2: "Error connecting to database"

**Causes:** Wrong database credentials in `odoo.conf`

**Solution:**
1. Check PostgreSQL is running:
   ```bash
   sc query postgresql-x64-14
   ```
2. Verify credentials in `odoo.conf` match what you set during Odoo installer
3. Test connection using pgAdmin or psql:
   ```bash
   psql -h localhost -U postgres -d admin
   ```
4. Update `db_user`, `db_password`, `db_name` in `odoo.conf` if needed

#### Issue 3: "Path does not exist" error

**Causes:** Incorrect file paths in `odoo.conf`

**Solution:**
1. Check all paths use correct backslashes: `C:\\Users\\Username\\...`
2. Verify Windows paths exist in File Explorer
3. Use absolute paths, not relative paths
4. Example correct path: `C:\\Users\\YourName\\AppData\\Local\\OpenERP S.A.\\Odoo`
5. Restart Odoo after correcting paths

#### Issue 4: "Permission Denied" when accessing files

**Causes:** VS Code or Odoo doesn't have file access

**Solution:**
1. Run VS Code as Administrator
2. Ensure `data_dir` path exists and is writable
3. Create missing folders using: `mkdir path\to\folder`
4. Check Windows file permissions (Right-click → Properties → Security)

#### Issue 5: Module shows errors in console

**Solution:**
1. Check Python syntax:
   ```bash
   python -m py_compile Hackathon/campus_event_erp/models/campus_club.py
   ```
2. View full logs: Check the `logfile` path set in `odoo.conf`
3. Enable debug logging in `odoo.conf`:
   ```ini
   log_level = debug
   ```
4. Look for error messages in the Python files listed in traceback

### PostgreSQL Troubleshooting

#### Check PostgreSQL is running

```bash
# Windows: Check service status
sc query postgresql-x64-14

# Should show: STATE        : 4  RUNNING
```

#### Restart PostgreSQL Service

```bash
# Windows
net stop postgresql-x64-14
net start postgresql-x64-14
```

#### Access PostgreSQL directly

```bash
# Using pgAdmin GUI from Windows Start Menu
# Or using psql command line (if in PATH):
psql -U postgres -d admin

# Common psql commands:
\l          # List databases
\du         # List users
\c admin    # Connect to admin database
\q          # Exit psql
```

#### Need to Reset Database

```bash
# Connect to PostgreSQL as admin
psql -U postgres

# Inside psql, run:
DROP DATABASE admin;
CREATE DATABASE admin;

\q

# Restart Odoo - fresh tables will be created
net stop Odoo
net start Odoo
```

### Odoo Service Issues

#### Odoo Service Won't Start

**Solution:**
1. Check logs: Open Odoo log file from path in `odoo.conf`
2. Verify all paths in `odoo.conf` exist and are valid
3. Check PostreSQL is running first
4. Try starting from command line to see errors:
   ```bash
   cd "C:\Program Files\Odoo\server"
   python odoo-bin --config=C:\Development\Odoo_hackathon\server\odoo.conf
   ```

#### Odoo Port Already in Use (8069)

**Solution:**
1. Check if another Odoo instance is running
2. Change port in `odoo.conf`:
   ```ini
   http_port = 8070
   ```
3. Access at `http://localhost:8070` instead
4. Restart service: `net stop Odoo && net start Odoo`

### Debug: View Odoo Logs

**On Windows, find and open the log file:**

1. Path is set in `odoo.conf` as `logfile`
2. Or default: `C:\Program Files\Odoo\server\odoo.log`
3. Open with: Notepad, VS Code, or PowerShell
4. View recent errors:
   ```bash
   Get-Content C:\path\to\odoo.log -Tail 50  # Last 50 lines
   ```

### Performance Issues

If Odoo is running slowly:

1. **Increase memory in `odoo.conf`:**
   ```ini
   limit_memory_soft = 4294967296  # 4GB
   ```

2. **Check Windows Task Manager:**
   - Press Ctrl+Shift+Esc
   - Look for Odoo/python process
   - If using >90% RAM, increase memory allocation above or close other apps

3. **Move `data_dir` to fast drive:**
   - Don't use network drives
   - Use local SSD if possible

4. **Check PostgreSQL Performance:**
   ```bash
   # pgAdmin can show database stats
   #  Right-click database → Statistics
   ```

---

## Contributing

### Development Workflow

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/add-venue-management
   ```

2. **Make Changes**
   - Edit models, views, or add new modules
   - Test thoroughly in development environment
   - Update documentation

3. **Test Before Committing**
   ```bash
   # Run full test suite
   python odoo-bin --config=odoo.conf -d admin --test-enable

   # Check for Python syntax errors
   python -m py_compile path/to/file.py
   ```

4. **Commit & Push**
   ```bash
   git add .
   git commit -m "Add venue management feature"
   git push origin feature/add-venue-management
   ```

5. **Create Pull Request**
   - Describe changes clearly
   - Reference any related issues
   - Wait for code review

### Code Review Checklist

- ✅ Code follows Odoo conventions
- ✅ All tests pass
- ✅ No console errors or warnings
- ✅ Database migrations handled properly
- ✅ Security rules properly configured
- ✅ Documentation updated
- ✅ Performance impact considered

### Reporting Bugs

When reporting issues, include:

1. **Environment Info**
   - OS and Python version
   - Odoo version
   - Browser and version

2. **Steps to Reproduce**
   - Exact steps that cause the issue
   - Expected vs actual behavior

3. **Error Details**
   - Full error message/traceback
   - Server logs if applicable

4. **Screenshots**
   - Visual representation of the issue

---

## Support

### Documentation Resources

- **Official Odoo Documentation**: https://www.odoo.com/documentation
- **Odoo API Reference**: https://www.odoo.com/documentation/17.0/developer.html
- **PostgreSQL Docs**: https://www.postgresql.org/docs/

### Getting Help

1. **Check Logs First**: Review `odoo.log` and server console
2. **Search Docs**: Look for similar issues in documentation
3. **Community Forum**: Post questions on Odoo community forum
4. **Contact Team**: Reach out to the Campus ERP development team

### Useful Commands Reference

```bash
# Update campus_event_erp module via command line
C:\Program Files\Odoo\server\odoo-bin --config=C:\Development\Odoo_hackathon\server\odoo.conf -d admin -u campus_event_erp

# Run tests via command line
C:\Program Files\Odoo\server\odoo-bin --config=C:\Development\Odoo_hackathon\server\odoo.conf --test-enable -u campus_event_erp

# Start server with debug logging
C:\Program Files\Odoo\server\odoo-bin --config=C:\Development\Odoo_hackathon\server\odoo.conf --log-level=debug

# Restart Odoo service (Windows)
net stop Odoo
net start Odoo

# Check Odoo service status (Windows)
sc query Odoo
```

---

## Quick Start Checklist

### Prerequisites
- [ ] Windows 10 or 11
- [ ] Odoo installed from Windows installer (https://www.odoo.com/app/download)
- [ ] PostgreSQL running (installed as part of Odoo)

### Setup
- [ ] Repository cloned or downloaded
- [ ] `Hackathon/campus_event_erp/` copied to Odoo addons folder
- [ ] `odoo.conf` updated with correct paths:
  - [ ] `addons_path` includes your custom modules directory
  - [ ] `data_dir` points to correct user profile path
  - [ ] `logfile` path is correct (if using)
- [ ] `.vscode/launch.json` updated with your local paths
- [ ] Database credentials verified in `odoo.conf`

### Testing
- [ ] Odoo restarted or service restarted
- [ ] Web interface accessible at http://localhost:8069
- [ ] Logged in with admin credentials
- [ ] Campus Event ERP module installed from Apps menu
- [ ] Campus Management menu visible in main navigation
- [ ] Created first club/event to test functionality

---

## License

This project extends the Odoo platform. Refer to:
- [LICENSE](LICENSE) - Main project license
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

## Version Information

- **Odoo Version**: 17.0+
- **Campus Event ERP**: 1.0
- **Python**: 3.10, 3.11, 3.12, 3.13
- **Last Updated**: April 6, 2026

---

**For questions or issues, please contact the Campus ERP development team.**

Happy coding! 🚀
