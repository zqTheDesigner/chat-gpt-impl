# chat-gpt-impl

Implementation of chat gpt with Jupyter notebook.
$20 per month is too expensive!

# Set up venv

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Create .env

```sh
touch .env
echo OPENAI_API_KEY >>> .env
```

Then copy your opne ai api key to .env file

# services.py

All api calling will happen in this file. Will slowly add in more and more functions

# How to use

Each jupiter notebook will do one very specific task, there will only be one required input field, the rest of fields can just run as it is. However, feel free to modify the prompts and change the behavior.
