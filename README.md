# Inventory Trail

Inventory Trail is a simple web application used for keeping an audit trail for any equipment you may have. The app has these main features:

- QR code identification system: Generate QR codes for each item or item group you want to track.
- Checkout: Scan an item's associated QR code, leave your name, and check out the item.
- Check in (with audit trail): Scan an item's associated QR code to see who checked it in last. Leave your name and check in the item. 

# Design philosophy

- As frictionless as possible: We understand there's nothing easier than just telling someone before you grab the item you want and hoping things work out. Any system that aims to overthrow a simple word-of-mouth system must be easy and have as few steps as possible.
- Mobile-first: If it's technology that needs to be as quick as possible, then pulling out your phone and scanning a QR code is as straightforward as it can get.
- Track the borrower, not the item: This application is not an inventory app; it's an inventory _trail_ app. When something goes missing--and something always goes missing--what's important is quickly figuring out who checked it out last.

# Technical notes

Stack: 
- Python 3.10.12
- Django 4.0.6
- Bootstrap 5.3

# Dev env setup

1. Install the `pip` Python package manager if you haven't yet.
1. (Recommendation) Install the `pyenv` Python version manager to manage your
   Python versions.
2. Install `pipenv` to manage Python virtual environments: `pip install pipenv`
3. Clone the repo
4. Install Python packages in the src folder: `pipenv install`
5. Run database migrations: `python manage.py migrate`
5. Create super user to access admin page: `python manage.py createsuperuser`




