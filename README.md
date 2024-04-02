# CS5100Project
## Amazon Book Reviews Sentiment Analysis
### Wanyi Li, Wenqin Wu, Feiquan Liu, Yilei Bai
### Objective 
Most customers shopping both on and off Amazon take Amazon product reviews significantly into account when making their purchasing decisions. For readers, authors, and publishers alike, navigating thousands of book reviews when seeking constructive feedback can be extremely time-consuming and overwhelming. Unfortunately, some reviews are unreasonable or emotionally charged, unhelpful, or filled with false information, leading to inaccurate ratings and rankings that may not reflect reality. Our project aims to tackle this problem specifically in the online book marketplace. The objective is to present a more accurate and reasonable ratings system by filtering out these kinds of unhelpful reviews and spotlighting highly valuable reviews using Artificial Intelligence-related technology.
### Materials & Method
We will be using the Amazon review dataset released in 2018 [1] as our dataset, pick up the specific book category review dataset; furthermore, for the purposes of our project, we will select data from approximately 50 books for analysis.
#### The approaches we plan to take is shown in the architecture below:
#####	General steps
1. Load Sample Data from Amazon Review Dataset and data processing
2. Method, Model and Network 
3. Model training process
4.	Performance
#####	Data Processing[2]
1.	Pick up around 50 books that are as representative as possible
2.	Collect the useful features from Amazon book reviews
3.	Eliminate instances with missing data
4.	Detect and remove Outliers
#####	Method 
1.	VADER model [3]
2.	RoBERTa model [5]
3.	Logistic regression, Naive Bayes, or support vector machines, to classify the reviews as fake or genuine based on the features
4.	CNN (Potentially for images) [6]
5.	Computer Vision (Potentially for images) 
6.	Decision Tree
#####	Representation
Be able to target and filter out “Unreasonable” comments. We define “unreasonable” comments to be ones that fall under these categories:<br> 
1.1 Off-topic from what the book is about<br>
1.2	Poorly written, hard to understand<br>
1.3	Reviews that do not elaborate on what was good/bad (criticism is valid and necessary, but should explain reasoning)<br>
Be able to provide more accurate rating (or stars) for each candidate's books after filtering out “unreasonable” reviews.<br>
Be able to select and highlight high quality and beneficial book reviews for users.

### Future Scope
Since Amazon allows including pictures and videos in review comments, our work could be extended in the future to perform recognition of pictures or videos submitted by users and detect unrelated pictures and videos.
Furthermore, we could build a user-friendly book review web-platform. Through specific query methods such as book title, author, book ISBN and so on, users would be able to retrieve valuable book review related information to choose an appropriate book.
### Reference
1.	Amazon review dataset. https://nijianmo.github.io/amazon/index.html
2.	Sentiment classification of skewed shoppers' reviews using machine learning techniques, examining the textual features  https://onlinelibrary.wiley.com/doi/10.1002/eng2.12280
3.	Example of usage of VADER model:  https://doi.org/10.1016/j.procs.2023.10.514.
4.	Reference for VADER model: https://github.com/RajathAkshay/Sentiment-Classification-for-Product-Reviews
5.	Reference for RoBERTa model: arXiv:1907.11692
6.	Reference for CNN: 10.5591/978-1-57735-516-8/IJCAI11-210
