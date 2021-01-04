#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyring
Version  : 21.8.0
Release  : 91
URL      : https://files.pythonhosted.org/packages/19/c7/e1a9c556745518c9c3d46613c10a968757b16e29341ec8e0815fd07e0f93/keyring-21.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/19/c7/e1a9c556745518c9c3d46613c10a968757b16e29341ec8e0815fd07e0f93/keyring-21.8.0.tar.gz
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
BuildRequires : toml-python

%description
.. image:: https://img.shields.io/pypi/v/keyring.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/keyring.svg
:target: `PyPI link`_

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
Requires: pypi(jeepney)
Requires: pypi(secretstorage)

%description python3
python3 components for the keyring package.


%prep
%setup -q -n keyring-21.8.0
cd %{_builddir}/keyring-21.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609777173
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
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
cp %{_builddir}/keyring-21.8.0/LICENSE %{buildroot}/usr/share/package-licenses/keyring/8e6689d37f82d5617b7f7f7232c94024d41066d1
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
/usr/share/package-licenses/keyring/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
