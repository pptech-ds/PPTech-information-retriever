#Clean text to have only clear words to process in BM25 algo
def replace_html_accent(text):
    text1 = text.replace("&acirc;", "â")
    text2 = text1.replace("&agrave;", "à")
    text3 = text2.replace("&eacute;", "é")
    text4 = text3.replace("&ecirc;", "ê")
    text5 = text4.replace("&egrave;", "è")
    text6 = text5.replace("&euml;", "ë")
    
    return text6

#text_in = "les oeufs de la poule frais de pr&eacute;f&eacute;rence"
text_in = "comment faire des crêpes"
print(text_in)

text_out = replace_html_accent(text_in)
print(text_out)
