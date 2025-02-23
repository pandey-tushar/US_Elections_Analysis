# Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.

# ~~~~~~~~~~~~~~~~~~~~~ Importing required packages -
 
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import webbrowser

# ~~~~~~~~~~~~~~~~~~~~~ Different User pages and respective functions - 

# ~~~~~~~~~~ Home Page -

def home_page():
    # Setting the title - 
    st.title("TAMIDS Data Science Competition")
    
    # Desription -
    st.write("""
             The 2021 TAMIDS Data Science Competition concerns the role of money in US Presidential Elections. The key
             idea of democracy is that every citizen should have input, via a vote, as to who is elected. Enormous amounts of
             money are expended by political campaigns to engage with voters, and so fundraising has become a major
             activity by candidates and other actors. Donations are an additional way for constituents to get involved in political
             races. Unions and corporations are able to donate through Political Action Committees (PACs), while the
             2010 Citizens United ruling by the US Supreme Court has removed caps on corporate donations via PACs and
             allowed campaign ads to be published or broadcast anonymously.  
             """)
    
    # Problem Statement - 
    st.write("""
             ## Problem Statement
             Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Data Collection and Pre-processing -
    st.write(" ")
    st.write("""
             ## Data Collection and Pre-processing
             Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Overview - 
    st.write("""
             ## Overview of Approach 
             Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Navigation - 
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")

# ~~~~~~~~~~ Expenditure Analysis Page -

def get_party_exp_graph(party, category):
    # Getting the Graph - 
    HtmlFile = open(f"Expenditure_Demographics_Analysis/Graphs/{party}_{category}.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=500)

def get_graph_inference(party, category):
    
    # Understanding Democratics Graph - 
    if party == "Democratics":
        
        # All expenses Graph -
        if category == "All Expenses":
            st.write("""
                     ### **Plot Overview: Democratics - All Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Communiations Expenses Graph -
        elif category == "Communiations Expenses":
            st.write("""
                     ### **Plot Overview: Democratics - Communiations Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Advertisement Expenses Graph -
        elif category == "Advertisement Expenses":
            st.write("""
                     ### **Plot Overview: Democratics - Advertisement Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Logistics Expenses Graph -
        elif category == "Logistics Expenses":
            st.write("""
                     ### **Plot Overview: Democratics - Logistics Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Others Graph -
        elif category == "Others":
            st.write("""
                     ### **Plot Overview: Democratics - Others**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
    
    # Understanding Republicans Graph - 
    elif party == "Republicans":
        
        # All expenses Graph -
        if category == "All Expenses":
            st.write("""
                     ### **Plot Overview: Republicans - All Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Communiations Expenses Graph -
        elif category == "Communiations Expenses":
            st.write("""
                     ### **Plot Overview: Republicans - Communiations Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Advertisement Expenses Graph -
        elif category == "Advertisement Expenses":
            st.write("""
                     ### **Plot Overview: Republicans - Advertisement Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Logistics Expenses Graph -
        elif category == "Logistics Expenses":
            st.write("""
                     ### **Plot Overview: Republicans - Logistics Expenses**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)
        
        # Others Graph -
        elif category == "Others":
            st.write("""
                     ### **Plot Overview: Republicans - Others**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)

def get_other_graph():
    # Getting the Graph - 
    HtmlFile = open("Expenditure_Demographics_Analysis/Graphs/Some_Graph.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=1200)
    
def expenditure_analysis():
    # Setting the title - 
    st.title("Expenditure and Demographics Analysis!")
    
    # Desription -
    st.write("""
             The key idea of democracy is that every citizen should have input, via a vote, as to who is elected. Enormous amounts of
             money are expended by political campaigns to engage with voters, and so fundraising has become a major
             activity by candidates and other actors. The money is spent for various purposes.
             """)
    
    st.write("")
    
     # Getting the initial image -
    col1, col2, col3 = st.beta_columns((1,2.5,1))
    image = Image.open('Expenditure_Demographics_Analysis/Data_Clean_Preprocess/Initial_Overview.png')
    col2.image(image)
    
    # Showing inital analysis -
    st.write("""
               **EXPLAIN ABOVE GRAPH. INSIGHTS!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
               """)
    
    st.write(" ")
    # State-wise graphs -
    st.write("""
             **TRANSITION INTO NEXT GRAPHS. BRIEF INTRODUCTION.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    st.write(" ")
    col1, col2 = st.beta_columns((1,1))
    # Getting party from the user -
    party_selected = col1.selectbox("Select Party", ['Democratics', 'Republicans'])
    
    # Getting expenditure from the user - 
    expenditure_category_selected = col2.selectbox("Select Expenditure", 
                                                   ["All Expenses", "Communiations Expenses", "Advertisement Expenses",
                                                    "Logistics Expenses", "Others"])
    
    # Getting the graph - 
    get_party_exp_graph(party_selected, expenditure_category_selected)
    
    # Geting the sponding explanation - 
    get_graph_inference(party_selected, expenditure_category_selected)
    
    # DIFFERENCE PLOT -
    st.info("Need to insert diff plots")
    st.write("---")
    
    # Entering the final plot of Tushar -
    st.write("""
             ### Some Title
             
             **Explain how to read the graph, how it can help.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Getting the graph - 
    get_other_graph()
    
    # Getting inference -
    st.write("")
    st.write("""
             ### **Plot Overview: **
            
            **Some intersting insight!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
            
            Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
            Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
            Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
            """)

# ~~~~~~~~~~ Industry Donations Analysis Page -

def get_year_wise_graph():
    # Getting the Graph - 
    HtmlFile = open("Graphs/swarnabha_yearwise_company_expenditure.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=450)

def get_state_wise_graph():
    # Getting the Graph - 
    HtmlFile = open("Graphs/swarnabha_state_company.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=450)
    
def industry_donations_analysis():
    # Setting the title - 
    st.title("Industry Donation Analysis")
    
    # Desription -
    st.write("""
             **Some background thinking. Initial thought process of going into this analysis.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
    st.write("""
             ### Some title 
             
             **Some intro into the grpahs. Why we are analyzing it that way.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
             
    # Getting the year wise graph - 
    get_year_wise_graph()
    
    # Inference/Result/Analysis (Insights)
    st.write("""
             ### Inference/Result/Analysis 
             
             **Interesting insights into the grphs** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
             * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
             Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
             Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
             Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
             Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
             Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
             Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     
             """)
    
    # State wise analysis -
    # Desription -
    st.write("""
             **Some background thinking. Reason for thinking in this direction!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
    
    # Getting the state wise graph - 
    get_state_wise_graph()
    
    # Getting inference -
    st.write("")
    st.write("""
             ### **Plot Overview: **
            
            **Some intersting insight!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
            
            Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
            Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
            Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
            """)
            

# ~~~~~~~~~~ Network Analysis Page -

def network_analysis():
    # Setting the title - 
    st.title("Network Analysis")
    
    # Desription -
    st.write("""
             **Explain how to read the graph, how it can help.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
    st.write("""
             ### Inference/Result/Analysis 
             
             **Some great inference or anything that helps!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
    st.write(" ")
    st.write("""
             You can go to the network analysis by clicking the button. Below is a snapshot of the network analysis.
             """)
    
    # To access the network analysis, press the button below - 
    st.write("")
    col1, col2, col3 = st.beta_columns((1,1,1))
    # link = '[Network Analysis](https://ritesh-suhag.github.io./)'
    # col2.markdown(link, unsafe_allow_html=True)
    url = 'https://ritesh-suhag.github.io./'
    if col2.button("Go to the Network Analysis"):
        webbrowser.open_new_tab(url)
    
    st.write(" ")
    # Setting the image - 
    image = Image.open('Images/Network_Analysis.png')
    
    # Setting the image width -
    st.image(image, use_column_width=True)
    
# ~~~~~~~~~~ Others Page -

def authors():
    # Setting the title - 
    st.title("About the Authors")
    st.write(" ")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/ritesh.png')
    
    # Setting the image width -
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Ritesh Singh Suhag")
    
    # About section - 
    col3.write("""
               Aspiring data scientist focused on executing data-driven solutions. Experienced at creating predictive models and analyzing raw data 
               to deliver insights and implement action-oriented solutions to complex business problems.  
               
               * **University:** Texas A&M University (Mays Business School)
               * **Degree:** MS in Management Information Systems (May 2021)
               * **Email:** ritesh_10@tamu.edu
               * **LinkedIn:** [linkedin.com/in/ritesh-singh-suhag/](https://www.linkedin.com/in/ritesh-singh-suhag/)
               * **Github:** [github.com/ritesh-suhag](https://www.github.com/ritesh-suhag)
               """)
    st.write(" ")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/tushar.png')
    
    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Tushar Pandey")
    
    # About section - 
    col3.write("""
               Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque.     
               
               * **University:** Texas A&M University (Department of Mathematics)
               * **Degree:** PhD Student (Maths n shitz) 
               * **Email:** tusharp@tamu.edu
               * **LinkedIn:** [linkedin.com/in/tushar-pandey1612/](https://www.linkedin.com/in/tushar-pandey1612/)
               * **Github:** [github.com/ritesh-suhag](https://www.github.com/ritesh-suhag)
               """)
    st.write("")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/sambandh.png')
    
    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Sambandh Dhal")
    
    # About section - 
    col3.write("""
               Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque.   
               
               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering) 
               * **Email:** sambandh@tamu.edu
               * **LinkedIn:** [linkedin.com/in/sambandh-dhal9163/](https://www.linkedin.com/in/sambandh-dhal9163/)
               * **Github:** [github.com/ritesh-suhag](https://www.github.com/ritesh-suhag)
               """)
    st.write("")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/swarnabha.png')
    
    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Swaranbha Roy")
    
    # About section - 
    col3.write("""
               Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque.     
               
               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering) 
               * **Email:** swarnabha7@tamu.edu
               * **LinkedIn:** [linkedin.com/in/swarnabha-roy-53a588a4/](https://www.linkedin.com/in/swarnabha-roy-53a588a4/)
               * **Github:** [github.com/ritesh-suhag](https://www.github.com/ritesh-suhag)
               """)
    st.write("")

# ~~~~~~~~~~~~~~~~~~~~~ Main application design -

st.set_page_config(layout='wide', page_title = 'US Elections')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Setting the image - 
image = Image.open('Images/image.png')

# Setting the image width -
st.image(image, use_column_width=True)

# Sidebar navigation for users -
st.sidebar.header('Navigation tab -')
navigation_tab = st.sidebar.selectbox('Choose a tab', ('Home-Page', 'Expenditure Analysis', 'Industry Donations Analysis', 'Network Analysis', 'About the Authors'))

# Displaying pages according to the selection -

# Home page -
if navigation_tab == 'Home-Page':
    home_page()

# First page -
elif navigation_tab == 'Expenditure Analysis':
    expenditure_analysis()

# Second page -
elif navigation_tab == 'Industry Donations Analysis':
    industry_donations_analysis()

# Third Page -
elif navigation_tab == 'Network Analysis':
    network_analysis()

# About Page - 
elif navigation_tab == 'About the Authors':
    authors()
