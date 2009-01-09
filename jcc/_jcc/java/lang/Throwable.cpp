/*
 *   Copyright (c) 2007-2008 Open Source Applications Foundation
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
 */

#include <jni.h>
#include "JCCEnv.h"
#include "java/lang/Object.h"
#include "java/lang/Class.h"
#include "java/lang/String.h"
#include "java/lang/Throwable.h"

namespace java {
    namespace lang {

        enum {
            mid_printStackTrace,
            mid_getMessage,
            max_mid
        };

        Class *Throwable::class$ = NULL;
        jmethodID *Throwable::_mids = NULL;

        jclass Throwable::initializeClass()
        {
            if (!class$)
            {
                jclass cls = env->findClass("java/lang/Throwable");

                _mids = new jmethodID[max_mid];
                _mids[mid_printStackTrace] = 
                    env->getMethodID(cls, "printStackTrace",
                                     "()V");
                _mids[mid_getMessage] = 
                    env->getMethodID(cls, "getMessage",
                                     "()Ljava/lang/String;");

                class$ = (Class *) new JObject(cls);
            }

            return (jclass) class$->this$;
        }

        void Throwable::printStackTrace() const
        {
            env->callVoidMethod(this$, _mids[mid_printStackTrace]);
        }
        
        String Throwable::getMessage() const
        {
            return String(env->callObjectMethod(this$, _mids[mid_getMessage]));
        }
    }
}


#include "structmember.h"
#include "functions.h"
#include "macros.h"

namespace java {
    namespace lang {

        static PyObject *t_Throwable_printStackTrace(t_Throwable *self);

        static PyMethodDef t_Throwable__methods_[] = {
            DECLARE_METHOD(t_Throwable, printStackTrace, METH_NOARGS),
            { NULL, NULL, 0, NULL }
        };

        DECLARE_TYPE(Throwable, t_Throwable, Object, java::lang::Throwable,
                     abstract_init, 0, 0, 0, 0, 0);

        static PyObject *t_Throwable_printStackTrace(t_Throwable *self)
        {
            OBJ_CALL(self->object.printStackTrace());
            Py_RETURN_NONE;
        }
    }
}
