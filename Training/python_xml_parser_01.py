import xml.sax
class UserHandler( xml.sax.ContentHandler ):
    # Call when an element starts
    def startElement(self, tag, attributes):
        print('startElement called for ',tag)
    # Call when a character is read
    def characters(self, data):
        print('characters called for ',data)
    # Call when an elements ends
    def endElement(self, tag):
        print('endElement called for ',tag)
Handler = UserHandler()
# create an XMLReader
parser = xml.sax.make_parser()
# override the default ContextHandler
parser.setContentHandler( Handler )
parser.parse("data1.xml")