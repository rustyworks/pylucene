from lucene import \
    StandardAnalyzer, RAMDirectory, Document, Field, \
    IndexWriter, IndexReader, TermPositionVector, initVM, CLASSPATH

if __name__ == '__main__':
    initVM(CLASSPATH)

directory = RAMDirectory()
iwriter = IndexWriter(directory, StandardAnalyzer(), True)
ts = ["this bernhard is the text to be index text",
      "this claudia is the text to be index"]
for t in ts:
    doc = Document()
    doc.add(Field("fieldname", t,
                  Field.Store.YES, Field.Index.TOKENIZED,
                  Field.TermVector.WITH_POSITIONS_OFFSETS))
    iwriter.addDocument(doc)
iwriter.optimize()
iwriter.close()

ireader = IndexReader.open(directory)
tpv = TermPositionVector.cast_(ireader.getTermFreqVector(0, 'fieldname'))

for (t,f,i) in zip(tpv.getTerms(),tpv.getTermFrequencies(),xrange(100000)):
    print 'term %s' % t
    print '  freq: %i' % f
    try:
        print '  pos: ' + str([p for p in tpv.getTermPositions(i)])
    except:
        print '  no pos'
    try:
        print '  off: ' + \
              str(["%i-%i" % (o.getStartOffset(), o.getEndOffset())
                   for o in tpv.getOffsets(i)])
    except:
        print '  no offsets'
