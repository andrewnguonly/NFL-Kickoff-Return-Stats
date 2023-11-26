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

    st.bar_chart(chart_data)

# Streamlit app
def main():
    st.title("NFL Kickoff Return Stats")

    # Read CSV file into DataFrame
    df = read_data("data/NFL_Kickoff_Return_Stats.csv")

    # Display DataFrame
    with st.expander("Raw data, source: NFL.com", expanded=False):
        st.write(df)

    # Column selection
    columns = df.columns.tolist()
    columns = [col for col in columns if col not in ["Year", "Player"]]
    y_column = st.selectbox("Select stat", columns)

    # Aggregation selection
    aggregation = st.selectbox(
        "Select Aggregation",
        ["Sum", "Mean", "Median", "Max", "Min", "Count"],
    )

    # Create and display the bar chart
    create_bar_chart(df, "Year", y_column, aggregation)

if __name__ == "__main__":
    main()
