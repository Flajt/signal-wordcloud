# Signal Wordcloud
This is a small tool to enable you the creation of a wordcloud for your signal chat<br>

## How to use?
1. Install: `wordcloud` by running `pip install worldcloud`
2. Get yourself stopwords for your language
3. Paste them in the file called stopwords.txt (just replace the old ones for now), make sure it's only **one** word per line
4. Use [this](https://github.com/carderne/signal-export) repo to get the data html and .md files
5. In **this** folder run: `python3 main.py <user-name> <path-to-.md-file> <output-file-with-type>`
<br>
If you want to get your own wordcloud in a chat use: `Me` as the name

### Known issues:
- Sometimes cryptic strings make their way into the wordcloud, my guess is that the regex to find the images needs to be improved

I just build it to play a bit around, feel free to improve it and add features if you want.