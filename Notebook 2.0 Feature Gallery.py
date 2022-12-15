# Databricks notebook source
# MAGIC %md
# MAGIC ### Improved code editing with Monaco

# COMMAND ----------

# MAGIC %md
# MAGIC ### Autocomplete-as-you-type
# MAGIC ![autocomplete](https://github.com/RafiKurlansik/notebook2/blob/main/assets/autocomplete2.gif?raw=true)

# COMMAND ----------

import numpy as np

# Type the following on the next line: a = np.array([1,2,3])



# COMMAND ----------

# MAGIC %md 
# MAGIC #### Variable inspection on mouse hover
# MAGIC ![var-inspect](https://github.com/RafiKurlansik/notebook2/blob/main/assets/variable_inspection.gif?raw=true)

# COMMAND ----------

# Run this cell then hover over 'variable' on line 3
variable = np.array([1,2,3])
variable

# COMMAND ----------

# MAGIC %md
# MAGIC #### Code Folding & Bracket Matching
# MAGIC 
# MAGIC Code blocks can be collapsed by clicking the arrow icon next to them:
# MAGIC 
# MAGIC ![code-folding](https://github.com/RafiKurlansik/notebook2/blob/main/assets/code_folding.gif?raw=true)
# MAGIC 
# MAGIC Clicking next to a bracket will highlight the corresponding bracket further down in the code:
# MAGIC 
# MAGIC ![bracket-matching](https://github.com/RafiKurlansik/notebook2/blob/main/assets/bracket_matching.gif?raw=true)

# COMMAND ----------

# Collapse and expand code blocks on lines 9, 17, 24 and 31
!pip install folium --quiet

import json
import folium
import requests

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
vis1 = json.loads(requests.get(f"{url}/vis1.json").text)
vis2 = json.loads(requests.get(f"{url}/vis2.json").text)
vis3 = json.loads(requests.get(f"{url}/vis3.json").text)
m = folium.Map(location=[46.3014, -123.7390], zoom_start=7, tiles="Stamen Terrain")

folium.Marker(
    location=[47.3489, -124.708],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(vis1, width=450, height=250)
    ),
).add_to(m)

folium.Marker(
    location=[44.639, -124.5339],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(vis2, width=450, height=250)
    ),
).add_to(m)

folium.Marker(
    location=[46.216, -124.1280],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(vis3, width=450, height=250)
    ),
).add_to(m)

m

# COMMAND ----------

# MAGIC %md
# MAGIC #### Multi-cursor support
# MAGIC 
# MAGIC ![multi-cursor-support](https://github.com/RafiKurlansik/notebook2/blob/main/assets/multi_cursor.gif?raw=true)
# MAGIC 
# MAGIC Monaco supports multiple cursors for fast simultaneous edits. You can add secondary cursors (rendered thinner) with `Alt+Click` on Windows. Each cursor operates independently based on the context it sits in. A common way to add more cursors is with `⌥⌘↓` or `⌥⌘↑` that insert cursors below or above. ([source](https://code.visualstudio.com/Docs/editor/codebasics#_multiple-selections-multicursor))

# COMMAND ----------

# Place your cursor on line 2, then press option+command+down ( ⌥⌘↓ ) to create additional cursors on lines 3 and 4


# COMMAND ----------

# MAGIC %md 
# MAGIC #### Column (box) selection
# MAGIC 
# MAGIC ![boxselection](https://github.com/RafiKurlansik/notebook2/blob/main/assets/column_selection.gif?raw=true)
# MAGIC 
# MAGIC Place the cursor in one corner and then hold `Shift+Alt` (or `Shift+option` on Mac) while dragging to the opposite corner. ([source](https://code.visualstudio.com/Docs/editor/codebasics#_column-box-selection))

# COMMAND ----------

