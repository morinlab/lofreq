from distutils.core import setup, Extension
import os

# see also http://docs.python.org/distutils/setupscript.html


DEBUG = False
#DEBUG = True

DEFINE_MACROS = []
EXTRA_COMPILE_ARGS = []
if not DEBUG:
    DEFINE_MACROS.append(('NDEBUG', '1'))
    EXTRA_COMPILE_ARGS.append('-O3')
    EXTRA_COMPILE_ARGS.append('-funroll-loops')
else:
    EXTRA_COMPILE_ARGS.append('-Wall')
    EXTRA_COMPILE_ARGS.append('-Wextra')
    EXTRA_COMPILE_ARGS.append('-pedantic')
    EXTRA_COMPILE_ARGS.append('-ansi')
    EXTRA_COMPILE_ARGS.append('-O0')
    EXTRA_COMPILE_ARGS.append('-g')
    pass



# C extensions
#
#EXT_PATH = os.path.join("src", "ext")
EXT_PATH = "lofreq_ext"
EXT_SOURCES = [os.path.join(EXT_PATH, f)
               for f in ["lofreq_ext.c",
                         os.path.join("cdflib90", "dcdflib.c"),
                         os.path.join("cdflib90", "ipmpar.c"),
                         ]
               ]

extension = Extension("lofreq_ext",
                      EXT_SOURCES,
                      include_dirs=[os.path.join(EXT_PATH, 'cdflib90')],
                      define_macros=DEFINE_MACROS,
                      extra_compile_args=EXTRA_COMPILE_ARGS,
                      depends=[os.path.join(EXT_PATH, "cdflib90", "cdflib.h")],
                      #library_dirs=[],
                      #libraries=[],
                      )


# where modules reside:
package_dir = {'': 'lofreq'}
    
setup(
    name = "snpcaller_ext",
    version = "0.1",
    description="Low frequency variant caller",
    author="Andreas Wilm",
    author_email='wilma@gis.a-star.edu.sg',
    # long_description = """FIXME.""" 
    url='http://www.gis.a-star.edu.sg/', # FIXME
    # classifiers=[],
    
    scripts = ["lofreq_snpcaller.py"],
    #py_modules = ["em", "qual", "samtools_helper", "utils"],
    packages=['lofreq'],
    ext_modules = [extension]
    )

