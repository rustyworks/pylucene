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


class BooleanTestMixin(object):

    def getBooleanQuery(self, clauses, disableCoord):

        extra_query = TermQuery(Term("all", "extra_clause"))
        extra_clause = BooleanClause(extra_query, BooleanClause.Occur.SHOULD)
        clauses.add(extra_clause)
                                             
        return super(BooleanTestMixin, self).getBooleanQuery(clauses,
                                                             disableCoord)


class PythonQueryParserTestCase(TestCase):

    def testOverrideBooleanQuery(self):

        class TestQueryParser(BooleanTestMixin, PythonQueryParser):
            pass
        
        qp = TestQueryParser('all', StandardAnalyzer())
        q = qp.parse("foo bar")
        self.assertEquals(str(q), "all:foo all:bar all:extra_clause")


class PythonMultiFieldQueryParserTestCase(TestCase):

    def testOverrideBooleanQuery(self):

        class TestQueryParser(BooleanTestMixin, PythonMultiFieldQueryParser):
            pass

        qp = TestQueryParser(['one', 'two'], StandardAnalyzer())
        q = qp.parse("foo bar", ['one', 'two'],
                     [BooleanClause.Occur.SHOULD, BooleanClause.Occur.SHOULD],
                     StandardAnalyzer())
        self.assertEquals(str(q), "(one:foo one:bar) (two:foo two:bar)")


if __name__ == "__main__":
    import sys
    initVM(CLASSPATH)
    if '-loop' in sys.argv:
        sys.argv.remove('-loop')
        while True:
            try:
                main()
            except:
                pass
    else:
         main()
