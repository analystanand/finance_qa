from transformers import pipeline
nlp = pipeline("question-answering")

def get_answers(context,question):
    result = nlp(question=question, context=context,topk=1)
    return result
if __name__ == '__main__':
    context = r"""Peloton has been one of the great Covid-19-era success stories. Demand is soaring for the company’s connected bikes, with gyms still shut down in many parts of the country, and shareholders are reaping the benefits.
                  Just how big a benefit will become clear this week—the company is due to report earnings on Thursday for the fiscal fourth quarter ended June 30. 
                  Expectations are sky high: Peloton Interactive (ticker: PTON) shares have rallied 140% since it last reported earnings in early May and more than tripled year to date. 
                  Before the market selloff late last week, the stock had rallied 37% over six trading days. 
                  Peloton bulls sniff the potential for the kind huge outperformance that Zoom Video Communications (ZM) reported last week (see Tech Trader), and they have bid up the stock accordingly.
                  When Peloton reported third-quarter results, it projected fiscal fourth-quarter revenue of $500 million to $520 million, up 128% at the midpoint of the range, with adjusted Ebitda (earnings before interest, taxes, depreciation, and amortization) of $55 million to $65 million. 
                  Full-year guidance calls for revenue of $1.72 billion to $1.74 billion, with $30 million to $40 million of adjusted Ebitda. However, Wall Street clearly sees guidance as far too low; the consensus revenue forecast is $574.6 million with a projected profit of nine cents a share.`.
    """
    question = "What is projected revenue of Peloton in fourth-quarter?"
    result = get_answers(context,question)

    print(result)