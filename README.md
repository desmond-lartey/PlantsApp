<h1> Sustainable Green Concept App</h1>

<div style="display: flex; justify-content: space-between;">
    <img src="https://agro-nl.nl/wp-content/uploads/2019/04/trees-bareroot-e1557303577410.jpg" alt="Image 1" style="width: 24%; margin-right: 1%;">
    <img src="https://agro-nl.nl/wp-content/uploads/2019/04/shrubs-p9-min-e1557303401583.jpg" alt="Image 2" style="width: 24%; margin-right: 1%;">
    <img src="https://agro-nl.nl/wp-content/uploads/2019/04/shrubs-full-ground-min-e1557303444131.jpg" alt="Image 3" style="width: 24%; margin-right: 1%;">
    <img src="https://agro-nl.nl/wp-content/uploads/2019/04/trees-open-ground-e1557303524105.jpg" alt="Image 4" style="width: 24%;">
</div>

<h2>Overview</h2>
<p>The Sustainable Green Concept App, developed by Agro-NL Consult SolutionS B.V, is a tool aimed at pioneering sustainable urban development. As countries grapple with the complexities of urban expansion, environmental preservation, and the effects of climate change, our app serves as a bridge to a greener future.</p>

<h2>Aim and Objectives</h2>
<p>The primary goal of this app is to initiate a comprehensive dialogue among municipalities, localities, and governments. We aim to emphasize the importance of sustainable urban green development and the need to prioritize it in city planning.</p>

<ul>
    <li>Assessing environmental challenges across city landscapes, examining factors such as CO2 levels, sun exposure, shading, and the types of plants currently grown.</li>
    <li>Providing insights into green solutions, such as vertical greening, roof greening, and the cultivation of strong root plants that can withstand snowstorms.</li>
    <li>Offering a unique perspective on the current state of European plant markets, particularly emphasizing the intertwined nature of greenery, climate, and sustainability.</li>
</ul>

<h2>Contribution to Sustainable Urban Greening</h2>
<p>As cities experience rapid growth, the threat of environmental hazards looms large. Our app provides cities with tangible solutions that not only enhance the aesthetic appeal of urban areas but also contribute positively to the environment.</p>

<p>By suggesting plants that are suitable for the changing climates of various cities, we ensure that urban greening efforts are sustainable in the long run. Our proposals are not merely about adding greenery but about adding the <i>right</i> kind of greenery. This app offers cities a roadmap to a future where urban areas are lush, environmentally friendly, and sustainable.</p>

<h2>Getting Started with the App</h2>
<ol>
    Remember that the app initialise a 1-to-1 relational algorithm if you select a single file, value or attributes. This means that there is a strict and accurate match based on how it is entered in the dataset. The one-to-one relation will not work well if you select multiples. This can work well sometimes but affect referential integrity.</li>
    <li>Select the relevant datasets.
    <li>Choose the attributes you're interested in.</li>
    <li>Filter out the values, and let the app suggest plants that match the criteria.</li>
    <li>Dive deeper into each plant's characteristics and understand its impact on the environment.</li>
    
<p>Read these dcoumentation carefully, <a href="https://plantsapp-ajjdvywmagmqbsty4f2r9c.streamlit.app/">visit the App here</a>.</p>

    ##Things to note
There is a problem with "climate zone from and till" as well as ph values. It is not possible to use ranges, you really have to use a multi select to capture the information you need from this category. The issue might be that when we use the multiselect widget for values of "climate zone from" and "climate zone till", if the selected values in the dropdown are not part of the unique values present in the dataset, the widget may default back to a single selection. To get around this, The current app force the options in the multiselect widget to be a range of possible climate zones, irrespective of whether they exist in the dataset.


    ##Things to note With PH
Some values have spaces around the hyphen, such as "7 - 8,5". Some values use a comma, such as "6,1-7,5".
    
    
    ##To simplify the logic and avoid these inconsistencies, you can follow these steps:
Standardize the pH values in the Excel sheet: Replace ",5" with ".5" for decimal values. For instance, "7 - 8,5" becomes "7-8.5".
Remove spaces around the hyphen. For instance, "4 - 6" becomes "4-6". Ensure there are no trailing or leading spaces in the values. The problem here arises due to the way the pH values are represented in the dataset. The dataset contains a mixture of ranges, individual values, and even combined representations like "7 - 8,5". The comma-separated values add a layer of unnecessary complexity to the filtering process. 


    ##To simplify the filtering process and make the system more robust, I recommend the following approach:
Standardize the Data Representation. Use a consistent format for ranges, for example, "5-8" (without spaces).
If a plant can tolerate multiple, non-sequential ranges, maybe consider adding separate rows for each range or breaking the pH column into multiple columns like pH_range1, pH_range2, etc. Avoid mixing ranges and single values in the same cell. Use separate rows if needed.

Once the data is standardized, the app's logic can be simplified. You can then filter based on the selected ranges without dealing with edge cases caused by the mixed format or even having to use multi select.

<h2>Use the installed Database for advanced operation of Matrix:</h2>
If the dataset is expected to grow or if more advanced filtering and querying are anticipated in the future, consider moving from this Excel-based system app to the postgresQL database which has been designed on the main computer. The relational database allows for more structured data storage, easier querying and advanced queries.
</ol>

<p>See the app version of the geodatabase which includes queries at the country level, climate, and recommended species for local adaptation strategies, <a href="https://agro-nl.nl/">visit the geodatabase website</a>.</p>

<h2>How to update the app online from the Excel sheet</h2>
<p>You have to open the folder 'data' in the list of files here. Then download the file you want to update. For instance 'biodiversity_corrected'. Go to the matrix and look for the column biodiversity you want to pick information from. Copy a single column from the matrix. Now you can see that the 'biodiversity_corrected file has the same column identity as the one you have copied. Create a 4 empty row on the top of the header in the file. Paste what you copied in the exact column. Now rename the header you posted this info as the original name. Delete the four rows you created, this only helped you to paste the correct rows exactly from the matrix to the file. Save the file. Make sure you have saved it in xlsl/Excel workbook and not in csv. You have permission to upload new files in the github repository of the PlantApp. So delete the old file and replace the new one. Remember that it should have the same name as before.</p>

<h2>Final Thoughts</h2>
<p>Urban green spaces are more than just decorative elements; they are essential components of city infrastructure. The Sustainable Green Concept App is a step towards realizing a vision of cities that are not only developed but also green, sustainable, and considerate of the planet's well-being.</p>

<p>For more information on our efforts and the larger vision of Agro-NL Consult SolutionS B.V, <a href="https://agro-nl.nl/">visit our official website</a>.</p>
