#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyring
Version  : 21.1.0
Release  : 77
URL      : https://files.pythonhosted.org/packages/7e/70/399b955e814380568c1f2e98145d37f0467b79531766b687bc27eb873a0a/keyring-21.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/70/399b955e814380568c1f2e98145d37f0467b79531766b687bc27eb873a0a/keyring-21.1.0.tar.gz
Summary  : Store and access your passwords safely.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: keyring-bin = %{version}-%{release}
Requires: keyring-license = %{version}-%{release}
Requires: keyring-python = %{version}-%{release}
Requires: keyring-python3 = %{version}-%{release}
Requires: importlib_metadata
Requires: jeepney
Requires: secretstorage
BuildRequires : buildreq-distutils3
BuildRequires : jeepney
BuildRequires : secretstorage
BuildRequires : setuptools
BuildRequires : setuptools-python
BuildRequires : setuptools_scm-python

%description
.. image:: https://img.shields.io/pypi/v/keyring.svg
   :target: https://pypi.org/project/keyring

.. image:: https://img.shields.io/pypi/pyversions/keyring.svg

.. image:: https://img.shields.io/travis/jaraco/keyring/master.svg
   :target: https://travis-ci.org/jaraco/keyring

.. image:: https://dev.azure.com/jaraco/skeleton/_apis/build/status/jaraco.skeleton?branchName=master
   :target: https://dev.azure.com/jaraco/skeleton/_build/latest?definitionId=1&branchName=master

.. image:: https://img.shields.io/travis/jaraco/skeleton/master.svg
   :target: https://travis-ci.org/jaraco/skeleton

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://img.shields.io/appveyor/ci/jaraco/keyring/master.svg
   :target: https://ci.appveyor.com/project/jaraco/keyring/branch/master

.. image:: https://readthedocs.org/projects/keyring/badge/?version=latest
   :target: https://keyring.readthedocs.io/en/latest/?badge=latest

.. image:: https://tidelift.com/badges/package/pypi/keyring
   :target: https://tidelift.com/subscription/pkg/pypi-keyring?utm_source=pypi-keyring&utm_medium=readme

=======================================
Installing and Using Python Keyring Lib
=======================================

.. contents:: **Table of Contents**

---------------------------
What is Python keyring lib?
---------------------------

The Python keyring lib provides an easy way to access the system keyring service
from python. It can be used in any application that needs safe password storage.

The keyring library is licensed under both the `MIT license
<http://opensource.org/licenses/MIT>`_ and the PSF license.

These recommended keyring backends are supported by the Python keyring lib:

* macOS `Keychain
  <https://en.wikipedia.org/wiki/Keychain_%28software%29>`_
* Freedesktop `Secret Service
  <http://standards.freedesktop.org/secret-service/>`_ supports many DE including
  GNOME (requires `secretstorage <https://pypi.python.org/pypi/secretstorage>`_)
* KDE4 & KDE5 `KWallet <https://en.wikipedia.org/wiki/KWallet>`_
  (requires `dbus <https://pypi.python.org/pypi/dbus-python>`_)
* `Windows Credential Locker
  <https://docs.microsoft.com/en-us/windows/uwp/security/credential-locker>`_

Other keyring implementations are available through `Third-Party Backends`_.

-------------------------
Installation Instructions
-------------------------

Install from Index
==================

Install using your favorite installer. For example:

    $ pip install keyring

Linux
-----

On Linux, the KWallet backend relies on dbus-python_, which does not always
install correctly when using pip (compilation is needed). So we recommend
that dbus-python is installed as a system package. The same also applies to
the Secret Storage backend under Python 2 (under Python 3 a different D-Bus
implementation is used).

.. _dbus-python: https://gitlab.freedesktop.org/dbus/dbus-python

-------------
Using Keyring
-------------

