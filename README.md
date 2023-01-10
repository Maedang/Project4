# MBTI Prediction

We wanted to create a website that could scrape someone's twitter and be able to predict someone Myers-Briggs personality type based on what they have posted.

## Extracting and Cleaning Data

First, we found a dataset from Kaggle that had several posts and the person's respective personality type and imported it into Jupyter Notebook.

![image](https://user-images.githubusercontent.com/105513598/211451505-87d84c8d-e320-425d-953a-eac0153b6404.png)

We then cleaned the data by creating a function to get rid unneccessary words such as stopwords, hyperlinks, symbols, etc. so we can get our data prepared to train it and create our model.

![image](https://user-images.githubusercontent.com/105513598/211452337-1121197f-da97-415b-9119-e651f37d4cd3.png)

## Training our Data and Creating our Models

After that, we trained our dataset by each individual letter option. For example, we trained based on whether someone is an extrovert or introvert. and we used vectorizer to transform the train and test data for all 4 letters and then combined the train and test data.

![image](https://user-images.githubusercontent.com/105513598/211452978-57619b15-2f8f-4c93-bbcb-961bd092be11.png)

To ensure that we were using the most accurate models for each letter we created a function to test different types of models such as logistic regression, SVC, random forest, etc. and then used the most accurate model for each letter.

![image](https://user-images.githubusercontent.com/105513598/211453330-add1bad7-9525-4b00-bfba-dc212f021a30.png)

![image](https://user-images.githubusercontent.com/105513598/211453371-69ac00f2-5ced-4a8b-8490-36b752b9287f.png)

## Data Visualizations

We also wanted to do some visualizations about our dataset to see things such as the most popular personality types, who has the longest posts, what words are these personality types using, etc. We used Tableau and matplotlib to create graphs and wordcloud to answer some of these questions.

![image](https://user-images.githubusercontent.com/105513598/211454355-a031cd54-473a-47e0-9add-7362f1bd2270.png)

![image](https://user-images.githubusercontent.com/105513598/211454418-c8bf5f83-1213-402b-a0ce-c3576aecd39e.png)

## Website

We created a website using HTML for people to be able for people to type in their Twitter handles and have our model predict their personality types. Once it predicts it will give you a small description of the predicted personality type and a link to a website just in case you want to find out more about your personality type.

![Screen Shot 2023-01-09 at 10 02 52 PM](https://user-images.githubusercontent.com/105513598/211459366-40f16463-b12a-43ee-bef2-882802765de6.png)
