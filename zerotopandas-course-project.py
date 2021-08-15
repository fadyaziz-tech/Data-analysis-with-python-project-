#!/usr/bin/env python
# coding: utf-8

# ## Data Analysis with Python: Zero to Pandas - Course Project Guidelines
# #### (remove this cell before submission)
# 
# Important links:
# - Make submissions here: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/course-project
# - Ask questions here: https://jovian.ml/forum/t/course-project-on-exploratory-data-analysis-discuss-and-share-your-work/11684
# - Find interesting datasets here: https://jovian.ml/forum/t/recommended-datasets-for-course-project/11711
# 
# 
# This is the starter notebook for the course project for [Data Analysis with Python: Zero to Pandas](https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas). You will pick a real-world dataset of your choice and apply the concepts learned in this course to perform exploratory data analysis. Use this starter notebook as an outline for your project . Focus on documentation and presentation - this Jupyter notebook will also serve as a project report, so make sure to include detailed explanations wherever possible using Markdown cells.
# 
# ### Evaluation Criteria
# 
# Your submission will be evaluated using the following criteria:
# 
# * Dataset must contain at least 3 columns and 150 rows of data
# * You must ask and answer at least 4 questions about the dataset
# * Your submission must include at least 4 visualizations (graphs)
# * Your submission must include explanations using markdown cells, apart from the code.
# * Your work must not be plagiarized i.e. copy-pasted for somewhere else.
# 
# 
# Follow this step-by-step guide to work on your project.
# 
# 
# ### Step 1: Select a real-world dataset 
# 
# - Find an interesting dataset on this page: https://www.kaggle.com/datasets?fileType=csv
# - The data should be in CSV format, and should contain at least 3 columns and 150 rows
# - Download the dataset using the [`opendatasets` Python library](https://github.com/JovianML/opendatasets#opendatasets)
# 
# Here's some sample code for downloading the [US Elections Dataset](https://www.kaggle.com/tunguz/us-elections-dataset):
# 
# ```
# import opendatasets as od
# dataset_url = 'https://www.kaggle.com/tunguz/us-elections-dataset'
# od.download('https://www.kaggle.com/tunguz/us-elections-dataset')
# ```
# 
# You can find a list of recommended datasets here: https://jovian.ml/forum/t/recommended-datasets-for-course-project/11711
# 
# ### Step 2: Perform data preparation & cleaning
# 
# - Load the dataset into a data frame using Pandas
# - Explore the number of rows & columns, ranges of values etc.
# - Handle missing, incorrect and invalid data
# - Perform any additional steps (parsing dates, creating additional columns, merging multiple dataset etc.)
# 
# 
# ### Step 3: Perform exploratory analysis & visualization
# 
# - Compute the mean, sum, range and other interesting statistics for numeric columns
# - Explore distributions of numeric columns using histograms etc.
# - Explore relationship between columns using scatter plots, bar charts etc.
# - Make a note of interesting insights from the exploratory analysis
# 
# ### Step 4: Ask & answer questions about the data
# 
# - Ask at least 4 interesting questions about your dataset
# - Answer the questions either by computing the results using Numpy/Pandas or by plotting graphs using Matplotlib/Seaborn
# - Create new columns, merge multiple dataset and perform grouping/aggregation wherever necessary
# - Wherever you're using a library function from Pandas/Numpy/Matplotlib etc. explain briefly what it does
# 
# 
# ### Step 5: Summarize your inferences & write a conclusion
# 
# - Write a summary of what you've learned from the analysis
# - Include interesting insights and graphs from previous sections
# - Share ideas for future work on the same topic using other relevant datasets
# - Share links to resources you found useful during your analysis
# 
# 
# ### Step 6: Make a submission & share your work
# 
# - Upload your notebook to your Jovian.ml profile using `jovian.commit`.
# - **Make a submission here**: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/course-project
# - Share your work on the forum: https://jovian.ml/forum/t/course-project-on-exploratory-data-analysis-discuss-and-share-your-work/11684
# - Browse through projects shared by other participants and give feedback
# 
# 
# ### (Optional) Step 7: Write a blog post
# 
# - A blog post is a great way to present and showcase your work.  
# - Sign up on [Medium.com](https://medium.com) to write a blog post for your project.
# - Copy over the explanations from your Jupyter notebook into your blog post, and [embed code cells & outputs](https://medium.com/jovianml/share-and-embed-jupyter-notebooks-online-with-jovian-ml-df709a03064e)
# - Check out the Jovian.ml Medium publication for inspiration: https://medium.com/jovianml
# 
# 
# 
# 
# 
# ### Example Projects
# 
# Refer to these projects for inspiration:
# 
# * [Analyzing StackOverflow Developer Survey Results](https://jovian.ml/aakashns/python-eda-stackoverflow-survey)
# 
# * [Analyzing Covid-19 data using Pandas](https://jovian.ml/aakashns/python-pandas-data-analysis) 
# 
# * [Analyzing your browser history using Pandas & Seaborn](https://medium.com/free-code-camp/understanding-my-browsing-pattern-using-pandas-and-seaborn-162b97e33e51) by Kartik Godawat
# 
# * [WhatsApp Chat Data Analysis](https://jovian.ml/PrajwalPrashanth/whatsapp-chat-data-analysis) by Prajwal Prashanth
# 
# * [Understanding the Gender Divide in Data Science Roles](https://medium.com/datadriveninvestor/exploratory-data-analysis-eda-understanding-the-gender-divide-in-data-science-roles-9faa5da44f5b) by Aakanksha N S
# 
# * [2019 State of Javscript Survey Results](https://2019.stateofjs.com/demographics/)
# 
# * [2020 Stack Overflow Developer Survey Results](https://insights.stackoverflow.com/survey/2020)
# 
# 
# 
# **NOTE**: Remove this cell containing the instructions before making your submission. You can do using the "Edit > Delete Cells" menu option.