The basic usage of keyring is pretty simple: just call `keyring.set_password`
and `keyring.get_password`:

    >>> import keyring
    >>> keyring.set_password("system", "username", "password")
    >>> keyring.get_password("system", "username")
    'password'

Command-line Utility
====================

Keyring supplies a ``keyring`` command which is installed with the
package. After installing keyring in most environments, the
command should be available for setting, getting, and deleting
passwords. For more information on usage, invoke with no arguments
or with ``--help`` as so::

    $ keyring --help
    $ keyring set system username
    Password for 'username' in 'system':
    $ keyring get system username
    password

The command-line functionality is also exposed as an executable
package, suitable for invoking from Python like so::

    $ python -m keyring --help
    $ python -m keyring set system username
    Password for 'username' in 'system':
    $ python -m keyring get system username
    password

--------------------------
Configure your keyring lib
--------------------------

The python keyring lib contains implementations for several backends. The
library will
automatically choose the keyring that is most suitable for your current
environment. You can also specify the keyring you like to be used in the
config file or by calling the ``set_keyring()`` function.

Customize your keyring by config file
=====================================

This section describes how to change your option in the config file.

Config file path
----------------

The configuration of the lib is stored in a file named "keyringrc.cfg". This
file must be found in a platform-specific location. To determine
where the config file is stored, run the following::

    python -c "import keyring.util.platform_; print(keyring.util.platform_.config_root())"

Some keyrings also store the keyring data in the file system. To determine
where the data files are stored, run this command::

    python -c "import keyring.util.platform_; print(keyring.util.platform_.data_root())"


Config file content
-------------------

To specify a keyring backend, set the **default-keyring** option to the
full path of the class for that backend, such as
``keyring.backends.OS_X.Keyring``.

If **keyring-path** is indicated, keyring will add that path to the Python
module search path before loading the backend.

For example, this config might be used to load the
``SimpleKeyring`` from the ``simplekeyring`` module in
the ``./demo`` directory (not implemented)::

    [backend]
    default-keyring=simplekeyring.SimpleKeyring
    keyring-path=demo

Third-Party Backends
====================

In addition to the backends provided by the core keyring package for
the most common and secure use cases, there
are additional keyring backend implementations available for other
use-cases. Simply install them to make them available:

- `keyrings.cryptfile <https://pypi.org/project/keyrings.cryptfile>`_
  - Encrypted text file storage.
- `keyring_jeepney <https://pypi.org/project/keyring_jeepney>`__ - a
  pure Python backend using the secret service DBus API for desktop
  Linux.
- `keyrings.alt <https://pypi.org/project/keyrings.alt>`_ - "alternate",
  possibly-insecure backends, originally part of the core package, but
  available for opt-in.
- `gsheet-keyring <https://pypi.org/project/gsheet-keyring>`_
  - a backend that stores secrets in a Google Sheet. For use with
  `ipython-secrets <https://pypi.org/project/ipython-secrets>`_.
- `bitwarden-keyring <https://pypi.org/project/bitwarden-keyring/0.1.0/>`_
  - a backend that stores secrets in the `BitWarden <https://bitwarden.com/>`_
  password manager.


Write your own keyring backend
==============================

The interface for the backend is defined by ``keyring.backend.KeyringBackend``.
Every backend should derive from that base class and define a ``priority``
attribute and three functions: ``get_password()``, ``set_password()``, and
``delete_password()``. The ``get_credential()`` function may be defined if
desired.

See the ``backend`` module for more detail on the interface of this class.

Keyring employs entry points to allow any third-party package to implement
backends without any modification to the keyring itself. Those interested in
creating new backends are encouraged to create new, third-party packages
in the ``keyrings`` namespace, in a manner modeled by the `keyrings.alt
package <https://github.com/jaraco/keyrings.alt>`_. See the ``setup.py`` file
in that project for a hint on how to create the requisite entry points.
Backends that prove essential may be considered for inclusion in the core
library, although the ease of installing these third-party packages should
mean that extensions may be readily available.

