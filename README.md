# google-mini-keymatch-to-searchblox-featured-result


## Python utility to convert Google Mini Keymatch to SearchBlox Featured Results

### Instructions

- Export Google Mini keymatch data to the files/ folder in this project
- Open the csv file in excel
- SaveAs the file in tab separate format in the files folder and name it googlemini.txt (**Don't change and of the data in the file**)
- In the project root run the consolidate.py python program

      python consolidate.py
      
Your results will be saved as outfile.txt in the files folder.  Import this file into SearchBlox as a Featured Result file.


If you already have Featured Results in your system that match those in this one you should delete them first from SearchBlox. Otherwise duplicate entries will result.

### Advanced Usage
You can edit the outfile.txt file and change the priorities.

### Google Mini to SearchBlox Mapping
In the mini you need to add multiple entries for different keywords or keyword phrases that map to the same url.  In SearchBlox multiple values can be associated with one url in one entry. The **consolidate.py** program consolidates multiple entries into one entry. However it uses only one title so if you want different titles for same url you will have to hand edit the results on the outfile.txt file or in SearchBlox once you have imported the value.

I hope you find this useful.  
<h1>google-mini-keymatch-to-searchblox-featured-result</h1>

<h2>Python utility to convert Google Mini Keymatch to SearchBlox Featured Results</h2>

<h3>Instructions</h3>

<ul>
<li>Export Google Mini keymatch data to the files/ folder in this project</li>
<li>Open the csv file in excel</li>
<li>SaveAs the file in tab separate format in the files folder and name it googlemini.txt (<strong>Don't change and of the data in the file</strong>)</li>
<li><p>In the project root run the consolidate.py python program</p>

<pre><code>python consolidate.py
</code></pre></li>
</ul>


<p>Your results will be saved as outfile.txt in the files folder.  Import this file into SearchBlox as a Featured Result file.</p>

<p>If you already have Featured Results in your system that match those in this one you should delete them first from SearchBlox. Otherwise duplicate entries will result.</p>

<h3>Advanced Usage</h3>

<p>You can edit the outfile.txt file and change the priorities.</p>

<h3>Google Mini to SearchBlox Mapping</h3>

<p>In the mini you need to add multiple entries for different keywords or keyword phrases that map to the same url.  In SearchBlox multiple values can be associated with one url in one entry. The <strong>consolidate.py</strong> program consolidates multiple entries into one entry. However it uses only one title so if you want different titles for same url you will have to hand edit the results on the outfile.txt file or in SearchBlox once you have imported the value.</p>

<p>I hope you find this useful.</p>

**Eric Palmer**

**University of Richmond**

**Web Services**