print("""
PassengerId,Name,Sex,Age,SibSp
1,"Braund, Mr. Owen Harris",male,22.0,1
2,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38.0,1
3,"Heikkinen, Miss. Laina",female,26.0,0
4,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35.0,1
5,"Allen, Mr. William Henry",male,35.0,0
6,"Moran, Mr. James",male,,0
7,"McCarthy, Mr. Timothy J",male,54.0,0
8,"Palsson, Master. Gosta Leonard",male,2.0,3
9,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27.0,0
10,"Nasser, Mrs. Nicholas (Adele Achem)",female,14.0,1
11,"Sandstrom, Miss. Marguerite Rut",female,4.0,1
12,"Bonnell, Miss. Elizabeth",female,58.0,0
13,"Saundercock, Mr. William Henry",male,20.0,0
14,"Andersson, Mr. Anders Johan",male,39.0,1
15,"Vestrom, Miss. Hulda Amanda Adolfina",female,14.0,0
""")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Run selected text
# MAGIC 
# MAGIC Run highlighted text with `Shift + Control + Enter`:
# MAGIC 
# MAGIC ![run_selected](https://github.com/RafiKurlansik/notebook2/blob/main/assets/run_selected.gif?raw=true)

# COMMAND ----------

# Give it a try
print(1)
print(2)
print(3)
print(4)
print(5)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Toggle Line Comment
# MAGIC 
# MAGIC <img src="https://github.com/RafiKurlansik/notebook2/blob/main/assets/togglecomment.gif?raw=true" width=500/>
# MAGIC 
# MAGIC We are making commenting easier to help users create clearly documented code faster. Users can now toggle comments on a line of code or for multiple lines of code at once. To do so, select the desired lines of code and hit the shortcut for your operating system.
# MAGIC 
# MAGIC Mac: `Cmd + /`
# MAGIC 
# MAGIC Windows: `Ctrl + /`

# COMMAND ----------

print(1)
print(2)
print(3)
print(4)
print(5)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Block quotes
# MAGIC 
# MAGIC <img src="https://github.com/RafiKurlansik/notebook2/blob/main/assets/blockquote.gif?raw=true" width=600>
# MAGIC 
# MAGIC Notebooks also now support block quotes if your programming language supports it. Users can use these commands to comment a whole block of code at once.
# MAGIC 
# MAGIC Mac:		`Shift+Option+A`
# MAGIC 
# MAGIC Windows: 	`Shift+Option+A`

# COMMAND ----------

# Use Shift+Option+A on the text within print() to put it in quotes
print(this is a 
multi-line text 
that you can put in quotes with
Shift + Option + A)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Python Formatting / Linting

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src="https://github.com/RafiKurlansik/notebook2/blob/main/assets/blackformatter2.gif?raw=true" width="500"/>

# COMMAND ----------

# MAGIC %md
# MAGIC [Python Formatter Public Preview Docs](https://docs.databricks.com/notebooks/notebooks-use.html#format-code-cells)
# MAGIC 
# MAGIC Databricks now supports Black, a PEP 8 compatible code formatter. Black formats all code the same so you spend less time formatting and more time creating what matters. All Black formatted code looks the same, regardless of what project you are reviewing, so code review goes faster too. To use Black, connect to a cluster on DBR 11.2 or later. Databricks preinstalls Black and Tokenize-rt.
# MAGIC 
# MAGIC **To try it out, in the following cell click on the cell and then click _Edit --> Format cell(s)_ in the Notebook menu bar** ([example source](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)).

# COMMAND ----------

def add(a,        b):
    answer  =  a   +       b

    return    answer

# COMMAND ----------

# MAGIC %md
# MAGIC ### Debugging
# MAGIC 
# MAGIC Notebooks run on Databricks Runtime 11.2 and above support [The Python Debugger](https://docs.python.org/3/library/pdb.html) (pdb).
# MAGIC 
# MAGIC Some examples of using pdb in a notebook:
# MAGIC 
# MAGIC * Use `%debug` to debug from the last exception. This is helpful when you run into an unexpected error and are trying to debug the cause (similar to `pdb.pm()`).
# MAGIC * Use `%pdb on` to automatically start the interactive debugger after exceptions (but before program terminates).
# MAGIC 
# MAGIC Note that when you use these commands, you must finish using the debugger before you can run any other cell. Here are a few ways to exit the debugger:
# MAGIC 
# MAGIC * `c` or `continue` to finish running the cell.
# MAGIC * `exit` to throw an error and stop code execution.
# MAGIC * Cancel the command by clicking `Cancel` next to the output box.