If you've created an extension for Keyring, please submit a pull request to
have your extension mentioned as an available extension.

Set the keyring in runtime
==========================

Keyring additionally allows programmatic configuration of the
backend calling the api ``set_keyring()``. The indicated backend
will subsequently be used to store and retrieve passwords.

Here's an example demonstrating how to invoke ``set_keyring``::

    # define a new keyring class which extends the KeyringBackend
    import keyring.backend

    class TestKeyring(keyring.backend.KeyringBackend):
        """A test keyring which always outputs same password
        """
        priority = 1

        def set_password(self, servicename, username, password):
            pass

        def get_password(self, servicename, username):
            return "password from TestKeyring"

        def delete_password(self, servicename, username, password):
            pass

    # set the keyring for keyring lib
    keyring.set_keyring(TestKeyring())

    # invoke the keyring lib
    try:
        keyring.set_password("demo-service", "tarek", "passexample")
        print("password stored successfully")
    except keyring.errors.PasswordSetError:
        print("failed to store password")
    print("password", keyring.get_password("demo-service", "tarek"))


Altering Keyring Behavior
=========================

Keyring provides a mechanism to alter the keyring's behavior through
environment variables. Each backend implements a
``KeyringBackend.set_properties_from_env``, which
when invoked will find all environment variables beginning with
``KEYRING_PROPERTY_{NAME}`` and will set a property for each
``{NAME.lower()}`` on the keyring. This method is invoked during
initialization for the default/configured keyring.

This mechanism may be used to set some useful values on various
keyrings, including:

- keychain; macOS, path to an alternate keychain file
- appid; Linux/SecretService, alternate ID for the application


Using Keyring on Ubuntu 16.04
=============================

The following is a complete transcript for installing keyring in a
virtual environment on Ubuntu 16.04.  No config file was used.::

  $ sudo apt install python3-venv libdbus-glib-1-dev
  $ cd /tmp
  $ pyvenv py3
  $ source py3/bin/activate
  $ pip install -U pip
  $ pip install secretstorage dbus-python
  $ pip install keyring
  $ python
  >>> import keyring
  >>> keyring.get_keyring()
  <keyring.backends.SecretService.Keyring object at 0x7f9b9c971ba8>
  >>> keyring.set_password("system", "username", "password")
  >>> keyring.get_password("system", "username")
  'password'


Using Keyring on headless Linux systems
=======================================

It is possible to use the SecretService backend on Linux systems without
X11 server available (only D-Bus is required). To do that, you need the
following:

* Install the `GNOME Keyring`_ daemon.
* Start a D-Bus session, e.g. run ``dbus-run-session -- sh`` and run
  the following commands inside that shell.
* Run ``gnome-keyring-daemon`` with ``--unlock`` option. The description of
  that option says:

      Read a password from stdin, and use it to unlock the login keyring
      or create it if the login keyring does not exist.

  When that command is started, enter your password into stdin and
  press Ctrl+D (end of data). After that the daemon will fork into
  background (use ``--foreground`` option to prevent that).
* Now you can use the SecretService backend of Keyring. Remember to
  run your application in the same D-Bus session as the daemon.

.. _GNOME Keyring: https://wiki.gnome.org/Projects/GnomeKeyring

-----------------------------------------------
Integrate the keyring lib with your application
-----------------------------------------------

API interface
=============

The keyring lib has a few functions:

* ``get_keyring()``: Return the currently-loaded keyring implementation.
* ``get_password(service, username)``: Returns the password stored in the
  active keyring. If the password does not exist, it will return None.
* ``get_credential(service, username)``: Return a credential object stored
  in the active keyring. This object contains at least ``username`` and
  ``password`` attributes for the specified service, where the returned
  ``username`` may be different from the argument.
* ``set_password(service, username, password)``: Store the password in the
  keyring.
* ``delete_password(service, username)``: Delete the password stored in
  keyring. If the password does not exist, it will raise an exception.

