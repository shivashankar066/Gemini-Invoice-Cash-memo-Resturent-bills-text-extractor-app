### Multi-Language invoice/Cash memo/ Resturent bills extractor Gemini LLM model Application.
#### Introduction:
 This application will help to extract any required information from invoices or cash memos or any type 
 of Resturent bills. 
 
 It will take Invoices as image and extract the our required informations like date, Name, address etc..
 
### How to build:

Step 1 : Create virtual environment in your local machine and can use pycharm IDE.

Step 2 : import all required libraries in requirements.txt file run it as pip install -r requirements.txt.

Step 3 : Create .env file and load your GOOGLE_API_KEY and load it in app.py file using load_dotenv.
            (https://makersuite.google.com/app/apikey)

Step 4 : Create Gemini OpenAI LLM model by adding "gemini-pro-vision" model.

Step 5 : set the Prompt template. 

Step 6 : Write function to convert image into Bytes.

Step 7 : Initialise the Streamlit and run the app.py file using command Streamlit run app.py.

Step 8 : upload any invoice and provide the prompt input and it will give the response as our required output.