# # Project Title - change this
# 
# TODO - Write some introduction about your project here: describe the dataset, where you got it from, what you're trying to do with it, and which tools & techniques you're using. You can also mention about the course [Data Analysis with Python: Zero to Pandas](zerotopandas.com), and what you've learned from it.

# ### How to run the code
# 
# This is an executable [*Jupyter notebook*](https://jupyter.org) hosted on [Jovian.ml](https://www.jovian.ml), a platform for sharing data science projects. You can run and experiment with the code in a couple of ways: *using free online resources* (recommended) or *on your own computer*.
# 
# #### Option 1: Running using free online resources (1-click, recommended)
# 
# The easiest way to start executing this notebook is to click the "Run" button at the top of this page, and select "Run on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running Jupyter notebooks. You can also select "Run on Colab" or "Run on Kaggle".
# 
# 
# #### Option 2: Running on your computer locally
# 
# 1. Install Conda by [following these instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Add Conda binaries to your system `PATH`, so you can use the `conda` command on your terminal.
# 
# 2. Create a Conda environment and install the required libraries by running these commands on the terminal:
# 
# ```
# conda create -n zerotopandas -y python=3.8 
# conda activate zerotopandas
# pip install jovian jupyter numpy pandas matplotlib seaborn opendatasets --upgrade
# ```
# 
# 3. Press the "Clone" button above to copy the command for downloading the notebook, and run it on the terminal. This will create a new directory and download the notebook. The command will look something like this:
# 
# ```
# jovian clone notebook-owner/notebook-id
# ```
# 
# 
# 
# 4. Enter the newly created directory using `cd directory-name` and start the Jupyter notebook.
# 
# ```
# jupyter notebook
# ```
# 
# You can now access Jupyter's web interface by clicking the link that shows up on the terminal or by visiting http://localhost:8888 on your browser. Click on the notebook file (it has a `.ipynb` extension) to open it.
# 

