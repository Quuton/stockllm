# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import config
import interface
import initializer
def main():
    try:
        import secret
    except:
        print("secret.py not found! API Keys are stored there, please create the file.")
        exit()
    
    if (config.INITIALIZE_ON_RUN):
        initializer.run()
    
    gradio_app = interface.initialize()
    gradio_app.launch(share = config.GRADIO_PUBLIC)




if __name__ == "__main__":
    main()