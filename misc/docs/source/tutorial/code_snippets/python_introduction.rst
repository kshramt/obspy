=====================================
Python Introduction for Seismologists
=====================================

Here we want to give a small, incomplete introduction to the Python_
programming language, with links to useful packages and further resources. The
key features are explained via the following Python script:

.. code-block:: python
   :linenos:

   #!/usr/bin/env python
   import glob
   from obspy.core import read
   
   for file in glob.glob('*.z'):
       st = read(file)
       tr = st[0]
       msg = "%s %s %f %f" % (tr.stats.station, str(tr.stats.starttime),
                              tr.data.mean(), tr.data.std())
       print msg

Description of each line of the example above:

    *Line 1*
       Shebang, specifying the location of the Python interpreter for Unix-like
       operating systems.
    *Lines 2-3*
       Import modules/libraries/packages in the current namespace. The :mod:`glob`
       module, which allows wildcard matching on filenames, is imported here. All
       functions inside this module can be accessed via ``glob.function()``
       afterwards, such as :func:`glob.glob()`.
       Furthermore, a single function :func:`~obspy.core.stream.read()` from the
       :mod:`obspy.core` module is imported, which is used to read various
       different seismogram file formats.
    *Line 5*
       Starts a ``for``-loop using the :func:`~glob.glob` function of the module
       :mod:`glob` on all files ending with ``'.z'``.
    
       .. note::
       
          The length of all loops in Python is determined by the indentation level.
          Do not mix spaces and tabs in your program code for indentation, this
          produces bugs that are not easy to identify.
    
    *Line 6*
       Uses the :func:`~obspy.core.stream.read()` function from the
       :mod:`obspy.core` module to read in the seismogram to a
       :class:`~obspy.core.stream.Stream` object named ``st``.
    *Line 7*
       Assigns the first :class:`~obspy.core.trace.Trace` object of the
       list-like :class:`~obspy.core.stream.Stream` object to the variable ``tr``.
    *Line 8-9*
       A Python counterpart for the well-known C function ``sprintf`` is the ``%``
       operator acting on a format string. Here we print the header attributes
       ``station`` and ``starttime`` as well as the return value of the methods
       :meth:`~numpy.mean` and :meth:`~numpy.std` acting on the data sub-object
       of the :class:`~obspy.core.trace.Trace` (which are of type
       :class:`numpy.ndarray`).
    *Line 10*
       Prints content of variable ``msg`` to the screen.

As Python_ is an interpreter language, we recommend to use the IPython_ shell
for rapid development and trying things out. It supports tab completion,
history expansion and various other features. E.g.
type ``help(glob.glob)`` or ``glob.glob?`` to see the help of the
:func:`~glob.glob` function (the module must be imported beforehand).

.. rubric:: Further Resources

* http://docs.python.org/tutorial/
    Official Python tutorial.
* http://docs.python.org/library/index.html
    Python library reference
* http://software-carpentry.org/4_0/
    Very instructive video lectures on various computer related topics. A good
    starting point for learning Python and Version Control with Subversion.
* http://ipython.scipy.org/moin
    An enhanced interactive Python shell.
* http://docs.scipy.org
   NumPy and SciPy are the matrix based computation modules of Python. The
   allow fast array manipulation (functions in C). NumPy and SciPy provide
   access to fft, lapack, atlas or blas. That is svd, eigenvalues...
   ObsPy uses the numpy.ndarrays for storing the data (e.g. tr.data).
* http://matplotlib.sourceforge.net/gallery.html
   matplotlib is the 2-D plotting package for Python. The gallery is the market
   place which allows you to go shopping for all kind of figures. The source
   code for each figure is linked. Note matplotlib has even its own latex
   renderer.
* http://matplotlib.org/basemap/
   Package plotting 2D data on maps in Python. Similar to GMT.
* http://trac.osgeo.org/gdal/wiki/GdalOgrInPython
   Package which allows to directly read a GeoTiff which then can be plotted
   with the basemap toolkit.
* http://www.tramy.us/numpybook.pdf
   The official NumPy reference.
* http://openbook.galileocomputing.de/python/
   An German Python book (free).
* http://svn.geophysik.uni-muenchen.de/trac/mtspecpy
   Multitaper spectrum bindings for Python


.. _Python: http://www.python.org
.. _IPython: http://ipython.org
