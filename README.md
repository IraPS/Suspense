# Suspense
This is a program that predicts the level of suspense of a paragraph.

Before using it be sure you have downloaded

Here is the instructions on how to use it:

1. Download this git.

2. Save the novel you want to analyze in a .txt file with 'utf-8' encoding.

3. Create a folder "Corpus". Inside of it create the folder which is called exactly as the file where your novel is stored.

4. Put the file with your novel to it's folder in the "Corpus" folder.

5. Inside of the folder with your novel create three folders called exactly like this: "Original", "Syntaxed", "Mystemed"

6. Go to "prepare_corpus.py" and change the directories in lines 10 and 22.
In line 10 

7. Run "predict_suspense_1.py". It will ask you to type the title of the novel. Type it exactly as it is without adding '.txt' or anything else.

8. After that you need to move files from the "out" folder of RU Syntax parser to the "Syntaxed" folder of your novel folder.

9. Run "predict_suspense_2.py". You will get your predictions now!


