#!/usr/bin/env python
# coding: utf-8

# In[4]:




# In[5]:


import streamlit as st


# In[12]:


import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Viewer</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/alasql/0.4.5/alasql.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.14.0/xlsx.core.min.js"></script>
</head>
<body class="bg-light">

<div class="container mt-5">
    <h2 class="text-center">Data Viewer</h2>
    <div class="row mt-4">
        <div class="col-md-4">
            <label for="fileSelector">Select a File:</label>
            <select id="fileSelector" class="form-control" onchange="populateAttributes()">
                <option value="biodiversity_corrected">Biodiversity</option>
                <option value="climate_corrected">Climate</option>
                <option value="maintenance_corrected">Maintenance</option>
                <option value="functional_corrected">Functional</option>
                <option value="ornamental_corrected">Ornamental</option>
                <option value="hazards_corrected">Hazard</option>
                <!-- ... add all file names here ... -->
                <option value="plants_corrected">Plants</option>
            </select>
        </div>
        <div class="col-md-4">
            <label for="attributeSelector">Select an Attribute:</label>
            <select id="attributeSelector" class="form-control" onchange="populateValues()"></select>
        </div>
        <div class="col-md-4">
            <label for="valueSelector">Select a Value:</label>
            <select id="valueSelector" class="form-control"></select>
        </div>
    </div>
    <div class="row mt-3">
        <div class="col text-center">
            <button onclick="fetchData()" class="btn btn-primary mt-2">Fetch Data</button>
        </div>
    </div>
    <div class="row mt-4">
        <div class="col">
            <h4>Matching Plant Names:</h4>
            <pre id="dataOutput"></pre>
        </div>
    </div>
</div>

<script>
    function populateAttributes() {
    const fileName = document.getElementById('fileSelector').value + ".xlsx";
    alasql.promise('SELECT * FROM XLSX("' + fileName + '", {headers:true}) LIMIT 1')
        .then(function(data) {
            if (data && data.length) {
                let columns = Object.keys(data[0]);
                let attributeDropdown = document.getElementById('attributeSelector');
                attributeDropdown.innerHTML = '';
                columns.forEach(column => {
                    let option = document.createElement('option');
                    option.value = column;
                    option.text = column;
                    attributeDropdown.appendChild(option);
                });
                populateValues();  // Call this to populate the values for the first attribute by default
            }
        }).catch(function(err) {
            console.log('Error:', err);
        });
}

function populateValues() {
    const fileName = document.getElementById('fileSelector').value + ".xlsx";
    const attributeName = document.getElementById('attributeSelector').value;
    alasql.promise('SELECT DISTINCT [' + attributeName + '] FROM XLSX("' + fileName + '", {headers:true})')
        .then(function(values) {
            let valueDropdown = document.getElementById('valueSelector');
            valueDropdown.innerHTML = '';
            values.forEach(value => {
                let option = document.createElement('option');
                option.value = value[attributeName];
                option.text = value[attributeName];
                valueDropdown.appendChild(option);
            });
        }).catch(function(err) {
            console.log('Error:', err);
        });
}

function fetchData() {
    const fileName = document.getElementById('fileSelector').value + ".xlsx";
    const attributeName = document.getElementById('attributeSelector').value;
    const selectedValue = document.getElementById('valueSelector').value;
    alasql.promise('SELECT [Plant name] FROM XLSX("' + fileName + '", {headers:true}) WHERE [' + attributeName + '] = ?', [selectedValue])
        .then(function(data) {
            document.getElementById('dataOutput').textContent = JSON.stringify(data, null, 2);
        }).catch(function(err) {
            console.log('Error:', err);
        });
}

// Initial population
populateAttributes();

</script>

</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Viewer</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/alasql/0.4.5/alasql.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.14.0/xlsx.core.min.js"></script>
</head>
<body>
>

    <script>
        function populateValues() {
            const attributeName = document.getElementById('attributeSelector').value;
            alasql('SELECT DISTINCT [' + attributeName + '] FROM XLSX("merged_plants_data.xlsx",{headers:true})', [], function(values){
                let valueDropdown = document.getElementById('valueSelector');
                valueDropdown.innerHTML = '';
                values.forEach(value => {
                    let option = document.createElement('option');
                    option.value = value[attributeName];
                    option.text = value[attributeName];
                    valueDropdown.appendChild(option);
                });
            });
        }

        function fetchData() {
            const attributeName = document.getElementById('attributeSelector').value;
            const selectedValue = document.getElementById('valueSelector').value;
            alasql('SELECT [Plant name] FROM XLSX("merged_plants_data.xlsx",{headers:true}) WHERE [' + attributeName + '] = ?', [selectedValue], function(data){
                document.getElementById('dataOutput').textContent = JSON.stringify(data, null, 2);
            });
        }

        // Initial population
        populateValues();
    </script>
</body>
</html>
"""

st.markdown(html_code, unsafe_allow_html=True)


# In[ ]:

