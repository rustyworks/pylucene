/* ====================================================================
 *   Copyright (c) 2004-2008 Open Source Applications Foundation
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 * ====================================================================
 */

package org.osafoundation.lucene.search;

import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.ScoreDocComparator;
import java.io.IOException;


public class PythonScoreDocComparator implements ScoreDocComparator {

    private long pythonObject;

    public PythonScoreDocComparator()
    {
    }

    public void pythonExtension(long pythonObject)
    {
        this.pythonObject = pythonObject;
    }
    public long pythonExtension()
    {
        return this.pythonObject;
    }

    public void finalize()
        throws Throwable
    {
        pythonDecRef();
    }

    public native void pythonDecRef();
    public native int compare(ScoreDoc i, ScoreDoc j);
    public native int sortType();
    public native Comparable sortValue(ScoreDoc i);
}
