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
    <li>Select the relevant datasets.</li>
    <li>Choose the attributes you're interested in.</li>
    <li>Filter out the values, and let the app suggest plants that match the criteria.</li>
    <li>Dive deeper into each plant's characteristics and understand its impact on the environment.</li>
    <li>The problem here arises due to the way the pH values are represented in the dataset. The dataset contains a mixture of ranges, individual values, and even combined representations like "7 - 8,5". The comma-separated values add a layer of complexity to the filtering process.

To simplify the filtering process and make the system more robust, I recommend the following approach:

Standardize the Data Representation:

Use a consistent format for ranges, for example, "5-8" (without spaces).
If a plant can tolerate multiple, non-sequential ranges, consider adding separate rows for each range or breaking the pH column into multiple columns like pH_range1, pH_range2, etc.
Avoid mixing ranges and single values in the same cell. Use separate rows if needed.
Modify the App Logic:

Once the data is standardized, the app's logic can be simplified. You can then filter based on the selected ranges without dealing with edge cases caused by the mixed format.
Use a Database:

If the dataset is expected to grow or if more advanced filtering and querying are anticipated in the future, consider moving from an Excel-based system to a database. A relational database would allow for more structured data storage and easier querying.
For now, if you can adjust the data to follow the first recommendation, it will significantly simplify the process. If you provide a standardized dataset, I can help further with the code to ensure it works as expected</li>.
</ol>

<h2>Final Thoughts</h2>
<p>Urban green spaces are more than just decorative elements; they are essential components of city infrastructure. The Sustainable Green Concept App is a step towards realizing a vision of cities that are not only developed but also green, sustainable, and considerate of the planet's well-being.</p>

<p>For more information on our efforts and the larger vision of Agro-NL Consult SolutionS B.V, <a href="https://agro-nl.nl/">visit our official website</a>.</p>
