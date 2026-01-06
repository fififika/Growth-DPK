# Growth-DPK
**Project Overview**
This Python-based tool is designed to analyze the growth of Third-Party Funds (DPK/Deposit). The script executes an end-to-end data pipeline, including Data Cleaning, Data Processing/Analysis, and Data Visualization.
This program is highly efficient for processing large-scale datasets where traditional spreadsheet software (like Excel) often reaches its performance limits or fails to handle the volume.

**Analysis Pipeline**
Data Cleansing: Converting raw string data into computable numeric formats and filtering invalid entries.
Data Processing: Aggregating balances and calculating growth (delta) across branches and customer segments.
Visualization: Producing professional-grade bar charts and geographical mapping (Folium) to pinpoint high-performing areas.

**How to Use**
**1.** Clone the Repository/Download Repository: 
**2.** Prepare the Data: Place your source file named Growth_DPK.csv in the root directory. Ensure the data structure follows the defined columns (Region, Branch, Name, Segment, etc.).
**3.** Install Dependencies: Run the following command to install the required Python libraries:
  pip install pandas
  pip install matplotlib
  pip install seaborn
  pip install folium

**Execute the Script**: Run the analysis program: python Analisis.py

**View Results:** The program will generate several output files in the same directory:
  1_Posisi_Saldo_Cabang.csv - Detailed branch ranking.
  2_Top_20_Loser.csv - Data of customers with the largest decrease.
  3_Top_20_Gainer.csv - Data of customers with the largest growth.
  Analisis_DPK_Visual.png - Static charts for reports.
