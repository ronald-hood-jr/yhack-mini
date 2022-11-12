import re
import pyap
import nltk
import numpy
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)
text = '''
Lorem ipsum
    225 E. John Carpenter Freeway,
    Suite 1500 Irving, Texas 75062
    Dorem sit amet
    Some economists have responded positively to Bitcoin, including 
Francois R. Velde, senior economist of the Federal Reserve in Chicago 
who described it as "an elegant solution to the problem of creating a 
digital currency." In November 2013 Richard Branson announced that 
Virgin Galactic would accept Bitcoin as payment, saying that he had invested 
in Bitcoin and found it "fascinating how a whole new global currency 
has been created", encouraging others to also invest in Bitcoin.
Other economists commenting on Bitcoin have been critical. 
Economist Paul Krugman has suggested that the structure of the currency 
incentivizes hoarding and that its value derives from the expectation that 
others will accept it as payment. Economist Larry Summers has expressed 
a "wait and see" attitude when it comes to Bitcoin. Nick Colas, a market 
strategist for ConvergEx Group, has remarked on the effect of increasing 
use of Bitcoin and its restricted supply, noting, "When incremental 
adoption meets relatively fixed supply, it should be no surprise that 
prices go up. And that’s exactly what is happening to BTC prices.
000-000-000
000-000-000
jdsk@bob.com.lol or popop@coco.com
'''


def findAddresses():
    addresses = pyap.parse(text, country='US')
    for address in addresses:
        print(address)
        print(address.as_dict())
        print('found an address')


def findOwner():
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))


def findPhones():
    reg = re.compile(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phones = re.findall(reg, text)
    for phone in phones:
        print(phone)


def findEmails():
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
    for a in match:
        print(match)


findAddresses()
findOwner()
findPhones()
findEmails()
