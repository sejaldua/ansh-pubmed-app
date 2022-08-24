import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import streamlit as st
import requests
from annotated_text import annotated_text, annotation
from annotated_text import annotated_text
from pymed import PubMed
from pprint import pprint
from Bio import Entrez
Entrez.email = "sejaldua@gmail.com"
handle = Entrez.einfo() # or esearch, efetch, ...
record = Entrez.read(handle)
handle.close()



def querySearch(keywords):
  refined_search = keywords.lower()
  article_info = []
  pubmed = PubMed(tool="MyTool", email="sejaldua@gmail.com")
  results = pubmed.query(refined_search , max_results=5)
  result_list = list(results)
  output_str = ""
  if len(result_list) == 0:
    zero_results = "Try Again"
    st.write(zero_results)
    return None
  else:
   for i, article in enumerate(result_list):
    
      article_info.insert(i, article.toDict())
      dicts = article_info[i]
      doi = dicts.get("doi")
      id = dicts.get("pubmed_id")
      if doi != None:
        if "\n" in doi:
            doi_index = doi.index("\n")
            dicts.update({"doi" : article.doi[0:doi_index]})
      if id != None:
        if "\n" in id:
            id_index = id.index("\n")
            dicts.update({"pubmed_id" : article.pubmed_id[0:id_index]})
      elif id == None:
          dicts.update({"pubmed_id" : "None"})
      dicts["link"] = "https://pubmed.ncbi.nlm.nih.gov/" + dicts.get("pubmed_id")
      st.write(f'Title: {dicts.get("title")}\nPublication Date: {dicts.get("publication_date")}\nPubMed Id: {dicts.get("pubmed_id")}\nJournal: {dicts.get("journal")}\nAuthors: {dicts.get("authors")}\nKeywords: "{dicts.get("keywords")}"\nAbstract: {dicts.get("abstract")}\nLink: {dicts.get("link")}\n')
  return None

diseases = ['Fabry Disease', 'Cystic Fibrosis', 'Hemophilia', 'Brugada Syndrome', 'Scleroderma', 'Primary biliary cholangitis', 'Alzheimer Disease', 'ALS ', 'Muscular dystrophy', 'Spinal Muscular Atrophy']
treatments = ['Nanoparticle drug delivery systems', 'Nanovaccines', 'nanoparticle-based treatments', 'Nanoparticle drugs', 'Nanoparticles for diagnosis', 'synthetic nanoparticles components']

mode = st.sidebar.selectbox('Select a research focus', ['Rare Diseases', 'Nanotechnology Treatments'])
if mode == 'Rare Diseases':
    choices = diseases
else:
  choices = treatments

search_term = st.sidebar.selectbox('Select a PubMed query term', choices)
run_query = st.sidebar.button('Learn More!')

if run_query == True:
  try:
    querySearch(search_term)
  except Exception as e:
    requests.get(link, headers = {'User-agent': 'your bot 0.1'})
  else:
    results = querySearch(search_term)
    st.write(results)
    index = results.find(search_term)
    annotated_text(
      (results[index], "search-term", "#8ef"),
    )

#for i in diseases: 
#  querySearch(i)
#for j in treatments:
#  querySearch(j)
