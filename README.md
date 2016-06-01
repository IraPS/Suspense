# Suspense
This is a program that predicts the level of suspense of a paragraph.

For using it be sure that:

1. You use Python 3

2. You have downloaded Mystem (https://tech.yandex.ru/mystem/)

3. You have dowloaded RU Syntax parser and followed the instructions (http://web-corpora.net/wsgi3/ru-syntax/)

4. You have installed following packages: re, os, pymystem3, numpy, copy, nltk, sklearn, pickle, sknn (which is http://scikit-neuralnetwork.readthedocs.io/) 



Here is the instructions on how to use it:

1. Download this git. Put your "mystem" file in the same directory with the files of this git.

2. Save the novel you want to analyze in a .txt file with 'utf-8' encoding.

3. Create a folder "Corpus". Inside of it create the folder which is called exactly as the file where your novel is stored.

4. Put the file with your novel to it's folder in the "Corpus" folder.

5. Inside of the folder with your novel create three folders called exactly like this: "Original", "Syntaxed", "Mystemed"

6. Go to "prepare_corpus.py" and change the directories in line 11. You have to change the directory where you store the RU Syntax parser's files. 

7. Run "predict_suspense_1.py". It will ask you to type the title of the novel. Type it exactly as it is without adding '.txt' or anything else.

8. After that you need to move files from the "out" folder of RU Syntax parser to the "Syntaxed" folder of your novel folder.

9. Run "predict_suspense_2.py". You will get your predictions now!


