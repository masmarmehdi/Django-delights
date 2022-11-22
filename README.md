# Django Delights Inventory Tracker


## Overview
For this project, I build an application for a restaurant owner to keep track of how much food he has throughout the day. The owner starts the day with:
- An inventory of different `Ingredient`s, their available quantity, and their prices per unit
- A list of the restaurant's `MenuItem`s, and the price set for each entry
- A list of the ingredients that each menu item requires (`RecipeRequirement`s)
- A log of all `Purchase`s made at the restaurant

the restaurant owner (the user) should be able to enter in new recipes along with their recipe requirements, and how much that menu item costs. They should also be able to add to the inventory a name of an ingredient, its price per unit, and how much of that item is available.

Lastly, they should be able to enter in a customer purchase of a menu item. When a customer purchases an item off the menu, the inventory should be modified to accommodate what happened, as well as recording the time that the purchase was made.

## Project Objectives

- Build an inventory and sales application using Django
- Develop locally on your machine
- Version control your application with Git and host the repository on GitHub
- Use the command line to manage your application locally and test out queries
- Users can log in and log out, and must be logged in to see the views
- Users can create items for the menu
- Users can add ingredients to the restaurant's inventory and update their quantities
- Users can add the different recipe requirements for each menu item
- Users can record purchases of menu items (only the ones that are able to be created with what's in the inventory!)
- Users can view the current inventory, menu items, their ingredients, and a log of all purchases made

## Prerequisites
- HTML
- Python
- Django
- Git
- Command Line
- Bootstrap

## Setup

## Install Django

Run:

```bash
pip install django
```

## Create the skeleton for your Django app

Use the `django-admin` CLI to initialize your project and use the `manage.py` tool inside to create our inventory app.

Run:
```bash
django-admin startproject djangodelights
cd djangodelights
python manage.py startapp inventory
```

## DB models

For this project, we'll have four models. Add definitions for each of these in `models.py`, so we can get started on creating some sample data for our inventory app that we can play around with.

### `Ingredient`
This model represents an ingredient that the restaurant has in its inventory.

An ingredient should have the following fields (at least):
- **`name`**: the name of the ingredient (i.e. `flour`)
- **`quantity`**: the quantity of the ingredient available in the inventory (i.e. `4.5`)
- **`unit`**: the unit used for the ingredient (i.e. `tbsp` or `lbs`)
- **`unit_price`**: the price per unit of the ingredient (i.e. `0.05`, for a `tbsp` of `flour`)

### `MenuItem`
This model represents an item on the restaurant's menu.

A menu item should have the following fields (at least):
- **`title`**: the title of the item on the menu (i.e. `Django Juice`)
- **`price`**: the price of the item (i.e. `3.49` for a glass)

### `RecipeRequirement`
This model represents a single ingredient and how much of it is required for an item off the menu.

A recipe requirement should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`ingredient`**: a reference to a required ingredient for the associated menu item (i.e. a foreign key to the `Ingredient` model)
- **`quantity`**: the amount of the associated ingredient that is required to create the menu item (i.e. `1.5` ounces of `sugar` to create `Django Djaffa Cake`)


### `Purchase`
This model represents a customer purchase of an item off the menu.

A purchase should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`timestamp`**: a timestamp indicating the time that the purchase was recorded (i.e. a `DateTimeField`)

## Populating some sample data

### An example
Here are the ingredients for **Django Djaffa Cake**:

- 100 grams of orange jelly
- 1 large egg
- 1.5 ounces cane sugar
- 1 ounces flour
- 6 ounces milk chocolate

First, we'd create the item on our menu by creating an entry in the menu item's table:

**`MenuItem` Model**

| id  | Title              | Price |
| --- | ------------------ | ----- |
| 1   | Django Djaffa Cake | 8.25  |

In our ingredients table, we would want to ensure that all of those ingredients are present, at least.

**`Ingredient` Model**

| id  | Name           | Quantity | Unit   | Unit Price |
| --- | -------------- | -------- | ------ | ---------- |
| 1   | orange jelly   | 300      | grams  | 0.03       |
| 2   | eggs           | 12       | eggs   | 0.30       |
| 3   | cane sugar     | 50.5     | ounces | 0.65       |
| 4   | flour          | 24.5     | ounces | 0.80       |
| 5   | milk chocolate | 20.8     | ounces | 1.40       |
| 6   | feta cheese    | 3.5      | lbs    | 4.00       |

In our recipe requirements table, we would have have 5 entries:

**`RecipeRequirement` Model**

| id  | Menu Item | Ingredient | Quantity |
| --- | --------- | ---------- | -------- |
| 1   | 1         | 1          | 100.0    |
| 2   | 1         | 2          | 1.0      |
| 3   | 1         | 3          | 1.5      |
| 4   | 1         | 4          | 1.0      |
| 5   | 1         | 5          | 6.0      |

Lastly, when someone wishes to purchase a **Django Djaffa Cake**, we would allow them to select that item off the menu, add a timestamp for when they purchased it, and (after making sure we have enough of the required ingredients in our inventory), we would subtract the required quantities from the inventory and record their purchase.

**`Purchase` Model**

| id  | Menu Item | Timestamp                |
| --- | --------- | ------------------------ |
| 1   | 1         | November 22, 2022, 4:18 p.m. |

### Generating and querying our sample data

After we're done creating our models, we can install the inventory app in the `djangodelights/settings.py`.

Once this is done, generate and run the database migrations migrations for the inventory app.

```bash
python manage.py makemigrations
python manage.py migrate
```

Then, you can use either the Django shell or the Django admin UI to create your sample data as described above. 

Remember, to use the admin site, we'll have to create a superuser first with:

```bash
python manage.py createsuperuser
```