# ## Downloading the Dataset
# 
# **TODO** - add some explanation here

# > Instructions for downloading the dataset (delete this cell)
# >
# > - Find an interesting dataset on this page: https://www.kaggle.com/datasets?fileType=csv
# > - The data should be in CSV format, and should contain at least 3 columns and 150 rows
# > - Download the dataset using the [`opendatasets` Python library](https://github.com/JovianML/opendatasets#opendatasets)

# In[1]:


get_ipython().system('pip install jovian opendatasets --upgrade --quiet')


# Let's begin by downloading the data, and listing the files within the dataset.

# In[6]:


# Change this
dataset_url = 'https://www.kaggle.com/mathurinache/world-happiness-report' 


# In[7]:


import opendatasets as od
od.download(dataset_url)


# The dataset has been downloaded and extracted.

# In[12]:


# Change this
data_dir = './world-happiness-report'


# In[13]:


import os
os.listdir(data_dir)


# Let us save and upload our work to Jovian before continuing.

# In[18]:


project_name = "zerotopandas-course-project-starter" # change this (use lowercase letters and hyphens only)


# In[19]:


get_ipython().system('pip install jovian --upgrade -q')


# In[20]:


import jovian


# In[21]:


jovian.commit(project='world_happiens')


# ## Data Preparation and Cleaning
# 
# **TODO** - Write some explanation here.
# 
# 

# > Instructions (delete this cell):
# >
# > - Load the dataset into a data frame using Pandas
# > - Explore the number of rows & columns, ranges of values etc.
# > - Handle missing, incorrect and invalid data
# > - Perform any additional steps (parsing dates, creating additional columns, merging multiple dataset etc.)

# In[27]:


import pandas as pd 


# In[40]:


happiens_csv = data_dir + '/2020.csv'


# In[41]:


happiens_csv


# In[42]:


happines_df = pd.read_csv(happiens_csv)


# In[44]:


happines_df


# In[45]:


happines_df.describe()


# In[46]:


happines_df.info()


# In[49]:


happines_df.nunique()


# In[64]:


happines_df.isna().sum()


# In[65]:


import jovian


# In[66]:


jovian.commit('happiens')


# ## Exploratory Analysis and Visualization
# 
# **TODO** - write some explanation here.
# 
# 

# > Instructions (delete this cell)
# > 
# > - Compute the mean, sum, range and other interesting statistics for numeric columns
# > - Explore distributions of numeric columns using histograms etc.
# > - Explore relationship between columns using scatter plots, bar charts etc.
# > - Make a note of interesting insights from the exploratory analysis

# Let's begin by importing`matplotlib.pyplot` and `seaborn`.

# In[67]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[68]:


#Ladder score fot top 10


# In[69]:


top_countries = happines_df['Country name'].head(10)


# In[70]:


top_countries


# In[71]:


ladder_score =  happines_df['Ladder score'].head(10)


# In[72]:


ladder_score


# In[73]:


sns.barplot(x=ladder_score,y=top_countries)


# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[80]:


pip install Plotly 


# In[81]:


import plotly.express as px


# In[83]:


fig = px.bar(happines_df, x="Generosity", y="Country name",color='Country name')
fig.show()


# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[74]:


#Freedom to make life choices


# In[75]:


freedom_top = happines_df['Freedom to make life choices'].head(10)
freedom_top


# In[76]:


sns.barplot(x=freedom_top,y=top_countries)


# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[ ]:


#Social support


# In[87]:


fig = px.sunburst(happines_df.head(30), path=['Country name'], values='Social support',
                  color='Social support', color_continuous_scale='RdBu')
fig.show()


# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[91]:


fig = px.bar(happines_df, x="Regional indicator", y="Healthy life expectancy", color="Country name", barmode="group",)
fig.show()


# In[ ]:





# Let us save and upload our work to Jovian before continuing

# In[92]:


import jovian


# In[93]:


jovian.commit('happines')


