# TTDS Assignment 3 — KNIME Data Pipeline

A data processing and visualization pipeline built in **KNIME Analytics Platform**. Processes a retail dataset across multiple dimensions (categories, customers, orders, geography) and generates analytical graphs and tables.

## Tech Stack

- **KNIME** — visual data workflow (.knwf)
- **Data** — retail dataset (CSV files)

## Project Structure

```
├── 0010-0001.knwf              # KNIME workflow file
├── Raw Table.xls               # Raw input data
├── Category.csv                # Product categories
├── City.csv
├── Customer.csv
├── Orders.csv
├── PostalCode.csv
├── Product.csv
├── Region.csv
├── Segment.csv
├── ShipMode.csv
├── State.csv
├── SubCategory.csv
├── Pipeline including all graphs.png   # Pipeline visualization
├── Pipeline including all tables.png
├── Assignment 3.docx           # Assignment specification
├── REPORT.docx                 # Analysis report
└── User Manual.docx            # KNIME workflow user guide
```

## Running the Workflow

1. Install [KNIME Analytics Platform](https://www.knime.com/downloads)
2. Import `0010-0001.knwf` via **File → Import KNIME Workflow**
3. Ensure CSV files are in the expected directory
4. Execute the workflow to regenerate all graphs and table outputs
