from text_blob_analysis import *

politicians = ["Theresa May", "Jeremy Corbyn", "Boris Johnson", "Nicola Sturgeon", "Sadiq Khan", "Philip Hammond", "John Bercow", "Michel Barnier", "Arlene Foster"]
number = 100
includeRetweets = True

print ""
for politician in politicians:
    [positive, neutral, negative, ratio] = get_approval_ratio(politician, number, includeRetweets)
    print "    Person:", politician
    print "Popularity: " + str(round(ratio, 2)) + "%"
    print ""

