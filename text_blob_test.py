from text_blob_analysis import *

politicians = ["Theresa May", "Jeremy Corbyn", "Boris Johnson", "Nicola Sturgeon", "Sadiq Khan", "Philip Hammond", "John Bercow", "Michel Barnier"]

print ""
for politician in politicians:
    [positive, neutral, negative, ratio] = get_approval_ratio(politician, 100)
    print "Person analysed:  ", politician
    print "Ratio (1=neutral): " + str(round(ratio, 2)) + "%"
    print ""
