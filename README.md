# CS5100Project
## Amazon Book Reviews Sentiment Analysis
### Wanyi Li, Wenqin Wu, Feiquan Liu, Yilei Bai
### Objective 
Most customers shopping both on and off Amazon take Amazon product reviews significantly into account when making their purchasing decisions. For readers, authors, and publishers alike, navigating thousands of book reviews when seeking constructive feedback can be extremely time-consuming and overwhelming. Unfortunately, some reviews are unreasonable or emotionally charged, unhelpful, or filled with false information, leading to inaccurate ratings and rankings that may not reflect reality. Our project aims to tackle this problem specifically in the online book marketplace. The objective is to present a more accurate and reasonable ratings system by filtering out these kinds of unhelpful reviews and spotlighting highly valuable reviews using Artificial Intelligence-related technology.
### Materials & Method
We will be using the Amazon review dataset released in 2018 [1] as our dataset, pick up the specific book category review dataset; furthermore, for the purposes of our project, we will select data from approximately 50 books for analysis.
 The approaches we plan to take is shown in the architecture below:
	General steps
	Load Sample Data from Amazon Review Dataset and data processing
	Method, Model and Network 
	Model training process
	Performance
	Data Processing[2]
	Pick up around 50 books that are as representative as possible
	Collect the useful features from Amazon book reviews
	Eliminate instances with missing data
	Detect and remove Outliers
	Method 
	VADER model [3]
	RoBERTa model [5]
	Logistic regression, Naive Bayes, or support vector machines, to classify the reviews as fake or genuine based on the features
	CNN (Potentially for images) [6]
	Computer Vision (Potentially for images) 
	Decision Tree
	Representation
o	Be able to target and filter out “Unreasonable” comments. We define “unreasonable” comments to be ones that fall under these categories:
	Off-topic from what the book is about
	Poorly written, hard to understand
	Reviews that do not elaborate on what was good/bad (criticism is valid and necessary, but should explain reasoning)
o	Be able to provide more accurate rating (or stars) for each candidate's books after filtering out “unreasonable” reviews.
o	Be able to select and highlight high quality and beneficial book reviews for users

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