# COMMAND ----------

# MAGIC %md 
# MAGIC #### `%debug` : Post-mortem debugging
# MAGIC To use `%debug` in Databricks notebooks:
# MAGIC 
# MAGIC 1. Run commands in the notebook until an exception is raised.
# MAGIC 2. Run `%debug` in a new cell. The debugger starts running in the output area of the cell.
# MAGIC 3. To inspect a variable, type the variable name in the input field and press **Enter**.
# MAGIC 4. You can change context and perform other debugger tasks, like variable inspection, using these commands. For the complete list of debugger commands, see the [pdb documentation](https://docs.python.org/3/library/pdb.html). Type the letter and then press **Enter**.
# MAGIC   * `n`: next line
# MAGIC   * `u`: move up 1 level out of the current stack frame
# MAGIC   * `d`: move down 1 level out of the current stack frame
# MAGIC 5. Exit the debugger using one of the methods described in the first cell of this notebook.
# MAGIC Below is an example following these steps using %debug.

# COMMAND ----------

class ComplexSystem1:
  def getAccuracy(self, correct, total):
    # ...
    accuracy = correct / total
    # ...
    return accuracy
  
class UserTest:
  def __init__(self, system, correct, total):
    self.system = system
    self.correct = correct
    self.total = 0 # incorrectly set total!
    
  def printScore(self):
    print(f"You're score is: {self.system.getAccuracy(self.correct, self.total)}")
  
test = UserTest(
  system = ComplexSystem1(),
  correct = 10,
  total = 100
)
 
test.printScore()

# COMMAND ----------

# MAGIC %debug

# COMMAND ----------

# MAGIC %md
# MAGIC #### `%pdb on` : Pre-mortem debugging
# MAGIC To use `%pdb on` in Databricks notebooks:
# MAGIC 
# MAGIC 1. Turn auto pdb on by running `%pdb on` in the first cell of your notebook.
# MAGIC 2. Run commands in the notebook until an exception is raised. The interactive debugger starts.
# MAGIC 3. To inspect a variable, type the variable name in the input field and press **Enter**.
# MAGIC 4. You can change context and perform other debugger tasks, like variable inspection, using these commands. For the complete list of debugger commands, see the [pdb documentation](https://docs.python.org/3/library/pdb.html). Type the letter and then press **Enter**.
# MAGIC   * `n`: next line
# MAGIC   * `u`: move up 1 level out of the current stack frame
# MAGIC   * `d`: move down 1 level out of the current stack frame
# MAGIC 5. Exit the debugger using one of the methods described in the first cell of this notebook.
# MAGIC 
# MAGIC Below is an example following these steps using `%pdb on`.

# COMMAND ----------

# MAGIC %pdb on

# COMMAND ----------

class ComplexSystem2:
  def getAccuracy(self, correct, total):
    # ...
    accuracy = correct / total
    # ...
    return accuracy
 
system = ComplexSystem2()
 
## test coverage
print("Tests")
print(system.getAccuracy(10, 100) == 0.1)
print(system.getAccuracy(10, 0), 0)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Side by side diffs in revision history
# MAGIC 
# MAGIC ![diffs](https://github.com/RafiKurlansik/notebook2/blob/main/assets/diffs.gif?raw=true)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Syntax Highlighting
# MAGIC Having properly highlighted code makes coding, editing, and troubleshooting much faster. Now, **Notebooks will recognize and highlight SQL code in Python code cells for you.** Previously users would need to parse through the code manually to ensure it was executing as intended. At a glance, users can now ensure that the proper SQL terms are included and sequenced in the proper order.

# COMMAND ----------

df = spark.sql('''
select carat, cut, color, price 
from default.diamonds
where price < 350
''')
