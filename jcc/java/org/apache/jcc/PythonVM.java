/* ====================================================================
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

package org.apache.jcc;


public class PythonVM {
    static protected PythonVM vm;

    static {
        System.loadLibrary("jcc");
    }

    static public PythonVM start(String programName, String[] args)
    {
        if (vm == null)
        {
            vm = new PythonVM();
            vm.init(programName, args);
        }

        return vm;
    }

    static public PythonVM start(String programName)
    {
        return start(programName, null);
    }

    static public PythonVM get()
    {
        return vm;
    }

    protected PythonVM()
    {
    }

    protected native void init(String programName, String[] args);

    public native Object instantiate(String moduleName, String className)
        throws PythonException;

    public native int acquireThreadState();
    public native int releaseThreadState();
}