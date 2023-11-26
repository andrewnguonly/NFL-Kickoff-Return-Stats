import streamlit as st
import pandas as pd

# Function to read CSV file into DataFrame
def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to create a bar chart based on user-selected aggregation
def create_bar_chart(data, x_column, y_column, aggregation):
    if aggregation == 'Sum':
        chart_data = data.groupby(x_column)[y_column].sum()
    elif aggregation == 'Mean':
        chart_data = data.groupby(x_column)[y_column].mean()
    elif aggregation == 'Count':
        chart_data = data.groupby(x_column)[y_column].count()
    else:
        st.error("Invalid aggregation type.")
        return

    st.bar_chart(chart_data)

# Streamlit app
def main():
    st.title("CSV File Explorer and Bar Chart Generator")

    # Read CSV file into DataFrame
    df = read_data("data/NFL_Kickoff_Return_Stats.csv")

    # Display DataFrame
    st.subheader("DataFrame:")
    st.write(df)

    # Column selection
    columns = df.columns.tolist()
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    # Aggregation selection
    aggregation = st.selectbox("Select Aggregation", ['Sum', 'Mean', 'Count'])

    # Create and display the bar chart
    st.subheader("Bar Chart:")
    create_bar_chart(df, x_column, y_column, aggregation)

if __name__ == "__main__":
    main()
