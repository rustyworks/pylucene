
import os, sys, lucene
lucene.initVM(lucene.CLASSPATH)

sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])))

from lia.indexing.VerboseIndexing import VerboseIndexing
VerboseIndexing.main(sys.argv)
