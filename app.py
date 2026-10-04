
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="ShopInsight | E-Commerce Analytics",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# DESIGN SYSTEM
# =========================================================
NAVY = "#14213D"
BLUE = "#4361EE"
TEAL = "#18A999"
ORANGE = "#F4A261"
PURPLE = "#8067DC"
TEXT = "#202B3C"
MUTED = "#758197"
BORDER = "#E8ECF3"
BG = "#F5F7FB"

PLOT_COLORS = [BLUE, TEAL, PURPLE, ORANGE, "#5C8DFF", "#E76F8A"]


st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'DM Sans', sans-serif;
    }}

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    [data-testid="stHeader"] {{
        background: rgba(245,247,251,0.92);
    }}

    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #14213D 0%, #1C3156 100%);
        border-right: none;
    }}

    [data-testid="stSidebar"] * {{
        color: #F4F7FF !important;
    }}

    [data-testid="stSidebar"] [data-baseweb="select"] * {{
        color: #202B3C !important;
    }}

    [data-testid="stSidebar"] input {{
        color: #202B3C !important;
    }}

    [data-testid="stSidebar"] hr {{
        border-color: rgba(255,255,255,0.16);
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }}

    h1, h2, h3 {{
        font-family: 'Manrope', sans-serif !important;
        color: {TEXT};
        letter-spacing: -0.6px;
    }}

    .hero {{
        background: linear-gradient(115deg, #14213D 0%, #263E70 65%, #4361EE 100%);
        border-radius: 22px;
        padding: 30px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 12px 32px rgba(20,33,61,0.12);
    }}

    .hero h1 {{
        color: white !important;
        font-size: 34px;
        font-weight: 800;
        margin: 8px 0 8px 0;
        letter-spacing: -1px;
    }}

    .hero p {{
        color: #DCE6FF;
        font-size: 14px;
        margin: 0;
        line-height: 1.7;
    }}

    .eyebrow {{
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 10px;
        font-weight: 700;
        color: #B9CBFF;
    }}

    .section-heading {{
        font-family: 'Manrope', sans-serif;
        font-size: 21px;
        font-weight: 800;
        color: {TEXT};
        margin-top: 15px;
        margin-bottom: 3px;
    }}

    .section-subtitle {{
        font-size: 12px;
        color: {MUTED};
        margin-bottom: 15px;
    }}

    .metric-card {{
        background: #FFFFFF;
        border: 1px solid {BORDER};
        border-radius: 17px;
        padding: 19px 19px 17px 19px;
        min-height: 126px;
        box-shadow: 0 4px 16px rgba(28,42,75,0.035);
    }}

    .metric-label {{
        color: {MUTED};
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 12px;
    }}

    .metric-value {{
        color: {NAVY};
        font-family: 'Manrope', sans-serif;
        font-size: 26px;
        font-weight: 800;
        letter-spacing: -0.7px;
        line-height: 1.2;
        overflow-wrap: anywhere;
    }}

    .metric-note {{
        color: {MUTED};
        font-size: 10px;
        margin-top: 10px;
    }}

    .metric-icon {{
        float: right;
        font-size: 20px;
        background: #EEF2FF;
        border-radius: 10px;
        width: 38px;
        height: 38px;
        text-align: center;
        line-height: 38px;
    }}

    .insight-card {{
        background: white;
        border: 1px solid {BORDER};
        border-left: 4px solid {BLUE};
        border-radius: 12px;
        padding: 15px 17px;
        min-height: 112px;
        margin-bottom: 10px;
    }}

    .insight-title {{
        color: {MUTED};
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }}

    .insight-value {{
        color: {NAVY};
        font-size: 16px;
        font-weight: 800;
        margin-bottom: 5px;
    }}

    .insight-detail {{
        color: {MUTED};
        font-size: 12px;
        line-height: 1.6;
    }}

    .footer {{
        color: {MUTED};
        font-size: 11px;
        text-align: center;
        padding: 24px 0 4px 0;
        border-top: 1px solid {BORDER};
        margin-top: 30px;
    }}

    div[data-testid="stPlotlyChart"] {{
        background: white;
        border: 1px solid {BORDER};
        border-radius: 16px;
        padding: 8px 8px 0 8px;
        box-shadow: 0 4px 16px rgba(28,42,75,0.025);
    }}

    div[data-testid="stDataFrame"] {{
        border: 1px solid {BORDER};
        border-radius: 12px;
        overflow: hidden;
    }}

    div.stButton > button,
    div.stDownloadButton > button {{
        border-radius: 10px;
        border: 1px solid {BORDER};
        font-weight: 600;
    }}

    div.stDownloadButton > button {{
        background: {BLUE};
        color: white;
        border: none;
    }}

    [data-testid="stCaptionContainer"] {{
        color: {MUTED};
    }}

    @media (max-width: 768px) {{
        .hero {{ padding: 23px 20px; }}
        .hero h1 {{ font-size: 27px; }}
        .metric-value {{ font-size: 22px; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# DATA LOADING AND CLEANING
# =========================================================
DATA_PATH = Path("data/online_retail_II.xlsx")
if not DATA_PATH.exists():
    st.error(f"Dataset not found at: {DATA_PATH.resolve()}")
    st.stop()

@st.cache_data
def load_data(file_path, modified_time):
    df = pd.read_excel(file_path, engine="openpyxl")
    return df

df = load_data(str(DATA_PATH), DATA_PATH.stat().st_mtime)

@st.cache_data(show_spinner=False)
def load_data(file_path, modified_time):
    raw = pd.read_excel(file_path, engine="openpyxl")
    raw.columns = raw.columns.str.strip()

    # Accommodate different versions of the Online Retail file.
    aliases = {
        "Invoice": "InvoiceNo",
        "Invoice No": "InvoiceNo",
        "Price": "UnitPrice",
        "Customer ID": "CustomerID",
        "Customer Id": "CustomerID",
    }

    raw = raw.rename(columns=aliases)

    required = [
        "InvoiceNo", "StockCode", "Description",
        "Quantity", "InvoiceDate", "UnitPrice",
        "CustomerID", "Country",
    ]

    missing = [col for col in required if col not in raw.columns]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}. "
            f"Columns found: {raw.columns.tolist()}"
        )

    original_rows = len(raw)

    raw["InvoiceDate"] = pd.to_datetime(
        raw["InvoiceDate"], errors="coerce"
    )
    raw["Quantity"] = pd.to_numeric(
        raw["Quantity"], errors="coerce"
    )
    raw["UnitPrice"] = pd.to_numeric(
        raw["UnitPrice"], errors="coerce"
    )

    raw = raw.drop_duplicates()

    valid = raw.dropna(
        subset=["InvoiceNo", "InvoiceDate", "Quantity", "UnitPrice"]
    ).copy()

    # Cancellation invoices are commonly marked with a C prefix.
    cancellations = valid[
        valid["InvoiceNo"].astype(str).str.startswith("C")
    ].copy()

    sales = valid[
        ~valid["InvoiceNo"].astype(str).str.startswith("C")
        & (valid["Quantity"] > 0)
        & (valid["UnitPrice"] > 0)
    ].copy()

    sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]
    sales["Month"] = sales["InvoiceDate"].dt.to_period("M").astype(str)
    sales["Year"] = sales["InvoiceDate"].dt.year
    sales["Hour"] = sales["InvoiceDate"].dt.hour
    sales["Description"] = (
        sales["Description"].fillna("Unknown product").astype(str)
    )
    sales["Country"] = sales["Country"].fillna("Unknown")

    quality = {
        "original_rows": original_rows,
        "valid_sales_rows": len(sales),
        "cancellation_rows": len(cancellations),
        "removed_or_invalid_rows": original_rows - len(sales),
        "missing_customer_ids": int(sales["CustomerID"].isna().sum()),
        "duplicate_rows_removed": original_rows - len(raw),
    }

    return sales, quality


if not DATA_PATH.exists():
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">E-commerce intelligence</div>
            <h1>ShopInsight</h1>
            <p>Your sales and customer analytics workspace.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.error(
        "Dataset not found. Place your Kaggle Excel file at "
        "`data/online_retail_II.xlsx`."
    )
    st.stop()


try:
    with st.spinner("Preparing your sales intelligence dashboard..."):
        sales, quality = load_data(
            str(DATA_PATH),
            DATA_PATH.stat().st_mtime,
        )
except Exception as error:
    st.error(f"Unable to process the dataset: {error}")
    st.stop()


if sales.empty:
    st.error("No valid sales records remain after cleaning.")
    st.stop()


# =========================================================
# SIDEBAR AND FILTERS
# =========================================================
with st.sidebar:
    st.markdown(
        """
        <div style="padding:8px 0 22px 0;">
            <div style="font-size:30px;">🛍️</div>
            <div style="font-family:Manrope,sans-serif;font-size:23px;
                        font-weight:800;letter-spacing:-0.6px;">
                ShopInsight
            </div>
            <div style="font-size:11px;color:#B9CBFF!important;">
                E-COMMERCE ANALYTICS
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### ⚙️ Dashboard filters")
    st.caption("Customise the data shown across your dashboard.")

    countries = sorted(sales["Country"].dropna().unique().tolist())

    selected_countries = st.multiselect(
        "🌍 Countries",
        options=countries,
        default=countries,
    )

    min_date = sales["InvoiceDate"].min().date()
    max_date = sales["InvoiceDate"].max().date()

    date_range = st.date_input(
        "📅 Invoice date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        format="DD/MM/YYYY",
    )

    st.markdown("---")
    st.markdown("### 📌 About this project")
    st.caption(
        "ShopInsight explores retail transactions using Python, "
        "Pandas, Streamlit and Plotly."
    )
    st.caption("Source: Kaggle Online Retail dataset.")
    st.caption("Currency shown: GBP (£).")

    if st.button("↻ Reset filters", use_container_width=True):
        st.rerun()


# =========================================================
# FILTERED DATA
# =========================================================
filtered = sales[sales["Country"].isin(selected_countries)].copy()

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        filtered["InvoiceDate"].dt.date.between(start_date, end_date)
    ]

if filtered.empty:
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">ShopInsight</div>
            <h1>No matching transactions</h1>
            <p>Try selecting a wider date range or additional countries.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()


# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">SALES PERFORMANCE • CUSTOMER INTELLIGENCE</div>
        <h1>Know your business.<br>Grow with insights.</h1>
        <p>
            Explore transaction trends, discover your strongest products,
            and understand customer purchasing behaviour — all in one place.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="font-size:12px;color:{MUTED};margin-bottom:18px;">
        <b style="color:{TEXT};">Overview</b>
        &nbsp; / &nbsp; Sales intelligence
        &nbsp; • &nbsp; {len(filtered):,} transaction lines in current view
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# KPI CARDS
# =========================================================
total_revenue = filtered["Revenue"].sum()
total_orders = filtered["InvoiceNo"].nunique()
units_sold = filtered["Quantity"].sum()
unique_customers = filtered["CustomerID"].nunique()

kpis = [
    ("TOTAL REVENUE", f"£{total_revenue:,.0f}", "💷", "Valid sales value"),
    ("TOTAL ORDERS", f"{total_orders:,}", "🧾", "Distinct invoices"),
    ("UNITS SOLD", f"{units_sold:,.0f}", "📦", "Total valid quantity"),
    ("UNIQUE CUSTOMERS", f"{unique_customers:,}", "👥", "Known customer IDs"),
]

cols = st.columns(4)

for col, (label, value, icon, note) in zip(cols, kpis):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">{icon}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# PREPARE REUSABLE AGGREGATIONS
# =========================================================
monthly = (
    filtered.groupby("Month", as_index=False)
    .agg(Revenue=("Revenue", "sum"), Orders=("InvoiceNo", "nunique"))
    .sort_values("Month")
)

products = (
    filtered.groupby("Description", as_index=False)
    .agg(Revenue=("Revenue", "sum"), Units=("Quantity", "sum"))
    .sort_values("Revenue", ascending=False)
)

country_data = (
    filtered.groupby("Country", as_index=False)
    .agg(Revenue=("Revenue", "sum"), Orders=("InvoiceNo", "nunique"))
    .sort_values("Revenue", ascending=False)
)

customer_sales = (
    filtered.dropna(subset=["CustomerID"])
    .groupby("CustomerID", as_index=False)
    .agg(
        TotalSpent=("Revenue", "sum"),
        Orders=("InvoiceNo", "nunique"),
        LastPurchase=("InvoiceDate", "max"),
    )
    .sort_values("TotalSpent", ascending=False)
)

average_order_value = (
    total_revenue / total_orders if total_orders else 0
)


# =========================================================
# CHART THEME
# =========================================================
def style_chart(fig, height=350):
    fig.update_layout(
        height=height,
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(
            family="DM Sans, sans-serif",
            color=TEXT,
            size=11,
        ),
        title=dict(
            font=dict(
                family="Manrope, sans-serif",
                size=15,
                color=NAVY,
            ),
            x=0.02,
            xanchor="left",
        ),
        margin=dict(l=20, r=20, t=60, b=30),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        hoverlabel=dict(
            bgcolor=NAVY,
            font_size=12,
            font_family="DM Sans",
        ),
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#EEF1F6",
        zeroline=False,
        linecolor=BORDER,
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#EEF1F6",
        zeroline=False,
        linecolor=BORDER,
    )

    return fig


# =========================================================
# SALES PERFORMANCE
# =========================================================
st.markdown(
    '<div class="section-heading">Sales performance</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">'
    'Track revenue over time and identify your leading products.'
    '</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([1.45, 1], gap="medium")

with left:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=monthly["Month"],
            y=monthly["Revenue"],
            mode="lines+markers",
            name="Revenue",
            line=dict(color=BLUE, width=3, shape="spline"),
            marker=dict(size=6, color=BLUE),
            fill="tozeroy",
            fillcolor="rgba(67,97,238,0.09)",
            hovertemplate="%{x}<br>Revenue: £%{y:,.2f}<extra></extra>",
        )
    )

    fig.update_layout(
        title="Monthly revenue trend",
        xaxis_title="Month",
        yaxis_title="Revenue (£)",
    )
    fig.update_yaxes(tickprefix="£", tickformat=",.0f")
    fig = style_chart(fig, 390)
    st.plotly_chart(fig, use_container_width=True)

with right:
    top_products = products.head(10).sort_values("Revenue")

    fig = px.bar(
        top_products,
        x="Revenue",
        y="Description",
        orientation="h",
        color="Revenue",
        color_continuous_scale=["#C7D2FE", BLUE],
        hover_data={"Revenue": ":,.2f", "Units": ":,.0f"},
        title="Top 10 products by revenue",
        labels={"Revenue": "Revenue (£)", "Description": ""},
    )

    fig.update_coloraxes(showscale=False)
    fig.update_yaxes(showgrid=False)
    fig.update_xaxes(tickprefix="£", tickformat=",.0f")
    fig = style_chart(fig, 390)
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# MARKET PERFORMANCE
# =========================================================
st.markdown(
    '<div class="section-heading">Market performance</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">'
    'Compare sales contribution across countries and order patterns.'
    '</div>',
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="medium")

with left:
    top_countries = country_data.head(10).sort_values("Revenue")

    fig = px.bar(
        top_countries,
        x="Revenue",
        y="Country",
        orientation="h",
        color="Revenue",
        color_continuous_scale=["#A8E6DB", TEAL],
        title="Revenue by country",
        labels={"Revenue": "Revenue (£)", "Country": ""},
        hover_data={"Orders": ":,.0f"},
    )

    fig.update_coloraxes(showscale=False)
    fig.update_xaxes(tickprefix="£", tickformat=",.0f")
    fig.update_yaxes(showgrid=False)
    fig = style_chart(fig, 365)
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.bar(
        monthly,
        x="Month",
        y="Orders",
        title="Monthly order volume",
        labels={"Month": "Month", "Orders": "Distinct invoices"},
        color_discrete_sequence=[PURPLE],
    )

    fig.update_traces(
        marker_line_width=0,
        hovertemplate="%{x}<br>Orders: %{y:,}<extra></extra>",
    )
    fig = style_chart(fig, 365)
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# AUTOMATIC INSIGHTS
# =========================================================
st.markdown(
    '<div class="section-heading">Insights at a glance</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">'
    'Key observations calculated from your current filter selection.'
    '</div>',
    unsafe_allow_html=True,
)

insight_cols = st.columns(3)

if not monthly.empty:
    peak_month = monthly.loc[monthly["Revenue"].idxmax()]
    peak_month_name = peak_month["Month"]
    peak_month_revenue = peak_month["Revenue"]
else:
    peak_month_name = "N/A"
    peak_month_revenue = 0

if not products.empty:
    leading_product = products.iloc[0]["Description"]
    leading_product_revenue = products.iloc[0]["Revenue"]
else:
    leading_product = "N/A"
    leading_product_revenue = 0

if not country_data.empty:
    leading_country = country_data.iloc[0]["Country"]
    leading_country_revenue = country_data.iloc[0]["Revenue"]
    country_share = (
        leading_country_revenue / total_revenue * 100
        if total_revenue else 0
    )
else:
    leading_country = "N/A"
    leading_country_revenue = 0
    country_share = 0

insights = [
    (
        "📈 Strongest month",
        peak_month_name,
        f"Revenue of £{peak_month_revenue:,.2f} in the selected period.",
        BLUE,
    ),
    (
        "🏆 Leading product",
        str(leading_product)[:42],
        f"Generated £{leading_product_revenue:,.2f} in revenue.",
        PURPLE,
    ),
    (
        "🌍 Leading country",
        str(leading_country),
        f"£{leading_country_revenue:,.2f} revenue ({country_share:.1f}% of selected revenue).",
        TEAL,
    ),
]

for col, (title, value, detail, accent) in zip(insight_cols, insights):
    with col:
        st.markdown(
            f"""
            <div class="insight-card" style="border-left-color:{accent};">
                <div class="insight-title">{title}</div>
                <div class="insight-value">{value}</div>
                <div class="insight-detail">{detail}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# CUSTOMER ANALYTICS
# =========================================================
st.markdown(
    '<div class="section-heading">Customer intelligence</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">'
    'Explore customer spending and repeat purchasing behaviour.'
    '</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1.35], gap="medium")

with left:
    repeat_customers = int((customer_sales["Orders"] > 1).sum())
    known_customers = len(customer_sales)
    repeat_rate = (
        repeat_customers / known_customers * 100
        if known_customers else 0
    )

    st.markdown(
        f"""
        <div class="metric-card" style="margin-bottom:15px;">
            <div class="metric-label">CUSTOMERS WITH MULTIPLE ORDERS</div>
            <div class="metric-value">{repeat_customers:,}</div>
            <div class="metric-note">
                {repeat_rate:.1f}% of customers with known IDs in the current view
            </div>
        </div>
        <div class="metric-card">
            <div class="metric-label">AVERAGE REVENUE PER ORDER</div>
            <div class="metric-value">£{average_order_value:,.2f}</div>
            <div class="metric-note">
                Total valid sales revenue divided by distinct invoices
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    if not customer_sales.empty:
        fig = px.histogram(
            customer_sales,
            x="TotalSpent",
            nbins=35,
            title="Customer spending distribution",
            labels={
                "TotalSpent": "Customer revenue (£)",
                "count": "Number of customers",
            },
            color_discrete_sequence=[BLUE],
        )

        fig.update_traces(
            marker_line_color="white",
            marker_line_width=0.5,
        )
        fig.update_xaxes(tickprefix="£", tickformat=",.0f")
        fig = style_chart(fig, 300)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No identified customers are available for this selection.")


with st.expander("View top customers"):
    if not customer_sales.empty:
        top_customers = customer_sales.head(10).copy()
        top_customers["CustomerID"] = top_customers["CustomerID"].astype(str)
        top_customers["TotalSpent"] = top_customers["TotalSpent"].round(2)

        st.dataframe(
            top_customers.rename(
                columns={
                    "CustomerID": "Customer ID",
                    "TotalSpent": "Total revenue (£)",
                    "Orders": "Distinct orders",
                    "LastPurchase": "Last purchase",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No customer records to display.")


# =========================================================
# DOWNLOADS AND DATA QUALITY
# =========================================================
st.markdown(
    '<div class="section-heading">Explore your data</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">'
    'Export the current filtered transactions or inspect data quality.'
    '</div>',
    unsafe_allow_html=True,
)

download_col, info_col = st.columns([1, 1])

with download_col:
    st.download_button(
        "⬇️ Download filtered sales CSV",
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="shopinsight_filtered_sales.csv",
        mime="text/csv",
        use_container_width=True,
    )

with info_col:
    st.download_button(
        "⬇️ Download monthly summary CSV",
        data=monthly.to_csv(index=False).encode("utf-8"),
        file_name="shopinsight_monthly_summary.csv",
        mime="text/csv",
        use_container_width=True,
    )

with st.expander("Data preparation and quality report"):
    q1, q2, q3 = st.columns(3)
    q1.metric("Original records", f"{quality['original_rows']:,}")
    q2.metric("Valid sales lines", f"{quality['valid_sales_rows']:,}")
    q3.metric("Cancellation lines", f"{quality['cancellation_rows']:,}")

    st.write(
        f"**Duplicate records removed:** "
        f"{quality['duplicate_rows_removed']:,}"
    )
    st.write(
        f"**Sales rows with missing customer IDs:** "
        f"{quality['missing_customer_ids']:,}"
    )
    st.write(
        "Sales metrics exclude cancellation invoices, non-positive "
        "quantities and non-positive prices. Customer analysis excludes "
        "records without a customer ID. These choices affect the reported "
        "totals and should be explained in the project report."
    )

    st.caption(
        "Revenue is calculated as Quantity × UnitPrice. "
        "It represents transaction value, not profit."
    )


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
    <div class="footer">
        <b style="color:{NAVY};">SHOPINSIGHT</b>
        &nbsp; • &nbsp; Built with Python, Pandas, Streamlit & Plotly
        <br><br>
        Educational data exploration project · Kaggle Online Retail dataset
    </div>
    """,
    unsafe_allow_html=True,
)