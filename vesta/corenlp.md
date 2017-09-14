# Stanford CoreNLP

I have set up [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/index.html) on Vesta. This
is a powerful library with a lot of advanced NLP functionality, particularly for dependency parsing, co-reference resolution, named-entity recognition, sentiment analysis, and information extraction. It is written in Java but can also be used by other languages, you can find details on interfaces [here](http://stanfordnlp.github.io/CoreNLP/other-languages.html).

I have included instructions to using some functions with a very basic Python wrapper below, but more work is necessary to get full functionality without
using Java.

# Running the CoreNLP server
The Java files for the Stanford CoreNLP server are located in
the Shared directory: `/Users/Shared/stanford-corenlp-full-2016-10-30`.

CoreNLP uses a server which can be run this directory using the
following command:
`java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer`
This runs on the default port `9000` but this can be changed and a
timeout parameter can be added, see details [here](http://stanfordnlp.github.io/CoreNLP/corenlp-server.html)

To simplify this process you can add the following alias to your `.bash_profile` and source it.

`alias corenlp='cd ~ && cd ../Shared/stanford-corenlp-full-2016-10-30 && java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer'`

This will allow you to start the server from anywhere on Vesta by typing
`corenlp` into the command line.

# Using the Python wrapper
I have included a basic Python script that [here](https://github.com/socdyn/wiki/blob/master/vesta/corenlp-demo.py) that uses the `corenlp_pywrap` package. You can run this script once the server is working and it should return a list of the named entities in the input sentence.

I have found it useful to use [screen](https://github.com/socdyn/wiki/blob/master/vesta/use_screen.md) to start the server and keep it running in the background. You can then detach from it and run the script.

Overall I have found the existing packages to be very limited in their functionality and have had to write my own wrappers to access some of functionality of CoreNLP. Please update this Wiki if you find better implementations or develop your own.

# Stanford CoreNLP and NLTK

I am aware that NLTK has the ability to call certain tools from the Stanford library. I am not sure if it has any functionality to use tools from CoreNLP. This may be a potential solution to some of these issues if somebody wants to look into it.
