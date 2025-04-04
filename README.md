
# Olympic Analysis Project

## Overview

The Olympic Analysis Project is an interactive web application designed to provide comprehensive insights into historical Olympic Games data.
Developed using **Python**, **Streamlit**, **Pandas**, and **Plotly**, the dashboard enables users to explore various aspects of the Olympics, including medal distributions, country-wise performances, athlete statistics, and trends over time.

## Features

- **Medal Tally**: View the overall medal counts, filterable by year and country, to analyze performance across different Olympic Games.

- **Overall Analysis**:
  - **Top Statistics**: Discover key statistics such as the most successful countries and athletes.
  - **Participating Nations Over the Years**: Visualize the growth in the number of countries participating in the Olympics over time.
  - **Number of Events Over the Years**: Examine how the number of events has evolved throughout Olympic history.
  - **Athletes Over the Years**: Analyze trends in athlete participation across different Olympic Games.
  - **Event Heatmap**: Explore a heatmap representation of the number of events held over time for various sports.
  - **Most Successful Athletes**: Identify top-performing athletes, with options to filter by specific sports.

- **Country-Wise Analysis**:
  - **Medal Analysis**: Delve into the medal counts of individual countries across different years.
  - **Country-Sport Heatmap**: Visualize the relationship between countries and the sports in which they have excelled.
  - **Most Successful Athletes by Country**: Discover the most decorated athletes from selected countries.

- **Athlete Analysis**:
  - **Age Distribution**: Examine the age distribution of athletes, including distinctions between medalists and non-medalists.
  - **Age Distribution by Sport and Medal Type**: Analyze how age varies among athletes across different sports and medal types.
  - **Men vs. Women Participation**: Compare the participation rates of male and female athletes over the years.

## Technologies Used

- **Python**: The core programming language used for data processing and analysis.
- **Streamlit**: Employed to create an interactive and user-friendly web interface for the dashboard.
- **Pandas**: Utilized for data manipulation and analysis, enabling efficient handling of large datasets.
- **Plotly**: Used to generate interactive and visually appealing graphs and charts.

## Dataset

The project utilizes the "120 Years of Olympic History: Athletes and Results" dataset, which encompasses comprehensive information on athletes and results from 1896 to 2016.
This dataset includes details such as athlete names, countries, sports, events, and medal types.

## Installation and Setup

To run the Olympic Analysis Project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhi12002/Olympic-Analysis-Project.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Olympic-Analysis-Project
   ```

3. **Install Required Dependencies**:
   Ensure that you have Python installed on your system. It's recommended to use a virtual environment to manage dependencies. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Launch the Streamlit application by executing:
   ```bash
   streamlit run app.py
   ```
   This command will start a local development server and open the application in your default web browser.

## Usage

Upon launching the application, you'll be presented with an interactive dashboard comprising multiple sections as outlined in the Features section.
Use the sidebar to navigate between different analyses and apply filters such as year, country, and sport to customize the visualizations according to your interests.

## Project Structure

The repository consists of the following key files:

- **app.py**: The main script that initializes and runs the Streamlit application, setting up the user interface and integrating various components.
- **preprocessor.py**: Contains functions for data cleaning and preprocessing, ensuring the dataset is structured appropriately for analysis.
- **helper.py**: Includes utility functions that support data analysis and visualization tasks, such as calculating statistics and generating plots.
- **athlete_events.csv**: The primary dataset file containing detailed records of Olympic athletes and their performances.
- **noc_regions.csv**: A supplementary dataset mapping National Olympic Committee (NOC) codes to their respective countries and regions.
- **requirements.txt**: A list of all Python packages required to run the application, facilitating easy setup of the development environment.

## Contributing

Contributions to enhance the Olympic Analysis Project are welcome.
If you have suggestions for new features, improvements, or bug fixes, please fork the repository and submit a pull request.
Ensure that your contributions align with the project's objectives and maintain code quality standards.

## License

This project is licensed under the [MIT License](LICENSE), permitting unrestricted use, distribution, and modification, provided that appropriate credit is given to the original author.

## Acknowledgments

Special thanks to the creators of the "120 Years of Olympic History: Athletes and Results" dataset for providing a comprehensive resource that made this analysis possible.
Gratitude is also extended to the developers of Streamlit, Pandas, and Plotly for their powerful tools that facilitated the creation of this interactive dashboard.

---

*This README provides a detailed overview of the Olympic Analysis Project, guiding users on its purpose, features, setup, and usage.*
