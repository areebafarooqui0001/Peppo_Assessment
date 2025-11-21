# 🎟️ Events Dashboard — Django RBAC Application  
A role-based access control (RBAC) application built using **Django**, providing three user roles:

- **Admin** – Full CRUD access to Events  
- **Editor** – Can add & edit events  
- **Viewer** – Can only view events in a modern UI (dark theme + search)  

The project includes a **modern UI**, dynamic event filtering (search), data validation (no past events), and custom management commands.

---

## 🚀 Features

### 🔐 Role-Based Access Control (RBAC)
- **Admin**  
  - Add / Edit 
  - Access Django Admin Panel  
  - Full permissions  
- **Editor**  
  - Add / Edit Events    
  - Access Django Admin Panel  
- **Viewer**  
  - Cannot access admin  
  - Can view upcoming events from the homepage  
  - Clean UI with modern dark theme  

### 🎨 Modern UI
- Dark theme with glassmorphism  
- Responsive event cards grid  
- Improved detail page  
- Search bar + instant filtering  
- Custom logout page  
- Homepage = Events viewer page

### 🛠 Backend Features
- Custom Django Command: `initroles`  
- Prevents adding *past* dates via model validators  
- Clean database schema via Django migrations 

---

## 🧩 Tech Stack
- **Python 3**
- **Django 4**
- **SQLite** (default)
- **Bootstrap 5**
- **JavaScript** (client-side filtering)
- **Custom Admin Commands**

---


## ⚙️ Installation & Setup

### 1️⃣ Create & Activate Virtual Environment

```bash

python3 -m venv env
source env/bin/activate      

```

### 2️⃣ Install Dependencies

```bash

pip install -r requirements.txt

```

### 3️⃣ Run Migrations

```bash

python3 manage.py makemigrations
python3 manage.py migrate    

```

### 4️⃣ Create Users & Roles

## 🔧 Create Superuser

```bash

python3 manage.py createsuperuser

```  
## 🔧 Initialize Roles (Admin, Editor, Viewer) + Sample Users

```bash

python3 manage.py initroles

```  
# This generates:

Username	Password	    Role	Access
admin_user	admin123	Admin	Full Admin
editor_user	editor123	Editor	Add/Edit
viewer_user	viewer123	Viewer	View Only

## Note: 
I haven't added login for viewers. They can directly access the home page that is the events page with all the upcoming event's information.

### ▶️ Run the Development Server

```bash

python3 manage.py runserver

```

## Open App:

# Events Homepage (Viewer Page):
  http://127.0.0.1:8000/

# Admin Panel:
  http://127.0.0.1:8000/admin/