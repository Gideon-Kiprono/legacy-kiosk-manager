# Kiosk Manager

A command-line stock and sales manager for a small Nairobi kiosk, written in Python. It replaces the owner's paper notebook: track stock, record sales, view a sales report, search products, and keep everything saved between days.

Built as a group capstone project using only core Python (Sessions 1-6): variables, conditionals, loops, functions, lists/dicts/tuples/sets, and string/file handling. No classes, no `try/except`, no `csv` module.

## Features

1. **View Stock**: neatly aligned table of every product, price and quantity.
2. **Add/Restock a Product**: add units to an existing product, or create a new one.
3. **Sell a Product**: checks the product exists and that there is enough stock, then reduces stock and records the sale.
4. **View Sales Report**: every sale this session, total revenue, number of unique products sold, and the best seller (by units).
5. **Search Products**: partial, case-insensitive search (`calc` finds `Calculator`).
6. **Exit**: saves all data to files, then quits.

## Requirements

- Python 3.8 or newer
- No third-party packages

## How to run

1. Put `Main.py` in a folder (add `Dictionary.txt` too if you have saved stock).
2. Open a terminal in that folder and run:

   ```bash
   python Main.py
   ```

3. Enter the kiosk name and owner's name, then use the menu.

Always leave through **option 6 (Exit)**. Data is saved only on exit, so closing the terminal window or pressing Ctrl+C loses that session's changes.

## Example session

```
Enter the Kiosk name: navas
Enter the name of the owner: navas herbert
Welcome to Navas's Kiosk Manager, run by Navas Herbert

==============MAIN MENU==============
1. View Stock
2. Add/ Restock a Product
3. Sell a Product
4. View Sales Report
5. Search Products
6. Exit
Enter your choice (Between 1 and 6): 3
Which product to sell: books
Enter the units to be sold: 5
Sale successful.
Product: Books
Quantity: 5
Total: KES 400
```

## Files

| File | Purpose | How it is saved |
|---|---|---|
| `Main.py` | The program | n/a |
| `Dictionary.txt` | Inventory: `name,price,quantity` per line | Overwritten on exit (always the current stock) |
| `sales_log.txt` | Sales history: `name,quantity,total` per line | Appended on exit (history is never erased) |
| `sold_products.txt` | Unique products sold in the last session | Overwritten on exit |

If `Dictionary.txt` does not exist, the program starts with a small default inventory (Pen, Books, Print Papers).

Example `Dictionary.txt`:

```
Pen,65,20
Books,80,105
Print Papers,160,10
```

Product names are stored in Title Case (for example `Print Papers`). If you edit the file by hand, keep that capitalisation, or the product will not be found.

## How the code is organised

| Part | Data structure / skill used |
|---|---|
| Stock | Dictionary of dictionaries: `{"Pen": {"price": 65, "quantity": 20}}` |
| Sales log | List of tuples: `(product, quantity, total)` |
| Unique products sold | Set |
| Input cleaning | `.strip()`, `.title()`, `.lower()`, `.isdigit()` |
| Features | One function each: `view_inventory`, `add_or_restock_product`, `sell_product`, `sales_report`, `search_products` |
| Persistence | `load_inventory`, `save_inventory`, `save_sales_log`, `save_sold_products` |
| Menu | `while True` loop that validates the choice before calling a function |

## Input handling

The program does not crash on bad input. These are all handled with a clear message:

- Letters, empty input or out-of-range numbers at the menu
- Letters, zero or negative numbers for quantity or price
- Selling more units than are in stock (the sale is cancelled and stock is unchanged)
- Selling or searching for a product that does not exist
- Empty product names or search terms

## Known limitations

- Prices and quantities must be whole numbers.
- The sales report covers the current session only; earlier sessions are kept in `sales_log.txt`.
- Data is saved on exit only.

## Possible improvements

- Shopping basket with an itemised receipt
- Change calculator (KES 1000 / 500 / 100 / 50)
- Top 3 best sellers
- `alerts.txt` listing low-stock items
- PIN check at startup

## Team

- Name 1: Gideon Kiprono
- Name 2: Emmanuel Kipngeno
- Name 3: Melvin Kipchumba
- Name 4: Kanan Mutuma

## Article relating to the project
Find the link to the article we wrote describiting out steps below:
[Article](https://dev.to/gideon_kiprono_bfdedde010/kioskmanager-end-to-end-python-project-4n61)
 
 Enjoy! Happy Coding!