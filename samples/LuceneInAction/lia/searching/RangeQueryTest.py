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

from lia.common.LiaTestCase import LiaTestCase

from lucene import Term, IndexSearcher, RangeQuery


class RangeQueryTest(LiaTestCase):

    def setUp(self):

        super(RangeQueryTest, self).setUp()

        self.begin = Term("pubmonth", "198805")

        # pub date of TTC was October 1988
        self.end = Term("pubmonth", "198810")

    def testInclusive(self):

        query = RangeQuery(self.begin, self.end, True)
        searcher = IndexSearcher(self.directory)

        hits = searcher.search(query)
        self.assertEqual(1, hits.length(), "tao")

    def testExclusive(self):

        query = RangeQuery(self.begin, self.end, False)
        searcher = IndexSearcher(self.directory)

        hits = searcher.search(query)
        self.assertEqual(0, hits.length(), "there is no tao")