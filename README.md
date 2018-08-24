# Intelligent Lyric Generator of Different Genres

## Project Description

Welcome to visit the homepage of our intelligent lyric generator.

### Big Picture
    - The main functionality of this project is to automatically generate the lyric based on the keywords extracted from users' input sentence and the genre users choose.

### DataSet
    - We chose a raw lyric dataset from Kaggle which contains nearly 380,000 songs. We designed an algorithm to clean and split the data, part of which were used to train the model.

### Seq2Se2 Model
    - In this project, we used a improved Seq2Seq model which is similar to the model of the research paper [Chinese Poetry Generation with Planning based Neural Network](https://arxiv.org/pdf/1610.09889.pdf).
      We trained the improved Seq2Seq model by LSTM and GRU and found GRU outperformed LSTM for this certain task.

### Keyword Extraction
    - The keyword extraction algorithm [RAKE](https://github.com/ruby/rake) was used for our keyword extraction module.


## Project Structure

### src
    - data_clean.py wraps the data_cleaning algorithm.
    - keyword_extraction.py wraps the RAKE keyword extraction algorithm.
    - Model_Training file contains the src for the process of training LSTM and GRU (pop and rock).
    - Lyric_Generator file contains the src for automatically generating the lyric for rock and pop style using trained GRU model.
  
### data
    - data file contains the dataset we used for training the model including the primary dataset and the cleaned dataset.

### report
    - project report introduces the project from the view of background, related work, technical implementation, result demo, user study, future work, reference.