# ## Asking and Answering Questions
# 
# TODO - write some explanation here.
# 
# 

# > Instructions (delete this cell)
# >
# > - Ask at least 5 interesting questions about your dataset
# > - Answer the questions either by computing the results using Numpy/Pandas or by plotting graphs using Matplotlib/Seaborn
# > - Create new columns, merge multiple dataset and perform grouping/aggregation wherever necessary
# > - Wherever you're using a library function from Pandas/Numpy/Matplotlib etc. explain briefly what it does
# 
# 

# #### Q1: TODO - ask a question here and answer it below

# In[ ]:


# how many regions we have and how many each many repated


# In[94]:


regions_count = happines_df['Regional indicator'].value_counts()
regions_count


# In[95]:


sns.barplot(x=regions_count,y=regions_count.index)


# #### Q2: TODO - ask a question here and answer it below

# In[ ]:


#what is the worst countries in Healthy life expectancy


# In[107]:


countries_name =happines_df['Country name'].tail(20)
countries_name


# In[108]:


life_expec = happines_df['Healthy life expectancy'].tail(20)
life_expec


# In[112]:


sns.barplot(x=life_expec,y=countries_name)


# #### Q3: TODO - ask a question here and answer it below

# In[ ]:


#let's know what is the correlation between corruption and health


# In[114]:


corr_health = happines_df['Perceptions of corruption'].corr(happines_df['Healthy life expectancy'])


# In[115]:


corr_health # increase in corruption lead to 35% decrease in health life 


# #### Q4: TODO - ask a question here and answer it below

# In[ ]:


#gdp for each region top(20)


# In[128]:


sns.barplot(x=happines_df['Logged GDP per capita'],y=happines_df['Regional indicator'])


# In[ ]:





# #### Q5: TODO - ask a question here and answer it below

# In[ ]:


#ladder for worst15 country 


# In[131]:


worst_15 = happines_df['Country name'].tail(15)
worst_15


# In[132]:


ladder_for_worst = happines_df['Ladder score'].tail(15)
ladder_for_worst                               


# In[133]:


plt.pie(ladder_for_worst,labels=worst_15,autopct='%1.1f%%', startangle=180);


# Let us save and upload our work to Jovian before continuing.

# In[134]:


import jovian


# In[135]:


jovian.commit('happiness')


# ## Inferences and Conclusion
# we can see now happiness it;s not about money or about cars or any physical items we can see that countries that you can find social support and people helping each other as we did we didn't measure the percentage of people whoms are the richest but also we found that almost the richest countries have a high percentage of happiness and in my opinion it's not because they have much money but because poorest country can't get food so how they can give a good education  as riches

# In[30]:


import jovian


# In[31]:


jovian.commit()


# ## References and Future Work
# 
# **TODO** - Write some explanation here: ideas for future projects using this dataset, and links to resources you found useful.

# > Submission Instructions (delete this cell)
# > 
# > - Upload your notebook to your Jovian.ml profile using `jovian.commit`.
# > - **Make a submission here**: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/course-project
# > - Share your work on the forum: https://jovian.ml/forum/t/course-project-on-exploratory-data-analysis-discuss-and-share-your-work/11684
# > - Share your work on social media (Twitter, LinkedIn, Telegram etc.) and tag [@JovianML](https://twitter.com/jovianml)
# >
# > (Optional) Write a blog post
# > 
# > - A blog post is a great way to present and showcase your work.  
# > - Sign up on [Medium.com](https://medium.com) to write a blog post for your project.
# > - Copy over the explanations from your Jupyter notebook into your blog post, and [embed code cells & outputs](https://medium.com/jovianml/share-and-embed-jupyter-notebooks-online-with-jovian-ml-df709a03064e)
# > - Check out the Jovian.ml Medium publication for inspiration: https://medium.com/jovianml
# 
# 
#  

# In[32]:


import jovian


# In[35]:


jovian.commit()


# In[ ]:




