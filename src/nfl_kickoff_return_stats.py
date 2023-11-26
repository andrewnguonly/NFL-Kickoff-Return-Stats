import streamlit as st
import pandas as pd


# Function to read CSV file into DataFrame
def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to create a bar chart based on user-selected aggregation
def create_bar_chart(data, x_column, y_column, aggregation):
    if aggregation == "Sum":
        chart_data = data.groupby(x_column)[y_column].sum()
    elif aggregation == "Mean":
        chart_data = data.groupby(x_column)[y_column].mean()
    elif aggregation == "Median":
        chart_data = data.groupby(x_column)[y_column].median()
    elif aggregation == "Max":
        chart_data = data.groupby(x_column)[y_column].max()
    elif aggregation == "Min":
        chart_data = data.groupby(x_column)[y_column].min()
    elif aggregation == "Count":
        chart_data = data.groupby(x_column)[y_column].count()
    else:
        st.error("Invalid aggregation type.")
        return

    st.bar_chart(chart_data, y=y_column)

# Streamlit app
def main():
    st.title("NFL Kickoff Return Stats")

    # Read CSV file into DataFrame
    df = read_data("data/NFL_Kickoff_Return_Stats.csv")
    df = df.rename(columns={
        "Avg": "Average Return (yds)",
        "Ret": "Total Returns (count)",
        "Yds": "Total Yards (yds)",
        "KRet TD": "Total Touchdowns (count)",
        "20+": "Returns > 20 yards (count)",
        "40+": "Returns > 40 yards (count)",
        "Lng": "Longest return (yds)",
    })

    # Display DataFrame
    with st.expander("Raw data, source: NFL.com", expanded=False):
        # Query options
        st.sidebar.header("Data Options")

        # Filter by column values
        selected_column = st.sidebar.selectbox("Filter by column", ["Player"])
        filter_value = st.sidebar.text_input(f"Enter column value", "")

        # Apply filter
        if filter_value:
            df = df[df[selected_column] == filter_value]

        st.write(df)

    # Column selection
    columns = df.columns.tolist()
    columns = [col for col in columns if col not in ["Year", "Player", "FC", "FUM"]]
    y_column = st.selectbox("Select stat", columns, index=2)

    # Aggregation selection
    aggregation = st.selectbox(
        "Select aggregation",
        ["Sum", "Mean", "Median", "Max", "Min", "Count"],
        index=0,
    )

    # Create and display the bar chart
    create_bar_chart(df, "Year", y_column, aggregation)

if __name__ == "__main__":
    main()
