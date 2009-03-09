# ====================================================================
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ====================================================================

from unittest import TestCase, main
from lucene import *


class PrefixQueryTestCase(TestCase):
    """
    Unit tests ported from Java Lucene
    """

    def testPrefixQuery(self):

        directory = RAMDirectory()

        categories = ["/Computers", "/Computers/Mac", "/Computers/Windows"]
        writer = IndexWriter(directory, WhitespaceAnalyzer(), True)
        for category in categories:
            doc = Document()
            doc.add(Field("category", category,
                          Field.Store.YES, Field.Index.UN_TOKENIZED))
            writer.addDocument(doc)

        writer.close()

        query = PrefixQuery(Term("category", "/Computers"))
        searcher = IndexSearcher(directory)
        hits = searcher.search(query)
        self.assertEqual(3, hits.length(),
                         "All documents in /Computers category and below")

        query = PrefixQuery(Term("category", "/Computers/Mac"))
        hits = searcher.search(query)
        self.assertEqual(1, hits.length(), "One in /Computers/Mac")


if __name__ == "__main__":
    import sys, lucene
    lucene.initVM(lucene.CLASSPATH)
    if '-loop' in sys.argv:
        sys.argv.remove('-loop')
        while True:
            try:
                main()
            except:
                pass
    else:
         main()