In all cases, the parameters (``service``, ``username``, ``password``)
should be Unicode text. On Python 2, these parameters are accepted as
simple ``str`` in the default encoding as they will be implicitly
decoded to text. Some backends may accept ``bytes`` for these parameters,
but such usage is discouraged.


Exceptions
==========

The keyring lib raises following exceptions:

* ``keyring.errors.KeyringError``: Base Error class for all exceptions in keyring lib.
* ``keyring.errors.InitError``: Raised when the keyring can't be initialized.
* ``keyring.errors.PasswordSetError``: Raise when password can't be set in the keyring.
* ``keyring.errors.PasswordDeleteError``: Raised when the password can't be deleted in the keyring.

------------
Get involved
------------

Python keyring lib is an open community project and highly welcomes new
contributors.

* Repository: https://github.com/jaraco/keyring/
* Bug Tracker: https://github.com/jaraco/keyring/issues/
* Mailing list: http://groups.google.com/group/python-keyring

For Enterprise
==============

Available as part of the Tidelift Subscription.

This project and the maintainers of thousands of other packages are working with Tidelift to deliver one enterprise subscription that covers all of the open source you use.

`Learn more <https://tidelift.com/subscription/pkg/pypi-PROJECT?utm_source=pypi-PROJECT&utm_medium=referral&utm_campaign=github>`_.

Security Contact
================

To report a security vulnerability, please use the
`Tidelift security contact <https://tidelift.com/security>`_.
Tidelift will coordinate the fix and disclosure.

Making Releases
===============

This project makes use of automated releases via Travis-CI. The
simple workflow is to tag a commit and push it to Github. If it
passes tests on a late Python version, it will be automatically
deployed to PyPI.

Other things to consider when making a release:

 - first ensure that tests pass (preferably on Windows and Linux)
 - check that the changelog is current for the intended release

Running Tests
=============

Tests are `continuously run <https://travis-ci.org/#!/jaraco/keyring>`_ using
Travis-CI.

To run the tests yourself, you'll want keyring installed to some environment
in which it can be tested. Recommended technique is described below.

Using tox
---------

Keyring prefers use of `tox <https://pypi.org/project/tox>`_ to run tests.
Simply install and invoke ``tox``.

This technique is the one used by the Travis-CI script.

----------
Background
----------

The project was based on Tarek Ziade's idea in `this post`_. Kang Zhang
initially carried it out as a `Google Summer of Code`_ project, and Tarek
mentored Kang on this project.

.. _this post: http://tarekziade.wordpress.com/2009/03/27/pycon-hallway-session-1-a-keyring-library-for-python/
.. _Google Summer of Code: http://socghop.appspot.com/


.. image:: https://badges.gitter.im/jaraco/keyring.svg
   :alt: Join the chat at https://gitter.im/jaraco/keyring
   :target: https://gitter.im/jaraco/keyring?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

%package bin
Summary: bin components for the keyring package.
Group: Binaries
Requires: keyring-license = %{version}-%{release}

%description bin
bin components for the keyring package.


%package license
Summary: license components for the keyring package.
Group: Default

%description license
license components for the keyring package.


%package python
Summary: python components for the keyring package.
Group: Default
Requires: keyring-python3 = %{version}-%{release}

%description python
python components for the keyring package.


%package python3
Summary: python3 components for the keyring package.
Group: Default
Requires: python3-core
Provides: pypi(keyring)

%description python3
python3 components for the keyring package.


%prep
%setup -q -n keyring-21.1.0
cd %{_builddir}/keyring-21.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583164500
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py ptr || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keyring
cp %{_builddir}/keyring-21.1.0/LICENSE %{buildroot}/usr/share/package-licenses/keyring/a1474494d96f6ddb3a9a0d767a09871ffc388faf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyring

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keyring/a1474494d96f6ddb3a9a0d767a09871ffc388faf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
