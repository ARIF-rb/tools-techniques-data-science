# TTDS Assignment 3 — KNIME Retail Data Pipeline

A no-code data processing and visualization pipeline built in **KNIME Analytics Platform**. Processes a retail dataset across multiple dimensions (categories, customers, orders, geography) and generates analytical charts and summary tables.

## Use Case

Data analysts and students learning no-code/low-code data pipelines. KNIME's visual workflow builder makes it easy to prototype ETL and analysis pipelines without writing code — useful for rapid exploration and reproducible analytics.

## Features

- Loads and joins normalized retail CSV tables (orders, customers, products, geography)
- Cleans and transforms data within the KNIME visual workflow
- Generates analytical graphs: sales by category, region, customer segment, ship mode
- Produces summary tables for reporting
- Fully visual — no coding required to modify or re-run

## Tech Stack

| Layer | Tools |
|---|---|
| Pipeline | KNIME Analytics Platform (free, open-source) |
| Workflow File | `.knwf` (KNIME workflow format) |
| Data | Normalized retail CSV files |

## Prerequisites

- [KNIME Analytics Platform](https://www.knime.com/downloads) (free download — Windows/macOS/Linux)
- No Python or coding required

## Running the Workflow

1. Download and install **KNIME Analytics Platform** from the link above
2. Open KNIME → **File → Import KNIME Workflow**
3. Select `0010-0001.knwf` and import it
4. Verify all CSV data files are in the same folder as the workflow (or update file paths in the CSV Reader nodes)
5. Press the **Execute All** button (▶▶) to run the full pipeline
6. View results in the output nodes (graphs and tables)

## Project Structure

```
├── 0010-0001.knwf                       # KNIME workflow file (open this)
├── Raw Table.xls                        # Original raw data
├── Category.csv / SubCategory.csv       # Product taxonomy
├── Customer.csv / Segment.csv           # Customer data
├── Orders.csv                           # Transaction records
├── City.csv / State.csv / Region.csv / PostalCode.csv  # Geography
├── Product.csv / ShipMode.csv           # Product and shipping data
├── Pipeline including all graphs.png    # Screenshot of pipeline with graph outputs
├── Pipeline including all tables.png    # Screenshot of pipeline with table outputs
├── Assignment 3.docx                    # Assignment specification
├── REPORT.docx                          # Analysis report
└── User Manual.docx                     # KNIME workflow user guide
```

## Output & Results

The pipeline produces:
- **Bar/pie charts**: Sales by product category, customer segment, shipping mode, and region
- **Summary tables**: Aggregated revenue, order counts, and customer metrics
- Screenshots of all outputs are included as `Pipeline including all graphs.png` and `Pipeline including all tables.png`

## Notes

- `.knwf` files are ZIP archives — they can be extracted to view the XML workflow definition
- If CSV file paths break after moving the workflow, right-click the CSV Reader node → **Configure** to update the file path
- The KNIME Community Edition is free and sufficient to run this workflow
