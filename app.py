import streamlit as st
from pymed import PubMed
from pprint import pprint
from Bio import Entrez
Entrez.email = "anshptl21@gmail.com"
handle = Entrez.einfo() # or esearch, efetch, ...
record = Entrez.read(handle)
handle.close()


def querySearch(keywords):
  refined_search = keywords.lower()
  article_info = []
  pubmed = PubMed(tool="MyTool", email="anshptl21@gmail.com")
  results = pubmed.query(refined_search , max_results=5)
  result_list = list(results)
  output_str = ""
  if len(result_list) == 0:
    return "Try Again"
  else:
   for i, article in enumerate(result_list):
    
      article_info.insert(i, article.toDict())
      dicts = article_info[i]
      doi = dicts.get("doi")
      id = dicts.get("pubmed_id")
      if "\n" in doi:
          doi_index = doi.index("\n")
          dicts.update({"doi" : article.doi[0:doi_index]})
      if "\n" in id:
          id_index = id.index("\n")
          dicts.update({"pubmed_id" : article.pubmed_id[0:id_index]})
      dicts["link"] = "https://pubmed.ncbi.nlm.nih.gov/" + dicts.get("pubmed_id")
      output_str += f'Title: {dicts.get("title")}\n'
      output_str += f'Publication Date: {dicts.get("publication_date")}\n'
      output_str += f'PubMed Id: {dicts.get("pubmed_id")}\nJournal: {dicts.get("journal")}\nAuthors: {dicts.get("authors")}\nKeywords: "{dicts.get("keywords")}"\nAbstract: {dicts.get("abstract")}\nLink: {dicts.get("link")}\n'
  return output_str

diseases = ['Fabry Disease', 'Cystic Fibrosis', 'Hemophilia', 'Brugada Syndrome', 'Scleroderma', 'Primary biliary cholangitis', 'Alzheimer Disease', 'ALS ', 'Muscular dystrophy', 'Spinal Muscular Atrophy']
treatments = ['Nanoparticle drug delivery systems', 'Nanovaccines', 'nanoparticle-based treatments', 'Nanoparticle drugs', 'Nanoparticles for diagnosis', 'synthetic nanoparticles components']

mode = st.sidebar.selectbox('Select a research focus', ['Rare Diseases', 'Nanotechnology Treatments'])
if mode == 'Rare Diseases':
  choices = diseases
else:
  choices = treatments

search_term = st.sidebar.selectbox('Select a PubMed query term', choices)

run_query = st.sidebar.button('Learn More!')
st.text(querySearch(search_term))
#for i in diseases: 
#  querySearch(i)
#for j in treatments:
#  querySearch(j)
