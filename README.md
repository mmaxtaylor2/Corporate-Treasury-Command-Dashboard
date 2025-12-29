## Corporate Treasury Command Dashboard

The Corporate Treasury Command Dashboard is a Streamlit-based analytical control center designed to centralize core treasury functions into a single reporting environment. It provides visibility into liquidity, cash positioning, revolver utilization, investment maturities, and overall short-term financial health.

This project simulates the type of reporting environment used by corporate treasury teams, CFOs, and liquidity managers to make informed operational and strategic decisions.

## Live App

## Key Capabilities

Cash by bank, business unit, and currency
Global liquidity snapshot with runway calculation
Burn rate to runway translation in weeks
Revolver capacity and utilization monitoring
Short-term investment ladder (MMF, T-Bills, Commercial Paper)
Risk classification based on liquidity stress indicators

## Dashboard Structure

The application consists of the main dashboard and five supporting pages:

Page	Purpose
Cash Position:	Real-time breakdown of bank balances and total cash
Liquidity Runway:	Forecasted runway based on burn rate and ending cash
Revolver Status:	Drawn vs available capacity and utilization percentage
Investment Ladder:	Maturity ladder for short-term investments
Risk Indicators:	Liquidity classification based on thresholds and leverage signals

## File Structure

Corporate-Treasury-Command-Dashboard-FINAL/
├── app.py
├── pages/
│   ├── 1_Cash_Position.py
│   ├── 2_Liquidity_Runway.py
│   ├── 3_Revolver_Status.py
│   ├── 4_Investment_Ladder.py
│   └── 5_Risk_Indicators.py
├── data/
│   ├── bank_balances.csv
│   ├── runway_forecast.csv
│   ├── revolver_status.csv
│   └── investments.csv
├── .gitignore
├── requirements.txt
└── README.md

## How to Run

Clone the repository:

git clone https://github.com/mmaxtaylor2/Corporate-Treasury-Command-Dashboard.git
cd Corporate-Treasury-Command-Dashboard

Install dependencies:

pip install -r requirements.txt

Launch the dashboard:

streamlit run app.py

The application will open in a browser window.

## Requirements

streamlit
pandas
plotly

## Data Inputs

The dashboard expects four CSV files in the /data folder:

bank_balances.csv – banking and currency position
runway_forecast.csv – projected ending cash and burn activity
revolver_status.csv – revolver facility structure and utilization
investments.csv – short-term instruments, yields, and maturities

These can be edited to reflect different treasury environments and assumptions.

## Intended Use Case

This project is designed as a portfolio artifact demonstrating:

Treasury reporting workflows
Liquidity decision-making frameworks
Corporate finance operational visibility
Dashboard development for financial stakeholders
