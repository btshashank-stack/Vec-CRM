# Vec CRM (Zoho-like CRM Starter)

This repository now contains a **production-ready starter foundation** for a sales CRM that can grow toward a Zoho-like feature set.

## What is included right now

- FastAPI backend with modular routers.
- JWT-based authentication (register/login).
- Core CRM entities:
  - Accounts
  - Contacts
  - Leads
  - Opportunities
- Dashboard summary endpoint for KPIs.
- SQLite persistence via SQLModel.
- API integration test covering a sales workflow.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open docs: `http://127.0.0.1:8000/docs`

## Example API flow

1. `POST /auth/register`
2. `POST /auth/login`
3. Use `Authorization: Bearer <token>`
4. Create records:
   - `POST /accounts`
   - `POST /contacts`
   - `POST /leads`
   - `POST /opportunities`
5. Review KPIs: `GET /dashboard/summary`

## Zoho-like feature roadmap (all features target)

### Sales core
- [x] Leads, Contacts, Accounts, Opportunities
- [ ] Quotes, Sales Orders, Invoices, Products, Price Books
- [ ] Territory management and assignment rules
- [ ] Forecasting and quota tracking

### Productivity and collaboration
- [ ] Tasks, meetings, calls, notes, timeline feed
- [ ] Team mentions, comments, approvals
- [ ] Email sync (Gmail/Outlook) and templates

### Automation and intelligence
- [ ] Workflow rules, blueprints, macros
- [ ] Lead scoring and assignment automation
- [ ] AI assistant for summaries and next-best actions

### Omnichannel
- [ ] Web forms and landing page capture
- [ ] WhatsApp/SMS/chat integrations
- [ ] Telephony and call logging

### Analytics and reporting
- [ ] Custom dashboards and drill-down reports
- [ ] Funnel, velocity, win/loss analysis
- [ ] Cohort and activity analytics

### Platform and extensibility
- [ ] Role/permission matrix and field-level security
- [ ] Custom modules/fields/layouts
- [ ] REST webhooks + public API keys
- [ ] Audit logs, SSO, data retention/compliance

## Suggested next implementation order

1. Add organizations/teams and role-based access control.
2. Add activities module (tasks/calls/meetings) linked to all records.
3. Add products + quotes + invoicing workflow.
4. Add workflow automation engine and event webhooks.
5. Add React frontend (pipeline board, list views, dashboards).

---

If you want, I can build the next step immediately (RBAC + Activities + UI) in this codebase.
