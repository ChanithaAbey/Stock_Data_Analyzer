
# Stock Data Analyzer

This script is a Python-based tool that fetches stock data from Yahoo Finance, analyzes price trends, calculates simple moving averages (SMAS), and visualizes the results in a graph.

---

## Features

- Fetches **stock data** from Yahoo Finance using `yfinance`.
- Calculates **Simple Moving Averages (SMA 50 & SMA 200)**.
- Displays:
  - Highest and lowest stock prices in the period.
  - Latest available stock data date.
- Saves stock data to **CSV files**.
- Plots price trends using **Matplotlib**.

---

## How to Use

1. Run the program.
2. Enter a valid stock ticker symbol (e.g., `AAPL`, `TSLA`, `MSFT`) or type `STOP` to exit.
3. View:
   - Highest & lowest price details.
   - A chart of historical prices with SMA lines.
4. Data is saved automatically as `TICKER_data.csv`.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ChanithaAbey/Stock_Data_Analyzer
   cd Stock-Data-Analyzer
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python stock_data_analyzer.py
   ```

---

## Dependencies

- `yfinance`
- `pandas`
- `matplotlib`

Install with:
```bash
pip install yfinance pandas matplotlib
```

---

## Example

```bash
Enter a stock ticker symbol or type STOP to exit: NKE
Highest price details:
Date            2024-06-24
Open                 95.89
High                 96.62
Low                  95.28
Close                95.76
Volume             9466900
Dividends              0.0
Stock Splits           0.0
SMA_50                 NaN
SMA_200                NaN
Name: 40, dtype: object

Lowest price details:
Date            2025-04-10
Open                 57.23
High                 57.25
Low                  52.28
Close                 54.4
Volume            53919800
Dividends              0.0
Stock Splits           0.0
SMA_50             71.2494
SMA_200            75.7952
Name: 240, dtype: object

Stock data for NKE:
         Date   Open   High    Low  Close   Volume  Dividends  Stock Splits  SMA_50  SMA_200
0  2024-04-25  92.28  93.05  90.75  92.22  5317900        0.0           0.0     NaN      NaN
1  2024-04-26  92.86  93.67  92.19  92.40  6115700        0.0           0.0     NaN      NaN
2  2024-04-29  92.71  93.15  91.98  92.34  5030700        0.0           0.0     NaN      NaN
3  2024-04-30  91.21  91.80  90.56  90.57  6493300        0.0           0.0     NaN      NaN
4  2024-05-01  90.13  90.19  88.44  88.68  9783100        0.0           0.0     NaN      NaN

Stock data saved to NKE_data.csv.
```

---

## Disclaimer

This tool uses data provided by **Yahoo Finance** through the `yfinance` library. Data accuracy and availability depend on Yahoo Finance.

---
